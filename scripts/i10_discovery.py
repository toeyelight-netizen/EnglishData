"""Build the installment-10 author discovery inventory (1946-2000).

The inventory is the research baseline for Audit 1 (author completeness) and
Audit 8 (second-pass discovery). It lists candidate authors with the evidence
that they were active in 1946-2000, drawn from peer-reviewed datasets of the
Post45 Data Collective (Emory University), downloaded from
https://github.com/Post45-Data-Collective/data:

  major_literary_prizes     US prize winners 1918-2020 (Wikidata/VIAF/LCCN ids)
  british_literary_prizes   British prize winners and shortlists 1990-2022
  nyt_hardcover_fiction_bestsellers   bestseller titles 1931-2020 (authority ids)
  asian_american_literature Asian American texts and authors by scholarly study
  nea_writing_fellowships   NEA literature fellows from 1967
  speculative_fiction_novels, playboy_fiction_index   (no index documentation in
      the repository: used for discovery only, never as verification)
  iowa_writers_workshop     Program Era Project records of the Iowa Writers' Workshop
      (graduations 1931-2014 with thesis genre; works by Workshop authors held by
      HathiTrust). Only graduates with a library authority record (LCCN, VIAF or
      Wikidata), i.e. published authors, are used.

Curated lists transcribed from cited sources (research/installment_10/lists/):

  booker_prize_1969_2000.csv   Booker Prize winners, shortlists and Lost Booker
  heinemann_african_writers_series_1962_2003.csv   every entry of the Heinemann
      African Writers Series table in Wikipedia's article, which reproduces Nourdin
      Bejjit's bibliography printed in James Currey, Africa Writes Back (2008),
      pp. 301-310, plus the unnumbered titles of 1985-2003 and the contributors the
      table names for anthologies. Translations (marked in the entry, or inferred
      from the author's other marked entries or a documented non-English writing
      language), reprints of earlier texts, unassigned numbers, collectives and
      pre-modern authors are transcribed but are not used as evidence.

A row is evidence of activity, not an inclusion decision. Priority tiers:

  P1  winner of a major prize (Pulitzer, National Book Award, Bollingen, US Poet
      Laureate/Consultant, Booker, Whitbread Book of the Year, T. S. Eliot,
      Orange, James Tait Black, PEN/Faulkner, Wallace Stevens, Lannan Lifetime);
      an Asian American text with 10+ instances of scholarly study; an author
      with 3+ NYT bestsellers 1946-2000
  P2  other prize winners, British shortlists, one or two bestsellers, Asian
      American texts with 3+ instances of study
  P3  NEA fellows, Playboy fiction contributors, speculative-fiction authors with
      10+ novels dated 1946-2000, published Iowa Writers' Workshop graduates and
      authors; African Writers Series editors, contributors, self-translations and
      non-fiction (an original English-language title in the series is P2)

Names given surname-first in a dataset ('Walsh, Jill Paton') are turned round before
matching, so that one author is one candidate whatever the dataset's name order.

Usage:  python3 scripts/i10_discovery.py [--data /tmp/post45/data-main]
Writes: research/installment_10/discovery_inventory.csv
"""

import argparse
import csv
import io
import os
import re
import subprocess
import sys
import unicodedata
import zipfile
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "research", "installment_10", "discovery_inventory.csv")
ARCHIVE = "https://codeload.github.com/Post45-Data-Collective/data/zip/refs/heads/main"
LO, HI = 1946, 2000
csv.field_size_limit(10 ** 9)

MAJOR_US = {"Pulitzer Prize", "National Book Award", "Bollingen Prize for Poetry", "Poet Laureate",
            "Faulkner Award for Fiction", "Wallace Stevens Award", "Lannan Lifetime Achievement Award"}
MAJOR_UK = {"Booker Prize", "Whitbread Book of the Year", "TS Eliot Prize", "Women's Prize for Fiction",
            "James Tait Black Prize for Fiction"}


def fold(name):
    s = unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(jr|sr|ii|iii)\b\.?", "", s)
    return re.sub(r"[^a-z]", "", s)


