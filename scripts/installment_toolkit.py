"""Shared tooling for the sequential research installments.

Permanent module (not a throwaway): every installment authors the same two
entity kinds (works, authors) plus taxonomy and relationship files, and every
installment is gated by the same mechanical checks before `import_data.py` is
allowed to run against the master database.

Commands
--------
  python scripts/installment_toolkit.py dump-taxonomy 07
      Writes scripts/_i07_taxonomy_names.txt: the verbatim movement/genre/theme
      names of installment 07 (from data/*/installment_07_*.json) followed by
      every name already in the database. Authoring agents copy from this file;
      they never paraphrase a taxonomy name.

  python scripts/installment_toolkit.py dump-corpus 07
      Writes scripts/_i07_existing_works.txt (titles) and
      scripts/_i07_existing_authors.json (names) so a new batch cannot collide
      with a record that already exists.

  python scripts/installment_toolkit.py check 07 2b
      Hard validator for one batch: 21-key work schema and key order, 18-key
      author schema, unique titles, no title already in the corpus, string
      date fields, controlled vocabularies, map<->works parity in both
      directions, and every author/genre/theme/movement name resolvable.
      Prints CLEAN or the list of problems and exits non-zero on any problem.

  python scripts/installment_toolkit.py gen-relationships 07
      Derives the three installment relationship files from the batch maps,
      the author records and the installment's own source list:
      data/relationships/installment_07_relationships_works.json,
      _authors.json and _sources_editions.json. A source is attached to an
      author when the author's surname appears in the source title or editor
      string (see SOURCE_AUTHOR_KEYS for the editions that name a work or an
      editor instead). Beyond that, only the titles listed in
      PERIOD_WIDE_SOURCES are attached without a name match, and the
      british/american groups follow each author's own literary tradition:
      a book about one writer is never allowed to become a source for another.
      Edition rows are built only from verified source records, so
      no edition detail is ever invented here.

Conventions enforced here (see documentation/DATA_DICTIONARY.md):
  * `works` date columns are VARCHAR: years are STRINGS, `"c. 1737"` for
    approximate dates. A JSON number is a defect.
  * `principal_characters` is a semicolon-joined string or null, never a list.
  * Taxonomy rows are created only from entity files; relationship entries
    merely link names that already resolve.
"""

import glob
import importlib
import json
import os
import re
import sqlite3
import sys

DB_PATH = "database/English_Literature_Master.db"

WORK_KEYS = [
    "title", "alternative_titles", "authorship_status", "composition_date_start",
    "composition_date_end", "publication_date", "first_performance_date",
    "manuscript_date", "original_language", "description", "plot_or_argument",
    "narrative_structure", "principal_characters", "literary_form",
    "meter_and_prosody", "historical_context", "literary_significance",
    "attribution_notes", "bibliographical_notes", "canonical_status",
    "research_status",
]

AUTHOR_KEYS = [
    "full_name", "alternative_names", "pseudonyms", "birth_date",
    "birth_date_approximate", "death_date", "death_date_approximate",
    "birthplace", "nationality_or_literary_tradition", "literary_identity",
    "biography", "literary_profile", "stylistic_characteristics",
    "intellectual_concerns", "historical_significance", "major_influences",
    "biographical_uncertainty", "research_status",
]

# Authors may optionally carry a documented significance classification
# (installment 8 onwards). The JSON records store it as "significance_tier";
# it is written to the authors table as a nullable column.
OPTIONAL_AUTHOR_KEYS = ["significance_tier"]

# Author-level note listing documented writings that cannot carry a full work record.
OPTIONAL_AUTHOR_NOTE_KEYS = ["bibliographical_notes"]

SIGNIFICANCE_TIERS = {
    "Major / canonical",
    "Significant / secondary",
    "Minor / lesser-known",
    "Obscure / historically neglected",
}

DATE_FIELDS = ("composition_date_start", "composition_date_end", "publication_date",
               "first_performance_date", "manuscript_date")

