## Method

**Scope.** 1 January 1946 to 31 December 2000 (decision of 2026-11-06). The core window is 1951–2000, and 1946–1950 is reported separately as the bridge from installment 9.
- **Traditions covered:** British (English, Scottish, Welsh), Irish and Northern Irish, and American literature. Also the English-language literatures of Canada, Australia, New Zealand, the Caribbean, Africa and South Asia, and their diasporas.
- **Inclusion test:** literary activity and publication in the period, not birth date or fame.
- **Theorists in translation:** non-English-language theorists named in Part VII (Barthes, Derrida, Foucault, Lacan and others) are admitted as theory in translation. Their records give the original language, and they are distinguished from critics writing in English.

**Records.**
- **Works.** Every literary work gets its own work record, with depth tiered by significance:
  - *major:* the full seven-part record, with a plot or argument of several paragraphs;
  - *significant:* every analytical field, shorter;
  - *minor:* shorter but specific.
- **Seven-part mapping:**
  - overview → `description`
  - content → `summary`
  - summary or argument → `plot_or_argument`
  - themes → `thematic_analysis`
  - literary characteristics → `narrative_structure` and `meter_and_prosody`
  - significance → `literary_significance`
  - critical context → `critical_context`
- **Bibliographic and verification fields:**
  - `bibliographical_notes` holds the first-edition details.
  - `research_notes` holds unresolved bibliographical questions.
  - `verification_status` records what has actually been checked.
- **Authors** carry a `bibliography_status` (complete, substantially complete or incomplete) and a written statement of what the bibliography covers, how it was checked and what is still missing.
- **Shared authors.** A writer recorded by an earlier installment keeps that single author record; installment-10 works link to it.

**Strict build.** `META["strict"]` turns off all template enrichment. `scripts/strict_checks.py` blocks the build when:
- a field falls short of its depth tier;
- boilerplate appears;
- a sentence is repeated across works;
- a date falls outside 1946–2000;
- a taxonomy name is undefined;
- a record is marked verified without the sources actually consulted.

No source is attached to records wholesale. Installments 8–9 attached four general reference works to every record; installment 10 does not.

**Discovery baseline.** `scripts/i10_discovery.py` builds `research/installment_10/discovery_inventory.csv` from the peer-reviewed datasets of the Post45 Data Collective (Emory University):
- US literary prizes, with Wikidata, VIAF and LCCN identifiers;
- British prizes, 1990–2022;
- NYT hardcover fiction bestsellers;
- the Asian American literary canon;
- NEA literature fellowships;
- *Playboy* fiction and speculative-fiction novels, used for discovery only because the repository index does not document them.

**Curated lists** in `research/installment_10/lists/` supplement the datasets; each list's source is a record in `data/sources/installment_10_sources.json`. So far there is one: the Booker Prize winners and shortlists 1969–2000, with the 1970 "Lost Booker" shortlist and longlist (205 rows, 140 authors).

Each candidate is assigned to the order's decades and given a priority tier: P1 for major prizes and the most-studied or best-selling authors, P2 for other prizes, shortlists and single bestsellers, and P3 for fellowships, periodical contributors and prolific genre authors. An inventory row is evidence of activity, not an inclusion decision.

**Verification levels.**
- *verified:* dates and bibliography cross-checked in at least two independent sources, listed with the record.
- *partially verified:* bibliographic facts checked, but the summary or critical text written from knowledge of the work and not checked against a source in this pass.
- *unverified:* not checked.

## 13. Corrections made

