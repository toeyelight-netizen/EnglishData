# Project Progress

Progress log for the English Literature Database (450–2000). One entry per
installment. The master database is cumulative: `database/English_Literature_Master.db`.

## Protocol state

- Current schema revision (Alembic): `c2d3e4f5a6b7` (initial schema + FTS5 +
  work detail columns).
- Backups: `database/backups/English_Literature_Master_installment_01.db`,
  `database/backups/English_Literature_Master_installment_02.db`,
  `database/backups/English_Literature_Master_installment_03.db`.
- Validation reports: `documentation/validation_reports/validation_report_01.md`,
  `documentation/validation_reports/validation_report_02.md`,
  `documentation/validation_reports/validation_report_03.md`.

## Installment 1 — Old English and Early Medieval Literature (c. 450–1100)

**Status: COMPLETE** — 2026-11-03

### Scope

Old English poetry and prose, Anglo-Latin literature written in England, and
the manuscript culture of Anglo-Saxon England (c. 450–1100). Coverage: the
heroic and elegiac corpus (Beowulf through the Exeter Book elegies), the
religious poetic corpus (Cynewulf, Genesis A/B, the Junius 11 poems, the
Exeter Book religious lyrics), the Alfredian translation programme, the
Benedictine Reform writers (Ælfric, Wulfstan, Byrhtferth), the Anglo-Saxon
Chronicle, law codes, hagiography, and letters.

### Records added

| Entity | Added | Cumulative |
|---|---|---|
| Authors | 24 | 24 |
| Works | 128 | 128 |
| Anonymous works | 84 | 84 |
| Periods | 1 | 1 |
| Movements | 4 | 4 |
| Genres | 27 | 27 |
| Themes | 23 | 23 |
| Sources | 11 | 11 |
| Work–author links | 42 | 42 |
| Work editions | 19 | 19 |
| Other relationship rows | 1,048 | 1,048 |

### Authors (24)

Cædmon, Aldhelm, Bede, Alcuin of York, Boniface, Cynewulf, Alfred the Great,
Asser, Ælfric of Eynsham, Wulfstan (of York), Byrhtferth of Ramsey,
Æthelweard, Wulfstan the Cantor, Gildas, Nennius, Felix of Crowland,
Werferth, **Stephen of Ripon, Æthelwold of Winchester, Abbo of Fleury,
Ælfric Bata, Tatwine, Hwætberht (Eusebius), Theodore of Tarsus**.

### Works (128) — summary by group

- **Heroic and elegiac verse (14):** Beowulf, Widsith, Deor, Waldere, the
  Finnsburh Fragment, The Battle of Brunanburh, The Battle of Maldon, The
  Wanderer, The Seafarer, The Wife's Lament, Wulf and Eadwacer, The Husband's
  Message, The Ruin, Cædmon's Hymn.
- **Religious poetry (27):** The Dream of the Rood, Christ I–III, Guthlac
  A/B, Juliana, Elene, The Fates of the Apostles, Andreas, Genesis A/B,
  Exodus, Daniel, Christ and Satan, Judith, The Phoenix, The Panther, The
  Whale, The Partridge, Soul and Body I/II, Maxims I/II, The Fortunes of Men,
  The Exeter Book Riddles, The Metrical Psalms of the Paris Psalter, The
  Metrical Charms, Solomon and Saturn I/II.
- **Minor poems and wisdom verse (23, added in the comprehensiveness
  expansion):** The Rhyming Poem, Resignation, The Descent into Hell,
  Azarias, The Lord's Prayer I–III, Gloria I–II, The Creed, The Kentish
  Hymn, Alms-Giving, Pharaoh, The Gifts of Men, Precepts, Vainglory, The
  Order of the World, The Judgement Day I–II, An Exhortation to Christian
  Living, A Summons to Prayer, The Menologium, Homiletic Fragment I–II, The
  Rune Poem, Seasons for Fasting, Bede's Death Song, The Leiden Riddle.
- **Prose (39):** Anglo-Saxon Chronicle, Bede's Historia ecclesiastica / De
  temporum ratione / Vita Cuthberti, Aldhelm's De virginitate / Aenigmata,
  Felix's Vita Guthlaci, Gildas's De excidio, the Historia Brittonum, Asser's
  Life of Alfred, all Alfredian translations (Pastoral Care, Boethius,
  Soliloquies, Orosius), the four major law codes, the Old English
  Martyrology, Blickling and Vercelli Homilies, Ælfric's Catholic Homilies /
  Lives of Saints / Grammar / Colloquy / Hexateuch, Wulfstan's Sermo Lupi /
  Institutes of Polity / Eschatological Homilies, Byrhtferth's Enchiridion,
  Æthelweard's Chronicon, Wulfstan the Cantor's Narratio metrica, Apollonius
  of Tyre, Wonders of the East, the Letter of Alexander, the letter corpora
  of Alcuin and Boniface.
