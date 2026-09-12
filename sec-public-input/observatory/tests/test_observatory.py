from __future__ import annotations

import json
import sys
import tempfile
import unittest
from datetime import UTC, datetime, timedelta
from pathlib import Path


OBSERVATORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(OBSERVATORY))

from update_observatory import (  # noqa: E402
    IndexEntry,
    automated_topics,
    build_feed,
    load_reviews,
    needs_full_refresh,
    parse_index,
    render_dashboard,
)


class IndexTests(unittest.TestCase):
    def test_parse_index_preserves_official_metadata(self) -> None:
        source = """
        <table><tr>
          <td>Sept. 10, 2026</td>
          <td>Public Comment</td>
          <td><a href="/comments/S7-2026-30/example.pdf">Example Person</a></td>
        </tr></table>
        """
        entries = parse_index(source)
        self.assertEqual(
            entries,
            [
                IndexEntry(
                    comment_id="example",
                    date="Sept. 10, 2026",
                    letter_type="Public Comment",
                    commenter_name="Example Person",
                    source_url=(
                        "https://www.sec.gov/comments/S7-2026-30/example.pdf"
                    ),
                )
            ],
        )

    def test_parse_index_fails_closed_on_empty_docket(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "refusing to publish"):
            parse_index("<html><body>No recognized table</body></html>")


class AnalysisTests(unittest.TestCase):
    def test_topic_scan_does_not_claim_to_summarize_position(self) -> None:
        taxonomy = {
            "TA-DIGITAL-ASSETS": {
                "label": "Digital assets",
                "keywords": ["blockchain"],
            }
        }
        topics = automated_topics("A blockchain record.", taxonomy)
        self.assertEqual(
            topics,
            [{"code": "TA-DIGITAL-ASSETS", "label": "Digital assets"}],
        )

    def test_full_refresh_is_required_after_24_hours(self) -> None:
        now = datetime.now(UTC)
        feed = {
            "last_full_source_refresh_at": (
                now - timedelta(hours=25)
            ).isoformat()
        }
        self.assertTrue(needs_full_refresh(feed, now))


class ReviewTests(unittest.TestCase):
    def test_changed_source_withholds_stale_review(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            review_dir = Path(directory)
            review = {
                "analysis_text_sha256": "a" * 64,
                "approved_at": "2026-09-10T00:00:00+00:00",
                "comment_id": "example",
                "review_status": "APPROVED",
                "reviewer": "Reviewer",
                "summary": "Summary",
            }
            (review_dir / "example.json").write_text(json.dumps(review))
            entries = {
                "example": {
                    "comment_id": "example",
                    "analysis_text_sha256": "b" * 64,
                }
            }
            reviews, warnings = load_reviews(review_dir, entries)
            self.assertEqual(reviews, {})
            self.assertEqual(len(warnings), 1)
            self.assertIn("withheld", warnings[0])

    def test_feed_marks_approved_review_separately(self) -> None:
        now = datetime.now(UTC).isoformat()
        prior_entry = {
            "comment_id": "example",
            "date": "Sept. 10, 2026",
            "letter_type": "Public Comment",
            "commenter_name": "Example",
            "source_url": (
                "https://www.sec.gov/comments/S7-2026-30/example.html"
            ),
            "source_sha256": "1" * 64,
            "analysis_text_sha256": "2" * 64,
            "source_media_type": "text/html",
            "retrieved_at": now,
            "automated_topics": [],
            "automated_analysis": "No configured signals detected.",
            "analysis_status": "AUTOMATED SIGNAL SCAN — NOT HUMAN REVIEWED",
            "is_foundation_submission": False,
        }
        previous = {
            "docket": "S7-2026-30",
            "last_full_source_refresh_at": now,
            "official_entries": [prior_entry],
        }
        with tempfile.TemporaryDirectory() as directory:
            review_dir = Path(directory)
            review = {
                "analysis_text_sha256": "2" * 64,
                "approved_at": "2026-09-10T00:00:00+00:00",
                "comment_id": "example",
                "review_status": "APPROVED",
                "reviewer": "Reviewer",
                "summary": "An attributable interpretation.",
            }
            (review_dir / "example.json").write_text(json.dumps(review))
            feed = build_feed(
                entries=[
                    IndexEntry(
                        comment_id="example",
                        date="Sept. 10, 2026",
                        letter_type="Public Comment",
                        commenter_name="Example",
                        source_url=prior_entry["source_url"],
                    )
                ],
                taxonomy={},
                reviews_dir=review_dir,
                previous_feed=previous,
                retrieved_at=now,
                timeout=1,
                delay=0,
            )
        self.assertEqual(feed["human_reviewed_count"], 1)
        self.assertEqual(feed["review_warnings"], [])
        self.assertEqual(
            feed["official_entries"][0]["analysis_status"],
            "HUMAN REVIEWED",
        )
        dashboard = render_dashboard(feed)
        self.assertIn("An attributable interpretation.", dashboard)
        self.assertIn("Open exact SEC filing", dashboard)

    def test_removed_review_is_not_republished_from_previous_feed(self) -> None:
        now = datetime.now(UTC).isoformat()
        prior_entry = {
            "comment_id": "example",
            "date": "Sept. 10, 2026",
            "letter_type": "Public Comment",
            "commenter_name": "Example",
            "source_url": (
                "https://www.sec.gov/comments/S7-2026-30/example.html"
            ),
            "source_sha256": "1" * 64,
            "analysis_text_sha256": "2" * 64,
            "source_media_type": "text/html",
            "retrieved_at": now,
            "automated_topics": [],
            "automated_analysis": "No configured signals detected.",
            "analysis_status": "HUMAN REVIEWED",
            "human_review": {
                "summary": "A retracted summary.",
                "reviewer": "Reviewer",
                "approved_at": "2026-09-10T00:00:00+00:00",
            },
            "is_foundation_submission": False,
        }
        previous = {
            "docket": "S7-2026-30",
            "last_full_source_refresh_at": now,
            "official_entries": [prior_entry],
        }
        with tempfile.TemporaryDirectory() as directory:
            feed = build_feed(
                entries=[
                    IndexEntry(
                        comment_id="example",
                        date="Sept. 10, 2026",
                        letter_type="Public Comment",
                        commenter_name="Example",
                        source_url=prior_entry["source_url"],
                    )
                ],
                taxonomy={},
                reviews_dir=Path(directory),
                previous_feed=previous,
                retrieved_at=now,
                timeout=1,
                delay=0,
            )
        entry = feed["official_entries"][0]
        self.assertEqual(feed["human_reviewed_count"], 0)
        self.assertEqual(
            entry["analysis_status"],
            "AUTOMATED SIGNAL SCAN — NOT HUMAN REVIEWED",
        )
        self.assertNotIn("human_review", entry)
        self.assertNotIn("A retracted summary.", render_dashboard(feed))


if __name__ == "__main__":
    unittest.main()
