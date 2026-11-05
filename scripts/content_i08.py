"""Installment 8 — Victorian and nineteenth-century American literature (1832-1901).

Research content module consumed by ``scripts/build_installment.py 08``.
The Victorian nucleus (Dickens to Hardy) is carried here; the system of
lesser-known, regional, genre and neglected writers of the same period is
carried in the companion files:

    content_i08.py            the Victorian core (novelists, poets, sages)
    content_i08_2.py          genre, regional, women, working-class, colonial
    content_i08_works_1.py    bibliographies of the authors above
    content_i08_works_2.py    bibliographies of the lesser-known authors
    content_i08_3.py          the American 1832-1901 strand
    content_i08_works_3.py    its bibliographies

Every field is researched; where a date or attribution is uncertain the record
says so in ``unc`` (authors) or ``attrib``/``biblio``/``status`` (works) rather
than inventing a value.
"""

META = {
    "period": "Victorian Period (1832–1901)",
    "period_movements": [
        "Victorian High Seriousness and the Public Poet",
        "Tractarian Prose and the Oxford Movement",
        "Carlyle and the Hero-Worship Lecture",
        "Chartism and the Condition-of-England Novel",
        "Sensation Fiction and the Serial Plot",
        "Pre-Raphaelitism and the Truth to Nature",
        "Ruskin and the Political Economy of Art",
        "Arnold and the Criticism of Culture",
        "Muscular Christianity and the Schoolboy Tale of Empire",
        "The Dramatic Monologue and the Masked Voice",
        "Aestheticism and the Decadent Decade",
        "The New Woman and the Fin-de-Siècle Problem Novel",
        "Transcendentalism and the Concord Lyceum",
        "Dark Romance and the Puritan Inheritance",
        "The Second American Renaissance and the Whitman-Dickinson Lyric",
        "Mark Twain and the Vernacular Performance",
        "American Realism and the Howells Program",
        "Local Colour and the Regionalist School",
        "American Naturalism and the Determinist Tragedy",
        "South-Western Humour and the Tall-Tale Sketch",
        "The Aesthetic Turn in 1890s America",
    ],
    # Sources that legitimately stand behind every record of the period.
    "sources_universal": [
        "The Oxford Dictionary of National Biography, 60 vols",
        "The Norton Anthology of English Literature, Vol. E: The Victorian Age (1830–1901), 11th edn",
    ],
    # (Victorian scholarship is framed by the Cambridge Companion to the
    # Victorian Novel and the journal Victorian Studies, both in the source list.)
    # Strand-specific reference works, attached by the author's own tradition.
    "sources_strand": {
        "american": [
            "The Columbia Literary History of the United States",
            "American Literature: A Journal of Literary History, Criticism, and Bibliography",
        ],
        "british": [
            "The Cambridge Companion to the Victorian Novel",
            "Victorian Studies: A Journal of the Humanities, Arts, and Sciences",
        ],
    },
    "authors_per_file": 8,
    "works_per_file": 25,
}