- **Prose supplement (25, added in the comprehensiveness expansion):** the
  West-Saxon Gospels, the Old English Rule of St Benedict, the Regularis
  Concordia, the Vita Sancti Wilfridi (Stephen of Ripon), the Passio Sancti
  Eadmundi (Abbo of Fleury), the Whitby Vita Sancti Gregorii, Tatwine's
  Aenigmata, Hwætberht's Aenigmata, Ælfric Bata's Colloquia, Bald's
  Leechbook, the Lacnunga, the Old English Herbarium, the Distichs of Cato,
  the Durham Proverbs, the Vision of Leofric, the Old English lives of St
  Margaret, St Mary of Egypt, St Giles, St Nicholas, St Euphrosyne, the
  Seven Sleepers, and St Christopher, the Old English Rule of Chrodegang,
  the Laterculus Malalianus (Theodore of Tarsus), and the Old English Gospel
  of Nicodemus.

### Validation results

- `PRAGMA integrity_check`: **ok**
- `PRAGMA foreign_key_check`: **0 violations**
- Validation script (`validate_database.py --installment 01`): **0 issues**
- Duplicate check: **0 duplicate groups**
- Test suite: **14/14 passing** (including idempotent re-import test)
- FTS5 indexes built and returning results for both `works_fts` and
  `authors_fts`

### Unresolved bibliographical issues (kept for review)

1. **Exact composition dates** remain scholarly estimates for virtually the
   entire poetic corpus (e.g. Beowulf c. 700–1025). Records store the
   accepted ranges and mark uncertainty in notes — no invented precision.
2. **Nennius attribution** — the Historia Brittonum is a composite text;
   recorded with traditional attribution and noted as such.
3. **Riddle solutions** are not encoded as data; interpretation is left to
   the description fields.
4. **Soul and Body** exists in two distinct versions (Vercelli and Exeter);
   recorded as one work entry with the two witnesses documented in
   `bibliographical_notes` — may be split into two records if scholarship
   requires.
