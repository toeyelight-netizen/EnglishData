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
| 2026-11-06 | *Trading Twelves* (2000) | Not attributed to Ellison alone; deferred until Albert Murray's author record exists | Wikipedia |
| 2026-11-06 | Pipeline | `build_installment.py` no longer fails on works by authors recorded in earlier installments (a `KeyError` on the owner lookup) | — |
| 2026-11-06 | Discovery inventory | Dataset typo "Step hen King" corrected to Stephen King and merged | Post45 NYT bestseller data |
| 2026-11-06 | Discovery inventory | Joint credits ("Larry Niven and Jerry Pournelle", "David and Leigh Eddings", "written and illustrated by Janet and Allan Ahlberg", and others) split into individual authors | Post45 datasets |
| 2026-11-06 | Discovery inventory | 17 reprinted authors who died before 1946 removed, among them Bierce, Conan Doyle, D. H. Lawrence, Keats, Milton and Swift; also three foreign classics (Maupassant, La Fontaine, Brantôme). Result: 5,617 candidates (P1 570, P2 1,692, P3 3,355) | Master database death dates |

## 14. Sources consulted

- **Peer-reviewed datasets** (Post45 Data Collective, https://github.com/Post45-Data-Collective/data, accessed 2026-11-06):
  - Major Literary Prizes (Grossman, Spahr and Young; doi:10.18737/CNJV1733p4520221212)
  - Selected British Literary Prizes (Binhammer, Batra, Gray and Jayasuriya; doi:10.18737/961425)
  - NYT Hardcover Fiction Bestsellers (Pruett; doi:10.18737/CNJV1733p4520220211)
  - NEA Creative Writing Fellowships (Manshel; doi:10.18737/096734)
  - Asian American Literary Canon (Le-Khac; doi:10.18737/092211)
  - Feminist Bookstore News (Enszer et al.; doi:10.18737/410409)
- **Reference sources for wave 01 (Ellison):** Wikipedia, "Ralph Ellison"; Encyclopedia.com, compiling Gale's *Contemporary Authors* and *Contemporary Black Biography*; New World Encyclopedia, "Ralph Ellison".
- **Not consulted.** The order's preferred subscription sources (ODNB, ANB, JSTOR, Project MUSE, WorldCat) are not available in this environment. Library of Congress catalogue records are the next verification step for first-edition data.

## 15. Remaining limitations and unresolved issues

1. **Coverage is at the very beginning.** Installment 10 holds one author and six works (the wave-01 pilot). The discovery baseline lists 5,617 candidate authors, and the movement, genre and theme taxonomies are defined, but almost all of the reconstruction is still to do.
2. **Gaps in the baseline itself.** The Post45 datasets are overwhelmingly American, and their British data begin in 1990. British writing of 1946–1989 and the Commonwealth and postcolonial literatures need further inventories with the source recorded on every row. Planned sources:
   - Booker shortlists from 1969, Whitbread from 1971, the Hawthornden Prize, the James Tait Black and Somerset Maugham awards, the Cholmondeley Award, and the Carnegie and Kate Greenaway Medals;
   - the Governor General's Awards, the Miles Franklin Award, the New Zealand book awards, the Sahitya Akademi Award for English, the Noma Award and the Commonwealth Writers' Prize;
   - the Hugo, Nebula, Edgar, CWA Dagger, Newbery, Caldecott, Lambda, Tony and Olivier awards;
   - the movement anthologies: *New Lines*, *The New American Poetry*, *Black Fire*, *Aiiieeeee!*, *The Mersey Sound*, *Mirrorshades*, *In the American Tree* and Granta 8.
3. **Name variants in the inventory.** For example "Angela Thirkell" and "Angela Mackail Thirkell". They are folded only by punctuation and accents, so a few authors appear twice; these are merged by hand when a wave reaches them.
4. **Translated foreign authors** (for example Camus and Moravia) appear among the bestsellers. They are out of scope unless they are theorists covered by Part VII.
5. **Partial verification.** Plot and critical texts in the pilot are marked *partially verified*; checking summaries against texts or scholarly sources is a separate pass.
6. **Audit 8** (the independent second pass) has not been run.

## Stopping point and outstanding tasks (2026-11-06)

**Done:**
- schema migration `f5a6b7c8d9e0`;
- the strict build path and checks;
- the record constructors;
- taxonomy: the 1946–2000 period, 69 movements, 181 genres in 10 families, and 33 themes;
- the discovery inventory (5,617 candidates);
- the audit script with the coverage matrix and this report;
- pilot wave 01 (Ralph Ellison: six works).

**Next, in order:**
1. **Inventories.** Compile the British, Irish and Commonwealth inventories listed above. The Booker shortlists of 1969–1989 and the Commonwealth and genre prize lists come first.
2. **Waves by decade × tradition × genre.** Work from P1 downwards. Each wave is built, imported and audited before the next starts. Planned order:
   - 1950s British fiction and poetry: the Movement and the Angry Young Men;
   - 1950s American: the Beats, confessional poetry and Jewish American fiction;
   - post-war drama;
   - African, Caribbean and South Asian founders;
   - then on through the 1960s–1990s, with genre fiction, children's literature and criticism and theory interleaved.
3. **Earlier-installment authors.** Add the 1946–2000 works of authors already in the database (Beckett, Tolkien, Rhys, Welty, Auden, Isherwood, Brooks, Christie and others) and extend their author records.
4. **Albert Murray.** Add his author record, then *Trading Twelves*.
5. **After the reconstruction.** Run Audit 8 (the second pass) and the external bibliographic comparison of Audit 3, then regenerate this report.
