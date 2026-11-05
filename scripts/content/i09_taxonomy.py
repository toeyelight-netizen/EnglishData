"""Taxonomy resolver for installment 9 content modules.

``_lib.g/t/m`` resolve against the installment-08 JSON only. Installment 9
adds 27 genres, 28 themes and 21 movements of its own, so its content modules
resolve against the union of every installment's taxonomy files instead, which
is what the importer will see once the new JSON is imported.

Each lookup takes a distinctive substring and requires exactly one match, so
an ambiguous abbreviation fails loudly at build time rather than silently
attaching the wrong taxonomy row.
"""

import glob
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _names(kind):
    out = []
    for path in sorted(glob.glob(os.path.join(ROOT, "data", kind, "*.json"))):
        with open(path, encoding="utf-8") as fh:
            for row in json.load(fh):
                if row["name"] not in out:
                    out.append(row["name"])
    return out


GENRES = _names("genres")
THEMES = _names("themes")
MOVEMENTS = _names("movements")


def _resolve(pool, bits, label):
    out = []
    for bit in bits:
        hits = [x for x in pool if bit.lower() in x.lower()]
        if len(hits) != 1:
            raise SystemExit("%s %r -> %r" % (label, bit, hits[:5]))
        if hits[0] not in out:
            out.append(hits[0])
    return out


def g(*bits):
    return _resolve(GENRES, bits, "genre")


def t(*bits):
    return _resolve(THEMES, bits, "theme")


def m(*bits):
    return _resolve(MOVEMENTS, bits, "movement")


def w(title, author, pub, form, desc, plot, ctx, sig, genres, themes, movements,
      alt=(), comp=None, perf=None, ms=None, chars=None, struct=None,
      canon="Secondary canon", biblio=None, attrib=None, status="complete",
      coauthors=()):
    """Build one work record, resolving the three taxonomy lists on the way."""
    from _lib import W

    return W(title, author, pub, form, desc, plot, ctx, sig,
             g(*genres), t(*themes), m(*movements),
             alt=alt, comp=comp, perf=perf, ms=ms, chars=chars, struct=struct,
             canon=canon, biblio=biblio, attrib=attrib, status=status,
             coauthors=coauthors)


# Convenience shorthands for substrings that are otherwise ambiguous across
# installments (checked to resolve to exactly one taxonomy row each).
G = {
    "condition": "Edwardian Social Panorama",
    "consciousness": "Novel of Consciousness",
    "experimental": "Experimental Novel",
    "longpoem": "Modernist Long Poem",
    "imagist": "Imagist Lyric",
    "georgian": "Georgian Anthology Lyric",
    "trench": "Trench Lyric",
    "warmemoir": "War Memoir and the Autobiographical",
    "peasant": "Peasant Play",
    "versedrama": "Verse Drama and the Poetic Play",
    "manners": "Comedy of Manners and the Drawing-Room Stage",
    "suffrage": "Suffrage Play",
    "romance": "Scientific Romance and the Utopian",
    "dystopia": "Dystopian Fiction",
    "detective": "Detective Novel and the Golden Age",
    "ghost": "Ghost Story and the Modern Weird Tale",
    "shortstory": "Modern Short Story and the Magazine",
    "newnegro": "New Negro Lyric",
    "regional": "Regional Novel and the American Local",
    "jazzage": "Jazz-Age Novel",
    "proletarian": "Proletarian Novel and the Working",
    "documentary": "Documentary Prose and the Reportage",
    "critical": "Critical Essay and the Modern Review",
    "biography": "Biography and the Modern Life",
    "childrens": "Children's Fantasy and the Golden-Age",
    "nature": "Nature Essay and the Rural",
    "autobiography": "Autobiography and the Modern Memoir",
    "growth": "Novel of Development and the Growth Story",
}
