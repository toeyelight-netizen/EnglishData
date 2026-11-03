# Database Schema

Master database: `database/English_Literature_Master.db` (SQLite 3)

Schema is managed by Alembic (`alembic upgrade head`). Current head:
`c2d3e4f5a6b7` (initial schema + FTS5 tables + work detail columns).

## Conventions

- Primary keys: surrogate integers (`*_id`), never reset between installments.
- Dates: `VARCHAR` where scholarly uncertainty requires non-ISO forms
  (`c. 700`, `871–899`, `c. 975–1025`); `INTEGER` for plain years.
- JSON-encoded list fields (TEXT): `alternative_names`, `pseudonyms`,
  `major_influences` (authors), `alternative_titles` (works), and (Inst. 2)
  `editions`, `modern_translations`, `related_works`, `manuscript_locations`.
- `authorship_status`: `single` | `anonymous` | `collaborative` | `attributed` | `disputed`.
- `research_status`: `complete` | `in_progress` | `needs_review` | `uncertain`.
- `created_at` / `updated_at`: automatic timestamps.
- All foreign keys enforced (`PRAGMA foreign_keys=ON` on every connection).

## Entity tables

### authors

| Column | Type | Notes |
|---|---|---|
| author_id | INTEGER PK | |
| full_name | VARCHAR(255) NOT NULL | unique import key |
| alternative_names | TEXT | JSON list |
| pseudonyms | TEXT | JSON list |
| birth_date / death_date | VARCHAR(32) | may be `c.`-prefixed |
| birth_date_approximate / death_date_approximate | BOOLEAN | |
| birthplace | TEXT | |
| nationality_or_literary_tradition | VARCHAR(255) | |
| literary_identity | VARCHAR(255) | poet, prose writer, critic… |
| biography | TEXT | |
| literary_profile | TEXT | |
| stylistic_characteristics | TEXT | |
| intellectual_concerns | TEXT | |
| historical_significance | TEXT | |
| major_influences | TEXT | JSON list |
| biographical_uncertainty | TEXT | explicit uncertainty notes |
| research_status | VARCHAR(32) | |

### works

| Column | Type | Notes |
|---|---|---|
| work_id | INTEGER PK | |
| title | VARCHAR(500) NOT NULL | |
| alternative_titles | TEXT | JSON list |
| authorship_status | VARCHAR(32) NOT NULL | see conventions |
| composition_date_start / composition_date_end | VARCHAR(32) | |
| composition_date_circa | BOOLEAN | approximate date flag (Inst. 2) |
| publication_date | VARCHAR(32) | first print/publication |
| first_performance_date | VARCHAR(32) | drama |
| manuscript_date | VARCHAR(64) | surviving manuscript(s) |
| original_language | VARCHAR(64) | Old English, Latin… |
| description | TEXT | |
| summary | TEXT | brief synopsis (Inst. 2) |
| plot_or_argument | TEXT | |
| narrative_structure | TEXT | |
| principal_characters | TEXT | |
| literary_form | VARCHAR(255) | |
| meter_and_prosody | TEXT | |
| historical_context | TEXT | |
| literary_significance | TEXT | |
| significance | TEXT | extended significance notes (Inst. 2) |
| attribution_notes | TEXT | |
| bibliographical_notes | TEXT | manuscript, editions |
| provenance_and_manuscripts | TEXT | witness details (Inst. 2) |
| editions | TEXT | JSON list (Inst. 2) |
| modern_translations | TEXT | JSON list (Inst. 2) |
| related_works | TEXT | JSON list (Inst. 2) |
| manuscript_locations | TEXT | JSON list (Inst. 2) |
| canonical_status | VARCHAR(32) | Inst. 2 |
| research_notes | TEXT | Inst. 2 |
| research_status | VARCHAR(32) | |

### periods

| Column | Type | Notes |
|---|---|---|
| period_id | INTEGER PK | |
| name | VARCHAR(255) NOT NULL | unique |
| start_year / end_year | INTEGER | |
| description | TEXT | |
| historical_context | TEXT | |
| literary_characteristics | TEXT | |

### movements

