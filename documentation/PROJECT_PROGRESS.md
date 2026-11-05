# Project Progress

Progress log for the English Literature Database (450–2000). One entry per
installment. The master database is cumulative: `database/English_Literature_Master.db`.

## Protocol state

- Current schema revision (Alembic): `c2d3e4f5a6b7` (initial schema + FTS5 +
  work detail columns).
- Installment snapshots: `database/English_Literature_Master_installment_07.db`
  (cumulative), with `database/backups/pre_import_07.db` as the pre-import
  recoverable backup.
- Backups: `database/backups/English_Literature_Master_installment_01.db`,
  `database/backups/English_Literature_Master_installment_02.db`,
  `database/backups/English_Literature_Master_installment_03.db`,
  `database/backups/English_Literature_Master_installment_04.db`,
  `database/backups/English_Literature_Master_installment_05.db`,
  `database/backups/pre_import_07.db`.
- Installment-07 data snapshot (the untracked JSON tree before the agents'
  file collision was fixed): `backups/data_snapshot_i07_20261105_0041.zip`.
- Validation reports: `documentation/validation_reports/validation_report_01.md`,
  `documentation/validation_reports/validation_report_02.md`,
  `documentation/validation_reports/validation_report_03.md`,
  `documentation/validation_reports/validation_report_04.md`,
  `documentation/validation_reports/validation_report_05.md`,
  `documentation/validation_reports/validation_report_06.md`,
  `documentation/validation_reports/validation_report_07.md`.

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

## Installment 4 — Elizabethan and Jacobean (1558–1625)

**Status: COMPLETE** — 2026-11-04

### Scope

English literature from the accession of Elizabeth I to the death of James I
(1558–1625): the Petrarchan sonnet vogue and the Sidney circle, Spenser's
allegorical epic, the rise of the commercial public theatre with the
University Wits and Marlowe, the whole Shakespearean canon, the Jacobean
tragedy and city comedy of Webster, Middleton, Tourneur, Marston, Dekker,
Beaumont, Fletcher, and Massinger, the metaphysical lyric of Donne, the
essayistic and philosophical prose of Bacon, the ecclesiastical and
historical prose of Hooker, Foxe, Stow, and Camden, the discovery literature
of Hakluyt, Ralegh, and Purchas, the great translations of Florio, North,
Golding, Fairfax, and Sylvester, and the first substantial body of printed
literature by women (Lanyer, Wroth, Elizabeth I).

### Records added

| Entity | Added | Cumulative |
|---|---|---|
| Authors | 48 | 149 |
| Works | 153 | 505 |
| Anonymous works | 2 | 146 |
| Periods | 1 | 4 |
| Movements | 6 | 24 |
| Genres | 13 | 63 |
| Themes | 12 | 57 |
| Sources | 8 | 37 |
| Work–author links | 160 | 350 |
| Work editions | 203 | 329 |
| Other relationship rows | 1,832 | 4,983 |

> Cumulative relationship-row totals are computed from the installment
> backups as all link-table rows except `work_authors` and `work_editions`
> (which are reported separately). On this basis the part-3 cumulative is
> 3,151; the figure of 3,998 shown in the Installment 3 table above was
> computed on a different basis and is superseded here.

### Authors (48)

Edmund Spenser, Sir Philip Sidney, Mary Sidney Herbert Countess of Pembroke,
Fulke Greville Lord Brooke, Samuel Daniel, Michael Drayton, William
Shakespeare, Christopher Marlowe, Ben Jonson, John Donne, Thomas Campion,
Sir John Davies, Thomas Kyd, John Lyly, Robert Greene, George Peele, Thomas
Nashe, George Chapman, John Webster, Thomas Middleton, Thomas Dekker, Cyril
Tourneur, John Marston, Francis Beaumont, John Fletcher, Philip Massinger,
Thomas Heywood, Francis Bacon, Richard Hooker, John Foxe, Thomas Sackville,
George Gascoigne, Thomas Deloney, Thomas Lodge, Richard Hakluyt, Sir Walter
Ralegh, John Florio, Sir Thomas North, Arthur Golding, Edward Fairfax,
Joshua Sylvester, Robert Burton, John Stow, William Camden, Samuel Purchas,
Aemilia Lanyer, Lady Mary Wroth, Queen Elizabeth I.

### Works (153) — summary by group

- **Shakespeare — plays and poems (42):** the 13 comedies (Two Gentlemen of
  Verona through Troilus and Cressida), the 10 histories (the three Henry VI
  plays, Richard III, King John, Richard II, the two Henry IV plays, Henry
  V, Henry VIII), the 10 tragedies (Titus Andronicus through Timon of
  Athens), the 5 late plays (Pericles, Cymbeline, The Winter's Tale, The
  Tempest, The Two Noble Kinsmen), and the 4 poems (Venus and Adonis, The
  Rape of Lucrece, the Sonnets, The Phoenix and the Turtle).
- **Marlowe (9):** Tamburlaine Parts 1 and 2, Doctor Faustus, The Jew of
  Malta, Edward II, The Massacre at Paris, Dido Queen of Carthage, Hero and
  Leander, and the translation of All Ovid's Elegies.
- **Jonson (9):** Every Man in His Humour, Volpone, Epicene, The Alchemist,
  Bartholomew Fair, Sejanus His Fall, The Masque of Blackness, Epigrams, and
  The Forest.
