"""Installment-10 extensions of earlier authors, the single-owner guard, the
bibliography-heading filter, the stale-row check and the taxonomy scope.

These cover the mechanisms that keep one record per author across
installments: an author first recorded by an earlier installment keeps that
record, installment 10 contributes its bibliographic statement through an
extension merged when the earlier installment is built, and the build refuses
to let a later installment redefine (and so silently overwrite) the record.
"""

import copy
import glob
import json
import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, os.path.join(ROOT, "scripts", "content"))

import build_installment as bi  # noqa: E402  (changes into the project root)
import check_duplicates as cd  # noqa: E402
import importlib  # noqa: E402
import i09_taxonomy  # noqa: E402
from installment_toolkit import author_owners  # noqa: E402

HEADING = "Other documented writings, recorded here because no separate work record"


def source_titles():
    titles = set()
    for path in glob.glob(os.path.join(ROOT, "data", "sources", "*.json")):
        titles.update(s["title"] for s in json.load(open(path, encoding="utf-8")))
    return titles


def built(kind, num):
    out = []
    for path in sorted(glob.glob(os.path.join(ROOT, "data", kind, "installment_%s_%s*.json" % (num, kind)))):
        out.extend(json.load(open(path, encoding="utf-8")))
    return out


class OwnershipTest(unittest.TestCase):
    def test_author_owners_maps_each_name_to_its_installments(self):
        with tempfile.TemporaryDirectory() as tmp:
            os.makedirs(os.path.join(tmp, "data", "authors"))
            for num, names in (("08", ["A", "B"]), ("09", ["B", "C"])):
                path = os.path.join(tmp, "data", "authors", "installment_%s_authors_a01.json" % num)
                with open(path, "w", encoding="utf-8") as handle:
                    json.dump([{"full_name": n} for n in names], handle)
            self.assertEqual(author_owners(tmp), {"A": {"08"}, "B": {"08", "09"}, "C": {"09"}})

    def test_only_an_earlier_owner_blocks_a_build(self):
        owners = {"H. G. Wells": {"08", "09"}, "George Orwell": {"09"}}
        self.assertEqual(bi.redefined_authors(["H. G. Wells"], "09", owners), {"H. G. Wells": ["08"]})
        self.assertEqual(bi.redefined_authors(["George Orwell"], "10", owners), {"George Orwell": ["09"]})
        # A later installment's not-yet-rebuilt JSON must not stop the earlier
        # installment, which defines the record, from being rebuilt first.
        self.assertEqual(bi.redefined_authors(["H. G. Wells"], "08", owners), {})

    def test_every_author_in_the_repository_has_exactly_one_owner(self):
        self.assertEqual({n: o for n, o in author_owners(ROOT).items() if len(o) > 1}, {})

    def test_wells_is_a_single_installment_8_record(self):
        owners = author_owners(ROOT)
        self.assertEqual(owners.get("Herbert George Wells"), {"08"})
        self.assertNotIn("H. G. Wells", owners)

    def test_the_authored_wells_uncertainty_still_matches_his_record(self):
        # The sentence is hand-written (his record spans installments 8 and 9),
        # so its counts must be revised if a listed title gains a work record.
        rec = [r for r in built("authors", "08") if r["full_name"] == "Herbert George Wells"][0]
        items = rec["bibliographical_notes"].split(": ", 1)[1].rstrip(".").split("; ")
        self.assertEqual(len(items), 27)
        self.assertTrue(rec["biographical_uncertainty"].startswith("Twenty-seven further writings"))
        self.assertIn("The ten works catalogued here", rec["biographical_uncertainty"])
        titles = {t for t, _ in bi.recorded_works([]).get("Herbert George Wells", [])}
        self.assertEqual(len(titles), 10)


def all_i10_works():
    """Every installment-10 work, gathered as build_installment.main() gathers them."""
    content = os.path.join(bi.PROJECT_ROOT, "scripts", "content")
    works = []
    for name in sorted(f[:-3] for f in os.listdir(content) if f.startswith("content_i10_") and f.endswith(".py")):
        works.extend(getattr(importlib.import_module(name), "WORKS", []))
    return works


class ExtensionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.extensions = bi.load_extensions()
        cls.owners = author_owners(ROOT)
        cls.known = source_titles()
        cls.works = all_i10_works()

    def problems(self, extensions=None, works=None, names=()):
        return bi.extension_problems(
            copy.deepcopy(self.extensions) if extensions is None else extensions, "10", set(names),
            copy.deepcopy(self.works) if works is None else works, self.owners, self.known)

    def test_every_extension_is_valid_and_already_merged(self):
        self.assertTrue({"George Orwell", "Jean Rhys", "Samuel Beckett", "W. H. Auden",
                         "Gwendolyn Brooks"} <= set(self.extensions))
        self.assertEqual(self.problems(), [])

    def test_the_merged_installment_9_records_carry_the_statements(self):
        for name, ext in self.extensions.items():
            with self.subTest(author=name):
                rec = [r for r in built("authors", "09") if r["full_name"] == name][0]
                self.assertEqual(rec["bibliographical_notes"], ext["biblio_note"])
                self.assertEqual(rec["bibliography_status"], ext["bibliography_status"])
                self.assertEqual(rec["verification_status"], ext["verification_status"])
                self.assertFalse([r for r in built("authors", "10") if r["full_name"] == name])

    def test_merge_sets_statement_and_status_and_unions_sources(self):
        author = {"name": "X", "sources": ["S1"]}
        bi.merge_extension(author, {"biblio_note": "note", "bibliography_status": "incomplete",
                                    "verification_status": "unverified", "sources": ["S1", "S2"]})
        self.assertEqual((author["biblio_note"], author["bibliography_status"], author["verification_status"]),
                         ("note", "incomplete", "unverified"))
        self.assertEqual(author["sources"], ["S1", "S2"])

    def test_an_author_without_an_installment_10_work_is_rejected(self):
        works = [w for w in self.works if w["author"] != "George Orwell"]
        self.assertTrue(any("has no installment-10 work" in p for p in self.problems(works=works)))

    def test_a_short_unsourced_or_unmerged_statement_is_rejected(self):
        ext = copy.deepcopy(self.extensions)
        ext["George Orwell"]["biblio_note"] = "Too short."
        ext["George Orwell"]["sources"] = ["No such source"]
        problems = self.problems(extensions=ext)
        self.assertTrue(any("shorter than 200 characters" in p for p in problems))
        self.assertTrue(any("cites unknown source" in p for p in problems))
        self.assertTrue(any("is not merged yet: rebuild installment 09" in p for p in problems))
        ext["George Orwell"]["sources"] = []
        self.assertTrue(any("cites no source" in p for p in self.problems(extensions=ext)))

    def test_an_author_defined_here_or_nowhere_earlier_is_rejected(self):
        ghost = {"Nobody In Particular": dict(self.extensions["George Orwell"], name="Nobody In Particular")}
        self.assertTrue(any("no earlier installment defines" in p for p in self.problems(extensions=ghost)))
        self.assertTrue(any("defined by installment 10 itself" in p
                            for p in self.problems(names={"George Orwell"})))


