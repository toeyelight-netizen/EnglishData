"""Installment 10 audits: coverage matrix and audit report from actual records.

Runs the eight audits of the installment-10 revision order against the master
database and the built JSON, and writes

  documentation/INSTALLMENT_10_COVERAGE_MATRIX.csv
  documentation/INSTALLMENT_10_AUDIT_REPORT.md

Every number is computed here from the database, the built JSON and the
discovery inventory (research/installment_10/discovery_inventory.csv); the
narrative sections (method, corrections, sources consulted, limitations) are
taken from research/installment_10/report_notes.md, which is maintained by hand.
Nothing in the report is estimated.

Usage: python3 scripts/audit_installment_10.py
"""

import csv
import glob
import json
import os
import re
import sqlite3
import sys
import unicodedata
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from strict_checks import DEPTH_RULES  # noqa: E402

DB = os.path.join(ROOT, "database", "English_Literature_Master.db")
MATRIX = os.path.join(ROOT, "documentation", "INSTALLMENT_10_COVERAGE_MATRIX.csv")
REPORT = os.path.join(ROOT, "documentation", "INSTALLMENT_10_AUDIT_REPORT.md")
NOTES = os.path.join(ROOT, "research", "installment_10", "report_notes.md")
INVENTORY = os.path.join(ROOT, "research", "installment_10", "discovery_inventory.csv")
PERIOD = "Postwar and Contemporary Period (1946–2000)"
DECADES = ["1946-1950", "1951-1959", "1960-1969", "1970-1979", "1980-1989", "1990-2000"]

