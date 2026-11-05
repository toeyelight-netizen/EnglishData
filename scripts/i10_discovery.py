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

A row is evidence of activity, not an inclusion decision. Priority tiers:

  P1  winner of a major prize (Pulitzer, National Book Award, Bollingen, US Poet
      Laureate/Consultant, Booker, Whitbread Book of the Year, T. S. Eliot,
      Orange, James Tait Black, PEN/Faulkner, Wallace Stevens, Lannan Lifetime);
      an Asian American text with 10+ instances of scholarly study; an author
      with 3+ NYT bestsellers 1946-2000
  P2  other prize winners, British shortlists, one or two bestsellers, Asian
      American texts with 3+ instances of study
  P3  NEA fellows, Playboy fiction contributors, speculative-fiction authors with
      10+ novels dated 1946-2000

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
NAME_FIXES = {"Step hen King": "Stephen King"}
# Reprinted classics by authors who died long before 1946 (not in the master database).
PRE_PERIOD = {"Guy de Maupassant", "Jean de la Fontaine", "Abbe de Brantome"}


def split_credit(name):
    """Split joint credits ('X and Y', 'X with Y', 'written and illustrated by X and Y')."""
    name = NAME_FIXES.get(name.strip(), name.strip())
    name = re.sub(r"^(?:written and illustrated by|illustrated by|edited by|by)\s+", "", name, flags=re.I)
    parts = [p.strip() for p in re.split(r"\s+(?:and|with|&)\s+", name) if p.strip()]
    if len(parts) > 1:
        surname = parts[-1].split()[-1]
        parts = [p if " " in p else "%s %s" % (p, surname) for p in parts]
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

    def add(name, yr, evidence, dataset, priority, hint, ids=None):
        if not name or not yr or not LO <= yr <= HI:
            return
        for person in split_credit(name):
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
            "uk_prizes", 1 if (win and prize in MAJOR_UK) else 2, "UK/Commonwealth", {"viaf": r.get("viaf")})
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
                % (r["title"], r.get("genre") or "?", n), "asian_american", prio, "US/Asian American")
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
            ev = sorted(set(e["evidence"]), key=lambda s: s[-5:-1])
            w.writerow([key, sorted(e["names"], key=len)[-1], "P%d" % e["priority"], ys[0], ys[-1],
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
