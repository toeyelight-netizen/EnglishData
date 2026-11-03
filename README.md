# English Literature Database (450–2000)

A comprehensive scholarly database of English literature from the Old English
period through 31 December 2000, built for future integration into web,
desktop, or mobile applications.

The database is populated in **ten sequential research installments**, all
writing to the same cumulative master database. No installment ever replaces
or deletes earlier data.

## Current status

| Installment | Period | Status |
|---|---|---|
| 1 | Old English and Early Medieval (c. 450–1100) | **Complete** |
| 2 | Middle English (c. 1100–1500) | **Complete** |
| 3 | Renaissance and Early Tudor (c. 1500–1558) | **Complete** |
| 4–10 | Elizabethan → Postwar (1558–2000) | Pending |

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
cd English-Literature-Database
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
# 1. Import research JSON (idempotent: safe to re-run)
python scripts/import_data.py

# 2. Validate the database (writes documentation/validation_reports/)
python scripts/validate_database.py --installment NN

# 3. Check for duplicates
python scripts/check_duplicates.py

# 4. Run the test suite
python -m unittest discover -s tests -v

# 5. Statistics and exports
python scripts/generate_statistics.py
python scripts/export_data.py
```

Back up the master database after every installment:

```bash
cp database/English_Literature_Master.db database/backups/English_Literature_Master_installment_NN.db
```

## Directory structure

```
English-Literature-Database/
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