| Date | Record | Correction | Source |
|---|---|---|---|
| 2026-11-06 | Ralph Ellison, birth year | 1913 recorded; the older 1914 date noted as a discrepancy, not silently chosen | Wikipedia; New World Encyclopedia; Gale (via Encyclopedia.com) |
| 2026-11-06 | *Flying Home and Other Stories* | 1996 recorded (Random House first edition, ISBN 0679457046); Gale's 1997 noted as a research question | Wikipedia; Gale |
| 2026-11-06 | *Trading Twelves* (2000) | Pilot: not attributed to Ellison alone, deferred. Wave 04: recorded under Ellison with Albert Murray as co-author and co-editor (authorship status *collaborative*); Ellison's bibliography note updated | Wikipedia; *Guardian* obituary of Murray |
| 2026-11-06 | Pipeline | `build_installment.py` no longer fails on works by authors recorded in earlier installments (a `KeyError` on the owner lookup) | — |
| 2026-11-06 | Discovery inventory | Dataset typo "Step hen King" corrected to Stephen King and merged | Post45 NYT bestseller data |
| 2026-11-06 | Discovery inventory | Joint credits ("Larry Niven and Jerry Pournelle", "David and Leigh Eddings", "written and illustrated by Janet and Allan Ahlberg", and others) split into individual authors | Post45 datasets |
| 2026-11-06 | Discovery inventory | 17 reprinted authors who died before 1946 removed, among them Bierce, Conan Doyle, D. H. Lawrence, Keats, Milton and Swift; also three foreign classics (Maupassant, La Fontaine, Brantôme). Result: 5,617 candidates (P1 570, P2 1,692, P3 3,355) | Master database death dates |
| 2026-11-06 | Discovery inventory | Booker Prize list 1969–2000 added. It contributed 140 authors, 89 of whom appear in no Post45 dataset (among them Achebe, Anita Desai, Gurnah, Okri, Pym, Bainbridge, Lodge and Storey). Result: 5,706 candidates (P1 691, P2 1,666, P3 3,349) | Booker list (Wikipedia, from raw wikitext) |
| 2026-11-06 | Coverage evidence | None of the three authors of waves 02–04 (Philip Larkin, Lorraine Hansberry, Albert Murray) appears in the inventory. They were recorded directly from reference sources, and the gap is documented under limitations | Inventory lookup |
| 2026-11-06 | Waves 03–04, before import | Two citations to Wikipedia mirrors whose URLs had not been recorded, and one to an edition record that was never consulted, were removed. Their facts were re-checked against identifiable sources (Chicago Public Library, the Internet Archive catalogue, Gale/Ashley, the *Guardian*, EBSCO) or marked unconfirmed in research notes | See section 14 |
| 2026-11-06 | *The Sign in Sidney Brustein's Window* | 101 performances recorded; an untraceable figure of 99 dropped | Gale; Chicago Public Library |
| 2026-11-06 | *What Use Are Flowers?* | Reclassified from stage one-act to a short television play about the aftermath of nuclear war | Ashley (1990), via Gale |
| 2026-11-06 | *All What Jazz* | First edition recorded as Faber 1970 (*A Record Diary 1961–68*); the reference sources consulted cite only the 1985 enlarged edition | Jonkers Rare Books; AbeBooks |
| 2026-11-06 | "Aubade" | First publication fixed at *TLS*, 23 December 1977; composition 1974–29 November 1977 | Philip Larkin Society; Gale Literature Resource Center |
| 2026-11-06 | *Selected Letters of Philip Larkin* | Theme changed from race and civil rights to the divided public and private self: the letters' racism is a critical issue, not their subject | — |

## 14. Sources consulted