- **Donne and the metaphysical lyric (8):** Donne's Songs and Sonnets,
  Elegies, Holy Sonnets, The Anniversaries, Devotions upon Emergent
  Occasions, and Satires; Campion's A Book of Airs; Davies's Nosce Teipsum.
- **Spenser (8):** The Shepheardes Calender, The Faerie Queene, Complaints,
  Amoretti and Epithalamion, Colin Clouts Come Home Againe, Prothalamion,
  A View of the Present State of Ireland, and Fowre Hymnes.
- **Sidney and his circle (9):** The Defence of Poesy, Astrophel and Stella,
  Arcadia, The Lady of May, and The Sidney Psalter; Mary Sidney's Antonius;
  Greville's Caelica; Daniel's Delia; Drayton's Idea.
- **The University Wits and their contemporaries (17):** Kyd's The Spanish
  Tragedy; Lyly's Campaspe, Sapho and Phao, Gallathea, Endymion, and the two
  Euphues romances; Greene's Friar Bacon and Friar Bungay, James IV,
  Pandosto, and Menaphon; Peele's The Arraignment of Paris and The Old
  Wives' Tale; Nashe's Summer's Last Will and Testament, Pierce Penniless,
  The Unfortunate Traveller, and Christ's Tears over Jerusalem.
- **Other Elizabethan and Jacobean dramatists (20):** Chapman's Bussy
  D'Ambois and Eastward Ho; Webster's The White Devil and The Duchess of
  Malfi; Middleton's A Mad World My Masters, A Chaste Maid in Cheapside,
  Women Beware Women, and The Changeling; Dekker's The Shoemaker's Holiday,
  The Honest Whore Part 1, and The Witch of Edmonton; Tourneur's The
  Atheist's Tragedy and The Revenger's Tragedy; Marston's The Malcontent and
  The Dutch Courtesan; Beaumont and Fletcher's Philaster, The Maid's Tragedy,
  and The Knight of the Burning Pestle; Massinger's A New Way to Pay Old
  Debts; Heywood's A Woman Killed with Kindness.
- **Anonymous and disputed plays (3):** Arden of Faversham, A Yorkshire
  Tragedy, and Mucedorus.
- **Prose: philosophy, religion, history, and travel (19):** Bacon's Essays,
  Advancement of Learning, Novum Organum, and New Atlantis; Hooker's Of the
  Laws of Ecclesiastical Polity; Foxe's Actes and Monuments; Sackville's
  contribution to A Mirror for Magistrates; Gascoigne's The Steel Glass and
  The Adventures of Master F.J.; Deloney's Jack of Newbury and The Gentle
  Craft; Lodge's Rosalynde; Hakluyt's Principal Navigations; Ralegh's
  Discoverie of Guiana and History of the World; Burton's Anatomy of
  Melancholy; Stow's Survey of London; Camden's Britannia; Purchas's
  Hakluytus Posthumus.
- **Translations (5):** Florio's Montaigne, North's Plutarch, Golding's
  Ovid, Fairfax's Tasso, and Sylvester's Du Bartas.
- **Women writers (4):** Lanyer's Salve Deus Rex Judaeorum, Wroth's The
  Countess of Montgomery's Urania, and Elizabeth I's The Doubt of Future
  Foes and On Monsieur's Departure.

### Validation results

- `PRAGMA integrity_check`: **ok**
- `PRAGMA foreign_key_check`: **0 violations**
- Validation script (`validate_database.py --installment 04`): **0 issues**
- Duplicate check: **0 duplicate groups**
- Test suite: **14/14 passing** (including idempotent re-import test)
- Import re-run idempotent: identical counts, no duplicates created

### Attribution notes

Collaborative plays are linked to every in-database co-author with
`author` contribution type: Titus Andronicus (Shakespeare and Peele), Timon
of Athens (Shakespeare and Middleton), Henry VIII and The Two Noble Kinsmen
(Shakespeare and Fletcher), Dido Queen of Carthage (Marlowe and Nashe),
Eastward Ho (Chapman, Jonson, and Marston), The Changeling (Middleton;
Rowley is not yet in the database), The Honest Whore Part 1 (Dekker and
Middleton), The Witch of Edmonton (Dekker; Ford and Rowley not yet in the
database), The Sidney Psalter (Sidney and Mary Sidney Herbert), A Book of
Airs (Campion; Rosseter not yet in the database), and A Mirror for
Magistrates (Sackville; the other contributors are not yet in the database).
Pericles is recorded as collaborative with the Wilkins attribution documented
in `attribution_notes` only, since Wilkins is not in the database. The four
works of uncertain authorship — Arden of Faversham and Mucedorus
(`anonymous`), A Yorkshire Tragedy (`disputed`), and The Revenger's Tragedy
(`attributed`, printed anonymously and now generally assigned to Middleton)
— carry no author links, consistent with the validator's anonymity rule and
the precedent of Gammer Gurton's Needle. Translations and compilations use
`translator` and `editor` contribution types (Marlowe's Ovid, Mary Sidney's
Antonius, Florio, North, Golding, Fairfax, Sylvester, Hakluyt, Purchas).

### Confirmation

Master database preserved; installment backup at
`database/backups/English_Literature_Master_installment_04.db`. Cumulative
totals: 149 authors, 505 works (146 anonymous), 4 periods, 24 movements, 63
genres, 57 themes, 37 sources. Next installment begins only on instruction.

---

