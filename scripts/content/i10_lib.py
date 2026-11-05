"""Record constructors for installment 10 (1946-2000; audits report 1951-2000 as the core).

Installment 10 is built in strict mode (``META["strict"]``): nothing is composed
from templates, every analytical field is written for the record it describes,
and ``scripts/strict_checks.py`` enforces the depth each tier requires.

Field mapping to the database (works):

    overview     -> description            what the work is: genre, form, context, subject
    content      -> summary                what the work actually contains
    summary      -> plot_or_argument       plot (fiction, drama), progression and argument
                                           (poetry), central argument (criticism, nonfiction)
    themes_text  -> thematic_analysis      principal themes, explained
    structure    -> narrative_structure    structure and narrative method
    style        -> meter_and_prosody      style, language, prosody, technique
    ctx          -> historical_context
    sig          -> literary_significance
    crit         -> critical_context       interpretations, controversies, reception
    notes        -> research_notes         unresolved bibliographical questions

Authors carry ``bibliography_status`` (complete | substantially complete |
incomplete) with an authored coverage statement, and every record carries a
``verification_status`` (verified | partially verified | unverified) and the
sources actually consulted for it. A work by an author recorded in an earlier
installment names that author exactly; no second author record is created.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))

MAJ = "Major / canonical"
SEC = "Significant / secondary"
MIN = "Minor / lesser-known"
OBS = "Obscure / historically neglected"
TIERS = {MAJ, SEC, MIN, OBS}
CANON = {"Major canon", "Secondary canon", "Minor canon"}
DEPTHS = {"major", "significant", "minor"}
VERIFICATION = {"verified", "partially verified", "unverified"}
BIBLIOGRAPHY = {"complete", "substantially complete", "incomplete"}


def _names(kind):
    path = os.path.join(ROOT, "data", kind, "installment_10_%s.json" % kind)
    return {row["name"] for row in json.load(open(path, encoding="utf-8"))} if os.path.exists(path) else set()


GENRES, THEMES, MOVEMENTS = _names("genres"), _names("themes"), _names("movements")


def _exact(kind, pool, names):
    out = []
    for n in names:
        if n not in pool:
            raise KeyError("installment 10 %s %r is not defined in data/%s/installment_10_%s.json"
                           % (kind, n, kind + "s", kind + "s"))
        out.append(n)
    return out


def G(*names):
    return _exact("genre", GENRES, names)


def T(*names):
    return _exact("theme", THEMES, names)


def M(*names):
    return _exact("movement", MOVEMENTS, names)


def A10(name, tier, b, d, bp, nat, ident, bio, prof, style, conc, sig, *, bib_status, bib_note, ver,
        sources=(), infl=(), alt=(), pseudo=(), b_approx=False, d_approx=False, unc=None,
        status="complete"):
    """An installment-10 author. ``bib_note`` states what the bibliography covers and how it was checked."""
    assert tier in TIERS, (name, tier)
    assert bib_status in BIBLIOGRAPHY, (name, bib_status)
    assert ver in VERIFICATION, (name, ver)
    return {
        "name": name, "tier": tier, "b": b, "d": d, "bp": bp, "nat": nat, "ident": ident,
        "bio": bio, "prof": prof, "style": style, "conc": conc, "sig": sig,
        "infl": list(infl), "alt": list(alt), "pseudo": list(pseudo),
        "b_approx": b_approx, "d_approx": d_approx, "unc": unc, "status": status,
        "biblio_note": bib_note, "bibliography_status": bib_status,
        "verification_status": ver, "sources": list(sources),
    }


def W10(title, author, pub, form, depth, *, genres, themes, overview, summary, themes_text,
        structure, style, ctx, sig, ver, sources=(), movements=(), content=None, crit=None,
        chars=None, comp=None, perf=None, ms=None, lang="English", alt=(), canon="Secondary canon",
        notes=None, biblio=None, coauthors=(), as_status="single", status="complete",
        contribution_type="author", coauthor_type="author"):
    """An installment-10 work; see the module docstring for the field mapping."""
    assert depth in DEPTHS, (title, depth)
    assert canon in CANON, (title, canon)
    assert ver in VERIFICATION, (title, ver)
    extra = {"thematic_analysis": themes_text, "verification_status": ver}
    if content:
        extra["summary"] = content
    if crit:
        extra["critical_context"] = crit
    if notes:
        extra["research_notes"] = notes
    return {
        "title": title, "author": author, "pub": pub, "form": form, "depth": depth,
        "desc": overview, "content": content, "plot": summary, "themes_text": themes_text,
        "struct": structure, "meter": style, "ctx": ctx, "sigtext": sig, "crit": crit,
        "genres": list(genres), "themes": list(themes), "movements": list(movements),
        "alt": list(alt), "composition": comp, "comp": comp, "perf": perf, "ms": ms, "lang": lang,
        "chars": chars, "canon": canon, "status": status, "coauthors": list(coauthors),
        "as_status": as_status, "contribution_type": contribution_type, "coauthor_type": coauthor_type,
        "sources": list(sources), "verification_status": ver, "notes": notes, "biblio": biblio,
        "extra": extra,
    }