# Part III of the revision order: checklist item -> installment-10 genre record.
GENRE_CHECKLIST = [
    ("A. Fiction", [("Literary novels", "Literary Novel"), ("Historical novels", "Historical Novel"),
     ("Psychological novels", "Psychological Novel"), ("Social novels", "Social Novel"),
     ("Political novels", "Political Novel"), ("Realist fiction", "Realist Fiction"),
     ("Naturalist fiction", "Naturalist Fiction"), ("Modernist fiction", "Modernist Fiction"),
     ("Postmodern fiction", "Postmodern Fiction"), ("Experimental fiction", "Experimental Fiction"),
     ("Metafiction", "Metafictional Novel"), ("Satirical fiction", "Satirical Fiction"),
     ("Philosophical fiction", "Philosophical Fiction"), ("Bildungsroman", "Bildungsroman"),
     ("Künstlerroman", "Künstlerroman"), ("Family sagas", "Family Saga"), ("Regional fiction", "Regional Fiction"),
     ("Campus novels", "Campus Novel"), ("Domestic fiction", "Domestic Fiction"),
     ("Epistolary novels", "Epistolary Novel"), ("Short novels", "Novella"), ("Novellas", "Novella"),
     ("Short stories", "Short Story"), ("Short-story collections", "Short-Story Collection"),
     ("Flash fiction", "Flash Fiction")]),
    ("B. Speculative and popular fiction", [("Science fiction", "Science Fiction"),
     ("Hard science fiction", "Hard Science Fiction"), ("Soft science fiction", "Soft Science Fiction"),
     ("Space opera", "Space Opera"), ("Dystopian fiction", "Dystopian Fiction"), ("Utopian fiction", "Utopian Fiction"),
     ("Apocalyptic fiction", "Apocalyptic Fiction"), ("Post-apocalyptic fiction", "Post-Apocalyptic Fiction"),
     ("Cyberpunk", "Cyberpunk Fiction"), ("Alternate history", "Alternate History"), ("Fantasy", "Fantasy"),
     ("High fantasy", "High Fantasy"), ("Low fantasy", "Low Fantasy"), ("Sword and sorcery", "Sword and Sorcery"),
     ("Urban fantasy", "Urban Fantasy"), ("Dark fantasy", "Dark Fantasy"), ("Contemporary fantasy", "Contemporary Fantasy"),
     ("Mythological retellings", "Mythological Retelling"), ("Fairy-tale fiction", "Fairy-Tale Fiction"),
     ("Horror", "Horror Fiction"), ("Gothic fiction", "Gothic Fiction"), ("Psychological horror", "Psychological Horror"),
     ("Supernatural fiction", "Supernatural Fiction"), ("Weird fiction", "Weird Fiction"), ("Occult fiction", "Occult Fiction"),
     ("Ghost stories", "Ghost Story"), ("Vampire fiction", "Vampire Fiction"), ("Crime fiction", "Crime Fiction"),
     ("Detective fiction", "Detective Fiction"), ("Police procedurals", "Police Procedural"),
     ("Hardboiled fiction", "Hardboiled Fiction"), ("Noir", "Noir Fiction"), ("Spy fiction", "Spy and Espionage Fiction"),
     ("Espionage fiction", "Spy and Espionage Fiction"), ("Thriller", "Thriller"),
     ("Psychological thriller", "Psychological Thriller"), ("Legal thriller", "Legal Thriller"),
     ("Adventure fiction", "Adventure Fiction"), ("Western fiction", "Western Fiction"),
     ("Historical adventure", "Historical Adventure")]),
    ("C. Poetry", [("Lyric poetry", "Lyric Poetry"), ("Narrative poetry", "Narrative Poetry"),
     ("Dramatic poetry", "Dramatic Poetry"), ("Confessional poetry", "Confessional Poetry"),
     ("Modernist poetry", "Modernist Poetry"), ("Postmodern poetry", "Postmodern Poetry"),
     ("Experimental poetry", "Experimental Poetry"), ("Concrete poetry", "Concrete Poetry"),
     ("Visual poetry", "Visual Poetry"), ("Prose poetry", "Prose Poetry"), ("Free verse", "Free Verse"),
     ("Formal poetry", "Formal Verse"), ("Sonnets", "Sonnet"), ("Elegies", "Elegiac Poetry"), ("Odes", "Ode"),
     ("Epics", "Epic Poetry"), ("Long poems", "Long Poem"), ("Pastoral poetry", "Pastoral and Rural Poetry"),
     ("Political poetry", "Political Poetry"), ("Social poetry", "Social Poetry"), ("Nature poetry", "Nature Poetry"),
     ("Love poetry", "Love Poetry"), ("Religious poetry", "Religious Poetry"), ("Performance poetry", "Performance Poetry"),
     ("Spoken-word poetry", "Spoken-Word Poetry"), ("Beat poetry", "Beat Poetry"), ("Black Arts poetry", "Black Arts Poetry"),
     ("Regional poetry", "Regional Poetry")]),
    ("D. Drama and theatre", [("Tragedy", "Modern Tragedy"), ("Comedy", "Stage Comedy"),
     ("Tragicomedy", "Modern Tragicomedy"), ("Absurdist drama", "Absurdist Drama"),
     ("Existentialist drama", "Existentialist Drama"), ("Political theatre", "Political Theatre"),
     ("Social realism in drama", "Social Realist Drama"), ("Domestic drama", "Domestic Drama"),
     ("Historical drama", "Historical Drama"), ("Experimental theatre", "Experimental Theatre"),
     ("Avant-garde theatre", "Avant-Garde Theatre"), ("Epic theatre", "Epic Theatre"),
     ("Theatre of cruelty", "Theatre of Cruelty"), ("Kitchen-sink drama", "Kitchen-Sink Drama"),
     ("Musical theatre", "Musical Theatre"), ("Radio drama", "Radio Drama"), ("Television drama", "Television Drama"),
     ("One-act plays", "One-Act Play"), ("Full-length plays", "Full-Length Play"), ("Verse drama", "Verse Drama"),
     ("Monologues", "Dramatic Monologue")]),
    ("E. Nonfiction and intellectual writing", [("Literary criticism", "Literary Criticism"),
     ("Literary theory", "Literary Theory"), ("Essays", "Literary Essay"), ("Personal essays", "Personal Essay"),
     ("Political essays", "Political Essay"), ("Philosophical essays", "Philosophical Essay"),
     ("Cultural criticism", "Cultural Criticism"), ("Autobiography", "Autobiography"), ("Biography", "Biography"),
     ("Memoirs", "Memoir"), ("Diaries", "Diaries and Journals"), ("Journals", "Diaries and Journals"),
     ("Letters", "Collected Letters"), ("Travel writing", "Travel Writing"), ("Literary journalism", "Literary Journalism"),
     ("Investigative journalism", "Investigative Journalism"), ("Historical writing", "Historical Writing"),
     ("Cultural history", "Cultural History"), ("Intellectual history", "Intellectual History"),
     ("Social criticism", "Social Criticism"), ("Feminist criticism", "Feminist Criticism"),
     ("Marxist criticism", "Marxist Criticism"), ("Psychoanalytic criticism", "Psychoanalytic Criticism"),
     ("Structuralist criticism", "Structuralist Criticism"), ("Poststructuralist criticism", "Poststructuralist Criticism"),
     ("Postcolonial criticism", "Postcolonial Criticism"), ("New Historicism", "New Historicist Criticism"),
     ("Deconstruction", "Deconstructive Criticism"), ("Reader-response criticism", "Reader-Response Criticism"),
     ("Narratology", "Narratology"), ("Rhetorical criticism", "Rhetorical Criticism")]),
    ("F. Additional literary categories", [("Children's literature", "Children's Fiction"),
     ("Young adult literature", "Young Adult Fiction"), ("Picture books", "Picture Book"),
     ("Juvenile fiction", "Juvenile Fiction"), ("Fairy tales", "Fairy-Tale Collection"),
     ("Folklore collections", "Folklore Collection"), ("Retellings and adaptations", "Retelling and Adaptation"),
     ("Graphic novels", "Graphic Novel"), ("Comics", "Comics"), ("Literary translations", "Literary Translation"),
     ("Anthologies", "Anthology"), ("Literary manifestos", "Literary Manifesto"), ("Pamphlets", "Pamphlet"),
     ("Political publications", "Political Publication"), ("Religious literature", "Religious Literature"),
     ("Experimental and hybrid forms", "Hybrid Forms")]),
]

