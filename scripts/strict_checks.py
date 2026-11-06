"""Strict record checks for installments built without template enrichment.

Installment 10 onwards sets ``META["strict"] = True``. The builder then skips
``content_enrich`` entirely (no composed text) and calls :func:`check`, which
blocks the build when a record falls short of the depth its tier requires,
repeats prose from another record, uses boilerplate, cites no source while
claiming verification, or falls outside the installment's date window.

Depth tiers (works):

    major        full seven-part record; several-paragraph plot or argument
    significant  every analytical field, shorter
    minor        shorter but specific record; critical context optional

Field names are those of the content-module dict produced by
``scripts/content/i10_lib.py`` (``desc`` overview, ``content`` contents,
``plot`` summary or argument, ``themes_text`` thematic analysis, ``struct``
structure and narrative method, ``meter`` style and language, ``ctx``
historical context, ``sigtext`` significance, ``crit`` critical context).
"""

import json
import os
import re
from collections import defaultdict

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEPTH_RULES = {
    "major": {"desc": 250, "content": 250, "plot": 1200, "themes_text": 350, "struct": 150,
              "meter": 150, "ctx": 150, "sigtext": 250, "crit": 200},
    "significant": {"desc": 150, "content": 120, "plot": 450, "themes_text": 150, "struct": 80,
                    "meter": 80, "ctx": 100, "sigtext": 120},
    "minor": {"desc": 100, "plot": 150, "themes_text": 60, "struct": 50, "meter": 50,
              "ctx": 60, "sigtext": 60},
}
FIELD_LABELS = {"desc": "overview", "content": "content", "plot": "summary/argument",
                "themes_text": "thematic analysis", "struct": "structure", "meter": "style",
                "ctx": "historical context", "sigtext": "significance", "crit": "critical context"}
TEXT_FIELDS = tuple(FIELD_LABELS)

VERIFICATION_STATUS = {"verified", "partially verified", "unverified"}
BIBLIOGRAPHY_STATUS = {"complete", "substantially complete", "incomplete"}

# Phrases that signal template or padding prose rather than a description.
BANNED = [
    "explores various aspects", "aspects of human nature", "it is catalogued here",
    "is a prose work of", "is a prose fiction work of", "stands as a testament",
    "rich tapestry", "delves into", "timeless classic", "lorem ipsum", "placeholder",
    "todo", "tbd", "? no", "to be written", "description pending", "[citation",
    "this work explores", "explores themes of", "explores the themes of", "in conclusion",
    "insert text", "add description", "the work deals with various",
]


def _banned_hits(low):
    """Banned phrases present in lower-cased text; alphabetic phrases match on word
    boundaries so that, e.g., 'todo' does not fire on 'Todorov'."""
    hits = []
    for phrase in BANNED:
        if phrase[0].isalnum() and phrase[-1].isalnum():
            if re.search(r"(?<![\w])" + re.escape(phrase) + r"(?![\w])", low):
                hits.append(phrase)
        elif phrase in low:
            hits.append(phrase)
    return hits

YEAR = re.compile(r"(1[89]\d\d|20\d\d)")


def _year(value):
    m = YEAR.search(str(value or ""))
    return int(m.group(1)) if m else None


def _sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text or "") if len(s.strip()) >= 60]


def _load_names(kind, num):
    path = os.path.join(PROJECT_ROOT, "data", kind, "installment_%s_%s.json" % (num, kind))
    if not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8") as handle:
        return {row["name"] for row in json.load(handle)}


def _source_titles(num):
    path = os.path.join(PROJECT_ROOT, "data", "sources", "installment_%s_sources.json" % num)
    if not os.path.exists(path):
        return set()
    with open(path, encoding="utf-8") as handle:
        return {row["title"] for row in json.load(handle)}


