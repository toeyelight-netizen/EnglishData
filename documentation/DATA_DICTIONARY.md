# Data Dictionary

Controlled vocabularies and field-level conventions for
`database/English_Literature_Master.db`. This file is updated as each
installment adds new values.

## Controlled vocabularies

### authorship_status (works)

| Value | Meaning |
|---|---|
| `single` | One known author |
| `anonymous` | No known author; no author links may exist |
| `collaborative` | Multiple contributors by design |
| `attributed` | Ascribed by tradition to one author |
| `disputed` | Attribution contested |

### contribution_type (work_authors)

Current values in use:

- `author`
- `author (attributed)`
- `author (runic signature)` — Cynewulf's signed poems
- `author (traditional attribution)`
- `compiler (traditional attribution)` — e.g. the Anglo-Saxon Chronicle
- `draftsman (attributed)`
- `legislator`
- `translator`
- `translator (Genesis portion)` — Genesis B
- `translator (adaptation)` — added in Installment 2
- `translator (traditional attribution)`

New values may be added in later installments (e.g. `editor`, `adaptor`).

### research_status

| Value | Meaning |
|---|---|
| `complete` | Record researched and reviewed |
| `in_progress` | Record partially researched |
| `needs_review` | Flagged for scholarly review; kept, never silently deleted |
| `uncertain` | Fundamental uncertainty about the record itself |

### source_type (sources)

| Value | Meaning |
|---|---|
| `edition` | Scholarly edition of a primary text |
| `anthology` | Multi-text collection (e.g. ASPR) |
| `encyclopedia` | Reference encyclopedia |
| `reference` | Dictionary, catalogue, handbook |
| `textbook` | Didactic/survey work |
| `archive` | Digital archive/collection |

## Date conventions

Date fields are `VARCHAR(32)` and accept scholarly forms. In use:

| Form | Example | Meaning |
|---|---|---|
| Exact year | `731` | Certain |
| Approximate | `c. 700` | Circa |
| Range | `871–899` | Terminus post/ante quem |
| Combined | `c. 975–1025` | Approximate range |

- `composition_date_*` — when the text was composed.
- `publication_date` — first printed publication (for Old English texts this
  is normally the first modern edition, e.g. 1815 for Beowulf).
- `manuscript_date` — date of the surviving manuscript witness.
- `first_performance_date` — only for drama.

Boolean flags `birth_date_approximate` / `death_date_approximate` (authors)
mark approximate dates; works carry uncertainty in `attribution_notes` /
`bibliographical_notes` instead. The `composition_date_circa` flag (works,
added in Installment 2) marks approximate composition dates.

## JSON-encoded list fields

Stored as JSON text; always lists of strings:

- `authors.alternative_names`, `authors.pseudonyms`, `authors.major_influences`
- `works.alternative_titles`
- `works.editions`, `works.modern_translations`, `works.related_works`,
  `works.manuscript_locations` — added in Installment 2

## Genre hierarchy (Installment 1)

```
Poetry
├── Heroic Epic          ├── Elegy            ├── Religious Narrative Poetry
├── Religious Lyric      ├── Dream Vision     ├── Wisdom Poetry
├── Riddle               ├── Battle Poetry    ├── Bestiary Poetry
├── Metrical Charm       └── Metrical Psalter
Prose
├── History and Chronicle├── Homily (Sermon)  ├── Hagiography
├── Translation          ├── Law Code         ├── Political Treatise
├── Grammar and Didactic Prose                ├── Prose Romance
├── Travel and Wonders Literature             └── Letters
├── Monastic Rule and Customary               ├── Medical and Scientific Writing
├── Vision Literature                         └── Biblical Commentary and Exegesis
```

## Theme list (Installment 1)

Flat list; parent-child links available for later consolidation:

