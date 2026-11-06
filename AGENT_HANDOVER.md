# Agent handover

This repository builds a structured database of English-language literary
history, installment by installment. It is written to be resumed by an agent
with no memory of the session that produced it. Read this file first, then
`documentation/PROJECT_PROGRESS.md` (the wave log) and
`research/installment_10/report_notes.md` (the research record and the
outstanding work).

**State at this handover (2026-11-06, wave 26 merged):** installments 1–9 are
complete; installment 10 (1946–2000) is in progress at **209 works by 65
authors**, with **165 of 255** in-scope Norton selections recorded. The
database holds **912 authors, 3,053 works, 641 sources, 2,432 editions**.

---

## 1. The one rule that is easy to get wrong

The SQLite file `database/English_Literature_Master.db` is **not in Git** and
never has been (`.gitignore`). The JSON under `data/` is the source of truth;
the database is a build product. Do not commit the `.db`, and do not treat a
missing `database/` directory as data loss — rebuild it:

```bash
mkdir -p database
alembic upgrade head
python scripts/import_data.py
```

This reproduces 912 / 3,053 / 641 / 2,432 exactly from a clean clone.

## 2. First run

```bash
python -m pip install -r requirements.txt   # sqlalchemy, alembic, pytest absent
python -m unittest discover -s tests -v     # 81 tests, ~14 s (pytest is NOT installed)
```

`python -m pytest` fails with "No module named pytest". Use `unittest`.

## 3. The build chain, in order

Content lives in Python modules under `scripts/content/`, not in the JSON.
The JSON is generated. Editing `data/works/*.json` by hand is erased by the
next build.

```bash
# 0. write or edit scripts/content/content_i10_waveNN.py
python scripts/build_installment.py 10 --check-only   # report only, writes nothing
python scripts/build_installment.py 10                # writes data/{works,authors}/...

# 1. rebuild the database (the importer never deletes; see §5)
rm -f database/English_Literature_Master.db && mkdir -p database
alembic upgrade head && python scripts/import_data.py

# 2. gates
python scripts/check_installment.py 08   # 08, 09, 10 must all print CLEAN
python scripts/check_installment.py 09
python scripts/check_installment.py 10
python scripts/validate_database.py --installment 10   # expect "Total issues: 0"
python scripts/check_duplicates.py                    # expect 0 groups, 0 stale rows
python scripts/audit_installment_10.py                # regenerates audit + coverage matrix

# 3. export and test
python scripts/export_app_data.py        # android asset, ~14.5 MB, DO commit it
python3 -m unittest discover -s tests -q

# 4. docs, then commit
```

`scripts/i08_i09_check_queue.py` is a work-ordering report, not a gate.

## 4. Definition of a "wave"

One wave is typically 3–5 new authors and ~10–20 works, taken in Norton's
order. For each selection: one author record (never a second record for an
author already recorded) and one work record, with depth tiered by
significance. `A10` / `W10(...)` constructors in `scripts/content/i10_lib.py`.

Depth minima (overview / content / summary / themes / structure / style /
context / significance / criticism), enforced by `scripts/strict_checks.py`:

| Tier | min lengths |
|---|---|
| major | 250 / 250 / 1200 / 350 / 150 / 150 / 150 / 250 / 200 |
| significant | 150 / 120 / 450 / 150 / 80 / 80 / 100 / 120 / — |
| minor | 100 / — / 150 / 60 / 50 / 50 / 60 / 60 / — |

Strict checks also block: banned template phrases (`BANNED` in
`scripts/strict_checks.py` — includes "to be written", "placeholder",
"explores themes of", "TODO"), duplicate titles, unresolved taxonomy names,
out-of-period dates, and records marked `verified` without sources.

## 5. Database traps

- `works` has **no** `publication_year` and **no** `author_id`. Join
  `work_authors` → `authors`; dates are in `publication_date`; editions live in
  `work_editions`, not on `works`.
- `authors` has **no** `id` column; it is `author_id`.
- **The importer never deletes.** After correcting a date that forms part of a
  work's identity, an old row survives. Rebuild from empty instead, then run
  `check_duplicates.py`, which lists rows no installment file defines.
- **Duplicate source titles silently overwrite.** `upsert_source` keys on
  `title` alone. Two titles are currently defined in both
  `installment_08_sources.json` and `installment_09_sources.json`:
  *The Oxford Dictionary of National Biography, 60 vols* and *The Columbia
  Literary History of the United States*. The installment-09 definition wins;
  the installment-08 `reliability_notes` are discarded, and the importer still
  prints `sources: 643` while the table holds 641. If a source count looks
  wrong, check for a repeated title before looking anywhere else.
- `validate_database.py` rewrites `documentation/validation_reports/
  validation_report_NN.md`. The only change is the `Generated:` timestamp, so
  any diff there can be `git checkout --`ed safely.

## 6. Data conventions

- `data/sources/installment_10_sources.json` must be dumped with `indent=2`
  (indent 1 produces a 6,000-line diff).
- Source titles in the JSON must equal the `W_…` constants in the content
  module.
- Norton lists are CSVs in `research/installment_10/lists/`, numbered 1-based.
  Row counts there drive the audit; `tests/test_norton_lists.py` checks their
  internal consistency.
- The app asset `android/app/src/main/assets/data/english_literature.json`
  (~14.5 MB) **is** committed and must be regenerated and committed with each
  wave. Launcher icons and design assets under `android/app/src/main/res/` and
  `android/design/` are tracked and should stay. What must **not** be
  committed are the build screenshots the Android build emits at the
  `android/` root; stage with
  `git add -A -- ':!android/*.png'` if you have just run a build.

## 7. Where the work stands

Next in Norton's order (American anthology), from
`research/installment_10/lists/norton_naal_11e_vol_e.csv`:

| Author | in-scope rows | note |
|---|---|---|
| Sylvia Plath | 8 | **all eight still undated** — the first job is dating them |
| Toni Morrison | 1 | |
| John Updike | 1 | |
| Philip Roth | 1 | |
| Philip K. Dick | 1 | |
| Ursula K. Le Guin | 1 | |
| Octavia E. Butler | 1 | |
| Amiri Baraka | 4 | 2 undated |

90 American selections remain; 17 selections are undated overall (11 English,
6 American). The English anthology is complete for the period (90 of 90).

## 8. Source policy

Preferred: Wikipedia (article text and raw wikitext), Poetry Foundation,
publisher catalogue and contents pages, the *New Yorker* archive, Literary Hub,
university and library reference pages.

Rejected: Grokipedia, Goodreads, SuperSummary, eNotes, poemanalysis,
LitCharts, GradeSaver, SparkNotes, Studocu, CliffsNotes, bookrags,
personal-anthology blogs, AI-generated analyses, fandom wikis.

Two practical notes: bash in this environment reaches only GitHub and PyPI, so
external reading is done with the page-fetch tool; and several Poetry
Foundation and *New Yorker* URLs 404, so verify a URL before citing it.

## 9. Network and environment gotchas

- Fresh network builds may fail TLS intermittently (`gnutls_handshake`).
  Retry; it usually succeeds.
- The sandbox can be restored between sessions, which removes the gitignored
  `database/` directory and installed packages. Rebuild both (§2, §1).
- The local `master` branch may sit behind `origin/master`. Always `git fetch`
  and branch from `origin/master`, not from a stale local `master`. (At this
  handover local `master` was 51 commits behind.)
- Read the last ~40 lines of `documentation/PROJECT_PROGRESS.md` before starting
  work: the wave log at the top of this file is authoritative, but older
  hand-written summaries further down can still describe an earlier wave.