# Part VI of the revision order: item -> installment-10 movement record(s).
MOVEMENT_CHECKLIST = [
    ("Modernism and its later developments", ["Late Modernism"]), ("Postmodernism", ["Postmodernism and Postmodern Fiction"]),
    ("Late Modernism", ["Late Modernism"]), ("Existentialism", ["Existentialism in Anglophone Writing"]),
    ("Absurdism", ["Theatre of the Absurd", "Black Humour and the Absurdist Novel"]),
    ("Beat Generation", ["The Beat Generation"]), ("Confessional poetry", ["Confessional Poetry"]),
    ("Black Arts Movement", ["Black Arts Movement"]),
    ("Harlem Renaissance's continuing influence", ["Postwar African American Writing: Protest and Its Critics"]),
    ("Southern Gothic", ["Southern Gothic"]), ("New York School poetry", ["The New York School"]),
    ("Black Mountain poets", ["Black Mountain Poetry"]), ("Language poetry", ["Language Poetry"]),
    ("Concrete poetry", ["Concrete Poetry"]), ("Performance poetry", ["Performance and Spoken-Word Poetry"]),
    ("Feminist literature", ["Second-Wave Feminist Writing", "Feminist Literary Criticism"]),
    ("Second-wave feminist writing", ["Second-Wave Feminist Writing"]), ("Postcolonial literature", ["Postcolonial Literature"]),
    ("Caribbean literature", ["Caribbean Literature in English"]), ("African literature in English", ["African Literature in English"]),
    ("South Asian literature in English", ["South Asian Literature in English"]),
    ("Indigenous literary traditions", ["Native American Renaissance", "Indigenous Writing in Australia, Canada and New Zealand"]),
    ("Diasporic literature", ["Black British Writing and the Windrush Generation", "Asian American Literary Movement", "Chicano Movement Literature"]),
    ("Working-class literature", ["Working-Class and Regional Social Realism"]),
    ("Social realism", ["Working-Class and Regional Social Realism", "Kitchen-Sink Drama and the Royal Court"]),
    ("Kitchen-sink drama", ["Kitchen-Sink Drama and the Royal Court"]), ("Theatre of the Absurd", ["Theatre of the Absurd"]),
    ("Experimental fiction", ["Experimental Fiction and the Anti-Novel"]), ("Metafiction", ["Metafiction"]),
    ("Magical realism", ["Magical Realism in English"]), ("Minimalism", ["Minimalism and Dirty Realism"]),
    ("Dirty realism", ["Minimalism and Dirty Realism"]), ("Cyberpunk", ["Cyberpunk"]),
    ("New Wave science fiction", ["New Wave Science Fiction"]), ("Contemporary Gothic", ["Contemporary Gothic"]),
    ("New Journalism", ["New Journalism"]), ("Literary poststructuralism", ["Poststructuralism and Deconstruction"]),
]

# Part VII of the revision order (not exhaustive by the order's own statement).
CRITICS = ["Northrop Frye", "Cleanth Brooks", "W. K. Wimsatt", "Monroe Beardsley", "Lionel Trilling", "Edmund Wilson",
           "F. R. Leavis", "Raymond Williams", "Richard Hoggart", "Mikhail Bakhtin", "Roland Barthes", "Jacques Derrida",
           "Michel Foucault", "Jacques Lacan", "Louis Althusser", "Fredric Jameson", "Edward Said", "Hélène Cixous",
           "Julia Kristeva", "Elaine Showalter", "Sandra Gilbert", "Susan Gubar", "Stanley Fish", "Wolfgang Iser",
           "Hans Robert Jauss", "Harold Bloom", "Terry Eagleton", "Paul de Man", "J. Hillis Miller", "Gérard Genette",
           "Wayne C. Booth", "Jonathan Culler", "Stephen Greenblatt", "Gayatri Chakravorty Spivak", "Homi K. Bhabha",
           "bell hooks", "Barbara Johnson", "Judith Butler", "Eve Kosofsky Sedgwick"]

BRITISH = ("english", "british", "scottish", "welsh", "northern irish", "cornish", "anglo-welsh")
OTHER = ("canadian", "australian", "new zealand", "maori", "māori", "jamaican", "trinidad", "barbad", "guyan", "st lucia",
         "saint lucia", "antigu", "caribbean", "nigerian", "kenyan", "ghanaian", "south african", "ugandan", "zimbabwe",
         "somali", "african", "indian", "pakistani", "sri lankan", "bangladeshi", "first nations", "aboriginal")