| Column | Type | Notes |
|---|---|---|
| movement_id | INTEGER PK | |
| name | VARCHAR(255) NOT NULL | unique |
| start_year / end_year | INTEGER | |
| description | TEXT | |
| historical_context | TEXT | |
| aesthetic_principles | TEXT | |
| defining_characteristics | TEXT | |
| historical_significance | TEXT | |

### genres

| Column | Type | Notes |
|---|---|---|
| genre_id | INTEGER PK | |
| name | VARCHAR(255) NOT NULL | unique |
| parent_genre_id | INTEGER FK → genres | self-referencing hierarchy |
| description | TEXT | |
| historical_development | TEXT | |

### themes

| Column | Type | Notes |
|---|---|---|
| theme_id | INTEGER PK | |
| name | VARCHAR(255) NOT NULL | unique |
| parent_theme_id | INTEGER FK → themes | self-referencing hierarchy |
| description | TEXT | |

### sources

| Column | Type | Notes |
|---|---|---|
| source_id | INTEGER PK | |
| title | VARCHAR(500) NOT NULL | unique |
| author_or_editor | VARCHAR(500) | |
| publisher | VARCHAR(255) | |
| publication_year | INTEGER | |
| source_type | VARCHAR(64) | edition, anthology, reference work, online resource… |
| url | TEXT | only verified stable URLs |
| doi_or_identifier | VARCHAR(255) | never invented |
| accessed_date | VARCHAR(32) | |
| reliability_notes | TEXT | |

### work_authors

Many-to-many with a contribution type.

| Column | Type | Notes |
|---|---|---|
| work_id | INTEGER PK, FK → works | |
| author_id | INTEGER PK, FK → authors | |
| contribution_type | VARCHAR(64) PK | author, collaborator, translator, editor, adaptor, disputed attribution… |

### work_editions

Scholarly editions of works.

| Column | Type | Notes |
|---|---|---|
| work_edition_id | INTEGER PK | |
| work_id | INTEGER FK → works | |
| edition_title | VARCHAR(500) | |
| editor | VARCHAR(500) | |
| publisher | VARCHAR(255) | |
| publication_year | INTEGER | |
| edition_notes | TEXT | |

## Relationship (junction) tables

Composite primary keys; all FK-enforced; `OR IGNORE` idempotent inserts.

| Table | Columns | Purpose |
|---|---|---|
| author_themes | author_id, theme_id | themes associated with an author |
| work_themes | work_id, theme_id | themes in a work |
| author_movements | author_id, movement_id | movements an author belongs to |
| work_movements | work_id, movement_id | movements a work belongs to |
| author_genres | author_id, genre_id | genres an author practised |
| work_genres | work_id, genre_id | genres of a work |
| work_periods | work_id, period_id | historical period(s) of a work |
| author_sources | author_id, source_id | sources for an author record |
| work_sources | work_id, source_id | sources for a work record |
| movement_sources | movement_id, source_id | sources for a movement record |
| period_movements | period_id, movement_id | movements within a period |
| author_influences | author_id, influenced_by_author_id | influence network edges |

## Full-text search (FTS5)

- `works_fts` — external-content table over `works` (title,
  alternative_titles, description, plot_or_argument, narrative_structure,
  principal_characters, literary_form, historical_context,
  literary_significance, attribution_notes, bibliographical_notes).
- `authors_fts` — external-content table over `authors` (full_name,
  alternative_names, pseudonyms, biography, literary_profile,
  stylistic_characteristics, intellectual_concerns, historical_significance).
- Both are kept in sync by INSERT/UPDATE/DELETE triggers on the base tables.
- Bulk imports finish with `INSERT INTO works_fts(works_fts) VALUES ('rebuild')`
  (same for `authors_fts`).

Example:

```sql
SELECT title, snippet(works_fts, 2, '[', ']', '…', 30)
FROM works_fts
WHERE works_fts MATCH 'dragon AND treasure'
ORDER BY rank;
```

## Additions beyond the specification

Two junction tables were added for normalization, documented here rather than
hidden: `work_genres` (spec lists author_genres but works need genre links for
filtering) and `work_periods` (works must belong to historical periods for
chronological browsing). Both follow the same composite-PK convention as the
specified relationship tables.
