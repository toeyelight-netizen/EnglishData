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
        "Joys, The Collected Essays, Journalism and Letters and 'The Freedom of the Press'. Every book he "
        "wrote that was published in his lifetime therefore has a record; the two volumes he edited do "
        "not. Not recorded individually: some 550 "
        "articles, reviews and columns (among them the Tribune 'As I Please' column and the fifteen "
        "'London Letters' for Partisan Review, 1941-46), the BBC scripts and the surviving poems, whose "
        "substance is represented through the collections. England Your England, Collected Essays and "
        "the Complete Works are listed but not separately recorded: the first overlaps Such, Such Were "
        "the Joys, the other two are compilations and a critical edition. Dates and publishers were "
        "checked against the Wikipedia and orwell.ru bibliographies and WorldCat; the Wikipedia list's "
        "1958 date for the American Dickens, Dali and Others is an error for 1946.")),
]
