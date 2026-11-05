"""Installment 9 — Edwardian, Georgian and Modernist literature (1901-1945).

Research content module consumed by ``scripts/build_installment.py 09``.
The period is carried in part modules so that no single file becomes
unmanageable; this module holds the META record, the period definition and
the period-wide source apparatus, and the authors and works are in
``content_i09_a*`` and ``content_i09_w*``:

    content_i09.py            META (period, movements, sources)
    content_i09_aNN.py        authors, 6-8 per part
    content_i09_wNN.py        bibliographies, 15-20 works per part

Every field is researched; where a date or attribution is uncertain the record
says so in ``unc`` (authors) or ``attrib``/``biblio``/``status`` (works) rather
than inventing a value.
"""

META = {
    "period": "Edwardian, Georgian and Modernist Period (1901–1945)",
    "period_movements": [
        "The Edwardian Country House and the Condition of England",
        "Georgian Poetry and the English Lyric",
        "The Irish Literary Revival and the Abbey Theatre",
        "Imagism and the Free-Verse Revolution",
        "Vorticism and the Modernist Little Magazine",
        "The Bloomsbury Group and the Novel of Consciousness",
        "The Waste Land Generation and the Mythical Method",
        "Trench Poetry and the Literature of the First World War",
        "Suffrage Drama and the Woman's Theatre",
        "The Auden Generation and the Thirties Poem",
        "The Hungry Thirties and the Documentary Novel",
        "The Harlem Renaissance and the New Negro",
        "The Lost Generation and the Expatriate Novel",
        "The Southern Renaissance and the American Regional Novel",
        "American Modernism and the Objectivist Lyric",
        "The Golden Age of Detective Fiction",
        "The Ghost Story and the Modern Weird Tale",
        "The Celtic Twilight and the Irish Short Story",
        "The Drawing-Room Stage and the Comedy of Manners",
        "The Scientific Romance and the English Utopia",
        "The Scottish Renaissance and the Vernacular Revival",
    ],
    # Sources that legitimately stand behind every record of the period.
    "sources_universal": [
        "The Oxford Dictionary of National Biography, 60 vols",
        "The Norton Anthology of English Literature, Vol. F: The Twentieth and Twenty-First Centuries, 11th edn",
        "The Oxford Companion to English Literature, 7th edn",
        "The Cambridge History of Twentieth-Century English Literature",
        "Modernism: A Guide to European Literature 1890–1930",
    ],
    # Strand-specific reference works, attached by the author's own tradition.
    "sources_strand": {
        "american": [
            "The Norton Anthology of American Literature, Vol. D: 1914–1945, 10th edn",
            "The Columbia Literary History of the United States",
        ],
        "british": [
            "The Cambridge Companion to Modernism, 2nd edn",
            "The Cambridge Companion to the Modernist Novel",
            "The Oxford Companion to Twentieth-Century Literature in English",
        ],
        "irish": [
            "The Oxford Companion to Irish Literature",
            "The Cambridge Companion to the Irish Novel",
        ],
        "scottish": [
            "The Cambridge Companion to Scottish Literature",
            "The Oxford Companion to Twentieth-Century Literature in English",
        ],
    },
    "authors_per_file": 8,
    "works_per_file": 20,
}
