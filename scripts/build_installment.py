"""Build one installment's research JSON from a compact content module.

The research content for installments 8-10 is authored in
``scripts/content_iNN.py`` as two plain Python lists (``AUTHORS`` and
``WORKS``) plus a ``META`` dict. This script expands them into exactly the
files and schemas that ``scripts/import_data.py`` consumes, so the schemas
stay identical to installments 1-7:

    data/authors/installment_NN_authors_<batch>.json      (AUTHOR_KEYS order)
    data/works/installment_NN_works_batch<batch>.json     (WORK_KEYS order)
    scripts/_iNN_map_b<batch>.py                          (toolkit maps)
    data/relationships/installment_NN_relationships_works.json
    data/relationships/installment_NN_relationships_authors.json
    data/relationships/installment_NN_relationships_sources_editions.json

Everything generated here is deterministic, so re-running the builder is
idempotent. It validates before writing: unresolved taxonomy names, duplicate
authors or titles, colliding titles already in the corpus, and bad controlled
vocabularies all abort the build with a non-zero exit code.

Usage:
    python scripts/build_installment.py 08 [--check-only]
"""

import argparse
import glob
import importlib
import json
import os
import re
import sqlite3
import sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "scripts"))

from installment_toolkit import (  # noqa: E402
    AUTHOR_KEYS, CANONICAL_STATUS, OPTIONAL_AUTHOR_AUDIT_KEYS, OPTIONAL_AUTHOR_KEYS, RESEARCH_STATUS,
    SIGNIFICANCE_TIERS, WORK_KEYS, author_owners, authors_for,
)

DB_PATH = "database/English_Literature_Master.db"


# --------------------------------------------------------------- validation
def db_names(table):
    con = sqlite3.connect(DB_PATH)
    try:
        return {r[0] for r in con.execute("select name from " + table) if r[0]}
    finally:
        con.close()


def db_corpus():
    con = sqlite3.connect(DB_PATH)
    try:
        titles = {r[0] for r in con.execute("select title from works")}
        authors = {r[0] for r in con.execute("select full_name from authors")}
        sources = {r[0] for r in con.execute("select title from sources")}
    finally:
        con.close()
    return titles, authors, sources


def installment_taxonomy(num):
    out = {}
    for kind in ("movements", "genres", "themes"):
        names = set()
        for name in sorted(os.listdir("data/%s" % kind)):
            if name.startswith("installment_%s_" % num) and name.endswith(".json"):
                for row in json.load(open("data/%s/%s" % (kind, name), encoding="utf-8")):
                    names.add(row["name"])
        out[kind] = names
    return out


# ------------------------------------------------------------------ shaping
EXTRA_WORK_COLUMNS = ("summary", "significance", "provenance_and_manuscripts",
                      "editions", "modern_translations", "related_works",
                      "manuscript_locations", "research_notes",
                      # installment 10 onwards (migration f5a6b7c8d9e0)
                      "thematic_analysis", "critical_context", "verification_status")


def work_record(w):
    """Expand one content-module work dict into the 21-key WORK_KEYS record.

    Optional extras (``extra``) may only use columns that exist on ``works``.
    """
    comp = w.get("composition")
    for key in (w.get("extra") or {}):
        if key not in EXTRA_WORK_COLUMNS:
            raise SystemExit("work %r: unknown extra column %r" % (w["title"], key))
    record = {
        "title": w["title"],
        "alternative_titles": list(w.get("alt") or []),
        "authorship_status": w.get("as_status", "single"),
        "composition_date_start": comp[0] if comp else None,
        "composition_date_end": comp[1] if comp and len(comp) > 1 else None,
        "publication_date": w.get("pub"),
        "first_performance_date": w.get("perf"),
        "manuscript_date": w.get("ms"),
        "original_language": w.get("lang", "English"),
        "description": w["desc"],
        "plot_or_argument": w.get("plot"),
        "narrative_structure": w.get("struct"),
        "principal_characters": w.get("chars"),
        "literary_form": w["form"],
        "meter_and_prosody": w.get("meter"),
        "historical_context": w["ctx"],
        "literary_significance": w["sigtext"],
        "attribution_notes": w.get("attrib"),
        "bibliographical_notes": w.get("biblio"),
        "canonical_status": w.get("canon", "Secondary canon"),
        "research_status": w.get("status", "complete"),
    }
    for key, value in (w.get("extra") or {}).items():
        record[key] = value
    return record


