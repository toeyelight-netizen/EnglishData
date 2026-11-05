"""Cumulative read-only audit of one installment's JSON before it may be imported.

The gate in installment_toolkit.check() validates ONE batch at a time against the
database vocabulary. This module audits the whole installment at once and asks the
questions that only become visible across batches: duplicate author records, authors
that no work claims, works that no author claims, schema drift in author and source
files, provenance missing from sources, and dates that fall outside the installment's
period.

It never writes to the database and never edits a data file. Exit code is non-zero
if any ERROR-class finding is present; `import_data.py` must not be run until it is.

Usage:
    python scripts/audit_installment.py 07
    python scripts/audit_installment.py 07 --warn-only
"""

import argparse
import glob
import json
import os
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from installment_toolkit import (  # noqa: E402
    AUTHOR_KEYS, CANONICAL_STATUS, DATE_FIELDS, RESEARCH_STATUS, WORK_KEYS,
    authors_for, batch_files, corpus_authors, corpus_titles, db, db_names,
    installment_names, load_maps, load_sources, works_for, year_num,
)

AUTHORSHIP_STATUS = {"single", "anonymous", "collaborative", "attributed", "disputed"}
SOURCE_KEYS = ["title", "author_or_editor", "publisher", "publication_year",
               "source_type", "reliability_notes"]
LIST_FIELDS = ("alternative_names", "pseudonyms", "major_influences")


def db_column(table, column):
    """Distinct values of one identifying column, for collision checks against the DB.

    installment_toolkit.db_names() assumes a 'name' column, which only the taxonomy
    tables have; authors use full_name and sources use title.
    """
    con = db()
    try:
        return {r[0] for r in con.execute("select %s from %s" % (column, table)) if r[0]}
    finally:
        con.close()


class Audit:
    def __init__(self):
        self.error = []
        self.warn = []

    def e(self, message):
        self.error.append(message)

    def w(self, message):
        self.warn.append(message)


def source_files(installment):
    return sorted(glob.glob("data/sources/installment_%s_sources*.json" % installment))


def audit_works(installment, a):
    seen = {}
    already = corpus_titles()
    for path in batch_files(installment):
        for w in json.load(open(path, encoding="utf-8")):
            t = w["title"]
            slug = os.path.basename(path)
            if list(w.keys()) != WORK_KEYS:
                a.e("WORKS %s/%s: key order drift" % (slug, t))
            if t in seen:
                a.e("WORKS duplicate title in both %s and %s: %r" % (seen[t], slug, t))
            seen[t] = slug
            if t in already:
                a.e("WORKS already in database: %r" % t)
            for f in DATE_FIELDS:
                v = w.get(f)
                if v is not None and not isinstance(v, str):
                    a.e("WORKS %s/%s: %s=%r must be a string year" % (slug, t, f, v))
            for f in ("alternative_titles",):
                if isinstance(w.get(f), str):
                    a.e("WORKS %s/%s: %s must be a JSON list or null" % (slug, t, f))
            if isinstance(w.get("principal_characters"), list):
                a.e("WORKS %s/%s: principal_characters must be a string" % (slug, t))
            if w.get("authorship_status") not in AUTHORSHIP_STATUS:
                a.e("WORKS %s/%s: authorship_status=%r" % (slug, t, w.get("authorship_status")))
            if w.get("canonical_status") not in CANONICAL_STATUS:
                a.e("WORKS %s/%s: canonical_status=%r" % (slug, t, w.get("canonical_status")))
            if w.get("research_status") not in RESEARCH_STATUS:
                a.e("WORKS %s/%s: research_status=%r" % (slug, t, w.get("research_status")))
            for k, v in w.items():
                if v == "":
                    a.e("WORKS %s/%s: empty string in %s (use null)" % (slug, t, k))
            c = year_num(w.get("composition_date_start"))
            e = year_num(w.get("composition_date_end"))
            p = year_num(w.get("publication_date"))
            if c and e and e < c:
                a.e("WORKS %s/%s: composition end %s before start %s" % (slug, t, e, c))
            if c and p and p < c:
                a.e("WORKS %s/%s: publication %s before composition start %s" % (slug, t, p, c))
            if p is None and c is None and year_num(w.get("first_performance_date")) is None:
                a.w("WORKS %s/%s: no date at all in any date field" % (slug, t))
    return seen


