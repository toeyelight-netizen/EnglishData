"""One authoritative read of installment 10's state, for the docs and the next wave.

Every wave has to restate the same numbers in five documents, and doing that by
hand has already produced two figures that disagreed with each other. This
script computes them once from the Norton lists and the built JSON, prints them,
and lists every line in the documentation that still carries the previous
figures, so the update is a check rather than a hunt.

Usage:
    python3 scripts/i10_state.py                # the figures
    python3 scripts/i10_state.py --stale        # only the lines to update
    python3 scripts/i10_state.py --next 12      # the next N selections, in Norton order
"""

import argparse
import collections
import csv
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LISTS = os.path.join(ROOT, "research", "installment_10", "lists")
BUILT = os.path.join(ROOT, "data", "works")
DOCS = ("README.md", "AGENT_HANDOVER.md", "documentation/PROJECT_PROGRESS.md",
        "research/installment_10/report_notes.md")


def load_list(name):
    path = os.path.join(LISTS, name)
    if not os.path.exists(path):
        return []
    return list(csv.DictReader(open(path, encoding="utf-8")))


def read_matrix():
    """The audit's own verdict, so the documents and the audit cannot disagree.

    scripts/audit_installment_10.py matches every Norton row to a record and
    writes the result to documentation/INSTALLMENT_10_COVERAGE_MATRIX.csv; this
    reads that file rather than repeating the matching.
    """
    path = os.path.join(ROOT, "documentation", "INSTALLMENT_10_COVERAGE_MATRIX.csv")
    if not os.path.exists(path):
        raise SystemExit("run scripts/audit_installment_10.py first: the coverage matrix is the source of these figures")
    return list(csv.DictReader(open(path, encoding="utf-8")))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stale", action="store_true")
    ap.add_argument("--figures", action="store_true",
                    help="print only the figures as shell assignments, for the doc update")
    ap.add_argument("--next", type=int, default=0)
    args = ap.parse_args()

    rows = read_matrix()
    works = [r for r in rows if r["record_type"] == "work"]
    todo = [r for r in rows if r["record_type"].startswith("Norton selection")]
    pending = [r for r in todo if r["bibliographical_verification_status"] == "to record"]
    undated = [r for r in todo if r["bibliographical_verification_status"] == "date to verify"]

    # one selection per author and title: Dove's three rows name one book
    unique = {}
    for r in pending:
        unique.setdefault((r["author"], r["work"]), r)
    pending = list(unique.values())

    by_author = collections.Counter(r["author"] for r in pending)
    nth = collections.Counter(by_author.values())
    recorded_sels = sum(1 for r in works
                        if not r["norton_selection"].startswith("not a Norton selection"))
    prefixes = collections.Counter(r["norton_selection"].split(":")[0] for r in works
                                   if ":" in r["norton_selection"])

    # Count anthology ROWS, not works. Two records legitimately answer two rows
    # each (Rushdie's Imaginary Homelands is printed twice in NAEL, Kingston's
    # The Woman Warrior twice in NAAL), so a work count understates coverage and
    # the gap it leaves is not the number of selections still to record.
    rows_done = collections.Counter()
    for r in works:
        for label in (r["norton_selection"] or "").split("; "):
            if label.startswith("NAEL: ") or label.startswith("NAAL: "):
                rows_done[label.split(":")[0]] += 1
    rows_todo = collections.Counter(r["norton_selection"].split(":")[0] for r in todo)

    if args.next:
        order = {}
        for i, r in enumerate(load_list("norton_naal_11e_vol_e.csv")):
            order.setdefault(r["author"], i)
        print("Next %d selections in Norton order:\n" % args.next)
        for r in sorted(pending, key=lambda r: order.get(r["author"], 10 ** 6))[: args.next]:
            print("  %-22s %-46s %s" % (r["author"], r["work"], r["publication_year"]))
        print()
        return 0

    print("works recorded            %d" % len(works))
    print("  of them Norton selections %d (%s)" % (recorded_sels, ", ".join(
        "%s %d" % (k, v) for k, v in sorted(prefixes.items()))))
    for short in ("NAEL", "NAAL"):
        done, total = rows_done[short], rows_done[short] + rows_todo[short]
        print("  %s rows recorded        %d of %d%s" % (short, done, total,
              "  COMPLETE" if done == total else ""))
    print("selections still to record %d" % len(pending))
    print("  undated (may be out of period) %d" % len(undated))
    by_auth_author = collections.Counter()
    for r in works:
        for name in (r["author"] or "").split("; "):
            if name:
                by_auth_author[name] += 1
    print("authors with records      %d" % len(by_auth_author))
    print("authors still to record   %d" % len(by_author))
    print("  of 1 selection          %d" % nth[1])
    print("  of 2-3                  %d" % (nth[2] + nth[3]))
    print("  of 4-6                  %d" % sum(nth[i] for i in (4, 5, 6)))
    print("  of 7 or more            %d" % sum(c for n, c in nth.items() if n >= 7))
    print("\nlargest remaining authors:")
    for a, n in by_author.most_common(10):
        print("  %-22s %d" % (a, n))

    if args.figures:
        print("WORKS=%d SEL=%d PENDING=%d AUTHORS=%d AUTH_PENDING=%d UNDATED=%d "
              "NAEL=%d/%d NAAL=%d/%d"
              % (len(works), recorded_sels, len(pending), len(by_auth_author),
                 len(by_author), len(undated),
                 rows_done["NAEL"], rows_done["NAEL"] + rows_todo["NAEL"],
                 rows_done["NAAL"], rows_done["NAAL"] + rows_todo["NAAL"]))
        return 0

    if args.stale:
        stale = re.compile(r"\b(217|66|173|84|165 of the 255|of 255 selections)\b")
        print("\nlines in the documentation that carry a superseded figure:")
        hits = 0
        for rel in DOCS:
            path = os.path.join(ROOT, rel)
            if not os.path.exists(path):
                continue
            for i, line in enumerate(open(path, encoding="utf-8"), 1):
                if stale.search(line):
                    hits += 1
                    print("  %s:%d  %s" % (rel, i, line.strip()[:140]))
        print("  %d line(s); the ones in the last three entries of PROJECT_PROGRESS.md and in the" % hits)
        print("  closing entries of report_notes.md are history, not state, and stay as they are.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