## Installment 5 — Caroline, Commonwealth, and Restoration Literature (1625–1700)

**Status: COMPLETE** — 2026-11-04

### Scope

English literature from the personal rule of Charles I through the Revolution
Settlement (1625–1700). Coverage: Caroline court and private-circle drama after
the closure of the public theatres; Cavalier and late metaphysical verse; the
Commonwealth and Interregnum corpus, above all Milton; the radical prose of the
civil-war decades (Levellers, Diggers, Harringtonian republicanism); the new
science and the Royal Society; Anglican and Latitudinarian devotional prose;
diary, letter and memoir writing; the re-opened Restoration stage, the heroic
drama and the comedy of manners; Restoration and Exclusion Crisis verse satire;
the first professional woman writers; and the philosophical and political
treatises of Hobbes and Locke that close the period.

### Records added

| Entity | Added | Cumulative |
|---|---|---|
| Authors | 65 | 214 |
| Works | 205 | 710 |
| Anonymous works | 0 | 146 |
| Periods | 1 | 5 |
| Movements | 10 | 34 |
| Genres | 12 | 75 |
| Themes | 12 | 69 |
| Sources | 15 | 52 |
| Work–author links | 206 | 556 |
| Work editions | 351 | 680 |
| Other relationship rows | 3,421 | 8,573 |

Total relationship rows created for this installment: 3,978 (including the
206 work–author links and 351 editions).

### Period added (1)

**Caroline, Commonwealth, and Restoration Period** (1625–1700).

### Movements (10 new; 11 linked to the period)

Cavalier Poetry; The Caroline Theatre; Commonwealth and Interregnum Literature;
The Restoration Theatre; Comedy of Manners; Heroic Drama; The Cambridge
Platonists; The New Science and the Royal Society; Civil War Radicalism: The
Levellers and the Diggers; The Anglican and Latitudinarian Divines. The
existing movement **Metaphysical Poetry** is also linked to the new period, so
that Herbert, Vaughan, Crashaw and Traherne sit correctly on both sides of
1625.

### Genres (12)

Cavalier Lyric; Comedy of Manners; Heroic Play; Dramatic Opera and Semi-Opera;
Closet Drama; Spiritual Autobiography; Diary and Journal; Mock-Heroic and Verse
Satire; Pindaric Ode; Prose Fiction and the Early Novel; Character Writing;
Verse Epistle.

### Themes (12)

Civil War, regicide, and the trial of the king; Liberty of conscience and
religious toleration; Country retirement and the estate poem; Wit, libertinism,
and the rake; Restoration politics: party, succession, and Exclusion; The New
Science and experimental philosophy; Carpe diem and the pleasures of the
present; Female authorship and the woman writer; Slavery, empire, and the
Atlantic world; Faith, grace, and the pilgrim's journey; The city and urban
life; Reason, faith, and the limits of understanding.

### Authors (65)

- **Poets (22):** John Milton, John Dryden, George Herbert, Henry Vaughan,
  Richard Crashaw, Thomas Traherne, Abraham Cowley, Andrew Marvell, Edmund
  Waller, Richard Lovelace, Thomas Carew, Sir John Suckling, Sir John Denham,
  Robert Herrick, Samuel Butler, John Wilmot, Earl of Rochester, Charles
  Sackville, Earl of Dorset, Matthew Prior, Katherine Philips, Anne Finch,
  Countess of Winchilsea, Anne Bradstreet, Francis Quarles.
- **Dramatists (15):** James Shirley, John Ford, Richard Brome, Sir William
  Davenant, William Wycherley, William Congreve, George Etherege, Thomas
  Shadwell, Thomas Otway, Aphra Behn, Thomas Southerne, John Vanbrugh, George
  Farquhar, Colley Cibber, Nathaniel Lee.
- **Prose, divinity, science and philosophy (28):** Sir Thomas Browne, Izaak
  Walton, Jeremy Taylor, John Bunyan, Thomas Fuller, John Aubrey, Dorothy
  Osborne, Sir William Temple, Samuel Pepys, John Evelyn, Thomas Hobbes, John
  Locke, Robert Boyle, Margaret Cavendish, Duchess of Newcastle, Anne Conway,
  Mary Astell, Joseph Glanvill, John Wilkins, Thomas Sprat, Robert Hooke,
  Henry More, Ralph Cudworth, James Harrington, Gerrard Winstanley, John
  Lilburne, John Tillotson, Gilbert Burnet, Lucy Hutchinson.

### Works (205) — summary by group

- **Milton (15):** the early poems (On the Morning of Christ's Nativity,
  L'Allegro and Il Penseroso, Comus, Lycidas, Milton's Sonnets); the major
  poems (Paradise Lost, Paradise Regained, Samson Agonistes); and the prose
  (Areopagitica, The Doctrine and Discipline of Divorce, Of Education, The
  Tenure of Kings and Magistrates, Eikonoklastes, Defensio Pro Populo
  Anglicano, The Ready and Easy Way to Establish a Free Commonwealth).
- **Metaphysical and religious lyric (12):** Herbert's The Temple and A Priest
  to the Temple; Vaughan's Silex Scintillans, Olor Iscanus and Pindarique
  Odes; Crashaw's Steps to the Temple, Carmen Deo Nostro and Roman Forgeries;
  Traherne's Centuries of Thankfulness and Davideis; Cowley's The Mistress and
  Essays in Verse and Prose.
