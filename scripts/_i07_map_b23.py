# -*- coding: utf-8 -*-
"""Installment-07 relationship map, batch 23.

Two early American novelists added to the installment (Hannah Webster Foster and
William Hill Brown) and the works called for by the completeness sweep for authors
already present (Maria Edgeworth, Washington Irving) or recorded as unsigned
serials (Blackwood's Edinburgh Magazine, The Quarterly Review, The Liberal).

Mechanical taxonomy assignment: title -> ([authors], [genres], [themes], [movements]).
Author strings are the exact ``authors.full_name`` values; genre/theme/movement
strings are copied verbatim from scripts/_i07_taxonomy_names.txt (the installment-07
vocabulary where it fits, otherwise the established database vocabulary recorded in
that file). A work whose authorship_status is ``anonymous`` is given an empty author
list, because the validator rejects anonymous works carrying author rows.
"""

# --- permitted authors (b23) ---
EDGEWORTH = ["Maria Edgeworth"]
IRVING = ["Washington Irving"]
FOSTER = ["Hannah Webster Foster"]
BROWN_WH = ["William Hill Brown"]

MAP_B23 = {
    # --- Maria Edgeworth ---
    "Belinda": (
        EDGEWORTH,
        ["Novel of Manners and Fashion", "Sentimental and Domestic Novel"],
        ["The marriage market and the limited estate",
         "Politeness, fashion, and the codes of conduct",
         "Women's experience and the feminine voice",
         "Slavery, empire, and the Atlantic world"],
        ["Austen and the Novel of Manners"]),
}