def audit_authors(installment, a):
    files = sorted(glob.glob("data/authors/installment_%s_authors*.json" % installment))
    owner = {}
    in_db = corpus_authors()
    for path in files:
        payload = json.load(open(path, encoding="utf-8"))
        slug = os.path.basename(path)
        if isinstance(payload, dict):
            payload = payload.get("authors", payload.get("data", []))
            a.e("AUTHORS %s: wrapped in an object; import_data.load_json_files() "
                "silently skips a non-list payload" % slug)
        for r in payload:
            n = r.get("full_name")
            if list(r.keys()) != AUTHOR_KEYS:
                a.e("AUTHORS %s/%s: key order drift" % (slug, n))
            if n in owner:
                a.e("AUTHORS duplicate record for %r in %s and %s" % (n, owner[n], slug))
            owner[n] = slug
            if n in in_db:
                a.e("AUTHORS %r already exists in the database" % n)
            for f in ("birth_date", "death_date"):
                v = r.get(f)
                if v is not None and not isinstance(v, str):
                    a.e("AUTHORS %s/%s: %s=%r must be a string year" % (slug, n, f, v))
            for f in ("birth_date_approximate", "death_date_approximate"):
                if not isinstance(r.get(f), bool):
                    a.e("AUTHORS %s/%s: %s must be a JSON boolean" % (slug, n, f))
            for f in LIST_FIELDS:
                if not isinstance(r.get(f), list):
                    a.e("AUTHORS %s/%s: %s must be a JSON list (or [])" % (slug, n, f))
            if r.get("research_status") not in RESEARCH_STATUS:
                a.e("AUTHORS %s/%s: research_status=%r" % (slug, n, r.get("research_status")))
            for k, v in r.items():
                if v == "":
                    a.e("AUTHORS %s/%s: empty string in %s (use null or [])" % (slug, n, k))
            b, d = year_num(r.get("birth_date")), year_num(r.get("death_date"))
            if b and d and d < b:
                a.e("AUTHORS %s/%s: death %s before birth %s" % (slug, n, d, b))
            if r.get("biography") and len(r["biography"]) < 150:
                a.w("AUTHORS %s/%s: biography is only %d characters" % (slug, n, len(r["biography"])))
    return owner, files


def audit_sources(installment, a):
    seen = {}
    rows = []
    already = db_column("sources", "title")
    for path in source_files(installment):
        slug = os.path.basename(path)
        for s in json.load(open(path, encoding="utf-8")):
            rows.append((slug, s))
            t = s["title"]
            if t in seen:
                a.e("SOURCES duplicate record for %r in %s and %s" % (t, seen[t], slug))
            seen[t] = slug
            if list(s.keys())[:6] != SOURCE_KEYS:
                a.e("SOURCES %s/%s: key order drift" % (slug, t))
            if not isinstance(s.get("publication_year"), int):
                a.e("SOURCES %s/%s: publication_year=%r must be an integer" % (slug, t, s.get("publication_year")))
            if not (s.get("reliability_notes") or "").strip():
                a.e("SOURCES %s/%s: no reliability_notes" % (slug, t))
            if not (s.get("publisher") or "").strip():
                if s.get("source_type") in ("periodical", "archive"):
                    a.w("SOURCES %s/%s: no publisher — long-running serials and archives "
                        "changed imprint, so none is asserted (schema allows null)" % (slug, t))
                else:
                    a.e("SOURCES %s/%s: no publisher" % (slug, t))
            if not (s.get("url") or "").strip():
                if s.get("source_type") == "archive":
                    a.e("SOURCES %s/%s: a digital archive with no url cannot be retrieved" % (slug, t))
                else:
                    a.w("SOURCES %s/%s: no url (installments 1-6 record urls for only "
                        "5 of 77 sources; reliability_notes carries the provenance)" % (slug, t))
            if t in already:
                a.e("SOURCES %r already exists in the database" % t)
    return rows


def audit_links(installment, titles, author_owner, a):
    merged, _ = load_maps(installment)
    statuses = {w["title"]: w.get("authorship_status") for w in works_for(installment)}
    names = set(author_owner) | corpus_authors()
    tax = installment_names(installment)
    vocab = {
        "genres": tax["genres"] | db_names("genres"),
        "themes": tax["themes"] | db_names("themes"),
        "movements": tax["movements"] | db_names("movements"),
    }
    for t in titles:
        if t not in merged:
            a.e("MAPS work %r has no map entry" % t)
    for t, entry in merged.items():
        if t not in titles:
            a.e("MAPS map entry %r has no work record" % t)
            continue
        aus, genres, themes, movements = entry
        if statuses.get(t) == "anonymous" and aus:
            a.e("MAPS %r is recorded as anonymous but the map names %s; validate_database "
                "rejects the row after import" % (t, ", ".join(aus)))
        if not aus:
            a.w("MAPS %r is linked to no author" % t)
        for n in aus:
            if n not in names:
                a.e("MAPS %r names an author with no record: %r" % (t, n))
        if not genres:
            a.e("MAPS %r has no genre" % t)
        if not themes:
            a.e("MAPS %r has no theme" % t)
        for kind, xs in (("genres", genres), ("themes", themes), ("movements", movements)):
            for x in xs:
                if x not in vocab[kind]:
                    a.e("MAPS %r names an unknown %s %r" % (t, kind[:-1], x))
    linked = {n for entry in merged.values() for n in entry[0]}
    for n, slug in sorted(author_owner.items()):
        if n not in linked:
            a.w("AUTHORS %r (%s) is claimed by no work in this installment" % (n, slug))