class BibliographyHeadingTest(unittest.TestCase):
    def test_bib_key_normalises_title_and_reads_the_year(self):
        self.assertEqual(bi._bib_key("The Invisible Man (1897)"), ("invisible man", 1897))
        self.assertEqual(bi._bib_key("The Invisible Man: A Grotesque Romance"), ("invisible man", None))
        self.assertEqual(bi._bib_key("A Modern Utopia (1905, serialised 1904-05)"), ("modern utopia", 1905))

    def test_recorded_titles_are_dropped_and_distinct_editions_kept(self):
        recorded = [("invisible man", 1897), ("poems", 1863)]
        items = ["The Invisible Man (1898)", "Poems (1880, collected)", "Kipps (1905)", "Poems"]
        # within one year, or undated on either side, counts as the recorded work
        self.assertEqual(bi.unrecorded(items, recorded), ["Poems (1880, collected)", "Kipps (1905)"])

    def test_author_note_lists_only_titles_without_records(self):
        author = {"name": "X", "nat": "n", "ident": "i", "bio": "b", "prof": "p", "style": "s",
                  "conc": "c", "sig": "g", "tier": "Minor", "also": ["The Invisible Man (1897)", "Kipps (1905)"]}
        rec = bi.author_record(author, {"X": [("invisible man", 1897)]})
        self.assertTrue(rec["bibliographical_notes"].startswith(HEADING))
        self.assertIn("Kipps (1905)", rec["bibliographical_notes"])
        self.assertNotIn("Invisible Man", rec["bibliographical_notes"])
        rec = bi.author_record(dict(author, also=["The Invisible Man (1897)"]), {"X": [("invisible man", 1897)]})
        self.assertNotIn("bibliographical_notes", rec)

    def test_no_built_heading_names_a_recorded_work(self):
        recorded = bi.recorded_works([])
        offenders = []
        for num in ("08", "09"):
            for rec in built("authors", num):
                note = rec.get("bibliographical_notes") or ""
                if note.startswith(HEADING):
                    items = note.split(": ", 1)[1].rstrip(".").split("; ")
                    kept = bi.unrecorded(items, recorded.get(rec["full_name"], []))
                    offenders += ["%s: %s" % (rec["full_name"], i) for i in items if i not in kept]
        self.assertEqual(offenders, [])


class StaleRowTest(unittest.TestCase):
    KEYS = ({("Pastors and Masters", "single", None), ("Poems", "single", "1590")}, {"Ivy Compton-Burnett"})

    def test_a_row_whose_key_changed_is_reported(self):
        works, authors = cd.stale_rows(
            [(1, "Pastors and Masters", "single", "1940"), (2, "Pastors and Masters", "single", None)],
            ["Ivy Compton-Burnett", "Ghost"], self.KEYS)
        self.assertEqual(works, [(1, "Pastors and Masters", "1940")])
        self.assertEqual(authors, ["Ghost"])

    def test_numeric_and_text_dates_compare_equal(self):
        self.assertEqual(cd.stale_rows([(3, "Poems", "single", 1590)], [], self.KEYS), ([], []))

    def test_the_repository_json_defines_every_record_it_lists(self):
        works, authors = cd.json_keys(cd.PROJECT_ROOT)
        self.assertIn(("Pastors and Masters", "single", None), works)
        self.assertNotIn(("Pastors and Masters", "single", "1940"), works)
        self.assertIn("George Orwell", authors)


class TaxonomyScopeTest(unittest.TestCase):
    def test_installment_9_lookups_ignore_later_vocabularies(self):
        # Installment 10 defines "Dystopian Fiction (1946-2000)"; an installment-9
        # lookup must still resolve to its own single genre.
        self.assertEqual(i09_taxonomy.g("Dystopian Fiction"), ["Dystopian Fiction and the Anti-Utopian Satire"])


class EnrichmentContextTest(unittest.TestCase):
    def test_wells_works_in_installment_9_use_the_installment_8_record(self):
        works = {r["title"]: r for r in built("works", "09")}
        tono = works["Tono-Bungay"]
        self.assertIn("rapid, transparent narrative built for a mass readership", tono["meter_and_prosody"])


if __name__ == "__main__":
    unittest.main()
