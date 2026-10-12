"""Offline regression checks; copy alongside existing observatory tests."""
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from foundation_reconcile import official_date_iso, reconcile_foundation


class ReconciliationTests(unittest.TestCase):
    def setUp(self):
        self.record = {
            "lastVerified": "2026-10-03",
            "filings": [{"id": "oct", "docket": "S7-2026-35", "submitted": "2026-10-03",
                         "localPdf": "test.pdf", "secPosted": False, "secUrl": None}],
        }
        self.url = "https://www.sec.gov/comments/S7-2026-35/abcdef.pdf"
        self.indexes = {"S7-2026-35": [
            SimpleNamespace(date="Oct. 3, 2026", commenter_name="Pamela Norton, TitleChain Foundation",
                            source_url=self.url)
        ]}

    def test_dates(self):
        self.assertEqual(official_date_iso("Sept. 23, 2026"), "2026-09-23")
        self.assertEqual(official_date_iso("Oct. 3, 2026"), "2026-10-03")
        self.assertIsNone(official_date_iso("bad"))

    def _run(self, sec_text="This is the exact filed PDF", entries=None):
        with tempfile.TemporaryDirectory() as d:
            Path(d, "test.pdf").write_bytes(b"This is the exact filed PDF")
            def extract(source, media):
                return source.decode()
            def fetch(url, timeout):
                self.assertEqual(url, self.url)
                return sec_text.encode(), "application/pdf"
            return reconcile_foundation(self.record,
                 self.indexes if entries is None else entries,
                 public_root=Path(d), request_bytes=fetch, extract_text=extract,
                 retrieved_at="2026-10-08T20:00:00+00:00")

    def test_verified_exact_match_posts_only_overlay(self):
        result, warnings = self._run()
        self.assertEqual(warnings, [])
        self.assertTrue(result["filings"][0]["secPosted"])
        self.assertEqual(result["filings"][0]["secUrl"], self.url)
        self.assertEqual(result["lastVerified"], "2026-10-08")
        self.assertFalse(self.record["filings"][0]["secPosted"])

    def test_different_pdf_must_not_be_claimed_posted(self):
        result, _ = self._run(sec_text="different text")
        self.assertFalse(result["filings"][0]["secPosted"])

    def test_unlisted_remains_pending(self):
        result, _ = self._run(entries={"S7-2026-35": []})
        self.assertFalse(result["filings"][0]["secPosted"])


if __name__ == "__main__":
    unittest.main()