def check(works, authors, meta):
    num = "%02d" % int(meta.get("installment", 10))
    lo, hi = meta.get("window", (1946, 2000))
    genres, themes, movements = (_load_names(k, num) for k in ("genres", "themes", "movements"))
    sources = _source_titles(num)
    problems = []

    # ---- authors
    work_authors = {w["author"] for w in works} | {c for w in works for c in w.get("coauthors") or []}
    for a in authors:
        n = a["name"]
        if a.get("bibliography_status") not in BIBLIOGRAPHY_STATUS:
            problems.append("author %r: bibliography_status must be one of %s" % (n, sorted(BIBLIOGRAPHY_STATUS)))
        if a.get("verification_status") not in VERIFICATION_STATUS:
            problems.append("author %r: verification_status must be one of %s" % (n, sorted(VERIFICATION_STATUS)))
        if len((a.get("biblio_note") or "").strip()) < 80:
            problems.append("author %r: bibliography note (coverage statement) missing or too short" % n)
        if len((a.get("bio") or "").strip()) < 400:
            problems.append("author %r: biography shorter than 400 characters" % n)
        if a.get("verification_status") != "unverified" and not a.get("sources"):
            problems.append("author %r: marked %s but cites no source" % (n, a.get("verification_status")))
        for s in a.get("sources") or []:
            if s not in sources:
                problems.append("author %r: unknown source %r" % (n, s))
        if n not in work_authors:
            problems.append("author %r has no work in this installment" % n)
        low = " ".join(str(a.get(k) or "") for k in ("bio", "prof", "style", "conc", "sig")).lower()
        for phrase in _banned_hits(low):
            problems.append("author %r: boilerplate phrase %r" % (n, phrase))

    # ---- works
    seen_text = {}
    sentence_owner = defaultdict(set)
    for w in works:
        t = w["title"]
        depth = w.get("depth")
        rules = DEPTH_RULES.get(depth)
        if rules is None:
            problems.append("work %r: depth must be one of %s" % (t, sorted(DEPTH_RULES)))
            continue
        for field, minimum in rules.items():
            text = (w.get(field) or "").strip()
            if len(text) < minimum:
                problems.append("work %r (%s): %s is %d characters; at least %d required"
                                % (t, depth, FIELD_LABELS[field], len(text), minimum))
        year = _year(w.get("pub")) or _year(w.get("perf"))
        if year is None:
            problems.append("work %r: no publication or first-performance year" % t)
        elif not lo <= year <= hi:
            problems.append("work %r: year %d outside %d-%d" % (t, year, lo, hi))
        if not w.get("genres"):
            problems.append("work %r: no genre" % t)
        if not w.get("themes"):
            problems.append("work %r: no theme" % t)
        for kind, names, pool in (("genre", w.get("genres"), genres), ("theme", w.get("themes"), themes),
                                  ("movement", w.get("movements"), movements)):
            for name in names or []:
                if name not in pool:
                    problems.append("work %r: %s %r is not in the installment %s taxonomy" % (t, kind, name, num))
        ver = w.get("verification_status")
        if ver not in VERIFICATION_STATUS:
            problems.append("work %r: verification_status must be one of %s" % (t, sorted(VERIFICATION_STATUS)))
        elif ver != "unverified" and not w.get("sources"):
            problems.append("work %r: marked %s but cites no source" % (t, ver))
        for s in w.get("sources") or []:
            if s not in sources:
                problems.append("work %r: unknown source %r" % (t, s))
        values = {}
        for field in TEXT_FIELDS:
            text = (w.get(field) or "").strip()
            if not text:
                continue
            low = text.lower()
            for phrase in _banned_hits(low):
                problems.append("work %r: boilerplate phrase %r in %s" % (t, phrase, FIELD_LABELS[field]))
            inner = [x.strip() for x in re.split(r"(?<=[.!?])\s+", text) if len(x.strip()) >= 20]
            for x in sorted({x for x in inner if inner.count(x) > 1}):
                problems.append("work %r: sentence repeated within %s: %r" % (t, FIELD_LABELS[field], x[:80]))
            if text in values:
                problems.append("work %r: %s repeats %s word for word" % (t, FIELD_LABELS[field], values[text]))
            values[text] = FIELD_LABELS[field]
            if len(text) >= 80:
                if text in seen_text and seen_text[text] != t:
                    problems.append("work %r: %s duplicates a field of %r" % (t, FIELD_LABELS[field], seen_text[text]))
                seen_text.setdefault(text, t)
            for s in _sentences(text):
                sentence_owner[s].add(t)
    for s, owners in sorted(sentence_owner.items()):
        if len(owners) > 1:
            problems.append("sentence repeated across works %s: %r" % (sorted(owners), s[:90]))
    return problems