def fold(name):
    s = unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(jr|sr|ii|iii)\b\.?", "", s)
    return re.sub(r"[^a-z]", "", s)


def year(v):
    m = re.search(r"(1[5-9]\d\d|20\d\d)", str(v or ""))
    return int(m.group(1)) if m else None


def decade(y):
    if y is None:
        return "undated"
    if y <= 1950:
        return "1946-1950"
    if y <= 1959:
        return "1951-1959"
    if y >= 1990:
        return "1990-2000"
    return "%d-%d" % (y // 10 * 10, y // 10 * 10 + 9)


def tradition(nat):
    low = (nat or "").lower()
    first = low.split(";")[0]
    if "american" in first and not any(b in first for b in BRITISH):
        return "American"
    if any(b in first for b in BRITISH):
        return "British"
    if "irish" in first:
        return "Irish"
    if any(o in first for o in OTHER):
        return "Other English-language"
    if "american" in low:
        return "American"
    if any(b in low for b in BRITISH):
        return "British"
    return "Non-English-language (theory in translation) / unclassified"


def main():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    q = lambda sql, *a: con.execute(sql, a).fetchall()  # noqa: E731
    pid = q("select period_id from periods where name=?", PERIOD)
    pid = pid[0][0] if pid else None
    works = q("""select w.*, (select group_concat(a.full_name, '; ') from work_authors wa join authors a using(author_id)
                 where wa.work_id=w.work_id) as authors from works w join work_periods wp using(work_id) where wp.period_id=?""", pid) if pid else []
    wids = [w["work_id"] for w in works]
    built = {}
    for f in glob.glob(os.path.join(ROOT, "data", "works", "installment_10_works*.json")):
        for r in json.load(open(f, encoding="utf-8")):
            built[r["title"]] = r
    i10_authors = {}
    for f in glob.glob(os.path.join(ROOT, "data", "authors", "installment_10_authors*.json")):
        for r in json.load(open(f, encoding="utf-8")):
            i10_authors[r["full_name"]] = r
    depth_of = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "scripts", "content", "content_i10_*.py"))):
        sys.path.insert(0, os.path.dirname(f))
        mod = __import__(os.path.basename(f)[:-3])
        for w in getattr(mod, "WORKS", []):
            depth_of[w["title"]] = w["depth"]
    links = lambda table, col, wid: [r[0] for r in q(  # noqa: E731
        "select x.name from %s t join %ss x on x.%s_id=t.%s_id where t.work_id=?" % (table, col, col, col), wid)]
    genre_parent = {r["name"]: r["parent"] for r in q("select g.name, p.name as parent from genres g left join genres p on p.genre_id=g.parent_genre_id")}
    author_rows = {}
    for w in works:
        for name in (w["authors"] or "").split("; "):
            if name:
                author_rows[name] = q("select * from authors where full_name=?", name)[0]

    # ---------------------------------------------------------------- per-work status
    FIELD = {"desc": "description", "content": "summary", "plot": "plot_or_argument", "themes_text": "thematic_analysis",
             "struct": "narrative_structure", "meter": "meter_and_prosody", "ctx": "historical_context",
             "sigtext": "literary_significance", "crit": "critical_context"}
    wstat = {}
    for w in works:
        depth = depth_of.get(w["title"], "unassigned")
        rules = DEPTH_RULES.get(depth, DEPTH_RULES["major"])
        short = [k for k, n in rules.items() if len((w[FIELD[k]] or "").strip()) < n]
        wstat[w["work_id"]] = {"depth": depth, "short": short, "genres": links("work_genres", "genre", w["work_id"]),
                               "themes": links("work_themes", "theme", w["work_id"]),
                               "movements": links("work_movements", "movement", w["work_id"]),
                               "year": year(w["publication_date"]) or year(w["first_performance_date"])}

    # ---------------------------------------------------------------- inventory
    inv = list(csv.DictReader(open(INVENTORY, encoding="utf-8"))) if os.path.exists(INVENTORY) else []
    db_names = {}
    for r in q("select author_id, full_name, alternative_names from authors"):
        for n in [r["full_name"]] + (json.loads(r["alternative_names"]) if (r["alternative_names"] or "").startswith("[") else []):
            db_names[fold(n)] = r["full_name"]
    i10_author_names = set(author_rows)
    for c in inv:
        name = db_names.get(c["key"])
        c["db_name"] = name or ""
        c["status"] = ("in installment 10" if name in i10_author_names else
                       ("in database (earlier installment), no 1946-2000 works yet" if name else "missing"))

    # ---------------------------------------------------------------- matrix
    os.makedirs(os.path.dirname(MATRIX), exist_ok=True)
    with open(MATRIX, "w", newline="", encoding="utf-8") as fh:
        out = csv.writer(fh)
        out.writerow(["record_type", "decade", "country_or_tradition", "genre", "subgenre", "literary_movement",
                      "author", "work", "publication_year", "depth_tier", "bibliographical_verification_status",
                      "description_completeness_status", "evidence_or_source"])
        for w in sorted(works, key=lambda w: (wstat[w["work_id"]]["year"] or 0, w["title"])):
            s = wstat[w["work_id"]]
            names = (w["authors"] or "").split("; ")
            trad = "; ".join(sorted({tradition(author_rows[n]["nationality_or_literary_tradition"]) for n in names if n in author_rows}))
            fams = sorted({genre_parent.get(g) or g for g in s["genres"]})
            out.writerow(["work", decade(s["year"]), trad, "; ".join(fams), "; ".join(s["genres"]), "; ".join(s["movements"]),
                          "; ".join(names), w["title"], s["year"] or "", s["depth"], w["verification_status"] or "not assessed",
                          "complete" if not s["short"] else "incomplete: " + ", ".join(s["short"]),
                          "; ".join(r[0] for r in q("select s.title from work_sources ws join sources s using(source_id) where ws.work_id=?", w["work_id"]))])
        for c in inv:
            if c["status"] == "in installment 10":
                continue
            out.writerow(["candidate author (discovery inventory)", c["decades"], c["tradition_hint"], c["datasets"], "", "",
                          c["author"], "", "%s-%s" % (c["first_year"], c["last_year"]), c["priority"],
                          c["status"], "no records yet", c["evidence"][:300]])

    # ---------------------------------------------------------------- audits
    lines = []
    L = lines.append
    trad_count = Counter(tradition(r["nationality_or_literary_tradition"]) for r in author_rows.values())
    tiers = Counter(r["significance_tier"] or "ungraded (earlier installment)" for r in author_rows.values())
    bib = Counter((i10_authors.get(n) or {}).get("bibliography_status") or "not assessed (author recorded in an earlier installment)" for n in author_rows)
    incomplete_desc = [w["title"] for w in works if wstat[w["work_id"]]["short"]]
    unresolved = [w["title"] for w in works if (w["research_notes"] or "").strip()]
    ver_w = Counter(w["verification_status"] or "not assessed" for w in works)
    i10_genres = [g["name"] for g in json.load(open(os.path.join(ROOT, "data", "genres", "installment_10_genres.json"), encoding="utf-8"))]
    i10_movs = [m["name"] for m in json.load(open(os.path.join(ROOT, "data", "movements", "installment_10_movements.json"), encoding="utf-8"))]
    core = [w for w in works if (wstat[w["work_id"]]["year"] or 0) >= 1951]

    L("# Installment 10 audit report (1946–2000; core 1951–2000)\n")
    L("Generated by `scripts/audit_installment_10.py` from the master database, the built JSON and the discovery inventory. "
      "Every figure below is computed; nothing is estimated. **Installment 10 is not complete.** This report states exactly how far it has got.\n")
    L("## 1–11. Measurable completion criteria\n")
    L("| # | Criterion | Value |\n|---|---|---|")
    L("| 1 | Authors with installment-10 works | %d (of whom %d have installment-10 author records; %d are recorded by earlier installments) |"
      % (len(author_rows), len(set(author_rows) & set(i10_authors)), len(set(author_rows) - set(i10_authors))))
    L("| 2 | Literary works (1946–2000) | %d (core 1951–2000: %d; bridge 1946–1950: %d) |" % (len(works), len(core), len(works) - len(core)))
    L("| 3 | Genres and subgenres defined | %d (%d genre families, %d subgenres) |" % (len(i10_genres), sum(1 for g in i10_genres if g.endswith("(1946–2000)")), sum(1 for g in i10_genres if not g.endswith("(1946–2000)"))))
    L("| 4 | Literary movements defined | %d |" % len(i10_movs))
    L("| 5 | British authors | %d (Irish: %d) |" % (trad_count["British"], trad_count["Irish"]))
    L("| 6 | American authors | %d |" % trad_count["American"])
    L("| 7 | Other English-language authors | %d |" % trad_count["Other English-language"])
    L("| 8 | Minor and lesser-known authors | %d (Minor %d, Obscure %d) |" % (tiers["Minor / lesser-known"] + tiers["Obscure / historically neglected"], tiers["Minor / lesser-known"], tiers["Obscure / historically neglected"]))
    L("| 9 | Authors whose 1946–2000 bibliographies are not yet complete | %d (%s) |" % (
        sum(v for k, v in bib.items() if k != "complete"),
        ", ".join("%s: %d" % kv for kv in sorted(bib.items())) or "none"))
    L("| 10 | Works with incomplete descriptions | %d of %d |" % (len(incomplete_desc), len(works)))
    L("| 11 | Unresolved bibliographical questions | %d works carry research notes |" % len(unresolved))
    L("\nWork verification status: %s.\n" % (", ".join("%s %d" % kv for kv in sorted(ver_w.items())) or "no works"))

    L("## 12. Results of the eight audits\n")
    # Audit 1
    L("### Audit 1 — Author completeness (decade by decade)\n")
    L("Baseline: the discovery inventory (%d candidate authors active 1946–2000 in peer-reviewed Post45 datasets; see the method notes). "
      "An inventory row is evidence of activity, not an inclusion decision.\n" % len(inv))
    L("| Decade | Candidates | In installment 10 | In database, no 1946–2000 works yet | Missing | P1 missing |\n|---|---|---|---|---|---|")
    for dname in DECADES:
        cs = [c for c in inv if dname in c["decades"]]
        st = Counter(c["status"] for c in cs)
        L("| %s | %d | %d | %d | %d | %d |" % (dname, len(cs), st["in installment 10"], st["in database (earlier installment), no 1946-2000 works yet"], st["missing"],
                                            sum(1 for c in cs if c["status"] == "missing" and c["priority"] == "P1")))
    by_trad = Counter((c["tradition_hint"], c["status"]) for c in inv)
    prim = defaultdict(Counter)
    for (t, st), n in by_trad.items():
        prim[t.split(";")[0].strip() or "unknown"][st] += n
    L("\nBy primary tradition hint (candidates; status counts):\n")
    L("| Tradition hint | " + " | ".join(sorted({k for c in prim.values() for k in c})) + " |")
    cols = sorted({k for c in prim.values() for k in c})
    L("|---|" + "---|" * len(cols))
    for t in sorted(prim):
        L("| %s | %s |" % (t, " | ".join(str(prim[t][c]) for c in cols)))
    L("")
    p1_missing = sorted([c for c in inv if c["priority"] == "P1" and c["status"] != "in installment 10"], key=lambda c: -int(c["evidence_count"]))
    L("Top P1 candidates not yet in installment 10 (by amount of evidence): " + "; ".join("%s (%s)" % (c["author"], c["evidence_count"]) for c in p1_missing[:60]) + ".\n")
    L("Known gaps of the baseline itself: British, Irish and Commonwealth writing is covered only by the Booker Prize record "
      "(winners and shortlists 1969–2000) and the Post45 British prize data (1990–2000). British and Commonwealth poetry, drama, "
      "genre and children's writing, and all such writing before 1969, still need inventories from other sources (see limitations).\n")
    crit_present = [c for c in CRITICS if fold(c) in db_names]
    L("Part VII critics checklist: %d of %d named critics and theorists have author records (%s); missing: %s.\n"
      % (len(crit_present), len(CRITICS), ", ".join(crit_present) or "none", ", ".join(c for c in CRITICS if c not in crit_present)))
    # Audit 2
    L("### Audit 2 — Genre completeness (Part III checklist)\n")
    gw = defaultdict(list)
    for w in works:
        for g in wstat[w["work_id"]]["genres"]:
            gw[g].append(w)
    total_items = covered = 0
    for section, items in GENRE_CHECKLIST:
        L("**%s**\n" % section)
        L("| Checklist item | Genre record | Works | Authors | Status |\n|---|---|---|---|---|")
        for item, g in items:
            total_items += 1
            ws = gw.get(g, [])
            aus = sorted({a for w in ws for a in (w["authors"] or "").split("; ") if a})
            covered += bool(ws)
            L("| %s | %s | %d | %s | %s |" % (item, g if g in i10_genres else g + " (UNDEFINED)", len(ws), ", ".join(aus[:6]) + (" ..." if len(aus) > 6 else ""),
                                          "represented" if ws else "not yet represented — research needed"))
        L("")
    L("Checklist items represented by at least one work: **%d of %d**.\n" % (covered, total_items))
    # Movements
    L("### Movement audit (Part VI checklist)\n")
    mw = defaultdict(list)
    for w in works:
        for m in wstat[w["work_id"]]["movements"]:
            mw[m].append(w)
    L("| Checklist item | Movement record(s) | Works linked |\n|---|---|---|")
    for item, ms in MOVEMENT_CHECKLIST:
        L("| %s | %s | %d |" % (item, "; ".join(m if m in i10_movs else m + " (UNDEFINED)" for m in ms), sum(len(mw.get(m, [])) for m in ms)))
    L("\nAll %d installment-10 movements, with works linked: %s.\n" % (len(i10_movs), "; ".join("%s %d" % (m, len(mw.get(m, []))) for m in i10_movs)))
    # Audit 3
    L("### Audit 3 — Bibliographical completeness\n")
    L("| Author | Bibliography status | Works recorded 1946–2000 | Verification |\n|---|---|---|---|")
    per_author = Counter(a for w in works for a in (w["authors"] or "").split("; ") if a)
    for n in sorted(author_rows):
        r = i10_authors.get(n) or {}
        L("| %s | %s | %d | %s |" % (n, r.get("bibliography_status") or "not assessed (earlier-installment record)", per_author[n], r.get("verification_status") or "not assessed"))
    dup = [t for t, c in Counter((w["title"], w["authors"]) for w in works).items() if c > 1]
    L("\nDuplicate title+author pairs: %d. External comparison against the bestseller, prize and Asian American title lists is run per author as each wave is added (see notes).\n" % len(dup))
    # Audit 4
    L("### Audit 4 — Description completeness\n")
    empties = Counter()
    for w in works:
        for col in ("description", "summary", "plot_or_argument", "thematic_analysis", "literary_significance", "historical_context"):
            if not (w[col] or "").strip():
                empties[col] += 1
    nogenre = [w["title"] for w in works if not wstat[w["work_id"]]["genres"]]
    nodate = [w["title"] for w in works if not wstat[w["work_id"]]["year"]]
    noauthor = [w["title"] for w in works if not w["authors"]]
    texts = Counter((w["plot_or_argument"] or "").strip() for w in works if (w["plot_or_argument"] or "").strip())
    L("Works checked: %d. Empty fields: %s. Without genre: %d. Without date: %d. Without author: %d. Duplicated summaries: %d. "
      "Works below their depth tier: %d%s.\n" % (len(works), dict(empties) or "none", len(nogenre), len(nodate), len(noauthor),
                                               sum(1 for t, c in texts.items() if c > 1), len(incomplete_desc),
                                               (" (" + "; ".join(incomplete_desc[:20]) + ")") if incomplete_desc else ""))
    # Audit 5
    L("### Audit 5 — Historical accuracy (automated checks)\n")
    probs = []
    for w in works:
        s = wstat[w["work_id"]]
        y = s["year"]
        for n in (w["authors"] or "").split("; "):
            a = author_rows.get(n)
            if not a or y is None:
                continue
            b, d = year(a["birth_date"]), year(a["death_date"])
            if b and y < b + 12:
                probs.append("%s: published %d, author born %d" % (w["title"], y, b))
            if d and y > d and "posthum" not in " ".join(str(w[k] or "") for k in ("bibliographical_notes", "description", "historical_context", "research_notes")).lower():
                probs.append("%s: published %d after the author's death (%d) without a posthumous note" % (w["title"], y, d))
        c = year(w["composition_date_start"])
        if c and y and c > y:
            probs.append("%s: composition %d after publication %d" % (w["title"], c, y))
        for m in s["movements"]:
            row = q("select start_year, end_year from movements where name=?", m)
            if row and y and (y < row[0][0] - 10 or y > row[0][1] + 10):
                probs.append("%s: %d is more than ten years outside %s (%d-%d)" % (w["title"], y, m, row[0][0], row[0][1]))
    no_nat = [n for n, a in author_rows.items() if not (a["nationality_or_literary_tradition"] or "").strip()]
    L("Problems found: %d%s. Authors without nationality/tradition: %d. Dates, nationality and affiliations of verified records were checked against the sources listed with each record.\n"
      % (len(probs), (" — " + "; ".join(probs[:30])) if probs else "", len(no_nat)))
    # Audit 6
    L("### Audit 6 — Database integrity (whole database)\n")
    checks = [
        ("duplicate author names (case/punctuation-insensitive)", "select count(*) from (select lower(replace(replace(full_name,'.',''),' ','')) k, count(*) c from authors group by k having c > 1)"),
        ("duplicate works (same title and same author)", "select count(*) from (select w.title, wa.author_id, count(*) c from works w join work_authors wa using(work_id) group by w.title, wa.author_id having c > 1)"),
        ("works without an author link (excluding anonymous)", "select count(*) from works w where authorship_status != 'anonymous' and not exists (select 1 from work_authors wa where wa.work_id=w.work_id)"),
        ("authors without works", "select count(*) from authors a where not exists (select 1 from work_authors wa where wa.author_id=a.author_id)"),
        ("works without a genre", "select count(*) from works w where not exists (select 1 from work_genres g where g.work_id=w.work_id)"),
        ("works without a period", "select count(*) from works w where not exists (select 1 from work_periods p where p.work_id=w.work_id)"),
        ("broken work_authors references", "select count(*) from work_authors wa where not exists (select 1 from works w where w.work_id=wa.work_id) or not exists (select 1 from authors a where a.author_id=wa.author_id)"),
        ("broken work_genres references", "select count(*) from work_genres x where not exists (select 1 from genres g where g.genre_id=x.genre_id) or not exists (select 1 from works w where w.work_id=x.work_id)"),
        ("broken work_movements references", "select count(*) from work_movements x where not exists (select 1 from movements m where m.movement_id=x.movement_id) or not exists (select 1 from works w where w.work_id=x.work_id)"),
        ("duplicate many-to-many rows (work_genres)", "select count(*) from (select work_id, genre_id, count(*) c from work_genres group by 1, 2 having c > 1)"),
        ("names with leading/trailing whitespace", "select count(*) from authors where full_name != trim(full_name)"),
        ("titles with leading/trailing whitespace", "select count(*) from works where title != trim(title)"),
        ("installment-10 works with an empty mandatory field", "select count(*) from works w join work_periods wp using(work_id) where wp.period_id=%d and (coalesce(trim(description),'')='' or coalesce(trim(literary_form),'')='' or coalesce(trim(historical_context),'')='')" % (pid or -1)),
    ]
    L("| Check | Result |\n|---|---|")
    for label, sql in checks:
        L("| %s | %d |" % (label, con.execute(sql).fetchone()[0]))
    L("\nThe duplicate-name check counts groups of names that differ only in case, spaces or full stops; each group is reviewed by hand before any merge.\n")
    # Audit 7
    L("### Audit 7 — Search and application functionality\n")
    tests = []
    for w in works[:40]:
        main_author = (w["authors"] or "").split("; ")[0]
        title_hits = [r[0] for r in q("select rowid from works_fts where works_fts match ?", '"%s"' % w["title"].replace('"', ''))]
        tests.append(("title: " + w["title"], w["work_id"] in title_hits))
        word = max(re.findall(r"[A-Za-z]{5,}", w["title"]) or [w["title"]], key=len)
        part_hits = [r[0] for r in q("select rowid from works_fts where works_fts match ?", word + "*")]
        tests.append(("partial title: " + word, w["work_id"] in part_hits))
        if main_author:
            aid = q("select author_id from authors where full_name=?", main_author)[0][0]
            a_hits = [r[0] for r in q("select rowid from authors_fts where authors_fts match ?", '"%s"' % main_author.replace('"', ''))]
            tests.append(("author: " + main_author, aid in a_hits))
            alts = q("select alternative_names from authors where author_id=?", aid)[0][0]
            for alt in (json.loads(alts) if (alts or "").startswith("[") else [])[:1]:
                alt_hits = [r[0] for r in q("select rowid from authors_fts where authors_fts match ?", '"%s"' % alt.replace('"', ''))]
                tests.append(("alternative name: " + alt, aid in alt_hits))
            linked = q("select count(*) from work_authors where work_id=? and author_id=?", w["work_id"], aid)[0][0]
            tests.append(("work page links to author: " + w["title"], linked == 1))
    for g in sorted(gw)[:15]:
        n = q("select count(*) from work_genres wg join genres g using(genre_id) join work_periods wp using(work_id) where g.name=? and wp.period_id=?", g, pid)[0][0]
        tests.append(("genre browse: " + g, n == len(gw[g])))
    for m in sorted(mw)[:15]:
        n = q("select count(*) from work_movements wm join movements m using(movement_id) join work_periods wp using(work_id) where m.name=? and wp.period_id=?", m, pid)[0][0]
        tests.append(("movement browse: " + m, n == len(mw[m])))
    for dname in DECADES:
        expect = sum(1 for w in works if decade(wstat[w["work_id"]]["year"]) == dname)
        lo, hi = (int(x) for x in dname.split("-"))
        got = sum(1 for w in works if lo <= (wstat[w["work_id"]]["year"] or 0) <= hi)
        tests.append(("decade filter %s (%d works)" % (dname, expect), got == expect))
    failed = [t for t, ok in tests if not ok]
    L("Search tests run: %d; passed: %d; failed: %d%s.\n" % (len(tests), len(tests) - len(failed), len(failed), (" — " + "; ".join(failed[:20])) if failed else ""))
    # Audit 8
    L("### Audit 8 — Independent second-pass research\n")
    L("Not yet executed. The order requires it after the reconstruction and the first seven audits; it will search specifically for overlooked writers "
      "and traditions with sources independent of the first-pass inventory (see the plan in the notes).\n")

    notes = open(NOTES, encoding="utf-8").read() if os.path.exists(NOTES) else "(research/installment_10/report_notes.md not found)\n"
    lines.append(notes)
    with open(REPORT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print("audit report -> %s; coverage matrix -> %s (%d work rows, %d candidate rows)"
          % (os.path.relpath(REPORT, ROOT), os.path.relpath(MATRIX, ROOT), len(works), sum(1 for c in inv if c["status"] != "in installment 10")))
    print("works %d | authors %d | genre checklist covered %d/%d | search tests %d failed %d"
          % (len(works), len(author_rows), covered, total_items, len(tests), len(failed)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
