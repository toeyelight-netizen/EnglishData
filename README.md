# English Literature Database (450–2000)

A comprehensive scholarly database of English literature from the Old English
period through 31 December 2000, built for future integration into web,
desktop, or mobile applications.

The database is populated in **ten sequential research installments**, all
writing to the same cumulative master database. No installment ever replaces
or deletes earlier data.

> Resuming this project, or working on it as an agent? Read
> [`AGENT_HANDOVER.md`](AGENT_HANDOVER.md) first: it has the build chain in
> order, the gate scripts, the database traps and where the work stands.

## Current status

| Installment | Period | Status |
|---|---|---|
| 1 | Old English and Early Medieval (c. 450–1100) | **Complete** |
| 2 | Middle English (c. 1100–1500) | **Complete** |
| 3 | Renaissance and Early Tudor (c. 1500–1558) | **Complete** |
| 4 | Elizabethan and Jacobean (1558–1625) | **Complete** |
| 5 | Caroline, Commonwealth, Restoration (1625–1700) | **Complete** |
| 6 | Augustan and Eighteenth Century (1700–1789) | **Complete** |
| 7 | Romantic, British and American (1789–1832) | **Complete** |
| 8 | Victorian, British and American (1832–1901) | **Complete** |
| 9 | Edwardian, Georgian and Modernist, British and American (1901–1945) | **Complete** |
| 10 | Postwar and Contemporary: British, Irish, American and Anglophone (1946–2000) | In progress (Norton anthologies: 249 works by 89 authors; 204 works recorded against 265 in-scope selections - English 89 of 96, American 115 of 169; 58 remain, none undated) |

Cumulative totals: **913 authors, 3061 works** (147 anonymous), 10 periods, 179
movements, 370 genres, 203 themes, 656 sources, 2432 recorded editions.

Installment 8 contributed **233 authors and 887 works** to the Victorian period
(1832–1901), with both a British and an American strand. It runs from the
Brontës, Tennyson and Eliot through Swinburne, Wilde, Hardy and Shaw, and from
Emerson, Dickinson and Twain to James, Crane, Dreiser and Wharton.

Installment 9 contributed **197 authors and 498 works** to the Edwardian,
Georgian and Modernist period (1901–1945). It runs from Wells, Bennett,
Galsworthy and Forster through Joyce, Woolf, Eliot, Lawrence and the war poets
to Auden and Orwell, and in America from the Harlem Renaissance to Hemingway,
Faulkner and Steinbeck.

Installment 10 (1946–2000, with 1951–2000 as the core) is **in progress, and
most of it is still to do.**
- **Scope (third decision, 2026-11-06).** The authors and selections of the
  Norton anthologies: *The Norton Anthology of English Literature* (11th
  edition, volume F) for British, Irish and Commonwealth writing, and *The
  Norton Anthology of American Literature* (volume E, 11th edition's table of
  contents) for American writing. Every selection first published 1946–2000
  gets its own record; the two lists are in `research/installment_10/lists/`.
- **Record standard.** A strict, template-free build: every work has a
  seven-part description, a bibliography status, a verification status and the
  sources actually consulted.
- **Current state.** 209 works by Ralph Ellison, Philip Larkin, Lorraine
  Hansberry, Samuel Selvon, Stevie Smith, Dylan Thomas, Louise Bennett, Kamau
  Brathwaite, Ngũgĩ wa Thiong'o, M. NourbeSe Philip, Salman Rushdie, Grace
  Nichols, Linton Kwesi Johnson, Doris Lessing, A. K. Ramanujan, Thom Gunn,
  Derek Walcott, Ted Hughes, Chinua Achebe, Alice Munro, Geoffrey Hill, V. S.
  Naipaul, Wole Soyinka, Caryl Churchill, Seamus Heaney, Les Murray, J. G.
  Ballard, Bessie Head, Ben Okri, Arundhati Roy, Margaret Atwood, J. M. Coetzee,
  Eavan Boland, Anne Carson, Paul Muldoon, bpNichol, Hanif Kureishi, Carol Ann
  Duffy, Kiran Desai, Vladimir Nabokov, Theodore Roethke, Elizabeth Bishop,
  Tennessee Williams, John Cheever, Robert Hayden, Saul Bellow, Arthur Miller and
  Robert Lowell, J. D. Salinger, Jack Kerouac, Kurt Vonnegut, Grace Paley, Frank
  O'Hara, Audre Lorde, Susan Sontag, John Barth, Joan Didion, James Baldwin,
  Flannery O'Connor, Allen Ginsberg, John Ashbery, Anne Sexton, Adrienne Rich,
  Martin Luther King Jr., Donald Barthelme, Sylvia Plath, Toni Morrison, John
  Updike, Philip Roth, Philip K. Dick, Ursula K. Le Guin and Octavia E. Butler,
  and by George
  Orwell, Jean Rhys, Samuel Beckett, W. H. Auden and Gwendolyn Brooks (their
  installment 9 author records, extended), and by Toni Morrison, John Updike,
  Philip Roth, Philip K. Dick, Ursula K. Le Guin, Octavia E. Butler, Amiri
  Baraka, N. Scott Momaday, Mary Oliver, Lucille Clifton, Don DeLillo, Thomas
  Pynchon, Raymond Carver, Toni Cade Bambara, Maxine Hong Kingston, Leslie
  Marmon Silko, Ishmael Reed and Richard Rodriguez. 204 works are recorded against
  the 265 selections in the period, leaving 58; every row is now dated.
  The measured state, the eight audits, the corrections made to installments
  8–9 and the exact stopping point are in
  [documentation/INSTALLMENT_10_AUDIT_REPORT.md](documentation/INSTALLMENT_10_AUDIT_REPORT.md).

