"""Installment-10 extensions of authors defined by earlier installments.

An author keeps the single record written by the installment that first
recorded them (the importer upserts authors by name, so a second definition
would silently overwrite the first; ``build_installment.py`` and
``check_installment.py`` now block that). When installment 10 adds works from
1946-2000 for such an author, its research on the author is recorded here:

* ``bib_note``    the authored statement of bibliographic coverage, now for the
                  whole career, naming the work records each installment holds
                  and what is still unrecorded;
* ``bib_status``  complete | substantially complete | incomplete;
* ``ver``         verified | partially verified | unverified;
* ``sources``     the sources actually consulted (installment_10_sources.json).

``build_installment.py`` merges each extension into the defining installment's
author record when that installment is built (so its JSON never goes stale),
and the installment-10 build refuses to run until every extension is merged,
names an author with installment-10 works, and cites only known sources.

Workflow after editing this file: build the defining installment (08 or 09),
then 10, then import.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from i10_lib import X10  # noqa: E402

ORWELL_SOURCES = [
    "George Orwell bibliography (Wikipedia)",
    "George Orwell Bibliography: Most referenced collections (orwell.ru)",
    "George Orwell published: list of works (orwell.ru)",
    "Shooting an elephant, and other essays (WorldCat record, OCLC 2552523)",
    "Darcy Moore, Orwell Collection (collector's list of first editions)",
    "The Freedom of the Press (The Orwell Foundation)",
]

EXTENSIONS = [
X10("George Orwell",
    bib_status="substantially complete", ver="partially verified", sources=ORWELL_SOURCES,
    bib_note=(
        "Whole-career bibliography, stated across installments 9 and 10. Books published in Orwell's "
        "lifetime: Down and Out in Paris and London (1933), Burmese Days (1934), A Clergyman's Daughter "
        "(1935), Keep the Aspidistra Flying (1936), The Road to Wigan Pier (1937), Homage to Catalonia "
        "(1938), Coming Up for Air (1939), Inside the Whale and Other Essays (1940), The Lion and the "
        "Unicorn (1941), Animal Farm (1945), Critical Essays (1946; New York, as Dickens, Dali and Others, "
        "April 1946), the pamphlets James Burnham and the Managerial Revolution (1946) and The English "
        "People (1947), and Nineteen Eighty-Four (1949). He edited Talking to India (1943) and, with "
        "Reginald Reynolds, British Pamphleteers, vol. 1 (1948). Posthumous: Shooting an Elephant and "
        "Other Essays (1950); Such, Such Were the Joys (New York, February 1953) and its British "
        "counterpart England Your England and Other Essays (November 1953), whose contents differ; "
        "Collected Essays (1961); The Collected Essays, Journalism and Letters, edited by Sonia Orwell and "
        "Ian Angus (four volumes, 1968); 'The Freedom of the Press', the unused preface to Animal Farm "
        "(Times Literary Supplement, 1972); and The Complete Works, edited by Peter Davison (twenty "
        "volumes, 1986-1998), the standard edition. Work records: installment 9 holds Down and Out in "
        "Paris and London, Burmese Days, A Clergyman's Daughter, Keep the Aspidistra Flying, The Road to "
        "Wigan Pier, Homage to Catalonia, Coming Up for Air, Inside the Whale and Other Essays, The Lion "
        "and the Unicorn and Animal Farm; installment 10 holds Critical Essays, James Burnham and the Managerial Revolution, The "
        "English People, Nineteen Eighty-Four, Shooting an Elephant and Other Essays, Such, Such Were the "
        "Joys, The Collected Essays, Journalism and Letters and 'The Freedom of the Press', and the essay "
        "'Politics and the English Language' (Horizon, 1946), a Norton selection. Every book he "
        "wrote that was published in his lifetime therefore has a record; the two volumes he edited do "
        "not. Not recorded individually: some 550 "
        "articles, reviews and columns (among them the Tribune 'As I Please' column and the fifteen "
        "'London Letters' for Partisan Review, 1941-46), the BBC scripts and the surviving poems, whose "
        "substance is represented through the collections. England Your England, Collected Essays and "
        "the Complete Works are listed but not separately recorded: the first overlaps Such, Such Were "
        "the Joys, the other two are compilations and a critical edition. Dates and publishers were "
        "checked against the Wikipedia and orwell.ru bibliographies and WorldCat; the Wikipedia list's "
        "1958 date for the American Dickens, Dali and Others is an error for 1946.")),
X10("Jean Rhys",
    bib_status="incomplete", ver="partially verified",
    sources=["'The Day They Burned the Books' (chapter 6 of a Cambridge University Press study of Jean Rhys, Cambridge Core)",
             "Sleep It Off Lady (Wikipedia)", "Sleep It Off Lady: Stories (Trove, National Library of Australia)"],
    bib_note=("Whole-career bibliography, stated across installments 9 and 10. Books: The Left Bank and Other Stories "
        "(1927), Quartet (1928), After Leaving Mr Mackenzie (1931), Voyage in the Dark (1934), Good Morning, Midnight "
        "(1939), Wide Sargasso Sea (1966), Tigers Are Better-Looking (1968, stories), Sleep It Off Lady (1976, stories), "
        "Smile Please (1979, unfinished autobiography, posthumous) and Letters 1931-1966 (1984, posthumous). Installment 9 "
        "holds work records for Quartet, Voyage in the Dark and Good Morning, Midnight. Installment 10, which since "
        "2026-11-06 records only the selections of the Norton anthologies, holds the stories 'The Day They Burned the "
        "Books' (1960, collected in Tigers Are Better-Looking) and 'On Not Shooting Sitting Birds' (collected in Sleep It "
        "Off Lady, 1976). Wide Sargasso Sea and the other books of 1946-1984 have no work records, so the bibliography "
        "is incomplete.")),
X10("Samuel Beckett",
    bib_status="incomplete", ver="partially verified",
    sources=["Waiting for Godot (Wikipedia)"],
    bib_note=("Whole-career bibliography, stated across installments 9 and 10, and incomplete. Installment 9 holds work "
        "records for the essay 'Dante...Bruno. Vico..Joyce' (1929), More Pricks Than Kicks (1934), Echo's Bones and Other "
        "Precipitates (1935) and Murphy (1938), and lists Molloy (1951, in French), Watt (1953), The Unnamable (1953) and "
        "Endgame (1957). Installment 10, which since 2026-11-06 records only the selections of the Norton anthologies, "
        "holds Waiting for Godot, recorded as Beckett's English version (1954) of En attendant Godot (written 1948-1949, "
        "published 1952, first performed 1953). His other prose, plays, poems and translations, in French and English, "
        "of 1946-1989 are neither listed in full nor recorded.")),
X10("W. H. Auden",
    bib_status="incomplete", ver="partially verified",
    sources=["In Praise of Limestone (Wikipedia)", "The Shield of Achilles (Wikipedia)"],
    bib_note=("Whole-career bibliography, stated across installments 9 and 10. Installment 9 holds work records for "
        "Poems (1930), The Orators (1932), Look, Stranger! (1936), Spain (1937) and Another Time (1940), and lists Poems "
        "(1928, privately printed), the plays written with Christopher Isherwood (The Dog Beneath the Skin, 1935; The "
        "Ascent of F6, 1936; On the Frontier, 1938) and The Dance of Death (1933), Letters from Iceland (1937, with Louis "
        "MacNeice), Journey to a War (1939, with Isherwood), The Double Man (1941; UK title New Year Letter), For the Time "
        "Being and The Sea and the Mirror (1944), The Age of Anxiety (1947), The Shield of Achilles (1955), Homage to Clio "
        "(1960), About the House (1965), City Without Walls (1969), Epistle to a Godson (1972), Thank You, Fog (1974, "
        "posthumous) and Collected Poems (1976, posthumous); Nones (1951) and Collected Shorter Poems, 1922-1957 (1966) "
        "are added here. Installment 10, which since 2026-11-06 records only the selections of the Norton anthologies, "
        "holds 'In Praise of Limestone' (1948, collected in Nones) and 'The Shield of Achilles' (1952, title poem of the "
        "1955 collection). The books of 1941-1976 have no work records, and the prose (The Enchafed Flood, The Dyer's "
        "Hand and others) and libretti are not listed, so the bibliography is incomplete.")),
X10("Gwendolyn Brooks",
    bib_status="incomplete", ver="partially verified",
    sources=["Annie Allen (Wikipedia)", "We Real Cool (Wikipedia)",
             "In the Mecca: Poems (University of Pennsylvania Libraries, Franklin catalogue)",
             "To The Diaspora (work) (Black Bibliography Project, Rutgers University)"],
    bib_note=("Whole-career bibliography, stated across installments 9 and 10. Books: A Street in Bronzeville (1945), "
        "Annie Allen (1949; Pulitzer Prize 1950), Maud Martha (1953, novel), Bronzeville Boys and Girls (1956, for "
        "children), The Bean Eaters (1960), Selected Poems (1963), In the Mecca (1968), Riot (1969), Family Pictures "
        "(1970), Report from Part One (1972, autobiography), Beckonings (1975), To Disembark (1981), The Near-Johannesburg "
        "Boy (1986) and Children Coming Home (1991). Installment 9 holds the record for A Street in Bronzeville. "
        "Installment 10, which since 2026-11-06 records only the selections of the Norton anthologies, holds seven "
        "poems: 'The Children of the Poor' (Annie Allen, 1949); 'We Real Cool', 'The Bean Eaters', 'A Bronzeville Mother "
        "Loiters in Mississippi. Meanwhile, a Mississippi Mother Burns Bacon' and 'The Last Quatrain of the Ballad of "
        "Emmett Till' (The Bean Eaters, 1960); 'The Blackstone Rangers' (In the Mecca, 1968); and 'To the Diaspora' (To "
        "Disembark, 1981). The books of 1949-1991 have no work records of their own, so the bibliography is "
        "incomplete.")),
]