- **Peer-reviewed datasets** (Post45 Data Collective, https://github.com/Post45-Data-Collective/data, accessed 2026-11-06):
  - Major Literary Prizes (Grossman, Spahr and Young; doi:10.18737/CNJV1733p4520221212)
  - Selected British Literary Prizes (Binhammer, Batra, Gray and Jayasuriya; doi:10.18737/961425)
  - NYT Hardcover Fiction Bestsellers (Pruett; doi:10.18737/CNJV1733p4520220211)
  - NEA Creative Writing Fellowships (Manshel; doi:10.18737/096734)
  - Asian American Literary Canon (Le-Khac; doi:10.18737/092211)
  - Feminist Bookstore News (Enszer et al.; doi:10.18737/410409)
- **Prize record:** "List of winners and nominated authors of the Booker Prize" (Wikipedia), transcribed from the raw wikitext into `research/installment_10/lists/booker_prize_1969_2000.csv`. The article cites the Booker Prize Foundation's records and Moseley's *Booker Prize Novels 1969–2005* (DLB 326); neither was consulted directly.
- **Wave 01 (Ellison):** Wikipedia, "Ralph Ellison"; Encyclopedia.com, compiling Gale's *Contemporary Authors* and *Contemporary Black Biography*; New World Encyclopedia, "Ralph Ellison".
- **Wave 02 (Larkin):**
  - Wikipedia (via Wikiwand), "Philip Larkin"; EBSCO Research Starters, "Philip Larkin"; New World Encyclopedia, "Philip Larkin";
  - Brother Anthony of Taizé, "Without Metaphysics: The Poetry of Philip Larkin" (Sogang University web essay);
  - the Philip Larkin Society's page on "Aubade"; a critical essay in the Gale Literature Resource Center (document A53257935);
  - Jonkers Rare Books' catalogue record for *All What Jazz* (a trade record, used only for the first-edition date).
- **Wave 03 (Hansberry):**
  - Encyclopaedia Britannica;
  - three Gale entries via Encyclopedia.com: *Contemporary Black Biography*, a criticism introduction, and an entry reprinting Leonard R. N. Ashley's 1990 essay;
  - the Chicago Public Library biography;
  - the Internet Archive catalogue record of *Les Blancs: The Collected Last Plays* (Random House, 1972);
  - AmericanLiterature.com (low reliability; used only for points no other consulted source covers, which are marked provisional).
- **Wave 04 (Murray):**
  - Gale *Contemporary Black Biography* and *Contemporary Literary Criticism* entries via Encyclopedia.com;
  - the Alabama Authors database; LibraryThing (user-maintained, used for corroboration only);
  - the *Guardian* obituary (23 August 2013); EBSCO Research Starters, "Albert Murray".
- **Not consulted.** The order's preferred subscription sources (ODNB, ANB, JSTOR, Project MUSE, WorldCat) are not available in this environment. Library of Congress and British Library catalogue records are the next verification step for first-edition data; the open questions are listed in each record's research notes.

## 15. Remaining limitations and unresolved issues

1. **Coverage is at the very beginning.** Installment 10 holds 4 authors and 35 works (waves 01–04: Ellison, Larkin, Hansberry and Murray). The discovery baseline lists 5,706 candidate authors, and the movement, genre and theme taxonomies are defined, but almost all of the reconstruction is still to do.
2. **Gaps in the baseline itself.** The Post45 datasets are overwhelmingly American, and their British data begin in 1990. The Booker list now covers British, Irish and Commonwealth *novels* from 1969, but only novels by Commonwealth and Irish citizens; it contains no poetry, drama or criticism.
   - **Evidence:** none of the three authors added in waves 02–04 was in the inventory: Larkin (poetry), Hansberry (drama) and Murray (criticism and jazz writing). The inventory therefore cannot serve as the denominator of completeness for poetry, drama or criticism.
   - **Planned inventories:**
     - Whitbread from 1971, the Hawthornden Prize, the James Tait Black and Somerset Maugham awards, the Cholmondeley Award, the Queen's Gold Medal for Poetry, and the Carnegie and Kate Greenaway Medals;
     - the Governor General's Awards, the Miles Franklin Award, the New Zealand book awards, the Sahitya Akademi Award for English, the Noma Award and the Commonwealth Writers' Prize;
     - the Hugo, Nebula, Edgar, CWA Dagger, Newbery, Caldecott, Lambda, New York Drama Critics' Circle, Tony and Olivier awards;
     - the movement anthologies: *New Lines*, *The New American Poetry*, *Black Fire*, *Aiiieeeee!*, *The Mersey Sound*, *Mirrorshades*, *In the American Tree* and Granta 8.
3. **Name variants in the inventory.** For example "Angela Thirkell" and "Angela Mackail Thirkell". They are folded only by punctuation and accents, so a few authors appear twice; these are merged by hand when a wave reaches them.
4. **Translated foreign authors** (for example Camus and Moravia) appear among the bestsellers. They are out of scope unless they are theorists covered by Part VII.
5. **Partial verification.**
   - All 35 work records are *partially verified*: their bibliographic facts were checked, but their plot and critical texts were not checked against a source in this pass.
   - Open bibliographic questions are written into the records' research notes. Examples: the first-edition publisher of *A Raisin in the Sun*; the 1971 or 1972 date of *South to a Very Old Place*; the publisher of *The Movement* (1964); the network behind *The Drinking Gourd*; the lecture series behind *The Hero and the Blues*.
6. **Unresolved attributions:** *Reflections on Logic, Politics, and Reality* (1989), listed under Albert Murray by Gale and the Alabama Authors database, and *The Fantasy Poets No. 21* (1954, contents unverified) are named in the authors' bibliography notes but have no work records.
7. **Orwell's 1946–1950 works** (*Nineteen Eighty-Four*, *Critical Essays*, "Politics and the English Language", *The English People*, *Shooting an Elephant*) are still missing. Orwell is an installment-9 author, and the way to extend an earlier author's record without overwriting it has not yet been settled.
8. **Audits 3 and 8** (the external bibliographic comparison and the independent second pass) have not been run.

## Stopping point and outstanding tasks (2026-11-06)

**Done:**
- schema migration `f5a6b7c8d9e0`;
- the strict build path and checks;
- the record constructors;
- taxonomy: the 1946–2000 period, 69 movements, 181 genres in 10 families, and 33 themes;
- the discovery inventory: 5,706 candidates, including the Booker supplement;
- the audit script with the coverage matrix and this report;
- waves 01–04:
  - Ralph Ellison: 7 works, including *Trading Twelves* with Murray;
  - Philip Larkin: 12 works;
  - Lorraine Hansberry: 7 works;
  - Albert Murray: 9 works under his own name.

**Next, in order:**
1. **Inventories for poetry, drama and the Commonwealth.** The gap in point 2 comes first: the Commonwealth Writers' Prize, the Governor General's and Miles Franklin awards, the poetry and drama prizes, and the movement anthologies.
2. **Waves by decade × tradition × genre.** Work from P1 downwards. Each wave is built, imported and audited before the next starts. Planned order:
   - complete the Movement (Amis, Wain, Jennings, Conquest, Enright, Davie, Gunn, Holloway) and the Angry Young Men;
   - 1950s American: the Beats, confessional poetry and Jewish American fiction;
   - post-war drama;
   - African, Caribbean and South Asian founders;
   - then on through the 1960s–1990s, with genre fiction, children's literature and criticism and theory interleaved.
3. **Earlier-installment authors.** Settle the method for extending an existing author's record, then add the 1946–2000 works of Orwell, Beckett, Tolkien, Rhys, Welty, Auden, Isherwood, Brooks, Christie and others.
4. **After the reconstruction.** Run Audit 8 (the second pass) and the external bibliographic comparison of Audit 3, then regenerate this report.
