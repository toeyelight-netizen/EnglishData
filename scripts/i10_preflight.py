"""Pre-flight gate for one installment-10 wave file, in about a second.

The full build chain is 22 seconds of machine time but minutes of wall clock,
because `build_installment.py` validates the whole installment and stops at the
first batch of problems. This script runs the *real* checker
(`scripts/strict_checks.py`, the same module the build calls) against a single
wave file, so a wave is proven correct before anything is written.

It adds the checks the build performs that strict_checks does not: collisions
with the database and with the other wave files.

Usage:
    python3 scripts/i10_preflight.py scripts/content/content_i10_wave29.py
    python3 scripts/i10_preflight.py --all
    python3 scripts/i10_preflight.py --all --json

Exit status is 0 when the wave would pass the strict stage of the build.
"""

import argparse
import glob
import importlib
import importlib.util
import json
import os
import re
import sqlite3
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "scripts", "content")
DB = os.path.join(ROOT, "database", "English_Literature_Master.db")
sys.path.insert(0, os.path.join(ROOT, "scripts"))
sys.path.insert(0, CONTENT)

import strict_checks  # noqa: E402  (the build's own gate)


def load(path):
    name = "preflight_" + re.sub(r"\W", "_", os.path.basename(path))
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def key(title):
    s = unicodedata.normalize("NFKD", title or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", s)


def db_state():
    """Authors and title->authors already in the database, if it has been built."""
    if not os.path.exists(DB):
        return {}, {}
    con = sqlite3.connect(DB)
    try:
        graded = {r[0]: r[1] for r in con.execute(
            "select full_name, significance_tier from authors")}
        titles = {}
        for title, name in con.execute(
                "select w.title, a.full_name from works w join work_authors wa "
                "on wa.work_id = w.work_id join authors a on a.author_id = wa.author_id"):
            titles.setdefault(key(title), set()).add(name)
    finally:
        con.close()
    return graded, titles


def wave_files():
    return sorted(glob.glob(os.path.join(CONTENT, "content_i10_wave*.py")))


def check_one(path, meta, graded, db_titles, taken_authors, taken_titles):
    try:
        mod = load(path)
    except Exception as exc:  # a wave that will not import cannot build
        return ["%s: will not import: %s: %s" % (os.path.basename(path), type(exc).__name__, exc)], {}
    authors = list(getattr(mod, "AUTHORS", []))
    works = list(getattr(mod, "WORKS", []))
    name = os.path.basename(path)
    if not authors and not works:
        return ["%s: no AUTHORS or WORKS list" % name], {}

    problems = list(strict_checks.check(works, authors, meta))

    # collisions the strict stage does not see, because it runs on one wave
    for a in authors:
        n = a["name"]
        if n in taken_authors:
            problems.append("author %r: already defined by %s (use an X10 extension)"
                            % (n, taken_authors[n]))
        elif n in graded and graded[n] is None:
            # A graded record is this installment's own (the import refreshes it
            # in place); an ungraded one belongs to an earlier installment.
            problems.append("author %r: already in the database from an earlier installment" % n)
    for w in works:
        t, k = w["title"], key(w["title"])
        if k in taken_titles:
            problems.append("work %r: title also used by %s" % (t, taken_titles[k]))
        owners = db_titles.get(k, set())
        if owners and w["author"] not in owners:
            problems.append("work %r: title already in the database under %s"
                            % (t, ", ".join(sorted(owners))))
    return problems, {a["name"]: name for a in authors} | {key(w["title"]): name for w in works}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    files = args.files or (wave_files() if args.all else [])
    if not files:
        ap.error("give a wave file, or --all")

    meta = importlib.import_module("content_i10").META
    graded, db_titles = db_state()
    taken_authors, taken_titles = {}, {}
    report, total = {}, 0
    for path in files:
        problems, claimed = check_one(path, meta, graded, db_titles, taken_authors, taken_titles)
        taken_authors.update({k: v for k, v in claimed.items() if k and not k.islower()})
        taken_titles.update({k: v for k, v in claimed.items()})
        report[os.path.basename(path)] = problems
        total += len(problems)

    if args.json:
        print(json.dumps({"problems": total, "waves": report}, indent=2, ensure_ascii=False))
    else:
        for name, problems in report.items():
            print("%s: %s" % (name, "PASS" if not problems else "%d problem(s)" % len(problems)))
            for p in problems:
                print("  - " + p)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