AUTHORSHIP_STATUS = {"single", "anonymous", "collaborative", "attributed", "disputed"}
CANONICAL_STATUS = {"Major canon", "Secondary canon", "Minor canon"}
RESEARCH_STATUS = {"complete", "partial"}

# Installment 10 onwards: per-record audit fields (migration f5a6b7c8d9e0).
OPTIONAL_AUTHOR_AUDIT_KEYS = ["bibliography_status", "verification_status"]
VERIFICATION_STATUS = {"verified", "partially verified", "unverified"}
BIBLIOGRAPHY_STATUS = {"complete", "substantially complete", "incomplete"}


def year_num(value):
    """Date fields are strings, sometimes 'c. 1737' or '8th century'."""
    if value is None:
        return None
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    return int(digits) if digits else None


def batch_files(installment):
    return sorted(glob.glob("data/works/installment_%s_works_batch*.json" % installment))


def map_files(installment):
    return sorted(glob.glob("scripts/_i%s_map_b*.py" % installment))


def load_maps(installment):
    """Merged {title: (authors, genres, themes, movements)} across all batches."""
    sys.path.insert(0, "scripts")
    merged = {}
    loaded = {}
    for p in map_files(installment):
        base = os.path.basename(p)[:-3]
        mod = importlib.import_module(base)
        table = getattr(mod, "MAP_" + base.split("_map_")[1].upper(), None)
        if table is None:
            raise SystemExit("%s defines no MAP_ constant" % p)
        for k, v in table.items():
            if k in merged:
                raise SystemExit("title in two maps: %r" % k)
            merged[k] = v
        loaded[base] = len(table)
    return merged, loaded


def works_for(installment, slug=None):
    out = []
    for p in batch_files(installment):
        if slug is not None:
            stem = p.split("batch")[1][:-5]
            if stem.lstrip("bB") != slug.lstrip("bB"):
                continue
        out.extend(json.load(open(p, encoding="utf-8")))
    return out


def authors_for(installment):
    out = []
    for p in sorted(glob.glob("data/authors/installment_%s_authors*.json" % installment)):
        payload = json.load(open(p, encoding="utf-8"))
        if isinstance(payload, dict):
            payload = payload.get("authors", [])
        out.extend(payload)
    return out


def db():
    return sqlite3.connect(DB_PATH)


def db_names(table):
    con = db()
    try:
        return {r[0] for r in con.execute("select name from " + table)}
    finally:
        con.close()


def installment_names(installment):
    """Names this installment's own taxonomy files create (one or more per kind)."""
    out = {}
    for kind in ("movements", "genres", "themes"):
        names = set()
        for p in sorted(glob.glob("data/%s/installment_%s_%s*.json" % (kind, installment, kind))):
            names |= {x["name"] for x in json.load(open(p, encoding="utf-8"))}
        out[kind] = names
    return out


def known(installment, kind):
    return db_names(kind) | installment_names(installment).get(kind, set())


def corpus_titles():
    con = db()
    try:
        return {r[0] for r in con.execute("select title from works")}
    finally:
        con.close()


def corpus_authors():
    con = db()
    try:
        return {r[0] for r in con.execute("select full_name from authors")}
    finally:
        con.close()


def dump_taxonomy(installment):
    path = "scripts/_i%s_taxonomy_names.txt" % installment
    with open(path, "w", encoding="utf-8") as fh:
        for kind in ("movements", "genres", "themes"):
            mine = sorted(installment_names(installment).get(kind, set()))
            fh.write("== INSTALLMENT-%s %s (use these exact names) ==\n" % (installment, kind.upper()))
            fh.write("\n".join(mine) + "\n\n")
        for kind in ("movements", "genres", "themes"):
            fh.write("== EXISTING DB %s ==\n" % kind.upper())
            fh.write("\n".join(sorted(db_names(kind))) + "\n\n")
        fh.write("== PERIODS ==\n")
        fh.write("\n".join(sorted(db_names("periods"))) + "\n")
    print("wrote", path)