- **Cavalier, court and women's verse (23):** Marvell's An Horatian Ode upon
  Cromwell's Return from Ireland, Upon Appleton House, To His Coy Mistress,
  The Garden, The Rehearsal Transpros'd and An Account of the Growth of Popery
  and Arbitrary Government in England; Lovelace's Lucasta; Suckling's Fragmenta
  Aurea; Carew's Carew's Poems; Waller's Waller's Poems and Cooper's Hill;
  Denham's The Sophy; Herrick's Hesperides; Katherine Philips's Poems by the
  Most Deservedly Admired Mrs Katherine Philips; Bradstreet's The Tenth Muse
  Lately Sprung Up in America and Contemplations; Quarles's Emblems; Finch's A
  Nocturnal Reverie; Rochester's The Spleen; Prior's The City Mouse and
  Country Mouse; Philips's Pompey.
- **Restoration and Exclusion verse (21):** Dryden's Astraea Redux, Annus
  Mirabilis, Absalom and Achitophel, Absalom and Achitophel Part II, Mac
  Flecknoe, The Medal, Religio Laici, The Hind and the Panther, To the Memory
  of Mr. Oldham, Threnodia Augustalis, A Song for St. Cecilia's Day 1687,
  Alexander's Feast, Eleonora, Fables Ancient and Modern, The Works of Virgil
  and The Satires of Juvenalis and Persius; Butler's Hudibras and Miscellaneous
  Thoughts; Rochester's A Satire Against Reason and Mankind and Poems on
  Several Occasions; Dorset's Songs and Poems.
- **Caroline and Commonwealth drama (28):** Shirley's The Wedding, The Changes,
  Hyde Park, The Lady of Pleasure, The Antipodes, The Traitor and The
  Cardinal; Ford's 'Tis Pity She's a Whore, The Broken Heart, Love's Sacrifice,
  Perkin Warbeck and The Lady's Trial; Brome's The Northern Lass, A Jovial
  Crew, The Sparagus Garden and The Covent Garden Weeded; Davenant's Love and
  Honour, The Platonic Lovers, Salmacida Spolia, The Siege of Rhodes and The
  Playhouse to Be Let; five late Massinger plays and two late Jonson plays
  (additive links to the existing authors).
- **Restoration tragedy, heroic drama and theory (23):** Dryden's The Wild
  Gallant, The Indian Queen, An Essay of Dramatic Poesy, The Tempest, The
  Conquest of Granada, Marriage à la Mode, Aureng-zebe, All for Love, Don
  Sebastian and King Arthur; Etherege's The Comical Revenge, She Would if She
  Could and The Man of Mode; Wycherley's Love in a Wood, The Gentleman
  Dancing-Master, The Country Wife and The Plain Dealer; Shadwell's Epsom
  Wells, The Virtuoso and The Squire of Alsatia; Lee's The Rival Queens,
  Sophonisba and Lucius Junius Brutus.
- **Restoration comedy and women's drama (26):** Congreve's The Old Bachelor,
  The Double Dealer, Love for Love, The Mourning Bride and The Way of the
  World; Otway's The Orphan, Caius Marius and Venice Preserv'd; Behn's The
  Forc'd Marriage, The Rover, The Rover Part II, Abdelazer, The Widow Ranter,
  Love-Letters, Oroonoko, The Fair Jilt and Poems upon Several Occasions;
  Southerne's The Fatal Marriage and Oroonoko adaptation; Vanbrugh's The
  Relapse and The Provoked Wife; Farquhar's Love and a Bottle, The Constant
  Couple, The Recruiting Officer and The Beaux' Stratagem; Cibber's Love's Last
  Shift.
- **Prose, diary, letter and life-writing (21):** Browne's Religio Medici,
  Pseudodoxia Epidemica, Hydriotaphia, The Garden of Cyrus and Christian
  Morals; Walton's The Compleat Angler and Lives; Taylor's Holy Living and Holy
  Dying; Fuller's The Holy State and The Worthies of England; Aubrey's Brief
  Lives; Osborne's Letters; Temple's Observations upon the United Provinces and
  Of Ancient and Modern Learning; Pepys's Diary; Evelyn's Diary and Sylva;
  Hutchinson's Memoirs, Order and Disorder and her Lucretius translation.
- **Philosophy, politics, science and heterodoxy (31):** Hobbes's Leviathan,
  De Cive, The Elements of Law and Behemoth; Locke's Essay Concerning Human
  Understanding, Two Treatises of Government, Letter Concerning Toleration,
  Some Thoughts Concerning Education and The Reasonableness of Christianity;
  Boyle's The Sceptical Chymist and New Experiments Physico-Mechanical;
  Cavendish's Blazing-World, Observations upon Experimental Philosophy and
  Plays; Conway's The Principles; Astell's A Serious Proposal to the Ladies and
  Some Reflections upon Marriage; Glanvill's The Vanity of Dogmatizing;
  Wilkins's Discovery of a World in the Moone and Essay towards a Real
  Character; Sprat's History of the Royal-Society; Hooke's Micrographia;
  More's Enthusiasmus Triumphatus; Cudworth's The True Intellectual System;
  Harrington's The Commonwealth of Oceana; Winstanley's The Law of Freedom and
  The New Law of Righteousness; Lilburne's England's Birth-Right Justified;
  Tillotson's Sermons; Burnet's History of the Reformation and History of His
  Own Time.