def _bib_key(title):
    """(normalised title, year) for matching bibliography items to work records:
    a trailing parenthesis (year, venue) and any subtitle are dropped, a leading
    article is ignored, punctuation is removed."""
    year = re.search(r"\((\d{4})", title or "")
    text = re.sub(r"\s*\([^)]*\)\s*$", "", title or "").split(":")[0].lower()
    text = re.sub(r"^(the|a|an)\s+", "", text.strip())
    return re.sub(r"[^a-z0-9 ]", "", text).strip(), (int(year.group(1)) if year else None)


def recorded_works(works):
    """Author name -> [(normalised title, year)] for every work record: this
    build's own works plus every installment's built JSON."""
    out = {}
    def add(author, title, year):
        out.setdefault(author, []).append((_bib_key(title)[0], year))
    for w in works:
        y = re.search(r"\d{4}", str(w.get("pub") or ""))
        for name in [w["author"]] + list(w.get("coauthors") or []):
            add(name, w["title"], int(y.group(0)) if y else None)
    years = {}
    for path in glob.glob(os.path.join("data", "works", "installment_*_works*.json")):
        payload = json.load(open(path, encoding="utf-8"))
        for r in (payload.get("works", []) if isinstance(payload, dict) else payload):
            y = re.search(r"\d{4}", str(r.get("publication_date") or ""))
            years.setdefault(r["title"], set()).add(int(y.group(0)) if y else None)
    for path in glob.glob(os.path.join("data", "relationships", "installment_*_relationships_works.json")):
        for row in json.load(open(path, encoding="utf-8")).get("work_authors", []):
            for y in years.get(row["work"], {None}):
                add(row["author"], row["work"], y)
    return out


def unrecorded(items, recorded):
    """The bibliography items that have no work record of their own (same
    normalised title and, where both are dated, a year within one)."""
    keep = []
    for item in items:
        title, year = _bib_key(item)
        if not any(t == title and (year is None or y is None or abs(year - y) <= 1)
                   for t, y in recorded):
            keep.append(item)
    return keep


def author_record(a, recorded=None):
    rec = {
        "full_name": a["name"],
        "alternative_names": list(a.get("alt") or []),
        "pseudonyms": list(a.get("pseudo") or []),
        "birth_date": a.get("b"),
        "birth_date_approximate": bool(a.get("b_approx", False)),
        "death_date": a.get("d"),
        "death_date_approximate": bool(a.get("d_approx", False)),
        "birthplace": a.get("bp"),
        "nationality_or_literary_tradition": a["nat"],
        "literary_identity": a["ident"],
        "biography": a["bio"],
        "literary_profile": a["prof"],
        "stylistic_characteristics": a["style"],
        "intellectual_concerns": a["conc"],
        "historical_significance": a["sig"],
        "major_influences": list(a.get("infl") or []),
        "biographical_uncertainty": a.get("unc"),
        "research_status": a.get("status", "complete"),
        "significance_tier": a["tier"],
    }
    # Works that are documented but that cannot honestly carry a full record are
    # listed on the author under a bibliography heading, so the record states the
    # known output without inventing a schema for lost or unverifiable titles.
    if a.get("biblio_note"):
        # Installment 10: an authored statement of bibliographic coverage.
        rec["bibliographical_notes"] = a["biblio_note"]
    elif a.get("also"):
        # The heading says these titles have no work record of their own, so any
        # title that does have one (in any installment) is left out of the list:
        # 343 author notes in installments 8-9 had named 876 recorded works
        # under this heading before the filter was added.
        others = unrecorded(a["also"], (recorded or {}).get(a["name"], []))
        if others:
            rec["bibliographical_notes"] = (
                "Other documented writings, recorded here because no separate work "
                "record with a verifiable description can be supported: "
                + "; ".join(others) + ".")
    for key in OPTIONAL_AUTHOR_AUDIT_KEYS:
        if a.get(key):
            rec[key] = a[key]
    return rec