# Corrections of names garbled in the source datasets (logged in report_notes.md).
NAME_FIXES = {"Step hen King": "Stephen King",
              # African Writers Series table: a misprinted name, or a spelling that differs
              # from the same person's other entries in the table
              "Sepho Sepamia": "Sipho Sepamla", "Cosmo Peterse": "Cosmo Pieterse",
              "Musaemura Zimuya": "Musaemura Zimunya", "Molara Ogunidpe Leslie": "Molara Ogundipe-Leslie",
              "Ezekiel Mphahlele": "Es'kia Mphahlele", "Herman C. Bosman": "Herman Charles Bosman",
              "JP Clark Bekederemo": "J. P. Clark"}
SUFFIX = re.compile(r"^(jr|sr|ii|iii|iv)\.?$", re.I)
EDITOR = re.compile(r"^(ed|eds|editor|editors|comp)\.?$", re.I)
# Reprinted classics by authors who died long before 1946 (not in the master database).
PRE_PERIOD = {"Guy de Maupassant", "Jean de la Fontaine", "Abbe de Brantome"}


def aws_evidence(r):
    where = "no. %s" % r["number"] if r["number"] != "u" else "unnumbered"
    role = "" if r["role"] == "original" else ", " + r["role"].replace("_", " ")
    return "African Writers Series %s%s: %s" % (where, role, r["title"])


CURATED = {
    "booker_prize_1969_2000.csv": {
        "label": "Booker Prize", "dataset": "booker", "hint": "UK/Commonwealth/Irish",
        "priority": {"winner": 1, "shortlist": 1, "lost_booker_winner": 1, "lost_booker_shortlist": 1,
                     "lost_booker_longlist": 2},
    },
    "heinemann_african_writers_series_1962_2003.csv": {
        "label": "African Writers Series", "dataset": "aws", "hint": "Africa (AWS)",
        "priority": {"original": 2, "self_translation": 3, "nonfiction": 3, "editor": 3,
                     "anthology_compiler": 3, "contributor": 3},
        "skip": {"translation", "translation_inferred", "contributor_translation", "reprint",
                 "never_assigned", "never_published", "collective", "premodern"},
        "evidence": aws_evidence,
    },
}


def natural_order(name):
    """'Walsh, Jill Paton' -> 'Jill Paton Walsh'; 'Gates, Henry Louis, Jr.' -> 'Henry Louis Gates Jr.'.

    Used only for datasets that give one person per field, surname first, so that a
    natural-order list such as 'A B, C D' is never turned round by mistake."""
    parts = [p.strip() for p in name.split(",") if not EDITOR.match(p.strip())]
    if len(parts) < 2:
        return parts[0] if parts else name
    rest = [p for p in parts[1:] if p and not SUFFIX.match(p)]
    suffix = [p for p in parts[1:] if SUFFIX.match(p)]
    if len(rest) != 1:
        return name
    return " ".join([rest[0], parts[0]] + suffix)


def heading_name(h):
    """A library authority heading without life dates or fuller forms:
    'Wright, Charles, 1935-' -> 'Wright, Charles'; 'McGalliard, John Calvin.' -> 'McGalliard, John Calvin'."""
    h = re.sub(r"\s*\([^)]*\)", "", h or "")
    h = re.sub(r",?\s*(?:b\.|d\.|fl\.)?\s*\d{4}-?(?:\d{4})?\??\.?\s*$", "", h)
    return h.strip().rstrip(".,").strip()


def split_credit(name, inverted=False):
    """Split joint credits ('X and Y', 'X with Y', 'written and illustrated by X and Y')."""
    name = NAME_FIXES.get(name.strip(), name.strip())
    name = re.sub(r"^(?:written and illustrated by|illustrated by|edited by|by)\s+", "", name, flags=re.I)
    parts = [p.strip() for p in re.split(r"\s+(?:and|with|&)\s+", name) if p.strip()]
    if inverted:
        parts = [natural_order(p) for p in parts]
    if len(parts) > 1:
        surname = parts[-1].split()[-1]
        parts = [p if " " in p else "%s %s" % (p, surname) for p in parts]
    parts = [NAME_FIXES.get(p, p) for p in parts]
    return [p for p in parts if p not in PRE_PERIOD]


