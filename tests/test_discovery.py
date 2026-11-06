"""The installment-10 discovery inventory: name normalisation, the curated
African Writers Series list and the reproducibility of the generated CSV.

The name helpers are pinned on the cases that produced duplicate candidates
(surname-first names from the British prize, Asian American and Iowa datasets)
and on the misspellings corrected from the African Writers Series table. The
list and inventory tests read the committed files, so they need neither the
Post45 download nor the database."""

import csv
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

import i10_discovery as d  # noqa: E402

LIST = os.path.join(ROOT, "research", "installment_10", "lists", "heinemann_african_writers_series_1962_2003.csv")
INVENTORY = os.path.join(ROOT, "research", "installment_10", "discovery_inventory.csv")
AWS = d.CURATED["heinemann_african_writers_series_1962_2003.csv"]


class NameHelpersTest(unittest.TestCase):
    def test_natural_order(self):
        self.assertEqual(d.natural_order("Walsh, Jill Paton"), "Jill Paton Walsh")
        self.assertEqual(d.natural_order("Gates, Henry Louis, Jr."), "Henry Louis Gates Jr.")
        self.assertEqual(d.natural_order("Amis, Martin, ed."), "Martin Amis")
        # Already in natural order, or ambiguous: left alone.
        self.assertEqual(d.natural_order("Martin Amis"), "Martin Amis")
        self.assertEqual(d.natural_order("A B, C D, E F"), "A B, C D, E F")

    def test_heading_name_drops_dates_and_fuller_forms(self):
        self.assertEqual(d.heading_name("Wright, Charles, 1935-"), "Wright, Charles")
        self.assertEqual(d.heading_name("McGalliard, John Calvin."), "McGalliard, John Calvin")
        self.assertEqual(d.heading_name("Smith, J. (John), 1950-2001"), "Smith, J")

    def test_split_credit(self):
        self.assertEqual(d.split_credit("Larry Niven and Jerry Pournelle"), ["Larry Niven", "Jerry Pournelle"])
        self.assertEqual(d.split_credit("David and Leigh Eddings"), ["David Eddings", "Leigh Eddings"])
        self.assertEqual(d.split_credit("Haldeman, Joe W", inverted=True), ["Joe W Haldeman"])
        # Natural-order datasets are never turned round.
        self.assertEqual(d.split_credit("Haldeman, Joe W"), ["Haldeman, Joe W"])

    def test_name_fixes(self):
        self.assertEqual(d.split_credit("Step hen King"), ["Stephen King"])
        self.assertEqual(d.split_credit("Sepho Sepamia"), ["Sipho Sepamla"])
        self.assertEqual(d.split_credit("Cosmo Peterse"), ["Cosmo Pieterse"])
        self.assertEqual(d.split_credit("Ezekiel Mphahlele"), ["Es'kia Mphahlele"])
        self.assertEqual(d.split_credit("Guy de Maupassant"), [])

    def test_fold_ignores_accents_and_punctuation(self):
        self.assertEqual(d.fold("Colm Tóibín"), d.fold("Colm Toibin"))
        self.assertEqual(d.fold("J. P. Clark"), d.fold("JP Clark"))


class AfricanWritersSeriesListTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(LIST, encoding="utf-8") as fh:
            cls.rows = list(csv.DictReader(fh))

    def test_columns_and_roles(self):
        self.assertEqual(list(self.rows[0].keys()),
                         ["number", "year", "author", "role", "genre", "title", "language", "notes"])
        known = set(AWS["priority"]) | set(AWS["skip"])
        self.assertEqual({r["role"] for r in self.rows} - known, set())

    def test_numbering(self):
        numbers = {int(r["number"]) for r in self.rows if r["number"] != "u"}
        # Every series number from 1 to 270 except 65, which the source table omits.
        self.assertEqual(set(range(1, 271)) - numbers, {65})

    def test_translations_are_not_counted(self):
        for role in ("translation", "translation_inferred", "contributor_translation", "reprint"):
            self.assertIn(role, AWS["skip"])
            self.assertNotIn(role, AWS["priority"])
        self.assertEqual(AWS["priority"]["original"], 2)
        self.assertEqual(AWS["priority"]["contributor"], 3)

    def test_counted_authors_are_in_the_inventory(self):
        with open(INVENTORY, encoding="utf-8") as fh:
            keys = {r["key"] for r in csv.DictReader(fh)}
        missing = set()
        for r in self.rows:
            year = d.year(r["year"])
            if r["role"] in AWS["skip"] or year is None or not 1946 <= year <= 2000:
                continue
            for name in d.split_credit(r["author"]):
                if d.fold(name) not in keys:
                    missing.add(name)
        # Every counted author in the period has a candidate row.
        self.assertEqual(missing, set(), sorted(missing)[:10])


class InventoryTest(unittest.TestCase):
    def test_no_surname_first_duplicates(self):
        with open(INVENTORY, encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))
        natural = {d.fold(r["author"]) for r in rows if "," not in r["author"]}
        dupes = [r["author"] for r in rows
                 if "," in r["author"] and d.fold(d.natural_order(r["author"])) in natural]
        self.assertEqual(dupes, [])

    def test_evidence_is_sorted_by_year_then_text(self):
        # Sorting by year alone left ties in hash-seed order, so reruns differed.
        with open(INVENTORY, encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))
        for r in rows:
            ev = [e for e in r["evidence"].split(" | ") if e != "..."]
            self.assertEqual(ev, sorted(ev, key=lambda s: (s[-5:-1], s)), r["key"])

if __name__ == "__main__":
    unittest.main()
