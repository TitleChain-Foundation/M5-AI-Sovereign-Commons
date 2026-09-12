from __future__ import annotations

import argparse
import hashlib
import html
import io
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass
from datetime import UTC, datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from pypdf import PdfReader


DOCKET = "S7-2026-30"
DOCKET_URL = "https://www.sec.gov/rules-regulations/public-comments/s7-2026-30"
SEC_ORIGIN = "https://www.sec.gov"
USER_AGENT = (
    "TitleChainFoundation-M5-SEC-Comment-Observatory/1.0 "
    "security@titlechainfoundation.org"
)
COMMENT_PATH = re.compile(
    r"^/comments/S7-2026-30/[A-Za-z0-9._-]+\.(?:html|pdf)$",
    re.IGNORECASE,
)
FOUNDATION_COMMENT_IDS = {"s7202630-1029659-3393926"}


def normalize_text(value: str) -> str:
    return " ".join(value.split())


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


@dataclass(frozen=True)
class IndexEntry:
    comment_id: str
    date: str
    letter_type: str
    commenter_name: str
    source_url: str


class DocketIndexParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.entries: list[IndexEntry] = []
        self._in_row = False
        self._in_cell = False
        self._cell_text: list[str] = []
        self._cells: list[str] = []
        self._comment_href: str | None = None

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        attributes = dict(attrs)
        if tag == "tr":
            self._in_row = True
            self._cells = []
            self._comment_href = None
        elif self._in_row and tag == "td":
            self._in_cell = True
            self._cell_text = []
        elif self._in_row and tag == "a":
            href = attributes.get("href")
            if href and COMMENT_PATH.fullmatch(href):
                self._comment_href = href

    def handle_data(self, data: str) -> None:
        if self._in_cell:
            self._cell_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "td" and self._in_cell:
            self._cells.append(normalize_text("".join(self._cell_text)))
            self._in_cell = False
        elif tag == "tr" and self._in_row:
            if self._comment_href and len(self._cells) >= 3:
                self.entries.append(
                    IndexEntry(
                        comment_id=Path(self._comment_href).stem,
                        date=self._cells[0],
                        letter_type=self._cells[1],
                        commenter_name=self._cells[2],
                        source_url=urllib.parse.urljoin(
                            SEC_ORIGIN, self._comment_href
                        ),
                    )
                )
            self._in_row = False


class CommentTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._capture_depth = 0
        self._ignored_depth = 0
        self._parts: list[str] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        del attrs
        if tag in {"script", "style", "nav", "footer"}:
            self._ignored_depth += 1
        elif self._ignored_depth == 0 and tag in {
            "h1",
            "h2",
            "h3",
            "p",
            "li",
            "blockquote",
        }:
            self._capture_depth += 1

    def handle_data(self, data: str) -> None:
        if self._ignored_depth == 0 and self._capture_depth:
            self._parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "nav", "footer"} and self._ignored_depth:
            self._ignored_depth -= 1
        elif tag in {"h1", "h2", "h3", "p", "li", "blockquote"}:
            if self._capture_depth:
                self._capture_depth -= 1
                self._parts.append("\n")

    @property
    def text(self) -> str:
        lines = [
            normalize_text(line)
            for line in "".join(self._parts).splitlines()
            if normalize_text(line)
        ]
        return "\n".join(lines) + "\n"


def request_bytes(url: str, timeout: float = 30.0) -> tuple[bytes, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/pdf,application/json",
            "Accept-Encoding": "identity",
        },
    )
    last_error: Exception | None = None
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read(), response.headers.get_content_type()
        except (TimeoutError, urllib.error.URLError) as error:
            last_error = error
            if attempt < 2:
                time.sleep(2**attempt)
    assert last_error is not None
    raise last_error


def parse_index(source: str) -> list[IndexEntry]:
    parser = DocketIndexParser()
    parser.feed(source)
    unique: dict[str, IndexEntry] = {}
    for entry in parser.entries:
        unique.setdefault(entry.comment_id, entry)
    if not unique:
        raise RuntimeError(
            "No SEC comments were found; refusing to publish an empty feed."
        )
    return list(unique.values())


