# Research Methodology

## Scope

This project builds a scholarly database of English literature from the Old
English period (c. 450) through 31 December 2000. "English literature" is
understood inclusively: Old and Middle English, Latin writings produced in
England, and the Anglophone traditions of Scotland, Wales, Ireland, and the
wider English-speaking world, together with anonymous, collaborative, and
translated texts that belong to the English literary record.

The Norton Anthology of English Literature provides the initial canonical
framework; the database deliberately expands far beyond its selection to
include lesser-known writers, women writers, and non-metropolitan traditions.

## Ten-installment protocol

Research proceeds in exactly ten sequential installments, each covering one
historical period. Every installment follows the same protocol:

1. Read `documentation/PROJECT_PROGRESS.md`.
2. Inspect the existing database, schema, and records.
3. Research **only** the next assigned period.
4. Prepare structured JSON research data under `data/<entity>/`.
5. Validate the JSON (import performs structural validation).
6. Import into the existing master database (`scripts/import_data.py`).
7. Resolve duplicates (`scripts/check_duplicates.py`).
8. Validate all foreign keys and integrity rules
   (`scripts/validate_database.py`).
9. Back up the database to `database/backups/`.
10. Update `documentation/PROJECT_PROGRESS.md`.
11. Run the automated test suite (`python -m unittest discover -s tests`).
12. Generate updated statistics (`scripts/generate_statistics.py`).

The master database is never deleted or recreated. Identifiers are never
reset. Imports are idempotent; a re-run can never duplicate records.

## Source hierarchy

Factual and interpretive claims are grounded in the following priority order:

1. **Primary texts and manuscript catalogues** — manuscript witnesses
   (Nowell Codex, Exeter Book, Vercelli Book, Junius 11), standard editions
   (ASPR, Klaeber's Beowulf), British Library digitised manuscripts, the
   Dictionary of Old English.
2. **Standard reference works** — Oxford Dictionary of National Biography,
   The Blackwell Encyclopaedia of Anglo-Saxon England, Oxford Reference,
   English Historical Documents.
3. **Scholarly companions and surveys** — Cambridge Companions, Norton
   Anthology introductions and headnotes.
4. **Scholarly journals and university archives** — used when needed for
   specific points of attribution or dating.

Every author, work, and movement record is linked to the sources that support
it (`author_sources`, `work_sources`, `movement_sources`).

## Attribution policy

- **No authorship or biographical information is invented.** Where tradition
  ascribes a work to an author without secure evidence, the record uses
  `authorship_status = 'attributed'` or `'disputed'`, the `contribution_type`
  marks traditional attribution, and `attribution_notes` states the state of
  scholarship (e.g. "Anonymous; ascribed by tradition, not by manuscript
  evidence").
- Anonymous works carry `authorship_status = 'anonymous'` and **no** author
  links; a validation rule enforces this.
- Signed or self-attributed texts (e.g. Cynewulf's runic signatures, Alfred's
  prefaces, Ælfric's and Wulfstan's homilies) are linked with the
  corresponding evidence-based `contribution_type`.

## Dating policy

Four distinct date concepts are never conflated:

- **Composition date** — when the text was written (`composition_date_*`).
- **Manuscript date** — when the surviving witness was copied
  (`manuscript_date`).
- **Publication date** — first print publication (`publication_date`).
- **Performance date** — for drama only (`first_performance_date`).

Uncertain dates use scholarly conventions (`c. 700`, `871–899`,
`c. 975–1025`) rather than fabricated precision. Authors have boolean
approximate-date flags; works carry the reasoning in `attribution_notes` and
`bibliographical_notes`.

## Information quality standards

- **Authors**: birth/death dates where known; biography; literary and
  intellectual profile; historical importance; style and major concerns;
  influences; complete known bibliography.
- **Works**: full title; authorship status; composition, manuscript,
  publication, and performance dates; genres, periods, movements; detailed
  description; principal themes; historical context; literary significance;
  bibliographical sources.
- Novels: plot, narrative structure, characters, themes. Poetry: form, meter,
  imagery, symbolism, intellectual concerns. Drama: plot, structure,
  characters, conflicts, theatrical importance. Criticism and philosophy:
  central arguments and concepts.
- Descriptions must be academically informative and specific — generic
  placeholders are not permitted.

## Citation policy

- **References, dates, URLs, and quotations are never invented.**
- URLs are recorded only when verified stable (in Installment 1: the
  Dictionary of Old English and British Library Digitised Manuscripts).
- DOIs are recorded only when verified; otherwise left null.
- All sources used are catalogued in `documentation/BIBLIOGRAPHY.md`.

## Validation regime

`scripts/validate_database.py` checks on every installment:

- SQLite `PRAGMA integrity_check` and `PRAGMA foreign_key_check`.
- Required fields present (names, titles, authorship status).
- Date sanity (birth ≤ death; composition within plausible bounds;
  publication not impossibly early — with an allowance for Old English texts
  whose first print edition postdates composition by centuries).
- Duplicate authors and works (natural keys).
- Anonymous works incorrectly linked to authors.
- Many-to-many links referencing missing records.
- Works/authors lacking source references.
- Period-assignment consistency (work composition dates vs. period bounds,
  within documented tolerance).

Questionable records are **flagged, never silently deleted**, and remain in
the database with `research_status` set appropriately.

## Progress and reproducibility

- Every installment ends with a completion report: counts added, cumulative
  counts, validation results, unresolved bibliographical issues, and
  confirmation that earlier installments remain intact.
- Each installment is committed to Git separately.
- Full JSON exports of all tables live in `data/exports/` and are refreshed
  after each installment.
- The next installment is never begun automatically; the curator's
  instruction is required.
