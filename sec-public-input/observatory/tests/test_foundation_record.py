import copy
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from foundation_record import copy_public_pdfs, filing_status, load_record, render_record


class FoundationRecordTests(unittest.TestCase):
    def test_current_inventory_and_deadlines(self):
        record = load_record()
        october = [f for f in record['filings'] if f['submitted'] == '2026-10-03']
        self.assertEqual(len(october), 2)
        for filing in october:
            self.assertFalse(filing['secPosted'])
            self.assertIsNone(filing['secUrl'])
            self.assertEqual(filing_status(filing), 'Submitted Oct. 3, 2026 — SEC posting pending')
        self.assertEqual(filing_status(record['filings'][0]), 'Posted on SEC.gov')
        self.assertEqual(record['proceedings'][0]['deadline'], 'Nov. 3, 2026')
        self.assertEqual(record['proceedings'][1]['deadline'], '60 days after Federal Register publication')

    def test_posting_changes_labels_and_retains_local_copy(self):
        record = copy.deepcopy(load_record())
        filing = record['filings'][-1]
        filing['secPosted'] = True
        filing['secUrl'] = 'https://www.sec.gov/comments/S7-2026-35/test.pdf'
        rendered = render_record(record)
        self.assertIn(filing['localPdf'], rendered)
        self.assertIn(filing['secUrl'], rendered)
        self.assertIn('Read Foundation copy', rendered)
        self.assertEqual(filing_status(filing), 'Posted on SEC.gov')
        self.assertIn('Submitted Oct. 3, 2026 — SEC posting pending', rendered)

    def test_public_build_copies_exact_pdfs_and_no_docx(self):
        from foundation_record import SEC
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)
            copy_public_pdfs(output)
            for filing in load_record()['filings']:
                for key in ('localPdf', 'additionalPdf'):
                    if filing.get(key):
                        self.assertEqual((output / filing[key]).read_bytes(), (SEC / filing[key]).read_bytes())
            self.assertFalse(list(output.rglob('*.docx')))

    def test_timeline_order_and_meaningful_single_quotes(self):
        rendered = render_record()
        dates = ['2026-09-01', '2026-09-05', '2026-09-23', '2026-10-01', '2026-10-03']
        positions = [rendered.index(f'datetime="{day}"') for day in dates]
        self.assertEqual(positions, sorted(positions))
        self.assertEqual(rendered.count('A private key establishes an ability to act;'), 1)
        self.assertEqual(rendered.count('Custody should protect the asset.'), 1)
