"""The installment-10 discovery inventory: name normalisation, the curated
lists (African Writers Series, Commonwealth Writers' Prize, Caribbean Writers
Series) and the reproducibility of the generated CSV.

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


def _list(fname):
    with open(os.path.join(ROOT, "research", "installment_10", "lists", fname), encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


class CuratedListsTest(unittest.TestCase):
    def test_every_role_is_counted_or_skipped(self):
        for fname, spec in d.CURATED.items():
            with open(os.path.join(ROOT, "research", "installment_10", "lists", fname), encoding="utf-8") as fh:
                roles = {r["role"] for r in csv.DictReader(fh)}
            self.assertEqual(roles - set(spec["priority"]) - set(spec.get("skip", ())), set(), fname)

    def test_commonwealth_prize_list(self):
        with open(os.path.join(ROOT, "research", "installment_10", "lists",
                               "commonwealth_writers_prize_1987_2000.csv"), encoding="utf-8") as fh:
            rows = list(csv.DictReader(fh))
        overall = [r["year"] for r in rows if r["role"] == "best_book_overall"]
        first = [r["year"] for r in rows if r["role"] == "best_first_book_overall"]
        # One overall Best Book winner a year from 1987, one overall Best First Book from 1989.
        self.assertEqual(sorted(overall), [str(y) for y in range(1987, 2001)])
        self.assertEqual(sorted(first), [str(y) for y in range(1989, 2001)])
        spec = d.CURATED["commonwealth_writers_prize_1987_2000.csv"]
        sample = next(r for r in rows if r["author"] == "Erna Brodber")
        self.assertEqual(spec["hint"](sample), "Jamaica (Commonwealth Writers' Prize)")
        self.assertEqual(spec["evidence"](sample),
                         "Commonwealth Writers' Prize, Best Book, Canada and the Caribbean (regional winner): Myal")


    def test_curated_authors_are_in_the_inventory(self):
        with open(INVENTORY, encoding="utf-8") as fh:
            datasets = {r["key"]: set(r["datasets"].split("; ")) for r in csv.DictReader(fh)}
        for fname, spec in d.CURATED.items():
            rows = _list(fname)
            missing, outside = set(), set()
            for r in rows:
                year = d.year(r["year"])
                names = d.split_credit(r["author"]) if r["author"] else []
                if r["role"] in spec.get("skip", ()) or year is None or not 1946 <= year <= 2000:
                    outside.update(d.fold(n) for n in names)
                    continue
                for name in names:
                    if spec["dataset"] not in datasets.get(d.fold(name), set()):
                        missing.add(name)
            # Every counted author in the period carries the list's dataset label (David
            # Harry Walker would be dropped as the abolitionist David Walker, d. 1830) ...
            self.assertEqual(missing, set(), (fname, sorted(missing)[:10]))
            # ... and an author with no counted entry does not (Paulette Ramsay's Aunt Jen
            # is of 2002, not of 1970 as the source table says; Gabrielle Roy's
            # Governor General's Awards were for translations).
            counted = {d.fold(n) for r in rows for n in (d.split_credit(r["author"]) if r["author"] else [])
                       if r["role"] not in spec.get("skip", ()) and d.year(r["year"]) and 1946 <= d.year(r["year"]) <= 2000}
            for key in outside - counted:
                self.assertNotIn(spec["dataset"], datasets.get(key, set()), (fname, key))

    def test_national_prize_lists(self):
        def by_year(rows, roles):
            out = {}
            for r in rows:
                if r["role"] in roles:
                    out.setdefault(int(r["year"]), []).append(r)
            return out
        sahitya = _list("sahitya_akademi_award_english_1960_2000.csv")
        years = [int(r["year"]) for r in sahitya]
        self.assertEqual(len(years), len(set(years)))           # one winner a year, 30 awards to 2000
        self.assertEqual(len(years), 30)
        self.assertEqual((sahitya[0]["author"], sahitya[0]["title"]), ("R. K. Narayan", "The Guide"))
        self.assertTrue({r["category"] for r in sahitya} <= {"Novel", "Poetry", "Biography", "Autobiography",
                                                             "Essays", "Drama"})
        gg = _list("governor_generals_award_english_fiction_1946_2000.csv")
        top = by_year(gg, {"winner", "winner_translation", "no_award"})
        self.assertEqual(sorted(top), list(range(1946, 2001)))  # every year has a result
        self.assertEqual(sorted(y for y, v in top.items() if len(v) > 1), [1968])
        self.assertEqual(sorted(top[y][0]["role"] for y in (1965, 1967)), ["no_award", "no_award"])
        finalists = by_year(gg, {"finalist"})
        self.assertEqual(min(finalists), 1979)                   # shortlists announced from 1979 ...
        self.assertNotIn(1981, finalists)                        # ... except for 1981
        miles = _list("miles_franklin_award_1957_2000.csv")
        mf = by_year(miles, {"winner", "withheld"})
        self.assertEqual(sorted(mf), [y for y in range(1957, 2001) if y != 1988])
        self.assertEqual(sorted(y for y, v in mf.items() if v[0]["role"] == "withheld"), [1973, 1983])
        self.assertEqual(sorted(y for y, v in mf.items() if len(v) > 1), [1962, 2000])
        pd = _list("pulitzer_prize_drama_1946_2000.csv")
        result = by_year(pd, {"winner", "winner_musical_book_or_lyrics", "no_award"})
        self.assertEqual(sorted(result), list(range(1946, 2001)))
        self.assertEqual(sorted(y for y, v in result.items() if v[0]["role"] == "no_award"),
                         [1947, 1951, 1963, 1964, 1966, 1968, 1972, 1974, 1986, 1997])
        self.assertEqual(min(by_year(pd, {"finalist"})), 1983)
        qgm = _list("queens_gold_medal_poetry_1952_2000.csv")
        self.assertEqual(len({r["year"] for r in qgm}), len(qgm))
        es = _list("evening_standard_award_best_play_1955_2000.csv")
        self.assertTrue(all(int(r["year"]) == 1954 + int(r["ceremony"]) for r in es))
        self.assertEqual({int(r["ceremony"]) for r in es}, set(range(1, 47)))

    def test_labelled_evidence(self):
        es = d.CURATED["evening_standard_award_best_play_1955_2000.csv"]
        row = next(r for r in _list("evening_standard_award_best_play_1955_2000.csv") if r["title"] == "The Caretaker")
        self.assertEqual(es["evidence"](row), "Evening Standard Theatre Award for Best Play (winner, ceremony 6): The Caretaker")
        qgm = d.CURATED["queens_gold_medal_poetry_1952_2000.csv"]
        row = next(r for r in _list("queens_gold_medal_poetry_1952_2000.csv") if r["author"] == "Sorley MacLean")
        self.assertEqual(qgm["evidence"](row), "Queen's Gold Medal for Poetry (recipient; a poet in Scottish Gaelic)")
        self.assertEqual(qgm["priority"][row["role"]], 2)
        sa = d.CURATED["sahitya_akademi_award_english_1960_2000.csv"]
        row = _list("sahitya_akademi_award_english_1960_2000.csv")[0]
        self.assertEqual(sa["evidence"](row), "Sahitya Akademi Award for English (winner, novel): The Guide")


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
