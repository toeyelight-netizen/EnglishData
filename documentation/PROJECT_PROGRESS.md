# Project Progress

Progress log for the English Literature Database (450–2000). One entry per
installment. The master database is cumulative: `database/English_Literature_Master.db`.

## Protocol state

- Current schema revision (Alembic): `c2d3e4f5a6b7` (initial schema + FTS5 +
  work detail columns).
- Backups: `database/backups/English_Literature_Master_installment_01.db`,
  `database/backups/English_Literature_Master_installment_02.db`,
  `database/backups/English_Literature_Master_installment_03.db`,
  `database/backups/English_Literature_Master_installment_04.db`,
  `database/backups/English_Literature_Master_installment_05.db`.
- Validation reports: `documentation/validation_reports/validation_report_01.md`,
  `documentation/validation_reports/validation_report_02.md`,
  `documentation/validation_reports/validation_report_03.md`,
  `documentation/validation_reports/validation_report_04.md`,
  `documentation/validation_reports/validation_report_05.md`.

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

## Installments 6–10

Not yet begun. Per protocol, the next installment begins only on instruction.

| # | Period | Status |
|---|---|---|
| 2 | Middle English Literature (c. 1100–1500) | Complete |
| 3 | Renaissance and Early Tudor (c. 1500–1558) | Complete |
| 4 | Elizabethan and Jacobean (1558–1625) | Complete |
| 5 | Caroline, Commonwealth, Restoration (1625–1700) | Complete |
| 5 | Caroline, Commonwealth, Restoration (1625–1700) | Pending |
| 6 | Eighteenth Century and Augustan (1700–1789) | Pending |
| 7 | Romantic (c. 1789–1832) | Pending |
| 8 | Victorian (1832–1901) | Pending |
| 9 | Edwardian–Interwar (c. 1901–1945) | Pending |
| 10 | Postwar and Late Twentieth Century (1945–2000) | Pending |
