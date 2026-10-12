"""Fail-closed, source-verified matching of TitleChain Foundation SEC comments.

This module is for public SEC metadata only. It never submits comments or
changes source PDFs. An exact extracted-PDF-text match is required before a
previously pending record is marked as SEC-posted.
"""
from __future__ import annotations

import copy
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Callable


MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}


def official_date_iso(raw: str) -> str | None:
    match = re.fullmatch(r"\s*([A-Za-z]+)\.?\s+(\d{1,2}),\s*(\d{4})\s*", raw)
    if not match:
        return None
    month = MONTHS.get(match.group(1)[:3].lower())
    if not month:
        return None
    try:
        return datetime(int(match.group(3)), month, int(match.group(2))).date().isoformat()
    except ValueError:
        return None


def normalized_pdf_text(text: str) -> str:
    return " ".join(text.casefold().split())


def reconcile_foundation(
    record: dict[str, Any],
    indexes: dict[str, list[Any]],
    *,
    public_root: Path,
    request_bytes: Callable[..., tuple[bytes, str]],
    extract_text: Callable[[bytes, str], str],
    retrieved_at: str,
    timeout: float = 30.0,
) -> tuple[dict[str, Any], list[str]]:
    """Return a PUBLIC rendering overlay; never mutate repository filing sources.

    Do not infer SEC publication from names/dates alone. Match extracted PDF text
    against the archived Foundation-submitted PDF; ambiguous/unreadable matches
    remain pending. Both SEC indexes must be successfully fetched before calling.
    """
    verified = copy.deepcopy(record)
    warnings: list[str] = []
    for filing in verified["filings"]:
        if filing["secPosted"]:
            continue  # Preserve previously source-verified postings.
        docket = filing["docket"]
        if docket not in indexes:
            warnings.append(f"{filing['id']}: SEC docket {docket} was not checked")
            continue
        local_pdf = filing.get("localPdf")
        if not local_pdf:
            warnings.append(f"{filing['id']}: no submitted PDF available for comparison")
            continue
        pdf_path = public_root / local_pdf
        try:
            local_text = normalized_pdf_text(extract_text(pdf_path.read_bytes(), "application/pdf"))
        except Exception as error:
            warnings.append(f"{filing['id']}: could not extract archived PDF ({type(error).__name__})")
            continue
        if not local_text:
            warnings.append(f"{filing['id']}: archived PDF has no extractable text")
            continue
        plausible = [
            entry for entry in indexes[docket]
            if official_date_iso(entry.date) == filing["submitted"]
            and ("titlechain foundation" in entry.commenter_name.casefold()
                 or "pamela norton" in entry.commenter_name.casefold())
            and entry.source_url.lower().startswith(f"https://www.sec.gov/comments/{docket.lower()}/")
        ]
        matches = []
        for entry in plausible:
            try:
                source, media_type = request_bytes(entry.source_url, timeout=timeout)
                if media_type != "application/pdf":
                    warnings.append(f"{filing['id']}: candidate SEC comment is not PDF")
                    continue
                official_text = normalized_pdf_text(extract_text(source, media_type))
                if official_text == local_text:
                    matches.append(entry.source_url)
            except Exception as error:
                warnings.append(f"{filing['id']}: SEC candidate could not be verified ({type(error).__name__})")
        if len(matches) == 1:
            filing["secPosted"] = True
            filing["secUrl"] = matches[0]
        elif len(matches) > 1:
            warnings.append(f"{filing['id']}: ambiguous duplicate exact-matching SEC records; no change")
        # No match: remain pending. This is not a runtime error.
    verified["lastVerified"] = retrieved_at[:10]
    return verified, warnings