def audit_period(installment, a):
    paths = sorted(glob.glob("data/periods/installment_%s_periods.json" % installment))
    if len(paths) != 1:
        a.e("PERIOD expected exactly one period file, found %s" % paths)
        return None
    rows = json.load(open(paths[0], encoding="utf-8"))
    if len(rows) != 1:
        a.e("PERIOD %s has %d rows; an installment adds one period" % (paths[0], len(rows)))
        return None
    p = rows[0]
    if p["name"] in db_names("periods"):
        a.e("PERIOD %r already exists in the database" % p["name"])
    lo, hi = year_num(p.get("start_year")), year_num(p.get("end_year"))
    if not lo or not hi or hi <= lo:
        a.e("PERIOD %r has unusable span %s-%s" % (p["name"], lo, hi))
    for f in ("description", "historical_context", "literary_characteristics"):
        if not (p.get(f) or "").strip():
            a.e("PERIOD %r: empty %s" % (p["name"], f))
    return lo, hi, p["name"]


def audit_taxonomy(installment, a):
    """Every taxonomy column is a string or an integer in the schema.

    A JSON list here aborts the INSERT inside import_data.py with a SQLite
    binding error, which is a confusing place to discover a data defect.
    """
    for kind in ("movements", "genres", "themes"):
        for path in sorted(glob.glob("data/%s/installment_%s_*.json" % (kind, installment))):
            slug = os.path.basename(path)
            for r in json.load(open(path, encoding="utf-8")):
                n = r.get("name")
                for f, v in r.items():
                    if isinstance(v, list):
                        a.e("TAXONOMY %s/%s: %s is a JSON list; %s columns are plain "
                            "strings and the INSERT will fail (join with '; ')"
                            % (slug, n, f, kind[:-1]))
                    if isinstance(v, int) and f not in ("start_year", "end_year"):
                        a.e("TAXONOMY %s/%s: %s=%r is a JSON number in a text column"
                            % (slug, n, f, v))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("installment")
    ap.add_argument("--warn-only", action="store_true",
                    help="report findings but exit 0 (used for progress reporting, never for import)")
    args = ap.parse_args(argv)

    a = Audit()
    titles = audit_works(args.installment, a)
    author_owner, author_files = audit_authors(args.installment, a)
    sources = audit_sources(args.installment, a)
    audit_links(args.installment, titles, author_owner, a)
    span = audit_period(args.installment, a)
    audit_taxonomy(args.installment, a)

    if span:
        lo, hi, name = span
        for w in works_for(args.installment):
            y = (year_num(w.get("composition_date_start")) or year_num(w.get("publication_date"))
                 or year_num(w.get("first_performance_date")))
            if y is None:
                continue
            if not lo - 5 <= y <= hi + 5:
                a.w("PERIOD %r dated %s sits outside %s (%d-%d)"
                    % (w["title"], y, name, lo, hi))

    ws = works_for(args.installment)
    print("AUDIT installment %s" % args.installment)
    print("  works        : %d in %d batch files" % (len(ws), len(batch_files(args.installment))))
    print("  authors      : %d in %d files" % (len(author_owner), len(author_files)))
    print("  sources      : %d records" % len(sources))
    print("  map entries  : %d" % len(load_maps(args.installment)[0]))
    print("  errors       : %d" % len(a.error))
    print("  warnings     : %d" % len(a.warn))
    for m in a.error:
        print("  ERROR  " + m)
    for m in a.warn:
        print("  warn   " + m)
    if a.error and not args.warn_only:
        print("RESULT: BLOCKED - do not import until the errors are cleared")
        return 1
    print("RESULT: %s" % ("IMPORT MAY PROCEED" if not a.error else "errors present, warnings only"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