def dump_corpus(installment):
    titles = sorted(corpus_titles())
    with open("scripts/_i%s_existing_works.txt" % installment, "w", encoding="utf-8") as fh:
        fh.write("\n".join(titles) + "\n")
    json.dump(sorted(corpus_authors()),
              open("scripts/_i%s_existing_authors.json" % installment, "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print("wrote %d titles, %d authors" % (len(titles), len(corpus_authors())))


def check(installment, slug):
    ws = works_for(installment, slug)
    if not ws:
        raise SystemExit("no batch found for installment %s slug %s" % (installment, slug))
    problems = []
    titles = [w["title"] for w in ws]
    seen = set()
    for t in titles:
        if t in seen:
            problems.append("DUPLICATE TITLE in batch: %r" % t)
        seen.add(t)
    for t in titles:
        if t in corpus_titles():
            problems.append("ALREADY-IN-DATABASE %r" % t)

    merged, _ = load_maps(installment)
    batch_titles = set(titles)
    map_here = {k: v for k, v in merged.items() if k in batch_titles}
    for t in batch_titles - set(map_here):
        problems.append("MISSING FROM MAP %r" % t)
    for t in set(map_here) - batch_titles:
        problems.append("IN MAP, NOT IN WORKS %r" % t)

    for w in ws:
        t = w["title"]
        if list(w.keys()) != WORK_KEYS:
            problems.append("KEYS %r: %s" % (t, "schema drift: %s" % list(w.keys())))
        for f in DATE_FIELDS:
            v = w.get(f)
            if v is not None and not isinstance(v, str):
                problems.append("TYPE %r %s=%r must be a string year (project convention)" % (t, f, v))
        if isinstance(w.get("principal_characters"), list):
            problems.append("TYPE %r principal_characters must be a string, not a list" % t)
        if w["authorship_status"] not in AUTHORSHIP_STATUS:
            problems.append("VOCAB %r authorship_status=%r" % (t, w["authorship_status"]))
        if w["canonical_status"] not in CANONICAL_STATUS:
            problems.append("VOCAB %r canonical_status=%r" % (t, w["canonical_status"]))
        if w["research_status"] not in RESEARCH_STATUS:
            problems.append("VOCAB %r research_status=%r" % (t, w["research_status"]))
        c, p = year_num(w.get("composition_date_start")), year_num(w.get("publication_date"))
        if c and p and p < c:
            problems.append("DATE %r publication %s before composition %s" % (t, p, c))
        for k in w:
            if w[k] == "":
                problems.append("EMPTY %r %s" % (t, k))

    auth_known = corpus_authors() | {a["full_name"] for a in authors_for(installment)}
    for t, entry in map_here.items():
        aus, genres, themes, movements = entry
        if not isinstance(aus, list):
            problems.append("MAP %r authors must be a list" % t)
            continue
        for a in aus:
            if a not in auth_known:
                problems.append("MAP %r unresolved author %r" % (t, a))
        if not genres:
            problems.append("MAP %r has no genre" % t)
        if not themes:
            problems.append("MAP %r has no theme" % t)
        for kind, xs in (("genre", genres), ("theme", themes), ("movement", movements)):
            table = kind + "s" if kind != "genre" else "genres"
            for x in xs:
                if x not in known(installment, table):
                    problems.append("MAP %r unresolved %s %r" % (t, kind, x))

    print("batch %s%s: %d works, %d map entries" %
          (slug, " (installment %s)" % installment, len(ws), len(map_here)))
    if problems:
        print("PROBLEMS (%d):" % len(problems))
        for p in problems:
            print("  - " + p)
        return 1
    print("CLEAN")
    return 0


def load_sources(installment):
    out = []
    for p in sorted(glob.glob("data/sources/installment_%s_sources*.json" % installment)):
        out.extend(json.load(open(p, encoding="utf-8")))
    return out


def author_keys(name):
    """Surname-ish tokens used to match a source to an author."""
    stop = {"the", "sixth", "fifth", "seventh", "baron", "earl", "lord", "sir",
            "lady", "of", "and", "third", "fourth", "second"}
    toks = [t for t in re.split(r"[^A-Za-z']+", name) if len(t) > 3 and t.lower() not in stop]
    return toks[-2:] if toks else [name]


# Sources that name a work or an editor rather than the author they document.
SOURCE_AUTHOR_KEYS = {
    "07": {
        "'Lyrical Ballads,' and Other Poems, 1797-1800": ["William Wordsworth"],
        "The Prelude: 1799, 1805, 1850 (Norton Critical Edition)": ["William Wordsworth"],
        "Frankenstein; or, The Modern Prometheus: The 1818 Text": ["Mary Wollstonecraft Shelley"],
        "Confessions of an English Opium-Eater and Other Writings (Oxford World's Classics)":
            ["Thomas De Quincey"],
        "The Edinburgh Edition of Walter Scott's 'Minstrelsy of the Scottish Border' (3 volumes)":
            ["Sir Walter Scott"],
        # Scholarly editions titled by the work they edit, so no surname can match.
        # Each attribution below is the settled one for the edition cited.
        "Zofloya: or, The Moor (Oxford World's Classics)": ["Charlotte Dacre"],
        "Melmoth the Wanderer (Oxford World's Classics)": ["Charles Robert Maturin"],
        "Self-Control: A Novel (Chawton House Library: Women's Novels, No. 17)": ["Mary Brunton"],
        "Discipline: A Novel (Chawton House Library: Women's Novels)": ["Mary Brunton"],
        "The Private Memoirs and Confessions of a Justified Sinner (Oxford World's Classics)":
            ["James Hogg"],
        "Plays on the Passions: The 1798 Edition": ["Joanna Baillie"],
        "Adeline Mowbray: or, The Mother and Daughter (Broadview Editions)": ["Amelia Opie"],
        "Memoirs of Modern Philosophers (Broadview Editions)": ["Elizabeth Hamilton"],
        "Rural Rides (Everyman's Library, 2 volumes)": ["William Cobbett"],
        "Glenarvon (Valancourt Classics, with a new introduction)": ["Lady Caroline Lamb"],
        "An Appeal in Favor of That Class of Americans Called Africans": ["Lydia Maria Child"],
        "Hobomok: A Tale of Early Times (Broadview Edition)": ["Lydia Maria Child"],
    },
}

GENERAL_SOURCE_TYPES = {"reference", "anthology", "archive", "periodical",
                        "encyclopedia", "textbook"}

# Sources may be attached in two ways only. "universal" titles stand behind every
# work and author of the period; "american"/"british" titles are attached according to
# the author's own literary tradition. Everything else is linked by name, because
# attaching a book about one writer to another writer's works would invent a reference.
PERIOD_WIDE_SOURCES = {
    "07": {
        "universal": ["Oxford Dictionary of National Biography"],
        "british": [
            "The Norton Anthology of English Literature, 10th edition, Volume D: "
            "The Romantic Period",
            "The Cambridge Companion to British Romanticism",
        ],
        "american": ["The Norton Anthology of American Literature (9th edition)"],
    },
}


def period_wide_sources(installment):
    """{strand: [titles]} that may be attached without a name match."""
    groups = PERIOD_WIDE_SOURCES.get(installment)
    if groups is None:
        raise SystemExit("no period-wide source list for installment %s; add one to "
                         "PERIOD_WIDE_SOURCES rather than letting every reference "
                         "attach to every work" % installment)
    known = {s["title"] for s in load_sources(installment)}
    con = db()
    try:
        known |= {r[0] for r in con.execute("select title from sources")}
    finally:
        con.close()
    missing = [t for group in groups.values() for t in group if t not in known]
    if missing:
        raise SystemExit("period-wide sources neither in this installment's source files "
                         "nor already in the database: %s" % missing)
    return {k: list(v) for k, v in groups.items()}


def source_authors(installment, sources, author_names):
    """{source title: [author names]} for sources that document a single author."""
    keys = dict(SOURCE_AUTHOR_KEYS.get(installment, {}))
    by_token = {}
    for a in author_names:
        for k in author_keys(a):
            by_token.setdefault(k, a)
    wide = {t for group in PERIOD_WIDE_SOURCES.get(installment, {}).values() for t in group}
    out = {}
    for s in sources:
        if s["title"] in wide:
            continue
        blob = "%s %s" % (s["title"], s.get("author_or_editor") or "")
        named = [a for tok, a in by_token.items() if tok in blob]
        if s["title"] in keys:
            named = list(dict.fromkeys(keys[s["title"]] + named))
        out[s["title"]] = named
    return out


def gen_relationships(installment):
    """Write the three installment relationship files from the batch maps."""
    ws = works_for(installment)
    merged, _ = load_maps(installment)
    new_authors = authors_for(installment)
    period_rows = json.load(open("data/periods/installment_%s_periods.json" % installment,
                                 encoding="utf-8"))
    period = period_rows[0]["name"]
    movements = sorted(installment_names(installment)["movements"])
    sources = load_sources(installment)
    src_authors = source_authors(installment, sources, [a["full_name"] for a in new_authors])
    strands = period_wide_sources(installment)

    # An author's strand decides which period-wide anthology and companion may be
    # cited for them; the American strand is identified from the record's own
    # nationality field, this installment's or the database's.
    american_names = {a["full_name"] for a in new_authors
                      if "American" in (a.get("nationality_or_literary_tradition") or "")}
    con = db()
    try:
        american_names |= {r[0] for r in con.execute(
            "select full_name from authors where nationality_or_literary_tradition "
            "like '%American%'")}
    finally:
        con.close()

    def strand_of(names):
        return "american" if any(n in american_names for n in names) else "british"

    def context_for(names):
        return strands["universal"] + strands[strand_of(names)]

    # Period links follow each work's own dates, not the installment's label: a work
    # written before 1789 (or after this installment's end) belongs to another period row.
    period_spans = [(r["name"], year_num(r.get("start_year")), year_num(r.get("end_year")))
                    for r in period_rows]
    con = db()
    try:
        period_spans += [(n, year_num(s), year_num(e)) for n, s, e in
                         con.execute("select name, start_year, end_year from periods")]
    finally:
        con.close()
    period_spans = sorted(set(period_spans))

    def period_of(w):
        y = year_num(w.get("composition_date_start")) or year_num(w.get("publication_date")) \
            or year_num(w.get("first_performance_date"))
        hits = [n for n, s, e in period_spans if y is not None and s is not None and s <= y <= e]
        if period in hits:
            return period
        return hits[0] if hits else period

    periods_by_work = {}
    for w in ws:
        periods_by_work.setdefault(period_of(w), []).append(w["title"])
    work_periods = [{"period": p, "works": sorted(t)} for p, t in sorted(periods_by_work.items())]

    work_authors, work_genres, work_themes, work_movements = [], [], [], []
    names = [a["full_name"] for a in new_authors]
    author_genres = {n: [] for n in names}
    author_movements = {n: [] for n in names}
    author_themes = {n: [] for n in names}
    work_sources, author_sources, work_editions = {}, {}, {}
    movement_authors = {m: [] for m in movements}

    for w in ws:
        t = w["title"]
        aus, genres, themes, moves = merged[t]
        for a in aus:
            work_authors.append({"work": t, "author": a, "contribution_type": "author"})
        if genres:
            work_genres.append({"work": t, "genres": genres})
        if themes:
            work_themes.append({"work": t, "themes": themes})
        if moves:
            work_movements.append({"work": t, "movements": moves})
        for a in aus:
            if a in author_genres:
                for g in genres:
                    if g not in author_genres[a]:
                        author_genres[a].append(g)
                for th in themes:
                    if th not in author_themes[a]:
                        author_themes[a].append(th)
                for m in moves:
                    if m not in author_movements[a]:
                        author_movements[a].append(m)
        for m in moves:
            for a in aus:
                if a not in movement_authors.setdefault(m, []):
                    movement_authors.setdefault(m, []).append(a)
        linked = [title for title, names in src_authors.items() if any(x in aus for x in names)]
        work_sources[t] = list(dict.fromkeys(linked + context_for(aus)))
        work_editions[t] = [
            {"edition_title": s["title"], "editor": s.get("author_or_editor"),
             "publisher": s.get("publisher"), "publication_year": s.get("publication_year"),
             "edition_notes": "Documented in %s; the scholarly text cited for this author."
                              % s["title"]}
            for s in sources if s["title"] in linked
        ]

    for a in new_authors:
        name = a["full_name"]
        author_sources[name] = list(dict.fromkeys(
            [t for t, linked in src_authors.items() if name in linked] + context_for([name])))

    movement_sources = {}
    for m, ms in movement_authors.items():
        linked = [t for t, owners in src_authors.items() if any(x in ms for x in owners)]
        # A movement spans both national strands, so only the universal reference is
        # attached by default; the rest comes from the authors named in it.
        movement_sources[m] = list(dict.fromkeys(linked + strands["universal"]))

    influences = []
    known_authors = corpus_authors() | {a["full_name"] for a in new_authors}
    for a in new_authors:
        raw = a.get("major_influences")
        if not raw:
            continue
        items = raw if isinstance(raw, list) else [x.strip() for x in raw.split(";") if x.strip()]
        names = [x.strip() for x in items if isinstance(x, str) and x.strip() in known_authors]
        names = [n for n in names if n != a["full_name"]]
        if names:
            influences.append({"author": a["full_name"], "influenced_by": names})

    out = {
        "works": {
            "work_authors": work_authors,
            "work_periods": work_periods,
            "work_genres": work_genres,
            "work_themes": work_themes,
            "work_movements": work_movements,
        },
        "authors": {
            "author_genres": [{"author": k, "genres": v} for k, v in sorted(author_genres.items()) if v],
            "author_movements": [{"author": k, "movements": v} for k, v in sorted(author_movements.items()) if v],
            "author_themes": [{"author": k, "themes": v} for k, v in sorted(author_themes.items()) if v],
            "author_influences": influences,
            "period_movements": [{"period": period, "movements": movements}],
        },
        "sources_editions": {
            "author_sources": [{"author": k, "sources": v} for k, v in sorted(author_sources.items()) if v],
            "work_sources": [{"work": k, "sources": v} for k, v in sorted(work_sources.items()) if v],
            "movement_sources": [{"movement": k, "sources": v}
                                 for k, v in sorted(movement_sources.items()) if v],
            "work_editions": [{"work": k, "editions": v} for k, v in sorted(work_editions.items()) if v],
        },
    }
    for kind, payload in out.items():
        p = "data/relationships/installment_%s_relationships_%s.json" % (installment, kind)
        json.dump(payload, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("wrote %s (%d keys)" % (p, len(payload)))
    print("period %r: %d works, %d new authors, %d movements, %d sources"
          % (period, len(ws), len(new_authors), len(movements), len(sources)))
    return 0


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd = argv[1]
    if cmd == "dump-taxonomy":
        dump_taxonomy(argv[2]); return 0
    if cmd == "dump-corpus":
        dump_corpus(argv[2]); return 0
    if cmd == "check":
        return check(argv[2], argv[3])
    if cmd == "gen-relationships":
        return gen_relationships(argv[2])
    print("unknown command %r" % cmd)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