1. Heroism and the heroic code
2. Wyrd (fate) and providence
3. Exile and homelessness
4. The transience of earthly glory (ubi sunt)
5. Sea voyage and seafaring
6. Loyalty and the comitatus bond
7. Kingship and good rule
8. Treasure, gift-giving, and reciprocity
9. Blood-feud, vengeance, and kinship
10. Christian-pagan synthesis
11. Death, the soul, and the afterlife
12. Judgment Day and eschatology
13. Wisdom and learning
14. Creation and cosmology
15. Typology and biblical interpretation
16. Consolation and endurance
17. Warfare and battle
18. Solitude and the hall community
19. Women's experience and the feminine voice
20. Mission, conversion, and the Church
21. Monsters and the marvellous
22. Monasticism and the religious life
23. Medicine, healing, and the body

## Periods (Installment 1)

| name | start | end |
|---|---|---|
| Old English Period (Anglo-Saxon) | 450 | 1100 |

## Movements (Installment 1)

| name | start | end |
|---|---|---|
| Anglo-Saxon Heroic Tradition | 450 | 1100 |
| Early Anglo-Latin Learning and the Northumbrian Golden Age | 650 | 800 |
| Alfredian Renaissance | 871 | 899 |
| Benedictine Reform | 960 | 1000 |

## Genre additions (Installment 2)

New genres under existing roots:

```
Poetry
├── Debate Poetry           ├── Fabliau            ├── Verse Chronicle
├── Lyric                   ├── Lay (Breton Lai)   └── Political Verse
├── Romance (root genre)
Prose
├── Devotional and Mystical Writing
├── Courtesy Book and Household Manual
└── Philosophy and Scholastic Writing
Drama (new root)
├── Mystery Play            ├── Morality Play      └── Miracle Play
```

## Theme list (Installment 2)

Flat list; parent-child links available for later consolidation:

1. Courtly love and fin'amor
2. Penance, confession, and sin
3. The Virgin Mary and Marian devotion
4. The Passion of Christ
5. Chivalry and knighthood
6. Fortune and mutability
7. Social satire and estates criticism
8. Ecclesiastical reform and criticism
9. Lollardy and religious dissent
10. The contemplative life
11. Marriage and women's conduct
12. Arthurian legend
13. National identity and Englishness

## Periods (Installment 2)

| name | start | end |
|---|---|---|
| Middle English Period | 1100 | 1500 |

## Movements (Installment 2)

| name | start | end |
|---|---|---|
| The Twelfth-Century Renaissance | 1100 | 1200 |
| The AB Language Group (West Midlands Devotional Prose) | 1190 | 1250 |
| The Alliterative Revival | 1350 | 1450 |
| Ricardian Poetry | 1367 | 1400 |
| Lollardy | 1380 | 1430 |
| The English Mystics | 1340 | 1420 |
| Fifteenth-Century Chaucerians | 1400 | 1500 |
| The Scottish Makars | 1424 | 1513 |
| Vernacular Religious Drama | 1350 | 1500 |

## original_language (works) — values in use