- **Bunyan and nonconformist prose (5):** Grace Abounding to the Chief of
  Sinners; The Pilgrim's Progress Parts I and II; The Life and Death of Mr.
  Badman; The Holy War.

### Sources (15)

Scholarly editions (Kerrigan/Rumrich/Fallon's Milton, Nigel Smith's Marvell,
Helen Wilcox's Herbert, Latham/Matthews's Pepys, Malcolm's Hobbes, Keeble's
Bunyan, Kinsley's Dryden, Patrides's Browne, Janet Todd's Behn); period
anthologies (Grierson's Metaphysical Lyrics, Kissing the Rod, Norton Volume C);
and reference works (Cambridge Companions to English Literature 1650–1740, to
Milton, and to Restoration Drama).

### Validation results

- `PRAGMA integrity_check`: **ok**
- `PRAGMA foreign_key_check`: **0 violations**
- Validation script (`validate_database.py --installment 05`): **0 issues**
- Duplicate check: **0 duplicate groups**
- Test suite: **14/14 passing** (including idempotent re-import test)
- Import re-run idempotent: identical counts, no duplicates created

### Attribution notes

Two works are linked to more than one author already in the database: Dryden's
adaptation of The Tempest (Dryden and Sir William Davenant) and the second part
of Absalom and Achitophel (Dryden and Tate — Tate is not yet in the database, so
the collaboration is recorded in `attribution_notes` only). The same rule keeps
The Indian Queen (Dryden and Sir Robert Howard), 'Tis Pity She's a Whore
collaborators, the Charles Montagu share in The City Mouse and Country Mouse,
and Charles Cotton's share in The Compleat Angler inside `attribution_notes`
rather than as links. Philip Massinger's five late plays and Ben Jonson's two
Caroline plays are attached additively to the authors created in Installment 4;
their earlier records are unchanged. No anonymous work in this installment
carries an author link, and the period-consistency rule (±50 years) accepts the
1620s Caroline drafts and the 1706–1707 Farquhar comedies within the 1625–1700
period.

### Confirmation

Master database preserved; installment backup at
`database/backups/English_Literature_Master_installment_05.db`. Cumulative
totals: 214 authors, 710 works (146 anonymous), 5 periods, 34 movements, 75
genres, 69 themes, 52 sources. Next installment begins only on instruction.

---

## Installment 6 — Augustan and Eighteenth-Century Literature (1700–1789)

Completed 2026-11-04.

### Scope

The long eighteenth century from the reign of Anne to the threshold of the
Romantic period: Augustan verse satire and the Scribleran circle, the periodical
press, the rise of the novel, neoclassical criticism and the rules,
topographical and graveyard poetry, sentimentalism, the English and Scottish
Enlightenments, the Bluestockings and women's letters, the Evangelical revival
and its hymnody, the regenerated London theatre, primitivism and the Ossianic
vogue, abolitionist writing, and the early Gothic.

### Records added

| Entity | This installment | Cumulative |
|---|---|---|
| Periods | +1 | 6 |
| Movements | +15 | 49 |
| Genres | +27 | 102 |
| Themes | +22 | 91 |
| Sources | +25 | 77 |
| Authors | +96 | 310 |
| Works | +351 | 1061 |

Relationship links added: 364 `work_authors`, 351 `work_periods`, 351
`work_genres`, 351 `work_themes`, 347 `work_movements`, 96 each of
`author_genres`, `author_movements` and `author_themes`, 83 `author_influences`,
1 `period_movements`, 96 `author_sources`, 351 `work_sources`, 15
`movement_sources` and 351 `work_editions`.

### Period added (1)

- Augustan and Eighteenth-Century Period (1700–1789)

### Movements (15 new, all linked to the period)

Abolitionist and Anti-Slavery Writing; Augustan Satire and the Scriblerans;
Garrick and the Regenerated London Theatre; Gothic and the Literature of
Terror; Neoclassical Criticism and the Rules; Primitivism, the Bardic
Revival and Ossian; Sentimentalism and the Culture of Feeling; The
Bluestockings and Women's Letters; The English Enlightenment and Deist
Controversy; The Evangelical Revival and Hymn Writing; The Graveyard School
and Preromantic Meditation; The Rise of the English Novel; The Scottish
Enlightenment; The Spectator and Periodical Journalism; Topographical and
Estate Poetry

### Genres (27 new)

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

### Themes (22 new)

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

### Authors (96 new)

  Adam Ferguson, Adam Smith, Alexander Pope, Anna Laetitia Barbauld, Anthony
  Ashley Cooper, Third Earl of Shaftesbury, Anthony Collins, Bernard
  Mandeville, Charles Wesley, Charlotte Lennox, Christopher Smart, Clara
  Reeve, Daniel Defoe, David Hartley, David Hume, Delarivier Manley, Edward
  Gibbon, Edward Moore, Edward Young, Eliza Haywood, Elizabeth Carter,
  Elizabeth Montagu, Elizabeth Rowe, Erasmus Darwin, Frances Burney, Francis
  Hutcheson, George Berkeley, George Whitefield, Gilbert White, Granville
  Sharp, Hannah Cowley, Hannah More, Henry Fielding, Henry Home, Lord Kames,
  Hester Chapone, Horace Walpole, Hugh Blair, Hugh Kelly, Isaac Watts, James
  Beattie, James Boswell, James Hervey, James Macpherson, James Ramsay,
  James Thomson, Jeremy Bentham, John Arbuthnot, John Dennis, John Dyer,
  John Gay, John Home, John Millar, John Newton, John Toland, John Wesley,
  Jonathan Swift, Joseph Addison, Joseph Butler, Joseph Priestley, Lady Mary
  Wortley Montagu, Laurence Sterne, Mark Akenside, Mary Chudleigh, Mary
  Wollstonecraft, Matthew Tindal, Nicholas Rowe, Olaudah Equiano, Oliver
  Goldsmith, Ottobah Cugoano, Philip Doddridge, Richard Blackmore, Richard
  Brinsley Sheridan, Richard Price, Richard Steele, Robert Blair, Robert
  Burns, Samuel Johnson, Samuel Richardson, Sarah Fielding, Susanna
  Centlivre, Thomas Chatterton, Thomas Gray, Thomas Paine, Thomas Parnell,
  Thomas Percy, Thomas Reid, Thomas Warton, Tobias Smollett, William
  Beckford, William Blackstone, William Collins, William Cowper, William
  Law, William Mason, William Paley, William Robertson, William Shenstone

Six further authors already held records from Installments 4 and 5 and were
linked additively rather than re-created: Matthew Prior, Colley Cibber, John
Vanbrugh, William Congreve, Thomas Southerne and Mary Astell. In all, 102
distinct author records are linked to this installment's works.

### Works (351) — grouped by movement

-   Abolitionist and Anti-Slavery Writing — 8 record(s). Examples recorded in
  this installment: *A Representation of the Injustice and Dangerous
  Tendency of Tolerating Slavery; or, of Admitting the Least Claim of
  Private Property in the Persons of Men, in England*, *An Inquiry into the
  Effects of Putting a Stop to the African Slave Trade, and of Granting
  Liberty to the Slaves in the British Sugar Colonies*, *Polly*, *Taxation
  Tyrannical; or, The Colonies and Britain Compared*, *The Commonwealth of
  Slaves*.
-   Augustan Satire and the Scriblerans — 56 record(s). Examples recorded in
  this installment: *A Modest Defence of Publick Stews*, *A Modest
  Proposal*, *A Political Romance*, *A Project for the Advancement of
  Learning*, *A Tale of a Tub*.
-   Garrick and the Regenerated London Theatre — 17 record(s). Examples
  recorded in this installment: *A Political Romance*, *Apology for the Life
  of Colley Cibber*, *Douglas*, *False Delicacy*, *Jane Shore*.
-   Gothic and the Literature of Terror — 15 record(s). Examples recorded in
  this installment: *A Description of the Villa of Mr. Horace Walpole*, *Tam
  o' Shanter*, *The Adventures of Ferdinand Count Fathom*, *The Bard*, *The
  Brothers*.
-   Neoclassical Criticism and the Rules — 68 record(s). Examples recorded in
  this installment: *A Dictionary of the English Language*, *A Plan of a
  Dictionary of the English Language*, *A Project for the Advancement of
  Learning*, *A Proposal for Correcting, Improving and Ascertaining the
  English Tongue*, *An Essay on Criticism*.
-   Primitivism, the Bardic Revival and Ossian — 34 record(s). Examples
  recorded in this installment: *A Man's a Man for A' That*, *A Red, Red
  Rose*, *Auld Lang Syne*, *Bohoursky*, *Caractacus: A Dramatic Poem*.
-   Sentimentalism and the Culture of Feeling — 82 record(s). Examples
  recorded in this installment: *A Journey Through France and Italy*, *A
  Red, Red Rose*, *A Sentimental Journey Through France and Italy*, *Account
  of Corsica*, *Amelia*.
-   The Bluestockings and Women's Letters — 20 record(s). Examples recorded in
  this installment: *All the Works of Epictetus*, *An Essay on the Learning
  and Genius of Shakespeare*, *An Essay to Defend the Women's Cause*,
  *Cecilia; or, Memoirs of an Heiress*, *Evelina; or, A Young Lady's
  Introduction to the World*.
-   The English Enlightenment and Deist Controversy — 65 record(s). Examples
  recorded in this installment: *A Discourse of the Grounds and Reasons of
  the Christian Religion*, *A Discourse on the Love of Our Country*, *A
  Fragment on Government*, *A Jubilate Agno*, *A Modest Defence of Publick
  Stews*.
-   The Evangelical Revival and Hymn Writing — 31 record(s). Examples recorded
  in this installment: *A Collection of Hymns for the Use of the People
  Called Methodists*, *A Collection of Psalms and Hymns*, *A Jubilate Agno*,
  *A Serious Call to a Devout and Holy Life*, *A Short Account of God's
  Dealings with the Reverend Mr. George Whitefield*.
-   The Graveyard School and Preromantic Meditation — 24 record(s). Examples
  recorded in this installment: *A Paraphrase upon Part of the Book of Job*,
  *Autumn*, *Bohoursky*, *Death and Doctor Hornbook*, *Elegy Written in a
  Country Church-Yard*.
-   The Rise of the English Novel — 46 record(s). Examples recorded in this
  installment: *A General History of the Pyrates*, *A Journal of the Plague
  Year*, *A Sentimental Journey Through France and Italy*, *Amelia*,
  *Cecilia; or, Memoirs of an Heiress*.
-   The Scottish Enlightenment — 33 record(s). Examples recorded in this
  installment: *A Man's a Man for A' That*, *A Short Introduction to Moral
  Philosophy*, *A Treatise of Human Nature*, *Account of Corsica*, *An
  Enquiry Concerning Human Understanding*.
-   The Spectator and Periodical Journalism — 23 record(s). Examples recorded
  in this installment: *A Journal of a Voyage to Lisbon*, *An Enquiry into
  the Causes of the Late Increase of Robbers*, *An Enquiry into the Present
  State of Polite Learning in Europe*, *Essays Moral and Political*, *Essays
  on Various Subjects, in Prose and Verse*.
-   Topographical and Estate Poetry — 20 record(s). Examples recorded in this
  installment: *A Description of the Villa of Mr. Horace Walpole*, *Alfred*,
  *Autumn*, *Britannia (Thomson)*, *Conversation*.

Authorship status: 1 attributed, 13 collaborative, 5 disputed, 332 single. Research status: 320 complete, 31 partial. Original language: 326 English; 11 Scots; 4 English (rendered from Gaelic); 3 English (translated from French); 2 English (translated from Greek); 2 English (translated from Latin); 2 English (translated from Norse); 1 English (translated from Latin and other languages).

### Sources (25 new)

Scholarly editions and series (the Twickenham *Pope*; Swift's *Critical,
Scholastic, and Variorum Edition*; the Yale *Johnson*; Birkbeck Hill's *Boswell*;
the Clarendon *Hume*; Bury's *Gibbon*; Kinsley's *Gray, Collins and Goldsmith*;
Scott's *Burns*; *The Poems of Ossian and Related Works*; the four-volume
*Spectator*; the seven-volume *Wollstonecraft*); criticism and anthology
(Norton Volume C as the teaching spine, Norton Volume D for the preromantic
figures, the Cambridge Companions to eighteenth-century poetry, the novel, Pope,
Johnson and Gothic fiction, *The Novel: An Anthology of Criticism and Practice,
1700-1800*, Watt's *The Rise of the Novel*, the *Encyclopedia of the
Enlightenment*, *Essays in the History of Ideas*); and the primary philosophical
texts (Adam Smith's *Wealth of Nations* and *Theory of Moral Sentiments*, Hume's
*Treatise*, Gibbon's *Decline and Fall*, Equiano's *Interesting Narrative*,
Wollstonecraft, and the ODNB).

### Validation results

- `PRAGMA integrity_check`: **ok**
- `PRAGMA foreign_key_check`: **0 violations**
- Validation script (`validate_database.py --installment 06`): **0 issues**
- Duplicate check: **0 duplicate groups**
- Test suite: **14/14 passing** (including the idempotent re-import test)
- Import re-run idempotent: identical counts, no duplicates created

### Attribution notes

9 works carry more than one linked author:

- *A Collection of Psalms and Hymns* — John Wesley, Charles Wesley
- *Hymns and Sacred Poems* — John Wesley, Charles Wesley
- *Olney Hymns* — William Cowper, John Newton
- *Peri Bathous, the Art of Sinking in Poetry* — Alexander Pope, Jonathan Swift, John Gay, Thomas Parnell
- *The Drummer* — Richard Steele, Joseph Addison
- *The Guardian Papers* — Richard Steele, Joseph Addison
- *The Provok'd Husband* — John Vanbrugh, Colley Cibber
- *The Spectator and Tatler Papers (Addison)* — Joseph Addison, Richard Steele
- *The Works of Mr. Martinus Scriblerus* — John Arbuthnot, Alexander Pope, Jonathan Swift, Thomas Parnell

Where a collaborator has no record in the database, the collaboration is stated
inside `attribution_notes` rather than invented as a link; A General History of the Pyrates is entered as
`disputed` and left unlinked for the same reason. 31 of the 351 works are
`research_status: partial`, where a composition or first-print date rests on
scholarly convention rather than on evidence recorded in the field.

Two corrections were made during review. Boswell's *Life of Samuel Johnson* is
dated to its first edition of 1791 (Prospectus 1790; revised second edition
1793), not 1793. James Thomson's poem is entered as `Britannia (Thomson)` to
keep it distinct from Camden's Latin *Britannia* already held from Installment
3, following the parenthetical-disambiguation convention used elsewhere in the
corpus. All date fields are stored as strings, with `c. NNNN` for approximate
dates, in conformity with the `VARCHAR` columns of the `works` table.

### Confirmation

Master database preserved; installment backup at
`database/backups/English_Literature_Master_installment_06.db`. Cumulative
totals: 310 authors, 1061 works (146 anonymous), 6 periods, 49 movements, 102
genres, 91 themes, 77 sources.

---

## Installment 7 — Romantic Period, British and American (c. 1789–1832)

**Status: COMPLETE** — 2026-11-05

### Scope

The British and American Romantic period. Coverage: the Lyrical Ballads
generation and the Lake poets, Byron and the Byronic revolt, Shelley and
radical Romanticism, Keats and the sensuous ode, the Regency popular-verse and
annual public, Labouring-class and village poetry, the Gothic and the
literature of terror, the philosophical fiction of the Godwin circle, the
essay and review, the Romantic sonnet revival, topographical and estate verse,
the drama of the Regency stage, and the transatlantic strand: Charles Brockden
Brown and the American Gothic, Cooper and the romance of forest and sea, the
Knickerbocker group and the American sketch, Bryant and the American nature
lyric, the early American republic and its letters, and abolitionist and
anti-slavery writing in both nations.

### Newly added by this installment

| Entity | Added | Cumulative |
|---|---|---|
| Authors | +108 | 418 |
| Works | +394 | 1455 |
| Periods | +1 (Romantic Period) | 7 |
| Movements | +17 | 66 |
| Genres | +24 | 126 |
| Themes | +24 | 115 |
| Sources | +167 | 244 |
| Editions recorded | +1401 | 2432 |
| `work_sources` links | +2515 | 6280 |
| `author_sources` links | +598 | 1771 |

### Verification gates run at completion

- `scripts/audit_installment.py 07` — 0 ERRORs before import (394 works in 16
  batch files, 108 authors in 21 files, 167 sources, 394 map entries).
- `scripts/installment_toolkit.py check 07 b*` — CLEAN for every batch.
- `scripts/import_data.py` run twice: byte-identical row counts on the second
  run, so the import is idempotent and created no duplicates.
- `scripts/validate_database.py --installment 07` — 0 issues
  (`documentation/validation_reports/validation_report_07.md`).
- `scripts/check_duplicates.py` — 0 potential duplicate groups.
- `python -m unittest discover -s tests` — 14 tests, OK.
- Installment backup preserved at
  `database/backups/pre_import_07.db`; the cumulative snapshot is
  `database/English_Literature_Master_installment_07.db`.

### Method notes and corrections made during research

- Sources are attached by strand. A period-wide reference (the ODNB) stands
  behind every work; the Norton *English Literature* Romantic volume and the
  Cambridge Companion attach to British works, the Norton *American
  Literature* volume to American ones. Nothing is stapled to a work whose
  subject it is not — the earlier behaviour of attaching every "general"
  reference to every work was removed, and the average is 6.38 sources per
  work against installment 6's 5.8.
- *Zofloya; or, The Moor* (1806) is Charlotte Dacre's, not Charlotte Smith's;
  an attribution to Smith was caught in verification and corrected.
- Morse's *The American Universal Geography* is dated to the verified 1793
  first edition, with the 1789 *American Geography* antecedent recorded in
  the bibliographical note rather than as a separate work.
- Five works first published anonymously but securely attributed (Byron's
  *English Bards and Scotch Reviewers*, Poe's *Tamerlane and Other Poems*,
  Malthus's *Essay on the Principle of Population*, Owen's *A New View of
  Society*, Croker's *Fairy Legends*) are recorded as `single`, with the
  original anonymity carried in `attribution_notes`; recording them as
  `anonymous` while naming an author contradicts the schema's meaning.
- Two movement rows carried `defining_characteristics` as a JSON list, which
  aborted the SQL INSERT. Fixed, and `audit_installment.py` now rejects any
  list in a taxonomy column and any map that names an author for a work
  recorded as anonymous, so neither defect can reach an import again.

### Deferred canonical gaps (deliberate, recorded so nothing is lost)

Research on installment 7 was closed on instruction to move on. These titles
are absent from the corpus and are the standing to-do list for a later
installment-7 supplement; they must be added as new records, never by
rewriting what is already imported:

*Lamia, Isabella, The Eve of St. Agnes, and Other Poems* (Keats, 1820);
*The Rights of Man* (Paine, 1791); *Plays on the Passions* and *The De Monfort*
(Baillie); *The Quarterly Review* (1809, ed. Gifford); *Blackwood's Edinburgh
Magazine* (1817); *The Liberal* (1822, Hunt and Byron); *Letters from France*
(Helen Maria Williams — no author record yet); *Zofloya* as a work (Dacre's
author record exists); *Adeline Mowbray* (Opie); *Glenarvon* (Lamb);
*Bracebridge Hall*, *A Tour on the Prairies*, *The Journal of Major John
André*, *Moral Pieces* (Irving); *The Deerslayer* (Cooper, 1841 — belongs to
installment 8); *The Coquette* (Foster — no author record yet); *The Power of
Sympathy* (Brown — no author record yet); *The Vision of Columbus* (Barlow);
*Hobomok* and *An Appeal* (Child); *Androborus* (Dunlap — no author record
yet); *The Frontier*; *The Battle of Blenheim* (Southey); *Letters from the
Federal Farmer*; *The Rights of All*; and the sweep's two unattributed
entries, *Milton: a Poem* and *Nature: An Essay*, which must be verified or
dropped. Author records that exist but claim no work: Andrew Bell, John
Hamilton Reynolds, Thomas Babington Macaulay (all essentially installment-8
careers).

---

## Installments 8–10

Under way. Per protocol, the next installment begins only on instruction.
Scope agreed for these installments: the English and British canon **and** a
distinct American strand, with broader Anglophone and postcolonial writing out
of scope.

| # | Period | Status |
|---|---|---|
| 2 | Middle English Literature (c. 1100–1500) | Complete |
| 3 | Renaissance and Early Tudor (c. 1500–1558) | Complete |
| 4 | Elizabethan and Jacobean (1558–1625) | Complete |
| 5 | Caroline, Commonwealth, Restoration (1625–1700) | Complete |
| 6 | Eighteenth Century and Augustan (1700–1789) | Complete |
| 7 | Romantic, British and American (c. 1789–1832) | Complete |
| 8 | Victorian and American nineteenth century (1832–1901) | Pending |
| 9 | Edwardian–Interwar, British and American (1901–1945) | Pending |
| 10 | Postwar and Late Twentieth Century, British and American (1945–2000) | Pending |
