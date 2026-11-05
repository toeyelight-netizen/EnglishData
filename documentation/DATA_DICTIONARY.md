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

### significance_tier (authors)

Nullable controlled vocabulary added in Installment 8, recording documented
literary-historical standing. NULL means "not yet graded" and is the correct
value for installments 1-7, which were researched before the column existed.

| Value | Meaning |
|---|---|
| `Major / canonical` | Central to the canon; taught, anthologised, continuously in print |
| `Significant / secondary` | Substantial and studied, but not central to the canon |
| `Minor / lesser-known` | Real but limited standing; read by specialists |
| `Obscure / historically neglected` | Recovered or marginal figure; the record exists to make them findable |

Rules of use: assign from documented reception (standard literary histories,
the Cambridge/OUP/Oxford companions, the Dictionary of Literary Biography),
never from personal taste. An author whose standing is genuinely contested is
graded at the lower tier and the disagreement is recorded in
`biographical_uncertainty`.

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

## Genre additions (Installment 5)

- `Cavalier Lyric` — the courtly, often Jonsonian, occasional lyric of the 1630s–1650s
- `Comedy of Manners` — wit-driven satire on fashionable intrigue and reputation
- `Heroic Play` — the rhymed five-act drama of love and honour on the restored stage
- `Dramatic Opera and Semi-Opera` — Davenant's and Dryden's spoken drama with sung music
- `Closet Drama` — dramatic poetry for reading rather than performance (Samson Agonistes)
- `Spiritual Autobiography` — Grace Abounding and Hutchinson's Memoirs
- `Diary and Journal` — Pepys and Evelyn
- `Mock-Heroic and Verse Satire` — Hudibras, Mac Flecknoe, Absalom and Achitophel
- `Pindaric Ode` — the irregular celebratory ode after Cowley and Dryden
- `Prose Fiction and the Early Novel` — Behn's tales, Cavendish's romance, Astell's prose
- `Character Writing` — the Theophrastus-derived prose character (Fuller, Temple)
- `Verse Epistle` — the familiar verse letter in the Jonson–Donne line

## Theme list (Installment 5)

- `Civil War, regicide, and the trial of the king`
- `Liberty of conscience and religious toleration`
- `Country retirement and the estate poem`
- `Wit, libertinism, and the rake`
- `Restoration politics: party, succession, and Exclusion`
- `The New Science and experimental philosophy`
- `Carpe diem and the pleasures of the present`
- `Female authorship and the woman writer`
- `Slavery, empire, and the Atlantic world`
- `Faith, grace, and the pilgrim's journey`
- `The city and urban life`
- `Reason, faith, and the limits of understanding`

## Periods (Installment 5)

| Period | Start | End |
|---|---|---|
| Caroline, Commonwealth, and Restoration Period | 1625 | 1700 |

## Movements (Installment 5)

| Movement | Start | End |
|---|---|---|
| Cavalier Poetry | 1625 | 1660 |
| The Caroline Theatre | 1625 | 1642 |
| Commonwealth and Interregnum Literature | 1642 | 1660 |
| The Restoration Theatre | 1660 | 1700 |
| Comedy of Manners | 1660 | 1700 |
| Heroic Drama | 1660 | 1680 |
| The Cambridge Platonists | 1633 | 1688 |
| The New Science and the Royal Society | 1645 | 1700 |
| Civil War Radicalism: The Levellers and the Diggers | 1645 | 1660 |
| The Anglican and Latitudinarian Divines | 1625 | 1700 |

The pre-existing movement `Metaphysical Poetry` (1590–1660) is additionally
linked to the new period, because Herbert, Vaughan, Crashaw and Traherne write
after 1625.

## original_language (works) — values in use in Installment 5

- `English` — the vernacular corpus (197 works)
- `Latin` — Milton's Defensio Pro Populo Anglicano, Hobbes's De Cive, Locke's
  A Letter Concerning Toleration, and Conway's The Principles
- `English (translated from Latin)` — Hutchinson's Lucretius, Dryden's Virgil
  and his Juvenal and Persius