def extract_text(source: bytes, media_type: str) -> str:
    if media_type == "application/pdf":
        reader = PdfReader(io.BytesIO(source))
        parts = [
            normalize_text(line)
            for page in reader.pages
            for line in (page.extract_text() or "").splitlines()
            if normalize_text(line)
        ]
        text = "\n".join(parts) + "\n"
    elif media_type in {"text/html", "application/xhtml+xml"}:
        parser = CommentTextParser()
        parser.feed(source.decode("utf-8", errors="replace"))
        text = parser.text
    else:
        raise ValueError(f"Unexpected SEC comment media type: {media_type}")
    if not text.strip():
        raise ValueError("SEC comment did not contain extractable text.")
    return text


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_previous_feed(url: str | None) -> dict[str, Any] | None:
    if not url:
        return None
    try:
        source, media_type = request_bytes(url, timeout=10.0)
    except (TimeoutError, urllib.error.HTTPError, urllib.error.URLError):
        return None
    if media_type != "application/json":
        return None
    try:
        data = json.loads(source)
    except json.JSONDecodeError:
        return None
    return data if data.get("docket") == DOCKET else None


def prior_entries(feed: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    if not feed:
        return {}
    return {
        entry["comment_id"]: entry
        for entry in feed.get("official_entries", [])
        if isinstance(entry, dict) and "comment_id" in entry
    }


def needs_full_refresh(feed: dict[str, Any] | None, now: datetime) -> bool:
    if not feed:
        return True
    value = feed.get("last_full_source_refresh_at")
    if not isinstance(value, str):
        return True
    try:
        refreshed_at = datetime.fromisoformat(value)
    except ValueError:
        return True
    return now - refreshed_at >= timedelta(hours=24)


def automated_topics(
    text: str, taxonomy: dict[str, dict[str, Any]]
) -> list[dict[str, str]]:
    lowered = text.casefold()
    topics: list[dict[str, str]] = []
    for code, definition in taxonomy.items():
        if any(keyword.casefold() in lowered for keyword in definition["keywords"]):
            topics.append({"code": code, "label": definition["label"]})
    return topics


def collect_entry(
    entry: IndexEntry,
    *,
    taxonomy: dict[str, dict[str, Any]],
    retrieved_at: str,
    timeout: float,
) -> dict[str, Any]:
    source, media_type = request_bytes(entry.source_url, timeout=timeout)
    text = extract_text(source, media_type)
    topics = automated_topics(text, taxonomy)
    return {
        **asdict(entry),
        "analysis_status": "AUTOMATED SIGNAL SCAN — NOT HUMAN REVIEWED",
        "analysis_text_sha256": sha256(text.encode("utf-8")),
        "automated_topics": topics,
        "automated_analysis": (
            "Automated signal scan detected language associated with: "
            + ", ".join(topic["label"] for topic in topics)
            + ". This identifies possible review topics; it does not characterize "
            "the commenter's position."
            if topics
            else "No configured topic signals were detected. This does not mean "
            "the filing lacks substantive issues."
        ),
        "is_foundation_submission": entry.comment_id in FOUNDATION_COMMENT_IDS,
        "retrieved_at": retrieved_at,
        "source_media_type": media_type,
        "source_sha256": sha256(source),
    }


def load_reviews(
    review_dir: Path, entries: dict[str, dict[str, Any]]
) -> tuple[dict[str, dict[str, Any]], list[str]]:
    reviews: dict[str, dict[str, Any]] = {}
    warnings: list[str] = []
    for path in sorted(review_dir.glob("*.json")):
        review = load_json(path)
        required = {
            "analysis_text_sha256",
            "approved_at",
            "comment_id",
            "review_status",
            "reviewer",
            "summary",
        }
        missing = required - review.keys()
        if missing:
            raise ValueError(f"{path.name} is missing fields: {sorted(missing)}")
        if review["review_status"] != "APPROVED":
            raise ValueError(f"{path.name} is not APPROVED")
        entry = entries.get(review["comment_id"])
        if not entry:
            raise ValueError(f"{path.name} has no matching SEC docket entry")
        if review["analysis_text_sha256"] != entry["analysis_text_sha256"]:
            warnings.append(
                f"{path.name} was withheld because the collected SEC analysis "
                "text no longer matches its approved digest"
            )
            continue
        reviews[review["comment_id"]] = review
    return reviews, warnings


def build_feed(
    *,
    entries: list[IndexEntry],
    taxonomy: dict[str, dict[str, Any]],
    reviews_dir: Path,
    previous_feed: dict[str, Any] | None,
    retrieved_at: str,
    timeout: float,
    delay: float,
) -> dict[str, Any]:
    now = datetime.fromisoformat(retrieved_at)
    previous = prior_entries(previous_feed)
    full_refresh = needs_full_refresh(previous_feed, now)
    collected: list[dict[str, Any]] = []
    for entry in entries:
        prior = previous.get(entry.comment_id)
        if (
            prior
            and not full_refresh
            and prior.get("source_url") == entry.source_url
            and prior.get("source_sha256")
            and prior.get("analysis_text_sha256")
        ):
            collected.append(
                {
                    **prior,
                    **asdict(entry),
                    "is_foundation_submission": (
                        entry.comment_id in FOUNDATION_COMMENT_IDS
                    ),
                }
            )
            continue
        if collected:
            time.sleep(delay)
        collected.append(
            collect_entry(
                entry,
                taxonomy=taxonomy,
                retrieved_at=retrieved_at,
                timeout=timeout,
            )
        )

    by_id = {entry["comment_id"]: entry for entry in collected}
    reviews, review_warnings = load_reviews(reviews_dir, by_id)
    for entry in collected:
        entry.pop("human_review", None)
        entry["analysis_status"] = "AUTOMATED SIGNAL SCAN — NOT HUMAN REVIEWED"
        review = reviews.get(entry["comment_id"])
        if review:
            entry["analysis_status"] = "HUMAN REVIEWED"
            entry["human_review"] = review

    return {
        "docket": DOCKET,
        "status": "Independent public-interest research; not an SEC position",
        "official_docket_url": DOCKET_URL,
        "official_index_count": len(collected),
        "human_reviewed_count": len(reviews),
        "pending_human_review_count": len(collected) - len(reviews),
        "review_warnings": review_warnings,
        "last_sec_retrieval_at": retrieved_at,
        "last_full_source_refresh_at": (
            retrieved_at
            if full_refresh
            else previous_feed["last_full_source_refresh_at"]
        ),
        "generated_at": datetime.now(UTC).isoformat(),
        "official_entries": collected,
    }


def render_dashboard(feed: dict[str, Any]) -> str:
    rows = []
    review_cards = []
    for entry in feed["official_entries"]:
        topics = ", ".join(
            topic["label"] for topic in entry["automated_topics"]
        ) or "No configured signals detected"
        first_party = (
            '<br><span class="status first-party">FOUNDATION-SUBMITTED FILING</span>'
            if entry["is_foundation_submission"]
            else ""
        )
        status_class = (
            "reviewed"
            if entry["analysis_status"] == "HUMAN REVIEWED"
            else "automated"
        )
        rows.append(
            "<tr>"
            f"<td>{html.escape(entry['date'])}</td>"
            f"<td>{html.escape(entry['commenter_name'])}{first_party}</td>"
            f"<td>{html.escape(entry['letter_type'])}</td>"
            f"<td><span class=\"status {status_class}\">"
            f"{html.escape(entry['analysis_status'])}</span>"
            f"<br><small>{html.escape(topics)}</small>"
            f"<br><small>{html.escape(entry['automated_analysis'])}</small></td>"
            f"<td><code>{html.escape(entry['source_sha256'][:12])}…</code></td>"
            f"<td><a href=\"{html.escape(entry['source_url'])}\">"
            "Open exact SEC filing</a></td>"
            "</tr>"
        )
        if "human_review" in entry:
            review = entry["human_review"]
            review_cards.append(
                "<article>"
                f"<h3>{html.escape(entry['commenter_name'])}</h3>"
                f"<p>{html.escape(review['summary'])}</p>"
                f"<p><strong>Reviewed by:</strong> "
                f"{html.escape(review['reviewer'])} · "
                f"{html.escape(review['approved_at'])}</p>"
                f"<p><a href=\"{html.escape(entry['source_url'])}\">"
                "Check this interpretation against the official filing</a></p>"
                "</article>"
            )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>SEC Public Comment Observatory — S7-2026-30</title>
  <style>
    :root {{ color-scheme: light; font-family: ui-sans-serif, system-ui, sans-serif; }}
    body {{ margin: 0; background: #f6f2ea; color: #1d1428; }}
    main {{ max-width: 1180px; margin: auto; padding: 3rem 1.25rem 5rem; }}
    header, section, article {{ background: #fff; border: 1px solid #d8c89f;
      border-radius: 16px; padding: 1.5rem; margin-bottom: 1.25rem; }}
    h1, h2, h3 {{ line-height: 1.12; }}
    a {{ color: #7b245f; }}
    .notice {{ border-left: 6px solid #8b2f70; }}
    .metrics {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(190px,1fr));
      gap: 1rem; }}
    .metric {{ background: #1d1428; color: white; border-radius: 12px; padding: 1rem; }}
    .metric strong {{ display: block; font-size: 2rem; }}
    .table-wrap {{ overflow-x: auto; }}
    table {{ width: 100%; border-collapse: collapse; }}
    th, td {{ text-align: left; vertical-align: top; padding: .7rem;
      border-bottom: 1px solid #ddd; }}
    code {{ overflow-wrap: anywhere; }}
    .status {{ display: inline-block; border-radius: 999px; padding: .2rem .55rem;
      font-size: .72rem; font-weight: 800; }}
    .status.reviewed {{ background: #e3f4ea; color: #175d38; }}
    .status.automated {{ background: #f7edcf; color: #74540b; }}
    .status.first-party {{ margin-top: .35rem; background: #eee5f4; color: #5d2674; }}
  </style>
</head>
<body>
<main>
  <header>
    <p>M5 AI Sovereign Commons · Public Research Feed</p>
    <h1>SEC Public Comment Observatory</h1>
    <p>Transfer Agent Rules · File No. S7-2026-30</p>
  </header>
  <section class="notice">
    <p><strong>{html.escape(feed['status'])}.</strong> The official SEC docket
    controls. This site records exact docket metadata, official links, retrieval
    time, and source hashes. It does not rehost filings as Foundation publications.</p>
    <p><strong>Automated signal scans are not summaries.</strong> Narrative
    summaries appear only after attributable human review.</p>
    <p><a href="{DOCKET_URL}">Open the official SEC docket</a> ·
    <a href="feed.json">Download the machine-readable feed</a></p>
  </section>
  <section class="metrics">
    <div class="metric"><strong>{feed['official_index_count']}</strong>official filings indexed</div>
    <div class="metric"><strong>{feed['human_reviewed_count']}</strong>human-reviewed summaries</div>
    <div class="metric"><strong>{feed['pending_human_review_count']}</strong>awaiting human review</div>
  </section>
  <section>
    <h2>Official filing index</h2>
    <div class="table-wrap">
      <table>
        <thead><tr><th>SEC date</th><th>Commenter</th><th>Type</th>
        <th>Analysis state</th><th>Source SHA-256</th><th>Official source</th></tr></thead>
        <tbody>{''.join(rows)}</tbody>
      </table>
    </div>
  </section>
  <section>
    <h2>Human-reviewed summaries</h2>
    {''.join(review_cards) if review_cards else '<p>No summaries have completed human review.</p>'}
  </section>
  <section>
    <h2>Provenance</h2>
    <p>Last SEC retrieval: <code>{html.escape(feed['last_sec_retrieval_at'])}</code></p>
    <p>Last full source refresh: <code>{html.escape(feed['last_full_source_refresh_at'])}</code></p>
    <p>Page generated: <code>{html.escape(feed['generated_at'])}</code></p>
    {
        '<p><strong>Review warning:</strong> '
        + html.escape(' '.join(feed['review_warnings']))
        + '</p>'
        if feed['review_warnings']
        else ''
    }
  </section>
</main>
</body>
</html>
"""


def write_site(feed: dict[str, Any], output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    (output / "feed.json").write_text(
        json.dumps(feed, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (output / "index.html").write_text(
        render_dashboard(feed),
        encoding="utf-8",
    )


def main() -> int:
    base = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Build the public S7-2026-30 observatory from SEC sources."
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--previous-feed")
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--delay", type=float, default=0.75)
    args = parser.parse_args()

    retrieved_at = datetime.now(UTC).isoformat()
    index_source, media_type = request_bytes(DOCKET_URL, timeout=args.timeout)
    if media_type not in {"text/html", "application/xhtml+xml"}:
        raise ValueError(f"Unexpected SEC docket media type: {media_type}")
    entries = parse_index(index_source.decode("utf-8", errors="replace"))
    taxonomy = load_json(base / "taxonomy.json")["topics"]
    previous_feed = load_previous_feed(args.previous_feed)
    feed = build_feed(
        entries=entries,
        taxonomy=taxonomy,
        reviews_dir=base / "reviews",
        previous_feed=previous_feed,
        retrieved_at=retrieved_at,
        timeout=args.timeout,
        delay=args.delay,
    )
    write_site(feed, args.output)
    print(
        f"Published {feed['official_index_count']} official entries: "
        f"{feed['human_reviewed_count']} human-reviewed, "
        f"{feed['pending_human_review_count']} awaiting review."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
