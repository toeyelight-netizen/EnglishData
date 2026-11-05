"""Installment 10 — Postwar and Contemporary literature in English (1946-2000).

Research content module consumed by ``scripts/build_installment.py 10``.
Scope (decided 2026-11-06): 1 January 1946 to 31 December 2000, with the audits
reporting 1951-2000 as the core and 1946-1950 separately. British (English,
Scottish, Welsh), Irish and Northern Irish, and American literature, plus the
English-language literatures of Canada, Australia, New Zealand, the Caribbean,
Africa and South Asia and their diasporas.

Strict build: ``META["strict"]`` disables template enrichment; every field is
written for its record and ``scripts/strict_checks.py`` enforces depth tiers,
rejects boilerplate and repeated prose, and requires the sources actually
consulted for any record marked verified. No source is attached universally.

    content_i10.py            META (period, movements, strict flags)
    content/i10_lib.py        record constructors (A10, W10) and taxonomy resolvers
    content/content_i10_*.py  waves of authors and works

Research apparatus: ``research/installment_10/`` (discovery inventory and
methodology) and ``scripts/audit_installment_10.py`` (the eight audits, the
coverage matrix and the audit report).
"""

META = {
    "installment": 10,
    "period": "Postwar and Contemporary Period (1946–2000)",
    "strict": True,
    "window": (1946, 2000),
    "core_window": (1951, 2000),
    "period_movements": [
        'Late Modernism',
        'Existentialism in Anglophone Writing',
        'The Angry Young Men',
        'Working-Class and Regional Social Realism',
        'Black Humour and the Absurdist Novel',
        'Postmodernism and Postmodern Fiction',
        'Metafiction',
        'Experimental Fiction and the Anti-Novel',
        'Southern Gothic',
        'Magical Realism in English',
        'Minimalism and Dirty Realism',
        'Contemporary Gothic',
        'New Journalism',
        'Second-Wave Feminist Writing',
        'Jewish American Fiction',
        'Postwar African American Writing: Protest and Its Critics',
        'Black Arts Movement',
        'Native American Renaissance',
        'Chicano Movement Literature',
        'Asian American Literary Movement',
        'Black British Writing and the Windrush Generation',
        'Caribbean Literature in English',
        'African Literature in English',
        'South African Writing under Apartheid',
        'South Asian Literature in English',
        'Postcolonial Literature',
        'Indigenous Writing in Australia, Canada and New Zealand',
        'Canadian Literary Nationalism',
        'Welsh Writing in English: The Second Flowering',
        'The Scottish Literary Revival of the 1980s and 1990s',
        'Northern Irish Poetry and the Belfast Group',
        'Gay and Lesbian Literature after Stonewall',
        'The Movement',
        'The Group',
        'The British Poetry Revival',
        'The Liverpool Poets and the British Underground',
        'Confessional Poetry',
        'The Beat Generation',
        'The San Francisco Renaissance',
        'The New York School',
        'Black Mountain Poetry',
        'Deep Image Poetry',
        'Concrete Poetry',
        'Language Poetry',
        'Performance and Spoken-Word Poetry',
        'Dub Poetry',
        'New Formalism',
        'The Martian Poets',
        'Theatre of the Absurd',
        'Kitchen-Sink Drama and the Royal Court',
        'Political Theatre and the Fringe',
        'Off-Off-Broadway and the American Theatre Avant-Garde',
        'New Wave Science Fiction',
        'Feminist Science Fiction',
        'Cyberpunk',
        'The New Criticism (Late Phase)',
        'The Chicago Critics',
        'Myth and Archetypal Criticism',
        'Leavisite Criticism and the Scrutiny Tradition',
        'Cultural Materialism and Marxist Criticism',
        'Structuralism and Narratology',
        'Poststructuralism and Deconstruction',
        'Reader-Response and Reception Theory',
        'Feminist Literary Criticism',
        'Psychoanalytic and Lacanian Criticism',
        'New Historicism',
        'Postcolonial Theory',
        'Queer Theory',
        'African American Literary Theory and the Black Aesthetic',
    ],
    "sources_universal": [],
    "sources_strand": {},
    "authors_per_file": 8,
    "works_per_file": 20,
}