See [documentation/PROJECT_PROGRESS.md](documentation/PROJECT_PROGRESS.md) for
the detailed progress log.

## Technology stack

- Python 3 (3.10+)
- SQLite 3 (with FTS5 full-text search)
- SQLAlchemy 2.0 (ORM)
- Alembic (schema migrations)
- JSON (research data interchange and exports)
- Markdown (documentation)
- Git (version control)

## Setup

```bash
cd EnglishData
python -m pip install -r requirements.txt
```

Create the schema (from migrations, recommended):

```bash
alembic upgrade head
```

Alternatively, `python scripts/initialize_database.py` creates the same
schema idempotently (convenience path; migrations remain canonical).

## Standard workflow (per installment)

```bash
# 0. Content changes only: build the installment JSON and run its strict checks.
#    --check-only reports problems without writing; the build exits non-zero on
#    a thin field, template text, an undefined taxonomy name or a duplicate title.
python scripts/build_installment.py 10 --check-only
python scripts/build_installment.py 10

# 1. Import research JSON (idempotent: safe to re-run)
python scripts/import_data.py

# 2. Check the installment's own integrity, then validate the database
#    (validation writes documentation/validation_reports/)
python scripts/check_installment.py 10
python scripts/validate_database.py --installment NN

# 3. Check for duplicates
python scripts/check_duplicates.py

# 4. Run the test suite
python -m unittest discover -s tests -v

# 5. Statistics and exports
python scripts/generate_statistics.py
python scripts/export_data.py
python scripts/export_app_data.py

# 6. Regenerate the installment audit and coverage matrix
python scripts/audit_installment_10.py
```

Back up the master database after every installment:

```bash
cp database/English_Literature_Master.db database/backups/English_Literature_Master_installment_NN.db
```

## Directory structure

```
EnglishData/
|-- database/            # English_Literature_Master.db + backups/
|-- data/                # research JSON by entity + exports/
|-- scripts/             # initialize, import, export, validate, duplicates, statistics
|-- models/              # SQLAlchemy models
|-- migrations/          # Alembic migrations
|-- documentation/       # schema, data dictionary, methodology, progress, bibliography
|-- tests/               # unittest suite
|-- requirements.txt
|-- README.md
|-- .gitignore
```

## Key design decisions

- **Idempotent imports** — records are matched by natural keys (author full
  name; work title + authorship status + composition start date; unique names
  for periods, movements, genres, themes, sources). Re-running an import
  updates records and never duplicates them. Relationship rows use composite
  primary keys with `OR IGNORE` semantics.
- **Stable identifiers** — primary keys are never reset between installments.
- **Authorship status** — `single`, `anonymous`, `collaborative`,
  `attributed`, `disputed`. Anonymous works have no author links.
- **Uncertain dates** — stored as VARCHAR with scholarly conventions
  (`c. 700`, `871–899`), plus boolean `*_date_approximate` flags on authors
  and explicit uncertainty notes on works.
- **Full-text search** — FTS5 external-content tables (`works_fts`,
  `authors_fts`) kept in sync by triggers and rebuilt after bulk imports.
- **Research provenance** — every author and work is linked to its
  bibliographic sources via `author_sources` and `work_sources`.

## License and provenance

All research data is compiled from established scholarly sources (see
[documentation/BIBLIOGRAPHY.md](documentation/BIBLIOGRAPHY.md) and
[documentation/RESEARCH_METHODOLOGY.md](documentation/RESEARCH_METHODOLOGY.md)).
No authorship or biographical information is invented; uncertainty is marked
explicitly.