def pre_period_db_authors():
    """Folded names of master-database authors who died before 1946 (reprints, not activity)."""
    db = os.path.join(ROOT, "database", "English_Literature_Master.db")
    if not os.path.exists(db):
        return set()
    import sqlite3
    out = set()
    for name, alts, death in sqlite3.connect(db).execute("select full_name, alternative_names, death_date from authors"):
        m = re.match(r"\s*(\d{3,4})", str(death or ""))
        if m and int(m.group(1)) < 1946:
            out.add(fold(name))
    return out


def decade(y):
    """The decade groups used by the installment-10 audits (1946-1950 is the bridge)."""
    if y <= 1950:
        return "1946-1950"
    if y <= 1959:
        return "1951-1959"
    if y >= 1990:
        return "1990-2000"
    return "%d-%d" % (y // 10 * 10, y // 10 * 10 + 9)


def year(v):
    m = re.search(r"(19|20)\d\d", str(v or ""))
    return int(m.group()) if m else None


def ensure_data(path):
    if os.path.isdir(path):
        return path
    os.makedirs(os.path.dirname(path), exist_ok=True)
    print("downloading", ARCHIVE)
    raw = subprocess.run(["curl", "-sSL", ARCHIVE], check=True, capture_output=True).stdout
    zipfile.ZipFile(io.BytesIO(raw)).extractall(os.path.dirname(path))
    return path


def rows(path):
    with open(path, encoding="utf-8-sig", errors="replace") as fh:
        yield from csv.DictReader(fh)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--data", default="/tmp/post45/data-main")
    args = ap.parse_args()
    d = ensure_data(args.data)
    inv = defaultdict(lambda: {"names": set(), "ids": {}, "evidence": [], "years": set(),
                               "datasets": set(), "hints": set(), "priority": 3})

    def add(name, yr, evidence, dataset, priority, hint, ids=None, inverted=False):
        if not name or not yr or not LO <= yr <= HI:
            return
        for person in split_credit(name, inverted):
            add_one(person, yr, evidence, dataset, priority, hint, ids)

    def add_one(name, yr, evidence, dataset, priority, hint, ids=None):
        key = fold(name)
        if not key:
            return
        e = inv[key]
        e["names"].add(name.strip().rstrip(".,; "))
        e["evidence"].append("%s (%d)" % (evidence, yr))
        e["years"].add(yr)
        e["datasets"].add(dataset)
        e["hints"].add(hint)
        e["priority"] = min(e["priority"], priority)
        for k, v in (ids or {}).items():
            if v and v.strip() and k not in e["ids"]:
                e["ids"][k] = v.strip()

    for r in rows(os.path.join(d, "major_literary_prizes", "major_literary_prizes-winners_judges.csv")):
        if r["role"] != "winner":
            continue
        prize = r["prize_name"].strip()
        label = prize + (" (%s)" % r["prize_genre"] if r["prize_genre"] not in ("", "no genre") else "")
        add(r["full_name"], year(r["prize_year"]), label, "us_prizes", 1 if prize in MAJOR_US else 2, "US",
            {"wikidata": r.get("author_wikidata"), "viaf": r.get("author_viaf"), "lccn": r.get("author_lccn")})
    for r in rows(os.path.join(d, "british_literary_prizes", "british_literary_prizes-1990-2022.csv")):
        prize = r["prize_name"].strip()
        win = r["person_role"] == "winner"
        add(r["name"], year(r["prize_year"]), ("%s %s: %s" % (prize, r["person_role"], r.get("book_title") or "")).strip(),
            "uk_prizes", 1 if (win and prize in MAJOR_UK) else 2, "UK/Commonwealth", {"viaf": r.get("viaf")},
            inverted=True)
    best = defaultdict(list)
    for r in rows(os.path.join(d, "nyt_hardcover_fiction_bestsellers", "nyt_hardcover_fiction_bestsellers-titles.csv")):
        y = year(r.get("first_week") or r.get("year"))
        if y and LO <= y <= HI:
            best[fold(r["author"])].append((r, y))
    for key, items in best.items():
        prio = 1 if len(items) >= 3 else 2
        for r, y in items:
            add(r["author"], y, "NYT bestseller: %s" % r["title"].title(), "nyt_bestsellers", prio, "US/popular",
                {"wikidata": r.get("author_wikidata"), "viaf": r.get("author_viaf"), "lccn": r.get("author_lccn")})
    for r in rows(os.path.join(d, "asian_american_literature", "asian_american_texts.csv")):
        n = int(r.get("instances_of_study") or 0)
        prio = 1 if n >= 10 else (2 if n >= 3 else 3)
        for col in ("author_name", "2_author_name", "3_author_name", "4_author_name"):
            add(r.get(col), year(r.get("publication_year")), "Asian American text: %s [%s; studied %d]"
                % (r["title"], r.get("genre") or "?", n), "asian_american", prio, "US/Asian American", inverted=True)
    for r in rows(os.path.join(d, "nea_writing_fellowships", "nea_fellowships.csv")):
        add(r["full_name_firstlast"], year(r["nea_grant_year"]), "NEA literature fellowship", "nea", 3, "US")
    for r in rows(os.path.join(d, "playboy_fiction_index", "playboy-fiction-index-metadata_20260415.csv")):
        add(r["author_name"], year(r.get("year") or r.get("publication_date")), "Playboy fiction: %s" % r["title"],
            "playboy", 3, "periodical")
    spec = defaultdict(list)
    for r in rows(os.path.join(d, "speculative_fiction_novels", "speculative-fiction-novels-dataset-CSV.csv")):
        y = year(r.get("year"))
        if y and LO <= y <= HI and (r.get("orig_lang") or "en").lower() in ("en", "english", "eng", ""):
            for a in (r.get("authors") or "").split("|"):
                spec[fold(a)].append((a.strip(), y, r["title"]))
    for key, items in spec.items():
        if len(items) >= 10:
            for a, y, t in items:
                add(a, y, "speculative novel: %s" % t, "speculative", 3, "SF/fantasy/horror")

    # Iowa Writers' Workshop (Program Era Project): published graduates and authors only.
    iww = os.path.join(d, "iowa_writers_workshop")
    people = {r["person_id"]: r for r in rows(os.path.join(iww, "iowa_writers_workshop-people.csv"))}

    def iww_hint(pid):
        country = (people.get(str(pid).split(".")[0]) or {}).get("country", "").strip()
        return "US" if country in ("", "United States") else "%s (Iowa Writers' Workshop)" % country

    # The name used is the library authority heading where there is one, then the
    # heading of the person's HathiTrust works, then given and family name without
    # middle names (the graduation records give full legal names, which would make a
    # second candidate for an author published under a shorter form).
    hathi_name = {}
    for r in rows(os.path.join(iww, "iowa_writers_workshop-hathitrust_metadata.csv")):
        pid = str(r.get("person_id", "")).split(".")[0]
        hathi_name.setdefault(pid, heading_name(r.get("author_authorized_heading")) or r.get("author1_normalized", ""))

    def iww_name(r):
        pid = str(r["graduate_id"]).split(".")[0]
        person = people.get(pid) or {}
        short = "%s, %s" % (person["family_name"], person["given_name"]) \
            if person.get("family_name") and person.get("given_name") else ""
        return heading_name(r.get("author_authorized_heading")) or hathi_name.get(pid) or short or r["graduate_name"]

    for r in rows(os.path.join(iww, "iowa_writers_workshop-graduations.csv")):
        ids = {"wikidata": r.get("author_wikidata"), "viaf": r.get("author_viaf"), "lccn": r.get("author_lccn")}
        if not any((v or "").strip() for v in ids.values()):
            continue
        add(iww_name(r), year(r["year"]), "Iowa Writers' Workshop %s, %s: %s"
            % (r.get("degree") or "graduate", (r.get("genre") or "genre not given").lower(), (r.get("thesis_title") or "").rstrip(" .")),
            "iowa", 3, iww_hint(r["graduate_id"]), ids, inverted=True)
    for r in rows(os.path.join(iww, "iowa_writers_workshop-hathitrust_metadata.csv")):
        add(heading_name(r.get("author_authorized_heading")) or r["author1_normalized"], year(r["date"]), "Iowa Writers' Workshop author, HathiTrust copy: %s"
            % (r.get("title") or "").rstrip(" ./"), "iowa", 3, iww_hint(r.get("person_id", "")),
            {"wikidata": r.get("author_wikidata_qid"), "viaf": r.get("author_viaf"), "lccn": r.get("author_lccn")},
            inverted=True)

    # Curated lists transcribed from cited sources (research/installment_10/lists/*.csv;
    # each list's source is recorded in data/sources/installment_10_sources.json).
    for fname, spec in CURATED.items():
        path = os.path.join(ROOT, "research", "installment_10", "lists", fname)
        if not os.path.exists(path):
            print("curated list missing: %s" % fname)
            continue
        for r in csv.DictReader(open(path, encoding="utf-8")):
            if r["role"] in spec.get("skip", ()):
                continue
            ev = spec["evidence"](r) if "evidence" in spec else \
                "%s %s: %s" % (spec["label"], r["role"].replace("_", " "), r["title"])
            add(r["author"], year(r["year"]), ev, spec["dataset"], spec["priority"].get(r["role"], 2), spec["hint"])

    # 'Joe W. Haldeman' and 'Joe Haldeman' are one candidate when either form comes from
    # the Iowa records, whose legal names and authority headings carry middle initials.
    merged = []
    for key in sorted(inv):
        e = inv.get(key)
        if not e:
            continue
        for name in sorted(e["names"]):
            tokens = name.replace(".", " ").split()
            if len(tokens) < 3 or not all(len(t) == 1 for t in tokens[1:-1]):
                continue
            short = fold(tokens[0] + " " + tokens[-1])
            if short != key and short in inv and "iowa" in (e["datasets"] | inv[short]["datasets"]):
                t = inv[short]
                t["names"] |= e["names"]
                t["evidence"] += e["evidence"]
                t["years"] |= e["years"]
                t["datasets"] |= e["datasets"]
                t["hints"] |= e["hints"]
                t["priority"] = min(t["priority"], e["priority"])
                for k, v in e["ids"].items():
                    t["ids"].setdefault(k, v)
                del inv[key]
                merged.append(name)
                break
    print("merged %d middle-initial variants into the shorter name: %s" % (len(merged), ", ".join(merged)))

    dead = pre_period_db_authors()
    dropped = sorted(k for k in inv if k in dead)
    for k in dropped:
        del inv[k]
    print("dropped %d candidates who died before 1946 (reprints): %s" % (len(dropped), ", ".join(dropped[:12])))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["key", "author", "priority", "first_year", "last_year", "decades", "tradition_hint",
                    "datasets", "evidence_count", "evidence", "wikidata", "viaf", "lccn"])
        for key, e in sorted(inv.items(), key=lambda kv: (kv[1]["priority"], kv[0])):
            ys = sorted(e["years"])
            decades = sorted({decade(y) for y in ys})
            # by year, then text: a deterministic order (sorting by year alone left ties
            # in set order, which changes with Python's hash seed)
            ev = sorted(set(e["evidence"]), key=lambda s: (s[-5:-1], s))
            w.writerow([key, sorted(e["names"], key=lambda n: (len(n), n))[-1], "P%d" % e["priority"], ys[0], ys[-1],
                        "; ".join(decades), "; ".join(sorted(e["hints"])), "; ".join(sorted(e["datasets"])),
                        len(ev), " | ".join(ev[:12]) + (" | ..." if len(ev) > 12 else ""),
                        e["ids"].get("wikidata", ""), e["ids"].get("viaf", ""), e["ids"].get("lccn", "")])
    counts = defaultdict(int)
    for e in inv.values():
        counts["P%d" % e["priority"]] += 1
    print("discovery inventory: %d candidate authors (%s) -> %s"
          % (len(inv), ", ".join("%s %d" % kv for kv in sorted(counts.items())), os.path.relpath(OUT, ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
