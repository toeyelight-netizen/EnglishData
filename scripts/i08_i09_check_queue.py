#!/usr/bin/env python3
"""Order the installment 8-9 work records for the outstanding title and plot check.

Installment 9 turned out to contain four wrong or invented plots and one
fabricated title ("Picture of Mortimer and Ray", removed 2026-11-06). The
fabricated record had a principal_characters field that names no one ("the two
young men; the lecturers; the reviewers"). Priority 1 lists every unchecked
record with that signature, priority 2 every other unchecked record, and
priority 3 the records already rewritten from a source (found through their
per-record source links).

The signal is weak, and the ordering is only a starting point:
- It would not have caught the four bad plots. Their character lists contained
  proper names, some of them invented ("John Easter", "Frieda").
- Any capitalised word clears it, so "the visitors; the guides; the Moscow
  scene" (the old Winter in Moscow record) is not flagged.
- Many hits are legitimate, such as poems whose speakers are unnamed.
Every priority 1 and 2 record still needs checking against a source.

Writes research/installment_10/i08_i09_check_queue.csv.
"""

import csv
import glob
import json
import os
import re

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(PROJECT_ROOT, "research", "installment_10", "i08_i09_check_queue.csv")
NON_NAMES = {"the", "a", "an", "his", "her", "their", "its", "two", "three"}


def load(kind, num):
    rows = []
    for path in sorted(glob.glob(os.path.join(PROJECT_ROOT, "data", kind, "installment_%s_%s*.json" % (num, kind)))):
        payload = json.load(open(path, encoding="utf-8"))
        rows.extend(payload[kind] if isinstance(payload, dict) else payload)
    return rows


def names_someone(part):
    """True if a character entry contains a proper name: a capitalised word that
    is not merely the sentence-initial article or possessive."""
    tokens = part.split()
    if not tokens:
        return False
    first = tokens[0]
    if first[:1].isupper() and first.lower() not in NON_NAMES:
        return True
    return any(t[:1].isupper() for t in tokens[1:] if t[:1].isalpha())


def nameless_characters(chars):
    parts = [p.strip() for p in (chars or "").split(";") if p.strip()]
    return bool(parts) and not any(names_someone(p) for p in parts)


def relationship_rows(num, key):
    rows = []
    for path in glob.glob(os.path.join(PROJECT_ROOT, "data", "relationships", "installment_%s_relationships*.json" % num)):
        payload = json.load(open(path, encoding="utf-8"))
        if isinstance(payload, dict):
            rows.extend(payload.get(key, []))
    return rows


def sourced_titles(num):
    """Titles whose work-source links include a per-record source added during
    installment 10 (the corrections), i.e. records already rewritten from a source.
    Rows have the shape {"work": title, "sources": [source titles]}."""
    path = os.path.join(PROJECT_ROOT, "data", "sources", "installment_10_sources.json")
    record_sources = {s["title"] for s in json.load(open(path, encoding="utf-8"))}
    return {row["work"] for row in relationship_rows(num, "work_sources")
            if record_sources.intersection(row.get("sources") or [])}


def authors_by_title(num):
    """Work title -> author names, from work_authors rows {"work", "author", ...}."""
    out = {}
    for row in relationship_rows(num, "work_authors"):
        out.setdefault(row["work"], []).append(row["author"])
    return out


def main():
    rows = []
    for num in ("08", "09"):
        checked = sourced_titles(num)
        authors = authors_by_title(num)
        for w in load("works", num):
            author = "; ".join(authors.get(w["title"], []))
            flag = nameless_characters(w.get("principal_characters"))
            status = "rewritten from a source" if w["title"] in checked else "not yet checked"
            rows.append({
                "installment": num,
                "priority": 1 if (flag and status == "not yet checked") else (2 if status == "not yet checked" else 3),
                "signal": "characters name no one" if flag else "",
                "check_status": status,
                "title": w["title"],
                "author": author,
                "publication_date": w.get("publication_date") or "",
                "literary_form": w.get("literary_form") or "",
                "principal_characters": w.get("principal_characters") or "",
            })
    # Installment 9's later batches are the least reliable, so within a priority
    # installment 9 comes first.
    rows.sort(key=lambda r: (r["priority"], r["installment"] != "09", r["title"].lower()))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    counts = {}
    for r in rows:
        counts[(r["installment"], r["priority"])] = counts.get((r["installment"], r["priority"]), 0) + 1
    print("wrote %s: %d records" % (os.path.relpath(OUT, PROJECT_ROOT), len(rows)))
    for key in sorted(counts):
        print("  installment %s, priority %d: %d" % (key[0], key[1], counts[key]))


if __name__ == "__main__":
    main()