- `English (translated from French)` — Katherine Philips's Pompey after
  Corneille

## contribution_type — values in use in Installment 5

- `author` — every linked work in this installment has a named author; no
  compiler or translator rows were needed, because the period's translations
  are recorded as works of the translator and their co-authorship handled in
  `attribution_notes`.



---

## Genre additions (Installment 6) — 27

- Periodical Essay and Spectator Paper
- Augustan Verse Satire
- Epistolary Fiction
- Picaresque and Journey Novel
- Sentimental and Domestic Novel
- Gothic Novel and Romance of Terror
- Philosophical Tale and Oriental Fiction
- Comic and Ballad Opera
- Domestic and Sentimental Tragedy
- Theatrical Occasional Verse
- Meditative Blank Verse
- Topographical and Descriptive Poetry
- Hymn and Devotional Song
- Ballad and Popular Song
- Fable and Apologue
- Critical Treatise and Dissertation
- Moral Philosophy and the Theory of Society
- Political Economy and Commercial Writing
- Philosophical and National History
- Slave Narrative and Abolitionist Testimony
- Polemic, Pamphlet, and Open Letter
- Natural and Revealed Theology
- Lexicography and Philological Writing
- Memoir and Autobiographical Prose
- Literary Biography and Prefatory Commentary
- Anthology, Reliques, and Editorial Collection
- Conduct, Education, and Domestic Prose

## Theme list (Installment 6) — 22

- The public sphere, print, and the periodical
- Wit, ridicule, and the war against dullness
- Sympathy, benevolence, and the moral sense
- Taste, decorum, and the rules of art
- Commerce, luxury, and commercial society
- Liberty, corruption, and the decline of nations
- Death, mourning, and the graveyard meditation
- The sublime, terror, and the ruin
- Primitive genius and national poetry
- Women's education and intellectual friendship
- Seduction and the betrayed heroine
- The slave trade and abolition
- Enthusiasm and the disease of the imagination
- Evangelical experience and assurance
- Rural labour, depopulation, and the deserted village
- Poverty, dependence, and the professional writer
- Self-knowledge and the philosophy of the mind
- Jacobitism, loyalty, and the '45
- The literature of the nations: Scotland, Ireland, and Wales
- Progress, decay, and the philosophy of history
- Politeness, fashion, and the codes of conduct
- Childhood, innocence, and education

## Periods (Installment 6) — 6 cumulative, 1 new

- Augustan and Eighteenth-Century Period (1700–1789)

## Movements (Installment 6) — 49 cumulative, 15 new

- Abolitionist and Anti-Slavery Writing
- Augustan Satire and the Scriblerans
- Garrick and the Regenerated London Theatre
- Gothic and the Literature of Terror
- Neoclassical Criticism and the Rules
- Primitivism, the Bardic Revival and Ossian
- Sentimentalism and the Culture of Feeling
- The Bluestockings and Women's Letters
- The English Enlightenment and Deist Controversy
- The Evangelical Revival and Hymn Writing
- The Graveyard School and Preromantic Meditation
- The Rise of the English Novel
- The Scottish Enlightenment
- The Spectator and Periodical Journalism
- Topographical and Estate Poetry

## original_language (works) — values in use in Installment 6

- `English` — 326 work(s)
- `Scots` — 11 work(s)
- `English (rendered from Gaelic)` — 4 work(s)
- `English (translated from French)` — 3 work(s)
- `English (translated from Greek)` — 2 work(s)
- `English (translated from Latin)` — 2 work(s)
- `English (translated from Norse)` — 2 work(s)
- `English (translated from Latin and other languages)` — 1 work(s)

## Date fields — convention restated

The five `works` date columns are `VARCHAR(32)` (`composition_date_start`,
`composition_date_end`, `publication_date`, `first_performance_date`) and
`VARCHAR(64)` (`manuscript_date`), and `composition_date_circa` is a BOOLEAN.
Years are therefore stored as **strings**: `"1737"`, or `"c. 1737"` where the
date is approximate. Integer years are not used anywhere in the corpus.
