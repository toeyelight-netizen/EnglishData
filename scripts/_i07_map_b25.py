"""Installment 07 (British and American Romantic, c. 1789-1832), batch b25.

MAP_B25 maps each exact work title authored in
``data/works/installment_07_works_batch25.json`` to the tuple
``([authors], [genres], [themes], [movements])`` used by the loader.
The titles are Ann Radcliffe's prose romances, her travel letters and the
posthumous 1826 volume; every taxonomy name is copied verbatim from the
installment 07 taxonomy plus the database vocabulary.
"""

MAP_B25 = {
    'A Journey Made in the Summer of 1794, through Holland and along the Eastern Frontier of France; in a Series of Letters. With Observations on the Sublime and Beautiful, as They Appear in the Works of Nature, and the Arts': (
        ['Ann Radcliffe'],
        ['Travel and Wonders Literature', 'Letters'],
        ['The sublime, terror, and the ruin', 'Nature, landscape, and the shaping mind', 'Exile, travel, and the southern sojourn', 'National identity and Englishness', 'Revolutionary hope and its disappointment'],
        ['Gothic and the Literature of Terror', 'Sentimentalism and the Culture of Feeling'],
    ),
    "Gaston de Blondeville; or, The Court of Henry the Third, Keeping Festival in Ardenne. A Romance; St. Alban's Abbey, a Metrical Tale; with Some Poetical Pieces": (
        ['Ann Radcliffe'],
        ['Gothic Novel and Romance of Terror', 'Metrical Tale and Romance in Verse', 'Memoir and Autobiographical Prose'],
        ['Chivalry and knighthood', 'Border, ballad, and national memory', 'Revenge and justice', 'The literature of the nations: Scotland, Ireland, and Wales'],
        ['Gothic and the Literature of Terror', 'The Rise of the English Novel'],
    ),
    'The Italian, or, The Confessional of the Black Penitents. A Romance. In Three Volumes': (
        ['Ann Radcliffe'],
        ['Gothic Novel and Romance of Terror'],
        ['Gothic confinement and the pursued heroine', 'Penance, confession, and sin', 'Religious persecution and martyrdom', 'Revenge and justice', 'Love, constancy, and betrayal', 'Tyranny and the abuse of power'],
        ['Gothic and the Literature of Terror', 'The Rise of the English Novel'],
    ),
    'The Mysteries of Udolpho. A Romance; and Interspersed with Some Pieces of Poetry. In Four Volumes': (
        ['Ann Radcliffe'],
        ['Gothic Novel and Romance of Terror'],
        ['Gothic confinement and the pursued heroine', 'The sublime, terror, and the ruin', 'Tyranny and the abuse of power', 'Penance, confession, and sin', 'Women, chastity, and constancy', 'Death, mourning, and the graveyard meditation'],
        ['Gothic and the Literature of Terror', 'The Rise of the English Novel', 'Sentimentalism and the Culture of Feeling'],
    ),
    'The Romance of the Forest, Interspersed with Some Pieces of Poetry. In Three Volumes': (
        ['Ann Radcliffe'],
        ['Gothic Novel and Romance of Terror', 'Sentimental and Domestic Novel'],
        ['Gothic confinement and the pursued heroine', 'Tyranny and the abuse of power', 'The supernatural ballad and willed belief', 'Women, chastity, and constancy', 'Patronage and the literary marketplace'],
        ['Gothic and the Literature of Terror', 'The Rise of the English Novel', 'Sentimentalism and the Culture of Feeling'],
    ),
}
