"""Non-destructive installment gate.

``installment_toolkit.check`` compares a batch against the database and is the
right gate before a first import, but it treats any title already present as a
collision, so it cannot be run after a build has been imported (which is
exactly when a re-run must be safe). This script applies the correct rule:
a record is a collision only when the existing database row belongs to a
different author, or when the author row predates this installment.

Usage:
    python scripts/check_installment.py 08 [--check-only]
"""

import argparse
import json
import os
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from installment_toolkit import (  # noqa: E402
    AUTHORSHIP_STATUS, CANONICAL_STATUS, DATE_FIELDS, RESEARCH_STATUS, WORK_KEYS,
    year_num,
)


from build_installment import EXTRA_WORK_COLUMNS  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("installment")
    args = ap.parse_args()
    num = args.installment

    con = sqlite3.connect("database/English_Literature_Master.db")
    try:
        owners = {}
        for title, name in con.execute(
                "select w.title, a.full_name from works w join work_authors wa "
                "on wa.work_id=w.work_id join authors a on a.author_id=wa.author_id"):
            owners.setdefault(title, set()).add(name)
        graded = {r[0] for r in con.execute(
            "select full_name from authors where significance_tier is not null")}
        all_authors = {r[0] for r in con.execute("select full_name from authors")}
        all_titles = {r[0] for r in con.execute("select title from works")}
    finally:
        con.close()

    problems = []
    works, authors = [], []
    for f in sorted(os.listdir("data/works")):
        if f.startswith("installment_%s_works_" % num):
            works += json.load(open("data/works/" + f, encoding="utf-8"))
    for f in sorted(os.listdir("data/authors")):
        if f.startswith("installment_%s_authors" % num):
            authors += json.load(open("data/authors/" + f, encoding="utf-8"))
    maps = {}
    for f in sorted(os.listdir("scripts")):
        if f.startswith("_i%s_map_" % num):
            pass
    sys.path.insert(0, "scripts")
    import importlib
    for f in sorted(os.listdir("scripts")):
        if f.startswith("_i%s_map_" % num) and f.endswith(".py"):
            mod = importlib.import_module(f[:-3])
            for k, v in mod.__dict__.items():
                if k.startswith("MAP_"):
                    maps.update(v)

    titles = [w["title"] for w in works]
    for t in {t for t in titles if titles.count(t) > 1}:
        problems.append("duplicate work title %r" % t)
    for w in works:
        keys = list(w.keys())
        # The 21 core keys in order, optionally followed by declared extra columns
        # (installment 10 onwards: summary, thematic_analysis, critical_context, ...).
        if keys[:len(WORK_KEYS)] != WORK_KEYS or not set(keys[len(WORK_KEYS):]) <= set(EXTRA_WORK_COLUMNS):
            problems.append("schema drift in %r: %s" % (w["title"], keys))
        if w["authorship_status"] not in AUTHORSHIP_STATUS:
            problems.append("bad authorship_status %r" % w["title"])
        if w["canonical_status"] not in CANONICAL_STATUS:
            problems.append("bad canonical_status %r: %r" % (w["title"], w["canonical_status"]))
        if w["research_status"] not in RESEARCH_STATUS:
            problems.append("bad research_status %r" % w["title"])
        for f in DATE_FIELDS:
            if w[f] is not None and not isinstance(w[f], str):
                problems.append("date field %s of %r is not a string" % (f, w["title"]))
        if isinstance(w["principal_characters"], list):
            problems.append("principal_characters of %r is a list" % w["title"])
        # A filled field can still be empty of content. Both of these phrasings
        # are generated, never authored: the first means the authored context
        # was replaced rather than extended (the revision-12 regression), the
        # second is the retired name-extraction fallback, which put composers,
        # dedicatees and book titles into the character lists.
        if (w["historical_context"] or "").startswith("The record dates the work"):
            problems.append("historical_context of %r is generated boilerplate only" % w["title"])
        if "named in the account above" in (w["principal_characters"] or ""):
            problems.append("principal_characters of %r is generated boilerplate" % w["title"])
        c, p = year_num(w["composition_date_start"]), year_num(w["publication_date"])
        if c and p and p < c:
            problems.append("publication %s before composition %s in %r"
                            % (w["publication_date"], w["composition_date_start"], w["title"]))
        for k, v in w.items():
            if v == "":
                problems.append("empty field %s in %r" % (k, w["title"]))
        if w["title"] not in maps:
            problems.append("work %r has no map entry" % w["title"])
            continue
        aus, genres, themes, movements = maps[w["title"]]
        for a in aus:
            if a not in all_authors:
                problems.append("map names unknown author %r (%r)" % (a, w["title"]))
        if w["title"] in all_titles and owners.get(w["title"]) and aus[0] not in owners[w["title"]]:
            problems.append("title %r already belongs to another author" % w["title"])
        if not genres:
            problems.append("work %r has no genre" % w["title"])
        if not themes:
            problems.append("work %r has no theme" % w["title"])

    names = [a["full_name"] for a in authors]
    for n in {n for n in names if names.count(n) > 1}:
        problems.append("duplicate author %r" % n)
    required = ["full_name", "nationality_or_literary_tradition", "literary_identity",
                "biography", "literary_profile", "stylistic_characteristics",
                "intellectual_concerns", "historical_significance",
                "significance_tier", "research_status"]
    for a in authors:
        for k in required:
            if not a.get(k):
                problems.append("author %r missing %s" % (a["full_name"], k))
        if a["full_name"] not in graded and a["full_name"] in all_authors:
            problems.append("author %r predates this installment" % a["full_name"])

    print("installment %s: %d authors, %d works, %d map entries"
          % (num, len(authors), len(works), len(maps)))
    if problems:
        print("PROBLEMS (%d):" % len(problems))
        for p in problems[:60]:
            print("  -", p)
        return 1
    print("CLEAN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