# ------------------------------------------------- cross-installment authors
def load_extensions():
    """Installment-10 extensions of authors defined by earlier installments.

    ``scripts/content/i10_extensions.py`` holds, for each such author with
    works in 1946-2000, the authored statement of bibliographic coverage (now
    spanning the whole career), its status, the verification status and the
    sources consulted. The author keeps the single record defined by the
    installment that first recorded them: the extension is merged into that
    record when that installment is built, so no installment's JSON goes stale
    and no second author record is ever written.
    """
    try:
        mod = importlib.import_module("i10_extensions")
    except ModuleNotFoundError:
        return {}
    out = {}
    for ext in getattr(mod, "EXTENSIONS", []):
        if ext["name"] in out:
            raise SystemExit("duplicate installment-10 extension for %r" % ext["name"])
        out[ext["name"]] = ext
    return out


def merge_extension(author, ext):
    """Merge an installment-10 extension into the author dict that defines the record."""
    author["biblio_note"] = ext["biblio_note"]
    author["bibliography_status"] = ext["bibliography_status"]
    author["verification_status"] = ext["verification_status"]
    author["sources"] = list(dict.fromkeys(list(author.get("sources") or []) + list(ext["sources"])))
    return author


def redefined_authors(names, num, owners):
    """Names this installment defines that an EARLIER installment's built JSON defines.

    Only earlier owners block the build: the importer upserts authors in
    installment order, so it is the later definition that silently overwrites
    the earlier one. A later installment whose JSON still defines the name (for
    instance before it has been rebuilt after a duplicate was merged into this
    one) is reported by ``check_installment.py``, which looks both ways; not
    blocking here is what allows the earlier installment to be rebuilt first.
    """
    out = {}
    for n in names:
        earlier = sorted(o for o in owners.get(n, set()) if int(o) < int(num))
        if earlier:
            out[n] = earlier
    return out


