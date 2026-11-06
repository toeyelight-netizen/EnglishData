"""Consistency of the Norton lists that define installment 10 (scope decision of
2026-11-06): research/installment_10/lists/norton_nael_11e_vol_f.csv and
norton_naal_11e_vol_e.csv, transcribed from the publisher's tables of contents."""
import csv
import os
import re
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from audit_installment_10 import NORTON, NORTON_SHORT, load_norton, tkey  # noqa: E402

COLUMNS = ["anthology", "edition", "volume", "section", "author", "author_dates_printed", "selection",
           "excerpt_or_part", "page", "new_in_edition", "first_published", "date_basis", "scope",
           "record_title", "notes"]
SCOPES = {"1946-2000", "before 1946", "after 2000", "date to verify",
          "excluded: written before 1946, first published later"}


def rows(path):
    with open(path, encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


class NortonListTests(unittest.TestCase):
    def test_columns_and_values(self):
        for path in NORTON:
            with open(path, encoding="utf-8") as fh:
                self.assertEqual(next(csv.reader(fh)), COLUMNS, path)
            for r in rows(path):
                self.assertIn(r["anthology"], NORTON_SHORT, r)
                self.assertIn(r["scope"], SCOPES, r)
                self.assertTrue(r["author"] and r["selection"], r)
                self.assertIn(r["new_in_edition"], ("", "yes"), r)
                self.assertTrue(r["date_basis"], r)

    def test_scope_agrees_with_the_recorded_year(self):
        """A dated selection's scope must follow from its year of first publication."""
        for path in NORTON:
            for r in rows(path):
                m = re.fullmatch(r"(1[89]\d\d|20\d\d)", r["first_published"])
                if not m:
                    self.assertIn(r["first_published"], ("",), r)
                    continue
                y = int(m.group(1))
                if r["scope"] == "1946-2000":
                    self.assertTrue(1946 <= y <= 2000, r)
                elif r["scope"] == "before 1946":
                    self.assertLess(y, 1946, r)
                elif r["scope"] == "after 2000":
                    self.assertGreater(y, 2000, r)

    def test_in_scope_rows_name_a_record_title(self):
        """Every in-scope selection names the record it will have, except two of
        Norton's bracketed excerpt titles whose source essays are still to be identified."""
        missing = [(r["author"], r["selection"]) for path in NORTON for r in rows(path)
                   if r["scope"] in ("1946-2000", "date to verify") and not r["record_title"]]
        self.assertTrue(all(sel.startswith("[") for _, sel in missing), missing)
        self.assertLessEqual(len(missing), 2)

    def test_page_numbers_increase_within_the_english_anthology(self):
        """The NAEL table of contents prints page numbers; out-of-order pages would
        mean a transcription slip."""
        pages = [int(r["page"]) for r in rows(NORTON[0]) if r["page"].isdigit()]
        self.assertGreater(len(pages), 250)
        self.assertEqual(pages, sorted(pages))

    def test_title_key_ignores_article_case_and_punctuation(self):
        self.assertEqual(tkey("A Valediction: Forbidding Mourning"), tkey("valediction forbidding mourning"))
        self.assertEqual(tkey("¡Yo!"), tkey("Yo"))
        self.assertNotEqual(tkey("High Windows (poem)"), tkey("High Windows"))

    def test_loader_labels_rows_by_anthology(self):
        loaded = load_norton()
        self.assertEqual({r["short"] for r in loaded}, {"NAEL", "NAAL"})
        self.assertEqual(len(loaded), sum(len(rows(p)) for p in NORTON))


if __name__ == "__main__":
    unittest.main()