5. **First-print dates** for several minor texts (Kentish Hymn, CCCC 201
   poems, Distichs of Cato, the saints' lives) are left null where the
   editio princeps year could not be verified; the standard modern editions
   are recorded instead in `bibliographical_notes` and `work_editions`.

### Comprehensiveness expansion (same installment)

After the initial import, the corpus was audited against the complete
Anglo-Saxon Poetic Records and the major prose canon; the gaps were filled
in a second, idempotent import (+7 authors, +48 works, +4 genres, +2
themes, +7 work editions). All validations were re-run clean afterwards.
The Old English corpus is now essentially complete: every surviving poem of
the period is represented, together with the Latin and vernacular prose of
the schools, the reform, medicine, law, and hagiography.

### Confirmation

Earlier installments: none (this is the first). Master database preserved
with backup at `database/backups/English_Literature_Master_installment_01.db`;
stable identifiers in use from this point forward.

---

## Installment 2 — Middle English Literature (c. 1100–1500)

**Status: COMPLETE** — 2026-11-03

### Scope

Middle English literature in all its forms (c. 1100–1500): the early Middle
English homiletic and devotional tradition, the romances and Breton lays,
the Alliterative Revival, Ricardian poetry, the mystery cycles and morality
plays, the English mystical writers, Lollard and anti-Lollard controversy,
the fifteenth-century Chaucerians, the Scottish Makars, and the Anglo-Latin
historical, philosophical, and scientific writing produced in England.

### Records added

| Entity | Added | Cumulative |
|---|---|---|
| Authors | 43 | 67 |
| Works | 132 | 260 |
| Anonymous works | 53 | 137 |
| Periods | 1 | 2 |
| Movements | 9 | 13 |
| Genres | 14 | 41 |
| Themes | 13 | 36 |
| Sources | 9 | 20 |
| Work–author links | 67 | 109 |
| Work editions | 69 | 88 |
| Other relationship rows | 1,272 | 2,320 |

### Authors (43)

Layamon, Orm, Robert Mannyng, Dan Michel of Northgate, John Trevisa, Richard
Rolle, Walter Hilton, Julian of Norwich, Margery Kempe, Nicholas Love, John
Wyclif, Reginald Pecock, John Gower, Geoffrey Chaucer, William Langland,
John Lydgate, Thomas Hoccleve, Thomas Usk, John Clanvowe, Thomas Malory,
William Caxton, Thomas Chestre, John Barbour, Blind Hary, Robert Henryson,
William Dunbar, James I of Scotland, Richard Holland, John Mirk, Osbern
Bokenham, John Capgrave, Geoffrey of Monmouth, William of Malmesbury, Henry
of Huntingdon, Gerald of Wales, Walter Map, John of Salisbury, Matthew
Paris, Richard de Bury, Roger Bacon, John Duns Scotus, William of Ockham,
Ranulf Higden.

### Works (132) — summary by group

- **Alliterative Revival (14):** Sir Gawain and the Green Knight, Pearl,
  Patience, Cleanness, St Erkenwald, Piers Plowman, Winner and Waster, The
  Parliament of the Three Ages, Alliterative Morte Arthure, The Destruction
  of Troy, Piers the Plowman's Creed, The Awntyrs off Arthure, The Siege of
  Jerusalem, The Buke of the Howlat.
- **Anglo-Latin historical, philosophical, and scientific writing (12):**
  Historia Regum Britanniae, Gesta Regum Anglorum, Historia Anglorum,
  Itinerarium Cambriae, Expugnatio Hibernica, De Nugis Curialium,
  Policraticus, Chronica Majora, Philobiblon, Opus Maius, Ordinatio, Summa
  Logicae.
- **Chaucer and the Ricardian court (10):** The Canterbury Tales, Troilus
  and Criseyde, The Book of the Duchess, The House of Fame, The Parliament
  of Fowls, The Legend of Good Women, Treatise on the Astrolabe, Boece, The
  Romaunt of the Rose (disputed), Chaucer's Short Poems.
- **Drama (10):** the York, Towneley, N-Town, and Chester cycles; The Castle
  of Perseverance, Mankind, Wisdom, Everyman, Croxton Play of the Sacrament,
  Digby Mary Magdalene.
- **Early Middle English (12):** The Owl and the Nightingale, Layamon's
  Brut, The Ormulum, Poema Morale, The Bestiary, Ancrene Wisse, the
  Katherine Group, Hali Meiðhad, Sawles Warde, The Wooing of Our Lord, The
  Proverbs of Alfred, The Land of Cokaygne.
- **Comic verse, fabliau, legend, and lyrics (7):** The Fox and the Wolf,
  Dame Sirith, the South English Legendary, the Harley Lyrics, The Middle
  English Lyric, Middle English Religious Lyrics, Cursor Mundi.
- **Didactic and devotional narrative (6):** Handlyng Synne, Robert
  Mannyng's Chronicle, The Ayenbite of Inwyt, Confessio Amantis, Vox
  Clamantis, Testament of Love.
- **Fifteenth-century Chaucerians and prose (11):** The Two Ways, The
  Regiment of Princes, The Series, Troy Book, The Siege of Thebes, Fall of
  Princes, The Temple of Glas, Le Morte Darthur, Recuyell of the Historyes
  of Troye, The Golden Legend, Reynard the Fox.
- **Mystical and devotional prose (14):** Incendium Amoris, Ego Dormio, The
  Form of Living, The Scale of Perfection, Epistle on the Mixed Life,
  Revelations of Divine Love, The Cloud of Unknowing, The Mirror of the
  Blessed Life of Jesus Christ, The Prick of Conscience, Dives and Pauper,
  Festial, Legends of Holy Women, The Life of St Katharine, The Book of
  Margery Kempe.
- **Wycliffite and religious controversy (5):** Wycliffite Bible, Twelve
  Conclusions of the Lollards, De Civili Dominio, The Repressor of Over Much
  Blaming of the Clergy, The Book of Faith.
- **Translation, chronicle, and practical prose (9):** Polychronicon
  (Trevisa's translation), On the Properties of Things, The Brut Chronicle,
  Mandeville's Travels, Paston Letters, Cely Letters, The Book of St Albans,
  The Forme of Cury, The Babees Book.
- **Romance and Breton lay (14):** King Horn, Havelok the Dane, Floris and
  Blancheflour, Sir Orfeo, Amis and Amiloun, Bevis of Hampton, Guy of
  Warwick, Sir Launfal, Ywain and Gawain, The Wedding of Sir Gawain and Dame
  Ragnelle, Sir Degaré, Emaré, Athelston, Lancelot of the Laik.
- **Scottish literature (8):** The Brus, The Wallace, The Kingis Quair, The
  Morall Fabillis of Esope the Phrygian, The Testament of Cresseid, Orpheus
  and Eurydice, The Tretis of the Tua Mariit Wemen and the Wedo, Lament for
  the Makaris.

### Schema extension (this installment)

Ten nullable detail columns were added to `works` (migration
`c2d3e4f5a6b7`): `composition_date_circa`, `summary`, `significance`,
`provenance_and_manuscripts`, `editions`, `modern_translations`,
`related_works`, `manuscript_locations`, `canonical_status`,
`research_notes`. The four list-typed fields are serialized as JSON text by
the import pipeline. Existing Part 1 records are unaffected.

### Validation results

- `PRAGMA integrity_check`: **ok**
- `PRAGMA foreign_key_check`: **0 violations**
- Validation script (`validate_database.py --installment 02`): **0 issues**
- Duplicate check: **0 duplicate groups**
- Test suite: **14/14 passing** (including idempotent re-import test)
- Import re-run idempotent: 0 warnings, no duplicates created

### Attribution notes

Works of traditional attribution with no author link (e.g. the Wycliffite
Bible, The Owl and the Nightingale, The Proverbs of Alfred, The Book of St
Albans) carry `attributed` status and the ascription is documented in
`attribution_notes`; no invented authorship. Disputed attributions (The
Romaunt of the Rose, The Prick of Conscience) and collaborative texts (the
four cycles, the Paston and Cely Letters) are recorded without author links,
consistent with the validator's anonymity rule.

### Confirmation

Master database preserved; installment backup at
`database/backups/English_Literature_Master_installment_02.db`. Cumulative
totals: 67 authors, 260 works (137 anonymous), 2 periods, 13 movements, 41
genres, 36 themes, 20 sources. Next installment begins only on instruction.

---

## Installment 3 — Renaissance and Early Tudor (c. 1500–1558)

**Status: COMPLETE** — 2026-11-04

### Scope

The English Renaissance from its humanist beginnings to the accession of
Elizabeth I (c. 1500–1558): Skelton and the early Tudor court poets, the
More circle and northern humanism, Wyatt and Surrey and the invention of
the English sonnet, the Reformation print war (Tyndale, More, Cranmer,
Latimer, Coverdale), the early Tudor interludes and morality plays, the
Tudor chroniclers, the first English biographies, and the Scottish
Renaissance of Douglas and Lindsay.

### Records added

| Entity | Added | Cumulative |
|---|---|---|
| Authors | 34 | 101 |
| Works | 92 | 352 |
| Anonymous works | 7 | 144 |
| Periods | 1 | 3 |
| Movements | 5 | 18 |
| Genres | 9 | 50 |
| Themes | 9 | 45 |
| Sources | 9 | 29 |
| Work–author links | 81 | 190 |
| Work editions | 38 | 126 |
| Other relationship rows | 1,678 | 3,998 |

### Authors (34)

John Skelton, Sir Thomas More, William Tyndale, Sir Thomas Wyatt, Henry
Howard Earl of Surrey, Thomas Cranmer, Hugh Latimer, John Bale, John
Heywood, Sir Thomas Elyot, Roger Ascham, Alexander Barclay, Stephen Hawes,
John Leland, Robert Fabyan, Edward Hall, Nicholas Udall, Henry Medwall,
Miles Coverdale, William Roper, John Fisher, William Baldwin, Anne Askew,
Catherine Parr, William Lily, John Colet, Thomas Linacre, John Rastell,
George Cavendish, Andrew Boorde, John Redford, Sir David Lindsay, Gavin
Douglas, Robert Whittington.

### Works (92) — summary by group

- **Early Tudor court poetry and satire (24):** Skelton's eight major
  poems (The Bowge of Courte, Philip Sparrow, The Tunning of Elinour
  Rumming, Magnificence, Speke Parrot, Colin Clout, Why Come Ye Nat to
  Courte?, The Garland of Laurel); Wyatt's Poems, Penitential Psalms, and
  Satires; Surrey's Poems and his blank-verse Aeneid II and IV; Hawes's
  Pastime of Pleasure and Example of Virtue; Barclay's Ship of Fools and
  Eclogues; Douglas's Palice of Honour, King Hart, and Eneados; Lindsay's
  Dreme, Testament of the Papyngo, and Ane Satyre of the Thrie Estaitis;
  Tottel's Miscellany.
- **Humanist prose (28):** More's Utopia, Richard III, Dialogue Concerning
  Heresies, Supplication of Souls, Dialogue of Comfort, and Epigrammata;
  Elyot's Governour, Castle of Health, and Dictionary; Ascham's Toxophilus
  and Schoolmaster; Roper's Life of More; Cavendish's Life of Wolsey;
  Baldwin's Treatise of Moral Philosophy and Beware the Cat; Leland's
  Itinerary and Cygnea Cantio; Fabyan's New Chronicles; Hall's Union of the
  Two Noble and Illustre Families; Fisher's exposition of the seven
  penitential psalms; Lily's Grammar; Colet's Aeditio; Linacre's De
  Emendata Structura and Galen translations; Rastell's Pastime of People;
  Boorde's Introduction of Knowledge and Dyetary of Health; Whittington's
  Vulgaria.
- **Early Tudor drama (21):** Medwall's Fulgens and Lucrece and Nature;
  Heywood's six interludes (The Play of the Weather, A Play of Love, The
  Pardoner and the Friar, The Four PP, Johan Johan, Witty and Witless);
  Redford's Wit and Science; Udall's Ralph Roister Doister; Rastell's Four
  Elements and the attributed Gentleness and Nobility; and the anonymous
  and attributed plays Gammer Gurton's Needle, Respublica, Godly Queen
  Hester, Jacob and Esau, Nice Wanton, Lusty Juventus, Calisto and Melebea,
  Hickscorner, and the Interlude of Youth.
- **Reformation literature (19):** Tyndale's New Testament, Pentateuch,
  Obedience of a Christian Man, Parable of the Wicked Mammon, Practice of
  Prelates, and Answer unto More; Cranmer's Book of Common Prayer (1549),
  Book of Homilies, and Defence of the Sacrament; Latimer's Sermon of the
  Plough and Sermons before Edward VI; Coverdale's Bible, Great Bible, and
  Goostly Psalmes; Askew's Examinations; Parr's Prayers or Meditations and
  Lamentation of a Sinner; Bale's King Johan and Chief Promises of God.

### Validation results

- `PRAGMA integrity_check`: **ok**
- `PRAGMA foreign_key_check`: **0 violations**
- Validation script (`validate_database.py --installment 03`): **0 issues**
- Duplicate check: **0 duplicate groups**
- Test suite: **14/14 passing** (including idempotent re-import test)
- Import re-run idempotent: 0 warnings, no duplicates created

### Attribution notes

The attributed plays (Gentleness and Nobility, Gammer Gurton's Needle,
Lusty Juventus, Beware the Cat) carry `attributed` status with the
ascription documented in `attribution_notes` and no author links,
consistent with the validator's anonymity rule; the seven anonymous plays
are recorded without author links. Collaborative compilations (Tottel's
Miscellany, the Book of Homilies, the authorized Lily's Grammar) are
recorded under their compiler or chief author with the collaboration noted.
Translation records use `translator` and `editor` contribution types
(Tyndale, Coverdale, Surrey's Aeneid, Douglas's Eneados, the Great Bible).

### Confirmation

Master database preserved; installment backup at
`database/backups/English_Literature_Master_installment_03.db`. Cumulative
totals: 101 authors, 352 works (144 anonymous), 3 periods, 18 movements,
50 genres, 45 themes, 29 sources. Next installment begins only on
instruction.

---

## Installments 4–10

Not yet begun. Per protocol, the next installment begins only on instruction.

| # | Period | Status |
|---|---|---|
| 2 | Middle English Literature (c. 1100–1500) | Complete |
| 3 | Renaissance and Early Tudor (c. 1500–1558) | Complete |
| 4 | Elizabethan and Jacobean (1558–1625) | Pending |
| 5 | Caroline, Commonwealth, Restoration (1625–1700) | Pending |
| 6 | Eighteenth Century and Augustan (1700–1789) | Pending |
| 7 | Romantic (c. 1789–1832) | Pending |
| 8 | Victorian (1832–1901) | Pending |
| 9 | Edwardian–Interwar (c. 1901–1945) | Pending |
| 10 | Postwar and Late Twentieth Century (1945–2000) | Pending |