def extension_problems(extensions, num, names, works, owners, known_sources):
    """Validate the installment-10 extensions while building installment 10."""
    problems = []
    for n, ext in sorted(extensions.items()):
        defined_by = sorted(owners.get(n, set()) - {num})
        if n in names:
            problems.append("extension %r names an author defined by installment %s itself" % (n, num))
        if not defined_by:
            problems.append("extension %r: no earlier installment defines this author" % n)
            continue
        if not any(w["author"] == n or n in (w.get("coauthors") or []) for w in works):
            problems.append("extension %r: the author has no installment-%s work" % (n, num))
        if len((ext.get("biblio_note") or "").strip()) < 200:
            problems.append("extension %r: bibliography statement missing or shorter than 200 characters" % n)
        if ext.get("verification_status") in ("verified", "partially verified") and not ext.get("sources"):
            problems.append("extension %r: marked %s but cites no source" % (n, ext["verification_status"]))
        for s in ext.get("sources") or []:
            if s not in known_sources:
                problems.append("extension %r cites unknown source %r" % (n, s))
        # The statement reaches the database through the defining installment's
        # JSON, so that installment must have been rebuilt since the last edit.
        built = [r for r in authors_for(defined_by[0]) if r["full_name"] == n]
        if not built or any(built[0].get(k) != v for k, v in (
                ("bibliographical_notes", ext["biblio_note"]),
                ("bibliography_status", ext["bibliography_status"]),
                ("verification_status", ext["verification_status"]))):
            problems.append("extension %r is not merged yet: rebuild installment %s, then this one"
                            % (n, defined_by[0]))
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("installment", help="two-digit installment number, e.g. 08")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    num = args.installment

    # Content lives in one content_iNN.py (META + optional inline lists) and any
    # number of content_iNN_a*/content_iNN_w*.py part modules, which are
    # concatenated in filename order so the output is deterministic.
    sys.path.insert(0, os.path.join(PROJECT_ROOT, "scripts", "content"))
    mod = importlib.import_module("content_i%s" % num)
    authors, works, meta = list(getattr(mod, "AUTHORS", [])), list(getattr(mod, "WORKS", [])), mod.META
    parts = sorted(
        f[:-3] for f in os.listdir(os.path.join(PROJECT_ROOT, "scripts", "content"))
        if f.startswith("content_i%s_" % num) and f.endswith(".py")
    )
    for name in parts:
        part = importlib.import_module(name)
        authors.extend(getattr(part, "AUTHORS", []))
        works.extend(getattr(part, "WORKS", []))
    if not authors or not works:
        raise SystemExit("no content for installment %s" % num)
    extensions = load_extensions()
    if int(num) < 10:
        for a in authors:
            if a["name"] in extensions:
                merge_extension(a, extensions[a["name"]])

    problems = []
    tax = installment_taxonomy(num)
    known = {k: db_names(k) | tax[k] for k in ("movements", "genres", "themes")}
    corpus_titles, corpus_authors, corpus_sources = db_corpus()

    # --- authors
    names = [a["name"] for a in authors]
    for n in sorted({n for n in names if names.count(n) > 1}):
        problems.append("duplicate author in module: %r" % n)
    # Same rule as for titles: a name already in the database is only a
    # problem when the existing record belongs to an earlier installment (its
    # significance_tier is NULL). A record this installment already imported is
    # refreshed in place, which is what makes repeated builds idempotent.
    con = sqlite3.connect(DB_PATH)
    try:
        graded = {r[0] for r in con.execute(
            "select full_name from authors where significance_tier is not null")}
    finally:
        con.close()
    for n in sorted(set(names) & (corpus_authors - graded)):
        problems.append("author already in database: %r" % n)
    # The rule above cannot see an author graded by an earlier installment (8
    # onwards set significance_tier), which would otherwise pass as a refresh and
    # silently overwrite that installment's record on import.
    owners = author_owners()
    for n, others in sorted(redefined_authors(names, num, owners).items()):
        problems.append("author %r is already defined by installment %s: link works to that "
                        "record (installment 10: extend it in scripts/content/i10_extensions.py)"
                        % (n, ", ".join(others)))
    for a in authors:
        if a["tier"] not in SIGNIFICANCE_TIERS:
            problems.append("bad tier %r for %r" % (a["tier"], a["name"]))
        for k in ("bio", "prof", "style", "conc", "sig", "nat", "ident"):
            if not (a.get(k) or "").strip():
                problems.append("missing %s for author %r" % (k, a["name"]))

    # --- works
    # A title already in the database is only a collision when it belongs to a
    # different author: the same author's record is updated by the idempotent
    # import (that is how a re-run after an edit refreshes text in place).
    con = sqlite3.connect(DB_PATH)
    try:
        title_owners = {}
        for title, name in con.execute(
                "select w.title, a.full_name from works w join work_authors wa "
                "on wa.work_id = w.work_id join authors a on a.author_id = wa.author_id"):
            title_owners.setdefault(title, set()).add(name)
    finally:
        con.close()
    titles = [w["title"] for w in works]
    for t in sorted({t for t in titles if titles.count(t) > 1}):
        problems.append("duplicate title in module: %r" % t)
    for w in works:
        t = w["title"]
        if t in corpus_titles and title_owners.get(t) and w["author"] not in title_owners[t]:
            problems.append("title already in database under another author %r: %r"
                            % (sorted(title_owners[t]), t))
    author_names = set(names) | corpus_authors
    for w in works:
        if w["author"] not in author_names:
            problems.append("unknown author %r for %r" % (w["author"], w["title"]))
        for co in w.get("coauthors") or []:
            if co not in author_names:
                problems.append("unknown coauthor %r for %r" % (co, w["title"]))
        if w.get("canon", "Secondary canon") not in CANONICAL_STATUS:
            problems.append("bad canonical_status %r for %r" % (w.get("canon"), w["title"]))
        if w.get("status", "complete") not in RESEARCH_STATUS:
            problems.append("bad research_status for %r" % w["title"])
        for field, key in (("genres", "genres"), ("themes", "themes"), ("movements", "movements")):
            for name in w.get(field) or []:
                if name not in known[{"genres": "genres", "themes": "themes",
                                      "movements": "movements"}[field]]:
                    problems.append("unresolved %s %r (work %r)" % (key, name, w["title"]))
        for k in ("desc", "ctx", "sigtext", "form"):
            if not (w.get(k) or "").strip():
                problems.append("missing %s for work %r" % (k, w["title"]))
        for field in ("pub", "perf"):
            v = w.get(field)
            if v is not None and not isinstance(v, str):
                problems.append("%s of %r must be a string" % (field, w["title"]))
        comp = w.get("composition")
        if comp and not all(isinstance(x, str) for x in comp):
            problems.append("composition years of %r must be strings" % w["title"])

    if problems:
        print("BUILD BLOCKED: %d problem(s)" % len(problems))
        for p in problems:
            print("  -", p)
        return 1

    # --- write files
    per_batch = meta.get("authors_per_file", 8)
    base = "installment_%s" % num
    author_files = []
    recorded = recorded_works(works)
    for i in range(0, len(authors), per_batch):
        chunk = authors[i:i + per_batch]
        slug = "a%02d" % (i // per_batch + 1)
        path = "data/authors/%s_authors_%s.json" % (base, slug)
        author_files.append(path)
        payload = [author_record(a, recorded) for a in chunk]
        for rec in payload:
            # AUTHOR_KEYS order plus the optional additions (significance tier and
            # the documented-only bibliography note); nothing else may appear.
            expected = list(AUTHOR_KEYS) + list(OPTIONAL_AUTHOR_KEYS)
            if "bibliographical_notes" in rec:
                expected.append("bibliographical_notes")
            expected += [k for k in OPTIONAL_AUTHOR_AUDIT_KEYS if k in rec]
            assert list(rec.keys()) == expected, list(rec.keys())
    # works in batches aligned to author order, 25 works per file
    work_files = []
    words_per_file = meta.get("works_per_file", 25)

    def batch_slug(n):
        # 1..26 -> b1..b26, then b27...
        return "b%d" % n

    author_payloads = [author_record(a, recorded) for a in authors]
    work_payloads = [work_record(w) for w in works]

    # Field-level parity with installments 1-7: every record leaves the builder
    # carrying the analytical fields that the compact content modules do not
    # spell out (metre or prose manner, narrative structure, attribution,
    # bibliography, principal characters, alternative titles, biographical
    # uncertainty). content_enrich composes them from the record's own dates,
    # form, genre, canon and status flags, from the curated first-edition and
    # variant-title tables, and from the author's stylistic profile; it never
    # supplies a fact the record does not already carry.
    work_meta = {w["title"]: ([w["author"]] + list(w.get("coauthors") or []),
                              list(w.get("genres") or []), list(w.get("themes") or []),
                              list(w.get("movements") or [])) for w in works}
    if meta.get("strict"):
        # Installment 10 onwards: every analytical field is authored per record.
        # No template text is composed; the strict checks enforce depth, reject
        # boilerplate and duplicated prose, and require sources for verified records.
        import strict_checks
        strict_problems = strict_checks.check(works, authors, meta)
        if strict_problems:
            print("BUILD BLOCKED (strict): %d problem(s)" % len(strict_problems))
            for p in strict_problems:
                print("  -", p)
            return 1
        print("strict checks: passed (%d works, %d authors); enrichment disabled" % (len(works), len(authors)))
    else:
        import content_enrich
        # Authors defined by earlier installments, for works recorded here whose
        # author is defined there (installment 9 records works by H. G. Wells,
        # who is defined by installment 8).
        context = []
        for path in sorted(glob.glob(os.path.join("data", "authors", "installment_*_authors*.json"))):
            found = re.match(r"installment_(\d+)_authors", os.path.basename(path))
            if found and int(found.group(1)) < int(num):
                payload = json.load(open(path, encoding="utf-8"))
                context.extend(payload.get("authors", []) if isinstance(payload, dict) else payload)
        filled = content_enrich.apply_enrichment(work_payloads, work_meta, author_payloads, context)
        print("enrichment: " + (", ".join("%s x%d" % (k, v) for k, v in sorted(filled.items()))
                                or "nothing to fill"))

    for rec in work_payloads:
        keys = list(rec.keys())
        assert keys[:len(WORK_KEYS)] == WORK_KEYS and set(keys[len(WORK_KEYS):]) <= set(EXTRA_WORK_COLUMNS), keys

    if not args.check_only:
        for path in author_files:
            os.makedirs(os.path.dirname(path), exist_ok=True)
    # (author payloads were validated above; write them now)
    if not args.check_only:
        for idx, path in enumerate(author_files):
            chunk = author_payloads[idx * per_batch:(idx + 1) * per_batch]
            with open(path, "w", encoding="utf-8") as fh:
                json.dump(chunk, fh, ensure_ascii=False, indent=1)

    # split works, keeping each author's works together as far as possible
    chunks, current = [], []
    for rec in work_payloads:
        current.append(rec)
        if len(current) >= words_per_file:
            chunks.append(current)
            current = []
    if current:
        chunks.append(current)

    map_modules = {}
    for idx, chunk in enumerate(chunks, start=1):
        slug = batch_slug(idx)          # b1, b2, ... (map module + glob convention)
        work_path = "data/works/%s_works_batch%d.json" % (base, idx)
        work_files.append(work_path)
        map_path = "scripts/_i%s_map_%s.py" % (num, slug)     # _i08_map_b1.py
        entries = []
        by_title = {w["title"]: w for w in works}
        for rec in chunk:
            w = by_title[rec["title"]]
            aus = [w["author"]] + list(w.get("coauthors") or [])
            entries.append((rec["title"], aus, w.get("genres") or [],
                            w.get("themes") or [], w.get("movements") or []))
        map_modules["MAP_B%s" % slug[1:].upper()] = entries   # MAP_B1 ...
        if not args.check_only:
            with open(work_path, "w", encoding="utf-8") as fh:
                json.dump(chunk, fh, ensure_ascii=False, indent=1)
            with open(map_path, "w", encoding="utf-8") as fh:
                fh.write('"""Installment %s, batch %s: work -> authors, genres, themes, '
                         'movements.\n\nGenerated by scripts/build_installment.py from '
                         'the scripts/content_i%s* modules.\n"""\n\nMAP_B%s = {\n'
                         % (num, slug, num, slug[1:].upper()))
                for title, aus, genres, themes, movements in entries:
                    fh.write("    %r: (%r,\n        %r,\n        %r,\n        %r),\n"
                             % (title, aus, genres, themes, movements))
                fh.write("}\n")

    # --- relationships
    period_name = meta["period"]
    all_authors = {a["name"]: a for a in authors}

    def strand(a):
        nat = (a.get("nat") or "").lower()
        return "american" if "american" in nat else "british"

    universal = meta.get("sources_universal", [])
    strand_sources = meta.get("sources_strand", {})
    every_source = set(corpus_sources)
    for name in sorted(os.listdir("data/sources")):
        if name.startswith(base) and name.endswith(".json"):
            for row in json.load(open("data/sources/" + name, encoding="utf-8")):
                every_source.add(row["title"])
    # The importer loads every installment's sources file before it links
    # anything, so an explicit citation of a source registered by a later
    # installment (e.g. an installment-9 correction researched during
    # installment 10) is valid: ``known_sources`` is the set used to check
    # citations. The surname-matched pool, by contrast, excludes titles found
    # only in later installments' files, so that rebuilding an earlier
    # installment after a later import cannot attach, say, the installment-10
    # sources on Albert Murray to an earlier author called Murray.
    own_or_earlier, later = set(), set()
    for name in sorted(os.listdir("data/sources")):
        found = re.match(r"installment_(\d+)_", name)
        if not (found and name.endswith(".json")):
            continue
        rows = json.load(open("data/sources/" + name, encoding="utf-8"))
        (later if int(found.group(1)) > int(num) else own_or_earlier).update(r["title"] for r in rows)
    known_sources = every_source | own_or_earlier | later
    match_pool = every_source - (later - own_or_earlier)

    def name_matched(title, author):
        """A source documents an author when the surname (or full name) appears."""
        surname = author["name"].split()[-1]
        blob = title
        return len(surname) > 3 and surname.lower() in blob.lower()

    work_authors = []
    work_genres = []
    work_themes = []
    work_movements = []
    work_sources = []
    author_sources = []
    author_genres = {}
    author_movements = {}
    author_themes = {}
    author_influences = []

    for w in works:
        aus = [w["author"]] + list(w.get("coauthors") or [])
        for i, name in enumerate(aus):
            work_authors.append({
                "work": w["title"], "author": name,
                "contribution_type": w.get("contribution_type", "author") if i == 0
                else w.get("coauthor_type", "author"),
            })
        # dict.fromkeys: an order-keeping de-duplication (a theme name split
        # at its own commas resolves once per fragment in the source helpers)
        if w.get("genres"):
            work_genres.append({"work": w["title"], "genres": list(dict.fromkeys(w["genres"]))})
        if w.get("themes"):
            work_themes.append({"work": w["title"], "themes": list(dict.fromkeys(w["themes"]))})
        if w.get("movements"):
            work_movements.append({"work": w["title"], "movements": list(dict.fromkeys(w["movements"]))})
        for name in aus:
            # Derived author-level genre, movement and theme links summarise every
            # work linked to an author, including works recorded by a later
            # installment than the author's own: the importer merges link rows
            # from all installment files (ownership is per author, INSERT OR
            # IGNORE), so these add to the defining installment's links. Author
            # sources and influences stay with the installment that defines the
            # author.
            if name not in all_authors and name not in corpus_authors:
                continue
            author_genres.setdefault(name, set()).update(w.get("genres") or [])
            author_movements.setdefault(name, set()).update(w.get("movements") or [])
            author_themes.setdefault(name, set()).update(w.get("themes") or [])
        # A work may belong to an author recorded by an earlier installment.
        owner = all_authors.get(w["author"])
        sources = set(universal) | (set(strand_sources.get(strand(owner), [])) if owner else set())
        sources |= set(w.get("sources") or [])
        for title in list(sources):
            if title not in known_sources:
                problems.append("work %r cites unknown source %r" % (w["title"], title))
        work_sources.append({"work": w["title"], "sources": sorted(sources)})

    for a in authors:
        srcs = set(universal) | set(strand_sources.get(strand(a), []))
        for title in match_pool:
            if name_matched(title, a):
                srcs.add(title)
        srcs |= set(a.get("sources") or [])
        for title in list(srcs):
            if title not in known_sources:
                problems.append("author %r cites unknown source %r" % (a["name"], title))
        author_sources.append({"author": a["name"], "sources": sorted(srcs)})
        for name in a.get("infl") or []:
            if name in author_names:
                pass
        resolved = [n for n in (a.get("infl") or []) if n in author_names]
        if resolved:
            author_influences.append({"author": a["name"], "influenced_by": resolved})

    if num == "10":
        problems += extension_problems(extensions, num, set(all_authors), works, owners, known_sources)

    if problems:
        print("BUILD BLOCKED (relationships): %d problem(s)" % len(problems))
        for p in problems[:80]:
            print("  -", p)
        return 1

    works_rel = {
        "work_authors": work_authors,
        "work_genres": work_genres,
        "work_themes": work_themes,
        "work_movements": work_movements,
        "work_periods": [{"period": period_name, "works": titles}],
    }
    authors_rel = {
        "author_genres": [{"author": k, "genres": sorted(v)} for k, v in sorted(author_genres.items())],
        "author_movements": [{"author": k, "movements": sorted(v)} for k, v in sorted(author_movements.items())],
        "author_themes": [{"author": k, "themes": sorted(v)} for k, v in sorted(author_themes.items())],
        "author_influences": author_influences,
        "author_sources": author_sources,
    }
    editions_rel = {
        "work_sources": work_sources,
        "period_movements": [{"period": period_name, "movements": meta["period_movements"]}],
    }

    if not args.check_only:
        out = "data/relationships"
        os.makedirs(out, exist_ok=True)
        for suffix, payload in (("works", works_rel), ("authors", authors_rel),
                                ("sources_editions", editions_rel)):
            with open("%s/%s_relationships_%s.json" % (out, base, suffix), "w",
                      encoding="utf-8") as fh:
                json.dump(payload, fh, ensure_ascii=False, indent=1)

    print("installment %s: %d authors, %d works, %d work files, %d author files"
          % (num, len(authors), len(works), len(work_files), len(author_files)))
    print("  work_authors=%d work_genres=%d work_themes=%d work_movements=%d "
          "author_sources=%d work_sources=%d"
          % (len(work_authors), len(work_genres), len(work_themes),
             len(work_movements), len(author_sources), len(work_sources)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