- `Old English`
- `Latin`
- `Old English and Latin`
- `Latin and Old English` (bilingual/parallel texts)
- `Old English (translated from Latin)`
- `Old English (translated from Old Saxon)` — Genesis B
- `Old English (teaching Latin)` — Ælfric's Colloquy
- `Middle English` — added in Installment 2
- `Middle English (Scots)` — added in Installment 2
- `Anglo-Norman` — added in Installment 2 (Mandeville's Travels)

## Genre additions (Installment 3)

- `Humanist Dialogue and Utopian Fiction` — More's Utopia and its tradition
- `English Sonnet` — the Wyatt/Surrey sonnet and its Tottel successors
- `Complaint and Satire` — Skeltonic and early Tudor satirical verse and prose
- `Tudor Interlude` — the early Tudor secular and moral interlude
- `Reformation Polemic and Controversy` — the Tyndale–More print war and its successors
- `Bible Translation` — Tyndale, Coverdale, and the authorized versions
- `Humanist Educational Treatise` — Elyot, Ascham, and the pedagogy of the schools
- `Pastoral Poetry` — Barclay's eclogues and the vernacular pastoral
- `Prose Biography` — Roper, Cavendish, and the first English biographies

## Theme list (Installment 3)

- `Humanist education and the ideal commonwealth`
- `Reformation faith and the authority of scripture`
- `Courtly service and courtly danger`
- `Tyranny and the abuse of power`
- `The English vernacular and national letters`
- `Love, constancy, and betrayal`
- `Conscience and moral self-examination`
- `Religious persecution and martyrdom`
- `The education of princes and magistrates`

## Periods (Installment 3)

| Period | Start | End |
|---|---|---|
| Renaissance and Early Tudor Period | 1500 | 1558 |

## Movements (Installment 3)

| Movement | Start | End |
|---|---|---|
| English Renaissance Humanism | 1500 | 1558 |
| The English Reformation | 1525 | 1558 |
| Early Tudor Court Poetry | 1500 | 1558 |
| Early Tudor Drama | 1495 | 1558 |
| The Scottish Renaissance | 1500 | 1560 |

## original_language (works) — values added in Installment 3

- `English` — vernacular prose, verse, and drama of the period
- `English and Latin` — bilingual works (Lily's Grammar, the Vulgaria)
- `Latin` — the humanist Latin corpus (More, Leland, Linacre)
- `English (translated from Greek)` — Tyndale's New Testament
- `English (translated from Hebrew)` — Tyndale's Pentateuch
- `English (translated from Latin)` — Surrey's Aeneid and the prose translations
- `Scots` — Douglas and Lindsay
- `Scots (translated from Latin)` — Douglas's Eneados

## Genre additions (Installment 4)

- `English Epic and Allegorical Romance` — Spenser's Faerie Queene and the heroic-allegorical mode
- `Sonnet Sequence` — the Petrarchan sequence from Astrophel and Stella to Idea
- `Revenge Tragedy` — the Senecan-derived revenge plot from The Spanish Tragedy to The Revenger's Tragedy
- `Romantic Comedy` — the comedy of love, disguise, and reconciliation
- `History Play` — the chronicle drama of English and classical history
- `Tragedy` — serious drama of the fall of a great person
- `Comedy` — the drama of social error, wit, and reconciliation
- `City Comedy` — the satirical comedy of London manners
- `Court Masque` — the allegorical courtly entertainment with song, dance, and spectacle
- `Essay` — the short prose meditation in the tradition of Montaigne and Bacon
- `Metaphysical and Devotional Lyric` — the witty lyric of Donne and his school
- `Prose Romance and Euphuism` — Elizabethan prose fiction of love and adventure
- `Tragicomedy` — the mixed genre bringing a potentially tragic action to a happy resolution

## Theme list (Installment 4)

- `Petrarchan desire and the sonnet mistress`
- `Ambition and the overreacher`
- `Revenge and justice`
- `Appearance, dissembling, and self-fashioning`
- `Order and degree: the body politic`
- `Time, death, and immortality through verse`
- `The public theatre and the players' world`
- `Colonial enterprise and the New World`
- `Melancholy and self-analysis`
- `Divine love and holy desire`
- `Patronage and the literary marketplace`
- `Women, chastity, and constancy`

## Periods (Installment 4)

| Period | Start | End |
|---|---|---|
| Elizabethan and Jacobean Period | 1558 | 1625 |

## Movements (Installment 4)

| Movement | Start | End |
|---|---|---|
| English Petrarchism and the Sonnet Vogue | 1580 | 1620 |
| The Elizabethan Public Theatre | 1576 | 1642 |
| The University Wits | 1580 | 1600 |
| Metaphysical Poetry | 1590 | 1660 |
| Jacobean Tragedy and Revenge Drama | 1600 | 1640 |
| Jacobean City Comedy | 1600 | 1640 |

## contribution_type — values added in Installment 4

- `editor` — Hakluyt's Principal Navigations and Purchas's Pilgrimes (compilers of others' voyages)

## original_language (works) — values in use in Installment 4

- `English` — the vernacular corpus (151 works)
- `Latin` — Bacon's Novum Organum and Camden's Britannia, both first published in Latin
