# Installment 7 authoring brief — British AND American Romantic period (c. 1789-1832)

You are writing ONE batch of installment 7 for a cumulative scholarly SQLite
database of English literature. Read this whole file before writing anything.

## Absolute rules

1. **Never invent** an author, a date, a first edition, a publisher, a quotation,
   a title, or a biographical fact. If you are not sure of a year, use `"c. 1802"`
   or leave the field `null`. A `null` is honest; a wrong year is a defect.
2. Do not touch any file outside the three your batch owns (listed at the end).
   Never edit `data/works/installment_0[1-6]*`, `scripts/_i06_*`, or the database.
3. Every work must be a real, individually titled literary work of 1785-1837
   (the working edges of the period), by an author of the roster you are given.
4. Do not duplicate anything already in the corpus: check
   `scripts/_i07_existing_works.txt` (1061 titles) and
   `scripts/_i07_existing_authors.json` (310 names) before using a title or name.
   Robert Burns, William Cowper, Thomas Gray, Samuel Johnson, Edward Gibbon,
   William Blake's *Songs of Innocence* and other pre-1790 items may already exist;
   if a title is present there, do not re-add it.

## Files you write

For batch slug `bN`:

- `data/works/installment_07_works_batchN.json` — a JSON array of work records.
- `data/authors/installment_07_authors_bN.json` — a JSON array of author records
  (omit the file entirely if your batch adds no new author).
- `scripts/_i07_map_bN.py` — `MAP_BN = { "<work title>": ([authors], [genres], [themes], [movements]) }`

## Work schema — exactly these 21 keys, in this order

```
title, alternative_titles, authorship_status, composition_date_start,
composition_date_end, publication_date, first_performance_date, manuscript_date,
original_language, description, plot_or_argument, narrative_structure,
principal_characters, literary_form, meter_and_prosody, historical_context,
literary_significance, attribution_notes, bibliographical_notes,
canonical_status, research_status
```

Types:

- `alternative_titles`: array of strings or `null`.
- `composition_date_start`, `composition_date_end`, `publication_date`,
  `first_performance_date`, `manuscript_date`: **STRING year** (`"1802"`) or
  `"c. 1802"`, or `null`. Never a JSON number. `manuscript_date` is `null` for
  print-era works.
- `principal_characters`: one **semicolon-joined string**
  (`"Gulliver; the Emperor of Lilliput"`) or `null`. Never a list.
- Every other field: string or `null`. Never an empty string — use `null`.
- `authorship_status` in `single, anonymous, collaborative, attributed, disputed`.
- `canonical_status` in `Major canon, Secondary canon, Minor canon`.
- `research_status` = `"complete"` unless attribution is genuinely contested.
- `original_language` = `"English"` for almost everything (`"Scottish English"`
  or `"Scots"` only where right; `"Latin"` etc. only where right).
- `publication_date` >= `composition_date_start` when both are present.
- **No author names inside work records.** Authorship lives in the map only.

Depth required per record: `description` 2-4 sentences; `plot_or_argument` 3-6
sentences; `historical_context` 2-4; `literary_significance` 2-4; `literary_form`
names the genre and its conventions; `meter_and_prosody` concrete
(`"Heroic couplets, iambic pentameter"`, `"Blank verse, five-beat lines"`);
`bibliographical_notes` names the first edition (publisher/format where known,
e.g. `"First published London, 1814, in three volumes, anonymously"`).
Fields you cannot fill honestly: `null`.

## Author schema — exactly these 18 keys, in this order

```
full_name, alternative_names, pseudonyms, birth_date, birth_date_approximate,
death_date, death_date_approximate, birthplace, nationality_or_literary_tradition,
literary_identity, biography, literary_profile, stylistic_characteristics,
intellectual_concerns, historical_significance, major_influences,
biographical_uncertainty, research_status
```

- `alternative_names`, `pseudonyms`: array of strings or `null`.
- `birth_date`, `death_date`: STRING year (`"1770"`) or `"c. 1770"`;
  `birth_date_approximate`, `death_date_approximate`: boolean.
- `biography` 4-8 sentences; `literary_profile`, `stylistic_characteristics`,
  `intellectual_concerns`, `historical_significance` 2-4 sentences each;
  `major_influences` a semicolon-joined string or `null`;
  `biographical_uncertainty` `null` unless something is genuinely disputed;
  `research_status` in `complete, partial`.

## Taxonomy

`scripts/_i07_taxonomy_names.txt` lists verbatim: installment-7 movements,
genres and themes (the primary vocabulary), then every pre-existing DB name that
may be reused where genuinely apt. **Names must match that file character for
character** (straight apostrophes). Every work needs at least one genre and one
theme; movements may be `[]` but usually should not be.

## Map format

```python
MAP_B1 = {
    "The Excursion": (
        ["William Wordsworth"],
        ["Philosophical Poem and Meditation"],
        ["Nature, landscape, and the shaping mind", "Memory and the growth of the poet's mind"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
}
```

One entry per work in your batch, keys identical to the works-file titles.
Authors are ALWAYS a list (empty list `[]` only for genuinely anonymous works).

## How to write the file (CRITICAL)

Emitting 45 records in one response fails. Build incrementally:

1. Write the first 6 records with the Write tool as a complete JSON array.
2. Append the next 6-8 with the Edit tool (replace the closing `]` with
   `,\n  {...records...}\n]`), and re-validate after each append:
   `python -c "import json;d=json.load(open('data/works/installment_07_works_batchN.json',encoding='utf-8'));print(len(d))"`
3. Do the same for the authors file.
4. Write the map file in one or two passes, then check it imports:
   `python -c "import sys;sys.path.insert(0,'scripts');import _i07_map_bN as m;print(len(m.MAP_BN))"`
5. Self-check before finishing: every work title appears in the map and vice
   versa; no JSON number in a date field; no `principal_characters` list; no
   empty strings; no title that already exists in `scripts/_i07_existing_works.txt`;
   no author name inside a work record.

Do **not** run `scripts/installment_toolkit.py check` — other batches are being
written concurrently and their half-finished files will confuse it. The
controller runs that gate centrally.

Report at the end: counts of works and authors written, and anything you had to
leave `null` because the evidence was not certain.
