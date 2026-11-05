"""Shared helpers for authoring content modules (writer-side only, not shipped)."""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def load_json(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as fh:
        return json.load(fh)

GENRES = [g["name"] for g in load_json("data/genres/installment_08_genres.json")]
THEMES = [t["name"] for t in load_json("data/themes/installment_08_themes.json")]
MOVEMENTS = [m["name"] for m in load_json("data/movements/installment_08_movements.json")]

def _all_genres():
    import glob
    out = []
    for path in sorted(glob.glob(os.path.join(ROOT, "data", "genres", "installment_*_genres.json"))):
        with open(path, encoding="utf-8") as fh:
            out += [x["name"] for x in json.load(fh)]
    return out

ALL_GENRES = _all_genres()

def g(*bits):
    """Resolve genre names from disambiguating substrings of this installment's
    genres; a bit matching none of them may name another installment's genre
    in full (e.g. "Fable and Apologue")."""
    out = []
    for b in bits:
        hits = [x for x in GENRES if b.lower() in x.lower()]
        if not hits:
            hits = [x for x in ALL_GENRES if b.lower() == x.lower()]
        if len(hits) != 1:
            raise SystemExit("genre %r -> %r" % (b, hits))
        out.append(hits[0])
    return out

def t(*bits):
    out = []
    for b in bits:
        hits = [x for x in THEMES if b.lower() in x.lower()]
        if len(hits) != 1:
            raise SystemExit("theme %r -> %r" % (b, hits))
        out.append(hits[0])
    return out

def m(*bits):
    out = []
    for b in bits:
        hits = [x for x in MOVEMENTS if b.lower() in x.lower()]
        if len(hits) != 1:
            raise SystemExit("movement %r -> %r" % (b, hits))
        out.append(hits[0])
    return out

def A(name, tier, b, d, bp, nat, ident, bio, prof, style, conc, sig, infl=(),
      alt=(), pseudo=(), b_approx=False, d_approx=False, unc=None, status="complete",
      also=()):
    return {
        "name": name, "tier": tier, "b": b, "d": d, "bp": bp, "nat": nat,
        "ident": ident, "bio": bio, "prof": prof, "style": style, "conc": conc,
        "sig": sig, "infl": list(infl), "alt": list(alt), "pseudo": list(pseudo),
        "b_approx": b_approx, "d_approx": d_approx, "unc": unc, "status": status,
        "also": list(also),
    }

def W(title, author, pub, form, desc, plot, ctx, sigtext, genres, themes, movements,
      alt=(), comp=None, perf=None, ms=None, lang="English", chars=None,
      struct=None, meter=None, attrib=None, biblio=None, canon="Secondary canon",
      status="complete", coauthors=(), coauthor_type="author",
      contribution_type="author", extra=None, as_status="single", sources=()):
    return {
        "title": title, "author": author, "pub": pub, "form": form, "desc": desc,
        "plot": plot, "ctx": ctx, "sigtext": sigtext, "genres": genres,
        "themes": themes, "movements": movements, "alt": list(alt), "comp": comp,
        "composition": comp, "perf": perf, "ms": ms, "lang": lang, "chars": chars,
        "struct": struct, "meter": meter, "attrib": attrib, "biblio": biblio,
        "canon": canon, "status": status, "coauthors": list(coauthors),
        "coauthor_type": coauthor_type, "contribution_type": contribution_type,
        "extra": extra, "as_status": as_status, "sources": list(sources),
    }

def write_module(path, header, authors, works, meta_source, imports="from content_i08 import META"):
    """Serialise to a content module (AUTHORS / WORKS / META)."""
    parts = [header.strip(), "", "import sys, os", "sys.path.insert(0, os.path.dirname(__file__))",
             "from _lib import A, W, g, t, m  # noqa: E402", imports, "",
             "AUTHORS = ["]
    for a in authors:
        parts.append("    A(" + ", ".join([
            repr(a["name"]), repr(a["tier"]), repr(a["b"]), repr(a["d"]), repr(a["bp"]),
            repr(a["nat"]), repr(a["ident"]), repr(a["bio"]), repr(a["prof"]),
            repr(a["style"]), repr(a["conc"]), repr(a["sig"]),
        ] + (["infl=%r" % (a["infl"],)] if a["infl"] else [])
          + (["alt=%r" % (a["alt"],)] if a["alt"] else [])
          + (["pseudo=%r" % (a["pseudo"],)] if a["pseudo"] else [])
          + (["b_approx=True"] if a["b_approx"] else [])
          + (["d_approx=True"] if a["d_approx"] else [])
          + (["unc=%r" % a["unc"]] if a["unc"] else [])
          + (["status=%r" % a["status"]] if a["status"] != "complete" else [])
          ) + "),")
    parts.append("]")
    parts.append("")
    parts.append("WORKS = [")
    for w in works:
        args = [repr(w["title"]), repr(w["author"]), repr(w["pub"]), repr(w["form"]),
                repr(w["desc"]), repr(w["plot"]), repr(w["ctx"]), repr(w["sigtext"]),
                "g(%s)" % ", ".join(repr(x) for x in w["genres"]),
                "t(%s)" % ", ".join(repr(x) for x in w["themes"]),
                "m(%s)" % ", ".join(repr(x) for x in w["movements"])]
        if w["alt"]: args.append("alt=%r" % (w["alt"],))
        if w["composition"]: args.append("comp=%r" % (w["composition"],))
        if w["perf"]: args.append("perf=%r" % w["perf"])
        if w["ms"]: args.append("ms=%r" % w["ms"])
        if w["lang"] != "English": args.append("lang=%r" % w["lang"])
        if w["chars"]: args.append("chars=%r" % w["chars"])
        if w["struct"]: args.append("struct=%r" % w["struct"])
        if w["meter"]: args.append("meter=%r" % w["meter"])
        if w["attrib"]: args.append("attrib=%r" % w["attrib"])
        if w["biblio"]: args.append("biblio=%r" % w["biblio"])
        if w["canon"] != "Secondary canon": args.append("canon=%r" % w["canon"])
        if w["status"] != "complete": args.append("status=%r" % w["status"])
        if w["coauthors"]:
            args.append("coauthors=%r" % (w["coauthors"],))
            args.append("coauthor_type=%r" % w["coauthor_type"])
        if w["contribution_type"] != "author": args.append("contribution_type=%r" % w["contribution_type"])
        if w["extra"]: args.append("extra=%r" % (w["extra"],))
        if w["as_status"] != "single": args.append("as_status=%r" % w["as_status"])
        if w["sources"]: args.append("sources=%r" % (w["sources"],))
        parts.append("    W(" + ", ".join(args) + "),")
    parts.append("]")
    parts.append("")
    parts.append("META = " + meta_source)
    parts.append("")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(parts))
    print("wrote %s: %d authors, %d works" % (path, len(authors), len(works)))


def wk(title=None, year=None, gb="", tb="", mb="", form=None, desc=None, plot=None,
       ctx=None, sig=None, context=None, **kw):
    """Compact work constructor: genres/themes/movements given as 'a, b' strings.

    ``context`` is accepted as an alias of ``ctx`` (the field is stored as
    historical_context), and ``sig`` as an alias of ``sigtext``.
    """
    ctx = ctx or context
    genres = g(*[x.strip() for x in gb.split(",") if x.strip()]) if gb else []
    themes = t(*[x.strip() for x in tb.split(",") if x.strip()]) if tb else []
    movements = m(*[x.strip() for x in mb.split(",") if x.strip()]) if mb else []
    return W(title, kw.pop("author"), year, form, desc, plot, ctx, sig,
             genres, themes, movements, **kw)


def wks(author, rows):
    """Build a list of works for one author from wk() rows."""
    return [wk(author=author, **row) for row in rows]
