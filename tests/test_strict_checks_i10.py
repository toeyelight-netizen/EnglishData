"""The installment-10 strict gate must reject thin, templated, out-of-period or unsourced records."""

import copy
import os
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "content"))

import content_i10  # noqa: E402
import content_i10_wave01 as wave  # noqa: E402
from strict_checks import check  # noqa: E402


class StrictChecksTest(unittest.TestCase):
    def run_check(self, works=None, authors=None):
        return check(works if works is not None else copy.deepcopy(wave.WORKS),
                     authors if authors is not None else copy.deepcopy(wave.AUTHORS), content_i10.META)

    def mutated(self, title, **changes):
        works = copy.deepcopy(wave.WORKS)
        for w in works:
            if w["title"] == title:
                w.update(changes)
        return works

    def assertRejected(self, works=None, authors=None, needle=""):
        problems = self.run_check(works, authors)
        self.assertTrue(problems, "expected the strict gate to reject the record")
        if needle:
            self.assertTrue(any(needle in p for p in problems), problems)

    def test_pilot_wave_passes(self):
        self.assertEqual(self.run_check(), [])

    def test_major_plot_too_short_is_rejected(self):
        self.assertRejected(self.mutated("Invisible Man", plot="A young man goes north and is disillusioned."))

    def test_boilerplate_is_rejected(self):
        self.assertRejected(self.mutated("Going to the Territory",
                                         desc="This work explores themes of identity. " * 6))

    def test_year_outside_period_is_rejected(self):
        self.assertRejected(self.mutated("Juneteenth", pub="2010"))

    def test_verified_without_sources_is_rejected(self):
        self.assertRejected(self.mutated("Shadow and Act", verification_status="verified", sources=[]))

    def test_unknown_source_is_rejected(self):
        self.assertRejected(self.mutated("Shadow and Act", sources=["A source nobody consulted"]))

    def test_undefined_genre_is_rejected(self):
        self.assertRejected(self.mutated("Juneteenth", genres=["Not A Genre"]))

    def test_sentence_repeated_across_works_is_rejected(self):
        works = copy.deepcopy(wave.WORKS)
        shared = works[0]["ctx"]
        works[1]["ctx"] = shared
        self.assertRejected(works)

    def test_theorist_names_are_not_mistaken_for_banned_words(self):
        # 'todo' is banned as a placeholder, but must not fire inside 'Todorov'.
        works = self.mutated("Shadow and Act", crit=wave.WORKS[1]["crit"]
                             + " Tzvetan Todorov's later structuralism offers a contrasting model of genre.")
        self.assertEqual(self.run_check(works), [])

    def test_sentence_repeated_within_a_field_is_rejected(self):
        self.assertRejected(self.mutated("Juneteenth", struct=wave.WORKS[5]["struct"] + " "
                                         + "The chapters alternate between past and present. " * 2),
                            needle="repeated within")

    def test_author_without_bibliography_status_is_rejected(self):
        authors = copy.deepcopy(wave.AUTHORS)
        authors[0]["bibliography_status"] = "unknown"
        self.assertRejected(authors=authors, needle="bibliography_status")


if __name__ == "__main__":
    unittest.main()
