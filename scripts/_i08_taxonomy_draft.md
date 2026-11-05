# INSTALLMENT 8 — TAXONOMY RESEARCH DRAFT
## The Victorian Period and the 19th-Century American Strand, 1832–1901

Scope: the British/English canon **plus** the American canon, c. 1832–1901. No
broader postcolonial Anglophone literatures (Indian, Caribbean, African,
Canadian and Irish-revival writing are deferred; where a writer works in English
and is claimed by two traditions, the British or American row carries them and
the deferral is stated in the row).

Read for style and collision control: `scripts/_i07_taxonomy_names.txt`
(installment-7 movement/genre/theme names plus the cumulative DB vocabularies —
nothing below duplicates a string in it); `data/periods/installment_06_periods.json`,
`data/movements/installment_06_movements.json`, `data/genres/installment_06_genres.json`,
`data/themes/installment_06_themes.json` and the installment-7 equivalents (field
shapes copied, no keys invented); `documentation/DATA_DICTIONARY.md` and
`documentation/DATABASE_SCHEMA.md` (columns of `periods`, `movements`, `genres`,
`themes`; junction tables `period_movements`, `movement_sources`, `work_movements`,
`work_genres`, `work_themes`); `data/relationships/installment_06_relationships_authors.json`
(payload shape for the cross-links in §5).

---

## 0. ROW SHAPES (taken verbatim from installments 6 and 7 — no invented keys)

| row type | keys, in this order |
|---|---|
| period | `name`, `start_year`, `end_year`, `description`, `historical_context`, `literary_characteristics` |
| movement | `name`, `start_year`, `end_year`, `description`, `historical_context`, `aesthetic_principles`, `defining_characteristics`, `historical_significance` |
| genre | `name`, `description`, `historical_development` |
| theme | `name`, `description` |

`genres.parent_genre_id` and `themes.parent_theme_id` are left unset here; the
candidate parents are noted against each renamed row in §7 (COLLISION CHECK).

### Evidence rules applied to this draft
- No writer's date, title or edition is invented. Where a title or its first
  year is not certain, the writer's body of work is described instead (e.g.
  "the New England village tales of Mary E. Freeman", never a guess at a title).
- Nothing published after 1901 anchors a row. *Peter Pan* (1904), *The Dynasts*
  (1903–08), *The Hound of the Baskervilles* (1901–02), *Heart of Darkness* in
  book form (1902, though Blackwood's printed it in 1899), *If It Die* (1925) and
  the *Spoon River Anthology* (1915) are named only as outside the window.
- Nothing earlier than 1830 is presented as Victorian. Tennyson's *Poems,
  chiefly Lyrical* (1830) is the legitimate hinge; Keble's *The Christian Year*
  (1827), the keepsakes of the 1820s and Cooper's forest and sea romances
  (carried by installment 7) are antecedents only.

---

## 1. PERIOD — 1 row

- name: `"Victorian Period (1832–1901)"`

```
name: Victorian Period (1832–1901)
start_year: 1832
end_year: 1901
```

**description** — Literature written in British and American English between the
first British Reform Act and the death of Queen Victoria. On the British side:
the lyric and the long poem of Tennyson, Browning, Arthur Hugh Clough, Matthew
Arnold and the Pre-Raphaelites; the serial novel from Dickens through the
sensation fiction of the 1860s to the problem fiction of the 1890s; the prose of
Carlyle, Ruskin, Newman, Pater and Arnold; and the stage from domestic drama and
burlesque to the problem play and Wilde. On the American side:
Transcendentalism; the dark romance of Hawthorne and Melville; the poetry of
Whitman and Dickinson; the slave narrative and the plantation tradition; the
tall tale and the local-colour school; the realist programme of Howells and
James; Twain's vernacular; and the naturalism of Crane, Norris and Chopin at the
century's close.

**historical_context** — The period opens with the Great Reform Act (1832) and
closes with Victoria's death in January 1901. Between: the New Poor Law (1834);
Chartism, the People's Charter of 1838 and the petitions of 1842 and 1848; the
Ten Hours Act (1847); the repeal of the Corn Laws (1846); the Second and Third
Reform Acts (1867, 1884); the Elementary Education Act (1870); and the rise of
organised labour and of the socialist societies of the 1880s. An expanding print
economy — railway bookstalls, the weekly and monthly part-issue, the
three-volume library, the penny periodical and after 1870 the cheap reissue —
creates the first mass reading public, with a rising proportion of women readers
and women writers. Empire supplies subject and capital: the Indian Mutiny of
1857–58 and the Crown settlement afterwards, the Crimean War (1854–56), the
reconquest of the Sudan (1898), the Diamond and Golden Jubilees (1887, 1897), and
after 1884 the East African partition; emigration and the colonial exhibitions
make London an imperial city. In the United States: Indian Removal after the
1830 act; the Mexican War (1846–48) and the gold rush of 1849; the Fugitive
Slave Law (1850); the Civil War (1861–65), Emancipation and the Reconstruction
amendments; the withdrawal of federal troops in 1877 and the loss of
Reconstruction; the transcontinental railroad (completed 1869), the great rail
and labour conflicts of the 1870s, 1886 and 1894; the census declaration of a
settled frontier line in the early 1890s; mass immigration from the 1880s; and
the Spanish-American War and the overseas settlements of 1898. International
copyright arrangements of the 1890s turn the two literary cultures into one
market.

**literary_characteristics** — A literature of large public prose and of
conscience: moral, religious and social argument carried in the quarterly
review, the sermon, the lecture and the treatise; a claimed "high seriousness"
for poetry after Arnold's phrase, matched by an equally deliberate
counter-programme of pleasure, surface and style in aesthetic and decadent
writing from the 1860s to the 1890s. Formally: the serial novel with its
sustained suspense; the dramatic monologue and the masked lyric; the revived
sonnet and the elegiac sequence; the blank-verse tale and the idyll; the problem
play and the sensation drama; in America the talk, the sketch, the yarn and the
long improvisation of Whitman's free line, answered by Dickinson's compressed
stanza. Forms are increasingly named from their publication venue — the magazine
story, the part-issue, the recited dialect poem, the "bestseller" — and the
period closes with the little magazines and the lyric anthologies that will make
the next century's repertoires.

---

## 2. MOVEMENTS — 21 rows (12 British, 9 American)

### 2A. BRITISH MOVEMENTS (12)

**M1**
- name: `"Victorian High Seriousness and the Public Poet"`
```
start_year: 1830
end_year: 1885
```
**description** — The mid-century conception of poetry as a public moral office,
held by Tennyson, Browning, Arthur Hugh Clough and Matthew Arnold and named
critically by Arnold's phrase "high seriousness". Its opening act is Tennyson's
*Poems, chiefly Lyrical* (1830), the hinge between the Romantic and the
Victorian lyric, followed by *The Princess* (1847), *In Memoriam A.H.H.*
(privately printed 1849, title page 1850), *Maud* (1855) and the Arthurian
*Idylls of the King* from 1859. Browning answered from inside with the monologues
of *Dramatic Lyrics* (1844) and *Men and Women* (1855); Arnold gave up verse for
criticism after *Empedocles on Aetna* (1852).
**historical_context** — The age asked its poets what it believed: Lyell's
*Principles of Geology* (vols. 1–3, 1830–33), the anonymous *Vestiges of the
Natural History of Creation* (1844) and the Tractarian controversy opened the
questions, and the factory town and the Crimean War supplied the subjects. Public
mourning attached verse to state occasions, and Tennyson's installation as poet
laureate in 1850 made the poet an official functionary; "The Charge of the Light
Brigade" (1854) is the mode's most quoted public poem.
**aesthetic_principles** — Poetry as a criticism of life; the high subject and
the severe diction; moral seriousness joined to finished execution; the poet as
the voice of an age to itself; art as solace and as discipline, never as licence.
**defining_characteristics** — The short lyric of perfected music; the long
meditative or narrative poem in blank verse; the dramatic monologue as ethical
probe; the medieval or classical retelling used as modern argument; the motto,
the title-page epigraph and the explanatory prose paratext.
**historical_significance** — It fixed the Victorian canonical hierarchy —
Tennyson and Browning as the age's poets, Arnold as its judge — and set the terms
on which aesthetic, decadent and modernist writers later defined themselves
against it.

**M2**
- name: `"Tractarian Prose and the Oxford Movement"`
```
start_year: 1833
end_year: 1890
```
**description** — The religious prose made by and against the Oxford Movement:
the *Tracts for the Times* (1833–41), the sermons and pamphlet controversies of
Newman, Pusey and Keble, and the long Victorian argument over authority, ritual
and conscience which their prose opened. Newman's *Tract 90* (1845) drove him to
Rome and produced two decades later the *Apologia Pro Vita Sua* (1864), the
period's most quoted religious autobiography; his earlier novels *Loss and Gain*
(1848) and *Callista* belong to the same traffic between doctrine and narrative.
**historical_context** — The movement is conventionally dated from Keble's assize
sermon "National Apostasy" (4 July 1833); behind it lie the government's
retrenchment of the Irish Church and the church-rate agitation, before it Keble's
hymn volume of 1827. Its consequences run through the ecclesiastical troubles of
the later 1840s, the Gorham judgment (1850), the *Essays and Reviews* controversy
and the Privy Council decision of 1864, and the ritualist prosecutions of the
1870s.
**aesthetic_principles** — The *via media*; reserve in religious speech; the
conscience as the court of appeal; patristic and catholic authority; the Church
as a visible body with a claim upon literature and upon the reader's feelings.
**defining_characteristics** — The tract, the sermon, the controversial pamphlet
and the open letter; the periodic prose of reasoning about belief; hymn and
daily-office devotion; autobiography written as legal defence; the novel of
religious conversion.
**historical_significance** — It gave Victorian prose its model of the religious
argument and, through the Broad Church and ritualist controversies, much of its
vocabulary of doubt and belief; Newman's prose remains the standard case of
Victorian religious style.

**M3**
- name: `"Carlyle and the Hero-Worship Lecture"`
```
start_year: 1830
end_year: 1881
```
**description** — The prophetic, coinage-hurrying prose of Thomas Carlyle and the
school of "carlylism" it created: *Sartor Resartus* (serialised in *Fraser's
Magazine* 1833–34, in book form 1838), *The French Revolution* (1837),
*Chartism* (1839), *On Heroes, Hero-Worship, and the Heroic in History* (from the
1840 course of lectures), *Past and Present* (1843), the *Occasional Discourse on
the Nigger Question* (1849) and the *Latter-Day Pamphlets* (1850). It is the
movement in which the Victorian lecture and the moral jeremiad become literary
forms, and through which Ruskin, Kingsley, Froude and Arnold learned their prose.
**historical_context** — Written for the Edinburgh and London magazines and
delivered to mechanics' institutes and to paid audiences in London and Edinburgh,
it answers the Chartist platform, the Irish question and the commercial
depression of the late 1840s. James Froude carries the school on: the *Short
Studies on Great Subjects* from 1868 and the *Life of Carlyle* (1882); Mill's
*Autobiography* (published 1873) is the great rival answer to it.
**aesthetic_principles** — Literature as moral force; the "everlasting Yea"
against the "everlasting No"; the gospel of work; history written as dramatic
present; hero-worship as the substance of history; contempt for the "cash nexus"
and for parliamentary talk.
**defining_characteristics** — The coined compound, the apostrophe, the
exclamation and the broken periodic sentence; the lecture and the pamphlet; the
jeremiad on "captains of industry"; the quarrel with laissez-faire; the
apostrophised dead hero.
**historical_significance** — It supplied the Victorian language of
hero-worship, of the "condition-of-England question" and of industrial duty, and
made the prophetic prose lecture a permanent literary institution on both sides
of the Atlantic.

**M4**
- name: `"Chartism and the Condition-of-England Novel"`
```
start_year: 1837
end_year: 1860
```
**description** — The fiction of the 1840s and 1850s written out of the "two
nations" panic and the Chartist agitations, which made wage labour, the lock-out,
the hand-loom weaver and the starving town subjects of serious prose fiction:
Gaskell's *Mary Barton: A Tale of Manchester Life* (1848) and *North and South*
(serialised 1854–55, in books 1855), Disraeli's *Coningsby* (1844) and *Sybil, or
The Two Nations* (1845), Kingsley's *Yeast* (1848) and *Alton Locke* (1850), and
Dickens's *Hard Times* (serialised 1854) as the mode's late satiric reckoning.
**historical_context** — Carlyle's phrase names the problem these novels answer.
Their occasions are the distress and the "Plug Plot" of 1842, the Chartist
petition of 1848, the cholera years, the ten-hours and factory legislation, and
the Christian-socialist and cooperative agitation carried in London by Kingsley
and F. D. Maurice; Gaskell writes from Manchester Unitarian circles, Disraeli
from Young England.
**aesthetic_principles** — Fiction as social evidence; sympathy compelled
across class lines; the indictment of the wage relation; the industrial sermon
addressed to the reader rather than to a party.
**defining_characteristics** — The mill town and the tenement; the strike, the
lock-out and the riot; the dying child and the consumption of the operative; the
Irish navvy in the English city; the reconciliation plot that marries capital to
labour.
**historical_significance** — It created the industrial novel as a permanent
branch of English fiction and forced the language of class, wage and factory
into the mid-century mainstream.

**M5**
- name: `"Sensation Fiction and the Serial Plot"`
```
start_year: 1859
end_year: 1868
```
**description** — The popular realism of the late 1850s and 1860s, built from
stolen inheritances, bigamy, poison, asylum confinement and disguised identity,
and set not in Apennine castles but in modern English houses: Collins's *The
Woman in White* (serialised 1859–60, three volumes 1860), *No Name* (1862),
*Armadale* (1866) and *The Moonstone* (1868); Braddon's *Lady Audley's Secret*
(1862) and *Aurora Floyd* (1863); Mrs Henry Wood's *East Lynne* (1861).
**historical_context** — The mode flourished in the cheap weeklies and the
library triple-decker and moved at once to the stage in the sensation drama of
the 1860s and 1870s. Collins, who began as Dickens's contributor and
collaborator (*The Frozen Deep*, 1857, and *No Thoroughfare*, 1867), is its
technical centre, while Braddon and Wood edited the magazines that carried it;
the expanding railway bookstall and circulating-library trade made its audience.
**aesthetic_principles** — A single "sensation" prolonged through a plot; the
modern domestic world as the true scene of terror; probability produced by
documentary effect; the reader's detective interest as the engine of the book.
**defining_characteristics** — Competing first-person witness statements; diary,
letter, report, will and medico-legal paper inserted as evidence; the woman whose
reputation or property is the plot's stake; the private asylum, the train, the
lime-light and the laudanum cup.
**historical_significance** — Sensation fiction created the modern plot-driven
bestseller, professionalised women's popular authorship, and supplied the
narrative machinery from which the detective story was separated.

**M6**
- name: `"Pre-Raphaelitism and the Truth to Nature"`
```
start_year: 1848
end_year: 1882
```
**description** — The programme of the *Germ* circle (1848–50) — Dante Gabriel
Rossetti, William Holman Hunt and John Everett Millais, with Coventry Patmore,
and at one remove William Morris, Edward Burne-Jones and Christina Rossetti —
which demanded "complete sincerity and thorough study of Nature" and made the
poem a picture. Its literary course runs from Rossetti's early Botticelli tale
*Hand and Soul* (written 1849–50, printed in the early 1860s) through Morris's
*The Defence of Guenevere* (1858) and *The Earthly Paradise* (1868–70) to
Rossetti's *Poems* (1870) and the sonnet-and-picture body of *The House of
Life* (published 1881).
**historical_context** — Ruskin's defence of the brotherhood after the controversy
over Millais's domestic *Christ in the House of His Parents* gave the movement
its patron and its doctrine; the single monthly issues of *The Germ* (1850) mark
its formal beginning; the decorative firm founded in 1861 and the later Kelmscott
Press carry it into the making of books. Christina Rossetti's *Goblin Market and
Other Poems* (1862) belongs to the same circle and partly repudiates it.
**aesthetic_principles** — "Truth to Nature"; serious subjects treated with
literal fidelity and dense detail; colour and the concrete image preferred to
generalisation; the poem and the picture as one object; the medieval and
Arthurian as living rather than antiquarian material.
**defining_characteristics** — The pictorial narrative poem; the sonnet written
to or on a picture and the emblazoned title-page; ballad stanza with archaising
diction; the decorated and illustrated book; the insistent named woman with her
hair, flowers and sleeves.
**historical_significance** — It fused literary and visual practice, gave
Victorian poetry its intense imagistic diction, and through Morris and Pater
leads directly into aestheticism and the arts-and-crafts book.

**M7**
- name: `"Ruskin and the Political Economy of Art"`
```
start_year: 1843
end_year: 1900
```
**description** — Ruskin's prose campaign which read painting, architecture and
wages as one moral system: *Modern Painters* (vol. I, 1843), *The Seven Lamps of
Architecture* (1849), *The Stones of Venice* (1851–53, with its chapter "The
Nature of Gothic"), *Sesame and Lilies* (1860), *Unto This Last* (serialised in
the *Cornhill Magazine*, 1860) and *The Storm-Cloud of the Nineteenth Century*
(1884).
**historical_context** — The Great Exhibition of 1851 and its language of
improvement, the Gothic Revival churches and offices built after Pugin published
*Contrasts* in 1841, the Lancashire and Sheffield wage conflicts, and Ruskin's
Oxford professorship held from 1870 give the writing its occasions; the Whistler
libel action and verdict of 1877–78 are its public crisis.
**aesthetic_principles** — The "life" and the "law" of a material; no great art
without a great society; the moral value of ornament and of the workman's
pleasure in his work; wealth defined as the maintenance of lives rather than as
accumulation; accurate sight as a duty.
**defining_characteristics** — The long descriptive paragraph that turns
observation into argument; the architectural and typological reading of a
surface; the lecture, the household manual and the open letter on wages; the
tract against political economy.
**historical_significance** — It made art criticism a social science, created the
ethical case against industrial capitalism that William Morris inherited, and
formed the period's standard prose of description from Turner to the Venice lagune.

**M8**
- name: `"Arnold and the Criticism of Culture"`
```
start_year: 1853
end_year: 1888
```
**description** — Matthew Arnold's programme of criticism and the school it
founded: the *Essays in Criticism* of 1865 and their second series of 1888,
which contains "The Study of Poetry" and its touchstone test, with *Culture and
Anarchy* (1869), *Literature and Dogma* (1873) and *Discourses in America*
(1885). His earlier verse is the poetic arm of the same position: "Sohrab and
Rustum" and "The Scholar-Gipsy" (1853), "Stanzas from the Grande Chartreuse"
(published 1855) and "Thyrsis" (1866).
**historical_context** — It is written for the reading public made by the
elementary codes, the school boards and the university reforms of the 1870s;
Arnold speaks as a schools inspector and as the poet who turned to criticism.
Its rivals are Froude's and Carlyle's prophetic prose and, at the century's
close, Pater's hedonist critique.
**aesthetic_principles** — Criticism as a disinterested pursuit of "the best that
has been known and thought"; culture as the study of perfection and not as
aesthetic materialism or as machinery; the touchstone and "high seriousness";
the authority of style and diction.
**defining_characteristics** — The critical essay of ideas addressed to a general
public; the lecture; the controversial prose against "Philistines" and the
"Populace"; the ironised personification of national types; the phrase made
technical vocabulary.
**historical_significance** — It established the idea of "culture" and the modern
discipline of literary criticism, and left the terms — "high seriousness",
"touchstone", "Hebraism and Hellenism", "sweetness and light" — through which
English literature is still taught.

**M9**
- name: `"Muscular Christianity and the Schoolboy Tale of Empire"`
```
start_year: 1849
end_year: 1889
```
**description** — The masculine, Christian and athletic programme of the late
1840s and 1850s associated with Thomas Hughes, Charles Kingsley and F. D.
Maurice's Working Men's College (founded 1854), and the boys' fiction it
produced: Hughes's *Tom Brown's School Days* (1857) and *Tom Brown at Oxford*
(1861), Kingsley's *Westward Ho!* (1855) and Ballantyne's *The Coral Island*
(1858). Its late-century descendants are the boys' empire story — Haggard's
*King Solomon's Mines* (1885) — and Kipling's *Kim* (1901), the last book
inside the period's boundary.
**historical_context** — Public-school reform and the Clarendon enquiries, the
"muscular" answer to over-civilisation and to the cholera town, the Volunteer
Force raised in the invasion scare of 1859–60, the emigration societies and the
mission field form its social setting; the Christian Social Union and the social
gospel of the 1880s carry its religious argument forward.
**aesthetic_principles** — The trained body in the service of God and country;
courage, fairness and the fourth-form code as moral categories; character built
by games, fagging and rough-rider discipline; the Anglo-Saxon as a historical
instrument.
**defining_characteristics** — The school story with its bully and its
cricket match; the island or frontier tale in which boys govern themselves; the
seafaring romance of English destiny; the cadet and the games story; the
muscular sermon addressed to the young man.
**historical_significance** — It created the British school story and the boys'
imperial romance, two of the century's most durable popular forms, and supplied
the still-familiar moral language of "muscular Christianity".

**M10**
- name: `"The Dramatic Monologue and the Masked Voice"`
```
start_year: 1841
end_year: 1889
```
**description** — The Victorian perfection of the poem in which a speaker
unwittingly reveals a character not the poet's own, and its extension into the
dramatic lyric. Its landmarks are Browning's *Pippa Passes* (1841), *Dramatic
Lyrics* (1844), *Dramatic Romances and Lyrics* (1845) and the collected *Dramatic
Works* (from 1868), *Men and Women* (1855) and *The Ring and the Book*
(1868–69), with Clough's ironic narratives and meditations of the 1850s and
Arnold's masked interlocutors.
**historical_context** — This is a poetry for readers rather than for audiences:
the annual, the two-volume collected edition and the review are its publication
world. Elizabeth Barrett Browning belongs to the same culture of the
constructed speaking self, with *Sonnets from the Portuguese* (1850) and the
verse-novel *Aurora Leigh* (1856).
**aesthetic_principles** — The masked speaker and the half-undisclosed
listener; involuntary self-revelation as the means of ethical judgment; the
refusal of the confident first person; character built out of diction, syntax and
the wrong word chosen.
**defining_characteristics** — A single utterance before a silent auditor; the
historical or literary "case"; parenthetical self-correction and the quoted
other; irony achieved without commentary; the lyric whose speaker is explicitly
not the poet.
**historical_significance** — It is the Victorian gift to modern poetry: the
technique of the constructed speaker, transmitted through Swinburne and Hardy to
the twentieth century, and its critical vocabulary is still ours.

**M11**
- name: `"Aestheticism and the Decadent Decade"`
```
start_year: 1866
end_year: 1897
```
**description** — The doctrine of the autonomous artefact, "art for art's sake",
as it took institutional shape in Britain from the mid-1860s to the 1890s:
Swinburne's *Poems and Ballads* (1866); Pater's Renaissance studies of 1873 with
their famous conclusion, then *Marius the Epicurean* (1885), *Imaginary
Portraits* (1887) and *Appreciation* (1889); Wilde's *The Picture of Dorian
Gray* (in *Lippincott's Magazine* 1890, with the prefatory manifesto in the book
of 1891), his comedies of the early 1890s and *The Ballad of Reading Gaol*
(1898); and the little magazines from *The Yellow Book* (1894–97) to *The Savoy*
(1896). Arthur Symons's *The Symbolist Movement in Literature* (1899) gives it a
criticism.
**historical_context** — The Oxford and London aesthetic debate of the 1870s,
artistic dress and the decorated house, the Whistler trial, and the parody of the
movement on the comic stage all precede it; the trials of 1895 and the reaction
after them end it. Wilde's *De Profundis*, written in prison and published after
1901, falls outside the window.
**aesthetic_principles** — Art for art's sake; style as the moral act of prose;
"the hard, gemlike flame"; the critic's impression and the paradox; the
independence of form from doctrine; the refinement of sensation as an end.
**defining_characteristics** — The little magazine and the decorated book; the
essay of the paradox and the dialogue on art; the prose poem and the decadent
verse of refrain and echo; the society comedy that argues by wit; the illustrated
cover and the black-bordered yellow book.
**historical_significance** — It separated the modern idea of literary art from
civic and moral instruction, created the small press and the coterie magazine,
and made the stylish critic a public role.

**M12**
- name: `"The New Woman and the Fin-de-Siècle Problem Novel"`
```
start_year: 1883
end_year: 1899
```
**description** — The late-Victorian fiction and polemic which turned the "woman
question" into a plot and a market: Schreiner's *The Story of an African Farm*
(1883), Meredith's *Diana of the Crossways* (1885), Gissing's *New Grub Street*
(1891) and *The Odd Women* (1893), the "marriage strike" and free-love
controversy of the mid-1890s, Grant Allen's *The Woman Who Did* (1895), and the
marriage-market and fallen-man fiction of Thomas Hardy, George Moore and
Murray.
**historical_context** — Its conditions are the Married Women's Property Act
(1882), the repeal campaign against the Contagious Diseases Acts and the protest
mobilisation of 1885–86, the college and medical-school openings for women, the
divorce court and its published cases, and the feminist journalism of the 1890s;
Ibsen's problem drama reaches the English stage and the English novel in
translations and adaptations during the 1890s.
**aesthetic_principles** — Fiction as a laboratory of conduct and a piece of
evidence; the marriage plot deliberately broken open; the argumentative novel
whose thesis its own characters state; plain statement of the facts of sex
against the older reticence.
**defining_characteristics** — The railway, the typewriter, the college and the
furnished lodging; the educated wage-earning heroine; the free-love quarrel and
the "new man"; the novel which answers another novel; the problem play as its
stage equivalent.
**historical_significance** — It forced marriage law, work, the double standard
and the biology of sex into English fiction as topics of public argument, and
created the "New Woman" debate that ran into the Edwardian suffrage movement.

### 2B. AMERICAN MOVEMENTS (9)

**M13**
- name: `"Transcendentalism and the Concord Lyceum"`
```
start_year: 1836
end_year: 1860
```
**description** — The revolt inside American Unitarianism, centred on Concord and
Boston and conducted in the lecture hall: Emerson's *Nature* (1836), the address
"The American Scholar" (delivered 1837), "Self-Reliance" and "The Over-Soul" in
*Essays: Second Series* (1844), Thoreau's *Walden* (1854) and his essay on civil
disobedience (published 1849), and the pages of *The Dial* (1840–44), edited
successively by Margaret Fuller and by Ripley. Bronson Alcott's school and
community experiments, and the fiction of his daughters in the 1860s and 1870s,
belong to its orbit.
**historical_context** — The Unitarian controversy over the miracles and the
nature of God, the lyceum and lecture circuit that carried the new prose to
Western and New England towns, the Transcendental club formed in 1836, Brook Farm
and the Fourierist communities of the late 1840s, and the anti-slavery platform
on which Parker and Phillips Garrison spoke, are its occasions; Carlyle and
German Idealism reach it through the *Edinburgh Review* and the *Dial*.
**aesthetic_principles** — Intuition and the "Over-Soul" above miracle and
institution; the infinite in every human breast; self-reliance and the
unwritten law; nature as a system of symbols; the American mind released from
European book-learning.
**defining_characteristics** — The prose lecture, the address and the aphoristic
essay; the journal of deliberate observation; the manifesto of intellectual
independence; the tract for the reform society; the idealist theory of language.
**historical_significance** — It created the first home-grown American
intellectual idiom, made the lecture a national literary form, and set the terms
— self-reliance, nonconformity, the scholar's obligation — on which later
American prose argued.

**M14**
- name: `"Dark Romance and the Puritan Inheritance"`
```
start_year: 1830
end_year: 1860
```
**description** — Hawthorne and Melville, the American romance that inherits and
interrogates New England Calvinism. Hawthorne's course runs from *Twice-Told
Tales* (1837) and *Mosses from an Old Manse* (1846) through *The Scarlet Letter*
(1850), *The House of the Seven Gables* (1851), *The Blithedale Romance* (1852)
to *The Marble Faun* (1860); Melville's from *Typee* (1846) and *White-Jacket*
(1850) through *Moby-Dick* (1851), *Pierre* (1852), the "Encantadas" pieces and
*Benito Cereno* (in *Putnam's* 1855–56), *The Piazza Tales* (1856) and
*The Confidence-Man* (1857).
**historical_context** — The decay of the Calvinist theology that still governed
American moral vocabulary, the custom-house and surveyorships that gave both
writers an income, the reform and communal experiments of the 1840s, the
fugitive-slave crisis that produced *Benito Cereno*, and the publishing
difficulties of the American London trade.
**aesthetic_principles** — The Romance, claiming a "truth of the human heart"
above photographic realism; the allegorical situation retained inside modern
prose; suspicion of benevolent systems and of the reformer's optimism; the
mutable interpretation and the sceptical question.
**defining_characteristics** — The moral hieroglyphic and the emblazoned
tapestry; the meditative, unreliable or interrogating narrator; the ship, the
custom house and the old manse as framing spaces; the secret sin and the public
pillory; the philosophical whale.
**historical_significance** — It supplied the central nineteenth-century American
canon, and its self-conscious theory of the Romance is the source of the
American distinction between romance and realism.

**M15**
- name: `"The Second American Renaissance and the Whitman-Dickinson Lyric"`
```
start_year: 1855
end_year: 1891
```
**description** — The lyric revolution that made American verse modern:
Whitman's *Leaves of Grass* (1855, reissued and enlarged through the edition he
was preparing when he died in 1891), the war sequences of *Drum-Taps* (1865) and
the Lincoln elegies, and the poems of Emily Dickinson — more than a thousand
composed in the 1860s, first published in a book only in 1890, with a second
series in 1891 and her *Letters* in 1894.
**historical_context** — Its occasion is the national crisis: the first edition
of 1855, the war years when Dickinson wrote most fast, and the post-bellum
consolidation of a national canon in which the recital circuit, the magazine and
the school and family anthology fixed the public poets.
**aesthetic_principles** — The free line, the catalog and the long breath as a
democratic form; the compressed stanza, the internal rhyme and slant as an
interior form; poetry as the adequate speech of an age and a continent; the
body and the soul without hierarchy.
**defining_characteristics** — The long improvisation and the anaphoric roll; the
hymn-metre poem turned against itself; the war lyric and the funeral elegy; the
titleless poem known by its first line; the editorial controversy over the
uncertain text.
**historical_significance** — It is the founding event of modern American poetry,
and its two opposed lines — Whitman's expansive free line and Dickinson's
contracted ballad stanza — remain the available American choices.

**M16**
- name: `"Mark Twain and the Vernacular Performance"`
```
start_year: 1865
end_year: 1894
```
**description** — The making of a written American voice out of spoken American
performance: the "jumping frog" tale first published in 1865, *Innocents Abroad*
(1869), *Roughing It* (1872), *The Adventures of Tom Sawyer* (1876),
*Life on the Mississippi* (1883), *Adventures of Huckleberry Finn* (published
1884 in Boston and 1885 in Hartford) and the race-and-law tragedy of
*Pudd'nhead Wilson* (1894).
**historical_context** — The Mississippi pilot's and cub's craft, the Virginia
City and Comstock silver booms, the special correspondent's trip, the Hartford
household and the failure of his own publishing house, and the financial crash
of 1894: all conditions of a literature made out of reporting, lecturing and
story-telling to a live audience.
**aesthetic_principles** — Talk as the medium of prose; the local dialect
recorded and graded; the tall-tale breath, the joke and the "stretch"; the
vernacular eye turned on the civilized forms — the Romance, the travel-book,
the boy's story.
**defining_characteristics** — The first-person yarn with its frame of hearth and
platform; the mock-travel book; the boy's adventure; the dialect sketch
of race and frontier justice; the burlesque quotation from the older Romances.
**historical_significance** — It established the American vernacular as a
literary medium, and the post-1884 Huck remains the reference point for every
claim about an authentic American style.

**M17**
- name: `"American Realism and the Howells Program"`
```
start_year: 1871
end_year: 1895
```
**description** — The post-bellum school that demanded of fiction "the
essentials of veracity", and its theory: Howells's *Venetian Life* (1866),
*A Modern Instance* (1882), *The Rise of Silas Lapham* (1885), *A Hazard of New
Fortunes* (1890), *The Landlord at Lion's Head* (1897) and *Criticism and
Fiction* (1891), alongside Henry James's American fictions — *The American*
(1877), *Daisy Miller* (1878–79), *The Portrait of a Lady* (1881) and, at the
century's close, *The Turn of the Screw* (1898).
**historical_context** — The post-war marriage of New York and Boston publishing,
*The Atlantic Monthly* (from 1857) and the great monthlies as its organ, the
rise of the professional editor and of the metropolitan novel of manners, and
the transatlantic circulation that made the two literatures one field.
**aesthetic_principles** — The homely and unlovely realities of common American
life made a fit subject for art; the refusal of the sensational plot; the moral
seriousness of the drawing-room, the office and the board of direction; a large,
free and generous dealing with things as they are.
**defining_characteristics** — The domestic and business novel of ordinary
experience; the tale of the invisible power of money and manners; the
international theme of American innocence before Europe; the editor-critic as a
literary figure.
**historical_significance** — It supplied the period's own name for its mature
fiction — "realism" — and the label, with all its later disputes, still
organises the account of American literature after the Civil War.

**M18**
- name: `"Local Colour and the Regionalist School"`
```
start_year: 1852
end_year: 1895
```
**description** — The writing of American "sections" as scenery, speech and type:
the California stories Bret Harte published in *The Overland Monthly* from 1868,
the Vermont and New Hampshire narratives of the 1870s–1880s, the New England
village tales of Mary E. Freeman and of Mary Wilkins Freeman, the Maine coastal
tales of Sarah Orne Jewett — gathered in *The Country of the Pointed Firs*
(1896) — the Georgia black-country tales of Joel Chandler Harris, and the
Louisiana Acadian and Creole fiction of George Washington Cable and of Kate
Chopin.
**historical_context** — It is a post-Reconstruction literature of reunion, in
which sections are marketed as picturesque differences: the illustrated
monthly, the regional lecture tour, the railroad and the summer colony, the
"sectional" typology of the 1880s, and the South's literary department.
**aesthetic_principles** — The group of types and the speech of a place as the
true subject; the "local colour" of dress, dialect and topography preferred to
plot; the sketch rather than the plotted intrigue.
**defining_characteristics** — The short descriptive tale; dialect spelling and
the oral frame; the characteristic "group" of a coastal village, a mining camp or
a river settlement; the retold folktale; the sentimental-ironic treatment of the
disappearing type.
**historical_significance** — It established the American short story as a
regional form and made dialect, and then the "section", the technical ground of
American fiction from Harris to the 1920s.

**M19**
- name: `"American Naturalism and the Determinist Tragedy"`
```
start_year: 1891
end_year: 1901
```
**description** — The American naturalist school of the 1890s, which read
character as the product of heredity, environment and money: Crane's *Maggie: A
Girl of the Streets* (1893) and *The Red Badge of Courage* (serialised 1894, in
books 1895); Norris's *McTeague* (1899), with *Vandover* privately printed in
the mid-1890s; Chopin's *The Awakening* (1899); and Paul Laurence Dunbar's
poems and prose of the 1890s.
**historical_context** — The doctrine is an Americaned Darwin and Spencer; its
social scene is the great city, the strike and the depressed labour market of
the 1890s; its publication venue is the mass monthly, the ten-cent edition, the
little magazine and the New York and Chicago Bohemia.
**aesthetic_principles** — Man read as a function of heredity, environment and
the passions; the case history and the clinical eye; the refusal of the reward
plot; the brute within.
**defining_characteristics** — The case-study novel; the crowd, the machine and
the mine; the instinctual body and its defeat; the compressed war and city tale;
the frank treatment of sex, labour and the colour line.
**historical_significance** — It is the first American school to define itself
in a doctrine of method, and it carried American fiction into the twentieth
century.

**M20**
- name: `"South-Western Humour and the Tall-Tale Sketch"`
```
start_year: 1833
end_year: 1885
```
**description** — The comic literature of the southern and western frontier, in
which the boast exceeds the fact: the sporting and political sketches of the
South-Western frontier newspapers and almanacs of the 1830s and 1840s — the
school later critics named the "backwoods humorists" — and the California comic
tale of the 1850s to the 1870s, in which Harte and Twain both begin.
**historical_context** — Its venues are the frontier weekly and the almanac,
the Mississippi steamboat and the mining camp, the political stump and the
platform; its audience was rural and popular, and it is the first American
literature to sell in bulk to its own lower-middle and western readers.
**aesthetic_principles** — The elaborate, matter-of-fact lie; the
one-upmanship of the boast and of the yarn told in high good humour; the
laughing, self-congratulating community.
**defining_characteristics** — The tall tale, the trick story and the comic
debate; the dialect of the sporting paper; the frame of the bar-room, camp-fire
and stump; the tall, lying hero with his horse and his rifle.
**historical_significance** — It was the first native American vernacular style,
and the technical ancestor of the sketch, the frame narrative and the tall
voice of Twain.

**M21**
- name: `"The Aesthetic Turn in 1890s America"`
```
start_year: 1880
end_year: 1901
```
**description** — "Art for art's sake" in the United States: the "artistic"
verse and criticism of the late 1870s and 1880s, including Edmund Clarence
Stedman's critical volumes and anthologies; the American little magazines of the
1890s, of which *The Chap-Book*, started in Chicago in 1894, is the most
visible; the aesthetic and decadent short story and the novel of the artist; and
the decorative book and the illustrated cover, carried across from London by
contributors to *The Yellow Book*.
**historical_context** — The American aesthetic movement arrives with the
decorative and interior-design vogue of the Gilded Age, with the Boston and New
York "art" world, and with the magazine and the little press; and it is
overlaid, and overwhelmed, by the realist, regionalist and naturalist debates.
**aesthetic_principles** — The autonomy of the art object; beauty against
instruction; the "artistic" personality; the magazine and the decorated cover
as the site of taste.
**defining_characteristics** — The little magazine; the aesthetic lyric; the
novel of the artist; the "artistic" interior and its furniture; the critical
anthology and its categories.
**historical_significance** — It created the American little magazine and
prepared the American lyric anthology and the repertoires of the 1910s and 1920s.

## 3. GENRES — 27 rows

**G1**
- name: `"Novel of Development and the Growth Story"`
- description: Extended prose fiction whose plot is the slow formation of one
  consciousness — childhood, apprenticeship, error, vocation — with education and
  marriage as its two ends.
- historical_development: The German model (Goethe's Wilhelm Meister) reaches
  English through Carlyle's *Sartor Resartus* (in books 1838) and is naturalised
  as the Victorian growth story: Dickens's *David Copperfield* (part-issue
  1849–50, the most self-consciously "educative" of his novels), Brontë's
  *Jane Eyre* (1847), Eliot's *The Mill on the Floss* (1860) and
  *Daniel Deronda* (1876), Meredith's *The Ordeal of Richard Feverel* (1859) and
  *The Egoist* (1879), and Hardy's *Jude the Obscure* (1895); in America the
  boy's adventure of Twain (1876) and Alcott's school-and-family fictions of the
  1870s, and at the century's end the deliberately frustrated development plots
  of the naturalists.

**G2**
- name: `"Sensation Novel"`
- description: The mid-Victorian domestic thriller of bigamy, forgery, poison,
  confinement and substituted identity, set in contemporary English houses and
  resolved by legal or medico-legal evidence.
- historical_development: Opened by Collins's *The Woman in White* (serialised
  1859–60) and answered in the same decade by Braddon's *Lady Audley's Secret*
  (1862), Wood's *East Lynne* (1861) and Collins's *The Moonstone* (1868); the
  mode's machinery descends from the Gothic romance of the 1790s but modernises
  its scene, and it passes into detective fiction and into the Edwardian
  thriller.

**G3**
- name: `"Industrial and Condition-of-England Novel"`
- description: Fiction that takes the mill, the wage, the strike and the
  starving town as its subject and addresses the reader as a citizen with a
  duty.
- historical_development: Named from Carlyle's "condition-of-England question";
  realised in Gaskell's *Mary Barton* (1848) and *North and South* (1855),
  Disraeli's *Sybil* (1845), Kingsley's *Alton Locke* (1850) and Dickens's
  *Hard Times* (1854); its late form is the naturalist industrial fiction of the
  1890s — Gissing's *The Nether World* (1889) and Moore's *Esther Waters*
  (1894) — and in America the railroad-labour novel.

**G4**
- name: `"Realist Novel of Common Life"`
- description: Prose fiction of probable, ordinary experience, without
  melodrama or marvel, that tests character in the everyday institutions of
  family, work and marriage.
- historical_development: The post-bellum American school named in Howells's
  criticism — *A Modern Instance* (1882), *The Rise of Silas Lapham* (1885) —
  and in James's international novels from *The American* (1877) to
  *The Portrait of a Lady* (1881); its British analogues are the domestic
  realism of Trollope and the analytic realism of Eliot.

**G5**
- name: `"Naturalist and Determinist Novel"`
- description: The case-study novel of a character explained by heredity,
  environment, appetite and money, written against the reward-and-punishment
  plot.
- historical_development: American in its institutional form in the 1890s —
  Crane's *Maggie* (1893) and *The Red Badge of Courage* (in books 1895),
  Norris's *McTeague* (1899), Chopin's *The Awakening* (1899) — and British in
  Gissing's *New Grub Street* (1891) and Moore's *Esther Waters* (1894); the
  doctrine is theorised in the reviews and little magazines of the decade.

**G6**
- name: `"New Woman and Marriage-Question Novel"`
- description: The fin-de-siècle novel built on a disputed marriage — the
  marriage strike, the wage-earning heroine, the double standard, the
  free-love quarrel and the "new man".
- historical_development: From Schreiner's *The Story of an African Farm* (1883)
  and Meredith's *Diana of the Crossways* (1885) through Gissing's
  *The Odd Women* (1893) and Allen's *The Woman Who Did* (1895) to du Maurier's
  *Trilby* (1894) and the marriage-law controversy of the decade.

**G7**
- name: `"Imperial Adventure Romance"`
- description: The plot of quest, survival, treasure and frontier discovery,
  with a small band of protagonists in an extra-European scene and a strong
  delineation of the landscape.
- historical_development: Descended from Haggard's *King Solomon's Mines* (1885)
  and the boys' stories of Ballantyne and Henty, and from Kipling's Indian and
  regimental tales; its American relative is the frontier and mining romance of
  Harte and of the Western, and its high literary form is Stevenson's romance
  of the 1880s.

**G8**
- name: `"Detective Story and the Tale of Detection"`
- description: A crime, its evidence and its solution by reasoning, with an
  amateur or professional solver and a tale of the pursuit.
- historical_development: Created by Poe's ratiocinative tales in the early
  1840s and grown out of sensation fiction in the 1860s; institutionalised in
  Collins's *The Moonstone* (1868), in the American courtroom detection of
  Anna Katharine Green's *The Leavenworth Case* (1878), and in the
  periodical short story of the 1890s, which becomes "the detective".

**G9**
- name: `"Ghost Story and Scientific Supernatural Tale"`
- description: The literary tale of a return of the dead or of a
  quasi-scientific marvel, framed as testimony and usually told at night or in
  a house.
- historical_development: The literary ghost story of the period runs from the
  Christmas tale of the 1840s and 1850s — Dickens's own ghostly Christmas books
  and the Christmas numbers he and his contributors wrote for *Household Words*
  and *All the Year Round* — through the ghostly tales of Gaskell, Braddon and
  Collins of the 1860s, to Henry James's *The Turn of the Screw* (1898) and the
  magazine tale of the 1890s; the form keeps the Gothic apparatus but moves it
  into the modern house and frames it as testimony.

**G10**
- name: `"Early Scientific Romance and Utopian Speculation"`
- description: Prose fiction in which a scientific or technological hypothesis
  is developed as a narrative, or an imaginary society is described as a
  critique of the present.
- historical_development: Prepared by the development hypothesis and by the
  "future-history" and social-surmise tales of the 1840s, and by the
  scientific romance already implicit in Darwin's and Lyell's imaginative
  scale; its principal works in this period are Butler's *Erewhon* (published
  anonymously 1872), Bellamy's *Looking Backward* (1888), Morris's *News from
  Nowhere* (1890), and Wells's *The Time Machine* (1895), *The Island of Doctor
  Moreau* (1896) and *The War of the Worlds* (1898).

**G11**
- name: `"Children's Fantasy and the Dream-Region Tale"`
- description: Narrative for or about children in which a real child enters a
  secondary or impossible world; dream and nonsense are its modes.
- historical_development: Breaks with the moralised children's book of the
  earlier century with Carroll's *Alice* (1865) and *Through the Looking-Glass*
  (1871), George Macdonald's fairy romances of the 1870s, Kingsley's
  *The Water-Babies* (1863), and in America the family fiction of Alcott (from
  the later 1860s) and the Oz books (1900); *Peter Pan* (1904) falls outside
  this period.

**G12**
- name: `"War Narrative of the Common Soldier"`
- description: The war told from the ranks — the march, the wound, the fear and
  the accidental heroism — rather than from the general or the nation.
- historical_development: Prepared by the public verse of the Crimean War —
  Tennyson's "The Charge of the Light Brigade" (1854) and the hostile
  denunciation of the campaign in the same decade — and by the war correspondence
  which made the staff and the hospital a public subject. In America it is
  created in Whitman's Civil War poems of the 1860s and in the soldier's tale of
  the post-war decades, and becomes a realist war narrative in the last years of
  the century with Crane's *The Red Badge of Courage* (serialised 1894, in
  books 1895); the South African war of 1899–1902, which fills the next
  decade's British war story, lies mostly outside this period.

**G13**
- name: `"Serial and Monthly-Part Novel"`
- description: A novel first issued in parts or in a serial column, shaped by
  the interval, the cliff-hanger, the illustration and the number of weeks of
  its run.
- historical_development: The serial column begins with the magazine miscellany
  of the 1830s and is made a high art by Dickens's monthly and weekly part-issues
  from *Pickwick Papers* (1836–37) to *Our Mutual Friend* (1864–65);
  *Household Words* (1850–59) and *All the Year Round* (1859–69) carry the
  weekly double-decker serial, Collins's *The Woman in White* (1859–60) and
  *The Moonstone* (1868) perfect the serial plot, and after 1860 the American
  monthlies — *The Atlantic Monthly*, and later *Harper's* and *Scribner's* —
  do the same work across the Atlantic.

**G14**
- name: `"Dramatic Monologue and Masked Lyric"`
- description: A poem whose speaker is a character distinct from the poet,
  overheard in an act of unintended self-revelation.
- historical_development: Established by Browning in *Dramatic Lyrics* (1844),
  *Dramatic Romances and Lyrics* (1845) and the volumes of 1846 and 1855, and
  carried to its extreme in *The Ring and the Book* (1868–69); Arnold's and
  Clough's masked meditations of the 1850s, Tennyson's soliloquies and Hardy's
  monologues of the 1890s extend it, and it is the form from which the
  twentieth century's confessional and dramatic lyrics descend.

**G15**
- name: `"Victorian Verse Drama and Revived Tragedy"`
- description: Tragedy written in verse chiefly for the reader rather than the
  manager: blank verse, an ancient, biblical or historical subject, and a modern
  moral or religious argument carried in the speeches.
- historical_development: The century's first important example is Kingsley's
  *Saint's Tragedy* (1848); Arnold's *Empedocles on Aetna* (1852) is a closet
  tragedy by intention, and its 1853 preface is the manifesto of a verse drama
  that knows it will not be acted. Clough's *Mariamne*, published in the early
  1860s, Swinburne's *Atalanta in Calydon* (1865), and Tennyson's *Queen Mary*
  (1875) and *Becket* (1884) complete the main line; the Greek revivals and the
  closets of the 1890s lead to the verse drama of the next century.

**G16**
- name: `"Problem Play and Well-Made Drama"`
- description: The play constructed as an argument about a social or moral
  problem, using — and then exposing — the machinery of the "well-made" play:
  the kept secret, the compromising letter, the delayed recognition and the
  prepared scene.
- historical_development: The French "well-made play" supplies the technique; the
  "new drama" of the 1890s supplies the argument, in Pinero's *The Second Mrs
  Tanqueray* (1893), Wilde's society comedies of the early 1890s, the problem
  plays of Henry Arthur Jones, and Shaw's first plays and his critical manifesto
  *The Quintessence of Ibsenism* (1891); the Independent Theatre's first
  experimental season of 1891 marks the institutional hour.

**G17**
- name: `"Sensation Drama and the Domestic Stage"`
- description: The theatrical equivalent of sensation fiction — the modern
  middle-class house as a scene of terror, played in realistic domestic detail
  and sustained on a long-held secret.
- historical_development: The sensation drama of the 1860s to 1880s dominated
  the West End and the touring repertoire; Collins's own stage version of *The
  Woman in White* (1871) and the long-running theatrical *East Lynne* are its
  most-copied examples, and its business of the surprise and the tableau passes
  into the melodrama of the 1890s and into the thriller of the next century.

**G18**
- name: `"Pastoral Elegy and the Mourning Sequence"`
- description: The long lyric poem of mourning for a friend or a poet, using the
  pastoral convention of shepherd, seasonal cycle and song, and the connected
  sequence of short poems built around a single death.
- historical_development: The elegiac sequence is the dominant serious form of
  the mid-century — Tennyson's *In Memoriam A.H.H.* (privately printed 1849,
  title page 1850) is its monument, with its own sub-title recording the years of
  the grief; Arnold's "Thyrsis" (1866) revives the pastoral mourning of a
  friend, and America's great elegies of the 1860s — Whitman's Lincoln poems of
  "Drum-Taps" (1865) — are the public version of the same form.

**G19**
- name: `"Sonnet Revival and Sequenced Sonnet"`
- description: The return of the sonnet to the first rank of English verse in
  the period, and its organisation into a long ordered sequence with a
  narrative, doctrinal or psychological argument.
- historical_development: The vogue begins with the Elizabethan revival of the
  1830s and matures in Elizabeth Barrett Browning's *Sonnets from the Portuguese*
  (1850), in the sonnets on pictures and on the "House of Life" body published by
  Dante Gabriel Rossetti in 1881, in Christina Rossetti's devotional and social
  sonnets, and in the engineering, architectural and lament sonnets of the 1870s
  to 1890s; America's first sustained sonnet vogue belongs to the 1880s and 1890s.

**G20**
- name: `"Nonsense Verse and the Parody of Rule"`
- description: Verse that turns the rules of grammar, prosody and logic against
  themselves for comic effect, including the limerick, the nonsense song and
  the learned parody of a recognised manner.
- historical_development: Lear's *A Book of Nonsense* (1846) and its successors
  make the limerick a literary form; "Jabberwocky", printed in Carroll's
  *Through the Looking-Glass* (1871), supplies the mock-translation and the
  invented lexicon; Calverley's parodies and the magazine verse of the 1880s and
  1890s carry the mode, which is continuous with the nonsense of Lear's own
  illustrated travel books.

**G21**
- name: `"Idyll and Domestic Narrative Poem"`
- description: The short or middle-length narrative poem of country and domestic
  life in a realised English scene, and the linked sequence of such poems; the
  name was given to the Arthurian narratives by Tennyson himself.
- historical_development: Tennyson's *Idylls of the King*, published as idylls
  from 1859 and collected in a single poem through the 1870s, fixes the term;
  the "idyll" then names the domestic or country narrative poem of the 1860s and
  1870s, in blank verse or in stanza, including the country tale and the
  farmhouse narrative.

**G22**
- name: `"Local-Colour Sketch and the Regional Portrait"`
- description: The short prose portrait of a place and its speech: a group of
  characteristic types, a scenery and a dialect, with incident held light so
  that the "colour" is the subject.
- historical_development: The regional sketch of the magazines of the 1850s
  grows after the war into the dominant American short form: Harte's California
  stories published in *The Overland Monthly* from 1868, the New England village
  tales of the 1870s to 1890s, Jewett's *The Country of the Pointed Firs* (1896),
  the Acadian and Creole sketches of Cable, the "Southwestern" tale and the
  dialect sketch of the 1880s.

**G23**
- name: `"Tall Tale and South-Western Humour Sketch"`
- description: The comic frontier yarn in which a boastful or impossible exploit
  is told in a matter-of-fact vernacular voice, usually inside a frame of
  hearth, bar-room, camp-fire or stump.
- historical_development: The backwoods humour of the frontier newspapers and
  almanacs of the 1830s and 1840s, collected and imitated through the 1850s,
  passes into the California comic sketch of the 1860s and 1870s and into
  Twain's platform and book tales; it is the technical ancestor of the American
  frame narrative and of the vernacular first person.

**G24**
- name: `"Dialect Poem and Vernacular Performance"`
- description: Verse composed in a class, regional or ethnic spoken dialect and
  written for recital, with its own orthography and its own stage of
  performance.
- historical_development: The British dialect-poem tradition of the mills and
  moors of the earlier century continues in the period; in America the mode
  becomes central with the plantation tales in dialect of the 1880s — Harris's
  *Uncle Remus, His Songs and His Sayings* (1880) — and with the recited
  dialect verse of the 1880s and 1890s, a form of which Dunbar and Riley are the
  standard examples; it ends as a dominant literary mode with the dialect
  controversy of the 1900s.

**G25**
- name: `"Lecture and Popular Address"`
- description: Prose composed to be spoken to a paying, subscribing or
  reform-society audience, and printed afterwards as a book or a magazine
  article.
- historical_development: Carlyle's 1840 course on hero-worship, Emerson's
  addresses of 1837 and the following decades, the anti-slavery and women's
  rights platforms, Ruskin's and Huxley's institutional lectures, and the lyceum
  and Chautauqua circuits of the 1870s to 1890s make the lecture a major
  literary form; the printed lecture is the common ancestor of the essay of
  ideas in both countries.

**G26**
- name: `"Review Essay and Quarterly Argument"`
- description: The long article that argues a general question — doctrine,
  policy, class, art — out of the review of several books.
- historical_development: The quarterlies of the 1840s to 1860s (the
  *Edinburgh*, *Quarterly*, *British Quarterly* and *Westminster Review*) and
  the new weeklies of 1855 onward carry the British essay; in America the
  *North American Review*, *Putnam's*, *Harper's* and *The Atlantic Monthly*
  (from 1857) do the same work. It is the form in which Carlyle, Arnold,
  Froude, Mill, Spencer and their American rivals published their argument, and
  the direct ancestor of academic criticism.

**G27**
- name: `"Social Inquiry and the Documented Survey"`
- description: Non-fiction built from question, interview, tally and direct
  observation, and printed as a serial or a numbered series, whose rhetoric is
  the document and whose end is reform.
- historical_development: The survey writing of the 1840s onward — the
  parliamentary and factory-commission evidence, Mayhew's *London Labour and the
  London Poor* (from 1851), the slum narrative and the missionary report — and,
  at the close of the period, Booth's metropolitan enquiry begun in 1889 and the
  American city survey of the 1890s. It supplies the documentary apparatus that
  sensation fiction and the naturalist novel borrow.

## 4. THEMES — 27 rows

**T1**
- name: `"Science, religion, and the question of design"`
- description: The argument over geology, deep time, development and design, and
  the literature it made. Lyell's *Principles of Geology* (vols. 1–3, 1830–33) and
  the anonymous *Vestiges of the Natural History of Creation* (1844) prepare
  Darwin's *Origin of Species* (1859) and *Descent of Man* (1871), and Tennyson's
  "Nature red to tooth and claw" in *In Memoriam* (1849/50) gives the argument its
  lyric phrase. Its British literary endpoints are the development hypothesis of
  Robert Browning's *Bishop Blougram's Apology* (in *Men and Women*, 1855), the
  anthropological romance of Samuel Butler's *Erewhon* (1872) and the
  evolution-and-degeneration fiction of the 1890s; in America the same argument
  is carried in the reviews, the lecture and the heredity novel of the 1870s and
  1880s.

**T2**
- name: `"Doubt, agnosticism, and the Broad Church conscience"`
- description: The felt loss of belief and the attempts to rebuild religion
  without the dogma. *Essays and Reviews* (1860) and the Privy Council's judgment
  in the controversy in 1864, the Broad Church theology of Maurice, Jowett and
  Kingsley, and the anonymously published *Ecce Homo* (1866) define the positions;
  the word "agnostic" is coined in the later 1860s and Tyndall's Belfast address
  of 1868 states the scientific claim. In literature the theme is the "doubt" of
  *In Memoriam* (1849/50), Arnold's "Dover Beach" (printed 1867), Clough's ironic
  verse narratives of the 1850s, and the religion of humanity of the positivist
  and ethical societies.

**T3**
- name: `"Bereavement, immortality, and the argument from grief"`
- description: Grief treated as both fact and evidence. Tennyson's *In Memoriam
  A.H.H.* (privately printed 1849, title page 1850), written on the death of
  Arthur Hallam, makes the long mourning-sequence the age's central form; Arnold's
  "Thyrsis" (1866) mourns a friend in pastoral terms; America's parallel is
  Whitman's Lincoln elegies of 1865. The theme also covers the culture of
  mourning — the funeral, the monument, the photograph, the spiritualist's seance
  — that the period's domestic fiction repeatedly registers.

**T4**
- name: `"The woman question, married disability, and the New Woman"`
- description: The argument over the legal being, education, property and
  franchise of women, and its fiction. The Married Women's Property Act (1882)
  and the campaign over the Contagious Diseases Acts in the 1870s and 1880s give
  it a legal shape; the tracts and review essays on women's franchise,
  education and paid labour of the 1850s to the 1870s are its debates, and
  Mill's *The Subjection of Women* (1869) its most quoted statement. Its
  literature runs from the marriage plots of *Jane Eyre* (1847) through Eliot's
  *Middlemarch* (serialised 1871–72) to Gissing's *The Odd Women* (1893), Allen's
  *The Woman Who Did* (1895) and Chopin's *The Awakening* (1899).

**T5**
- name: `"Wage labour, the strike, and the two nations"`
- description: The moral and narrative problem of industrial wage labour.
  *Sybil, or The Two Nations* (1845) names the division, Gaskell's *Mary Barton*
  (1848) and *North and South* (1855) give it a Manchester plot, *Hard Times*
  (serialised 1854) satirises its political economy, and at the century's close
  Gissing's *The Nether World* (1889) and Moore's *Esther Waters* (1894) return
  to it in naturalist terms.

**T6**
- name: `"The metropolis, the crowd, and the imperial capital"`
- description: London as a vast, unreadable modern city. *Bleak House*
  (serialised 1852–53) makes the fog, the court and the slum a single system;
  the documented survey of the capital — Mayhew's enquiries of the early 1850s and
  Booth's enquiry begun in the late 1880s — the West End and East End essay, the
  impressionist walking tour of the 1880s and 1890s and the poem of the crowd
  complete the theme. Its American twin is T21.

**T7**
- name: `"Empire, jingoism, and the literature of the metropole"`
- description: The empire as subject, audience and vocabulary. Indian Mutiny and
  Crown rule after 1857–58, the Crimean campaign, the Sudan and the South African
  war of 1899 supply the material; the boy's imperial romance (Haggard's
  *King Solomon's Mines*, 1885), Kipling's verse and tales of the 1880s and 1890s,
  and the "jingo" temper of the later 1890s and of the Jubilees of 1887 and 1897
  give it its public language, with Conrad's and Kipling's fiction the most
  quoted literary answers to it.

**T8**
- name: `"Education, the schools, and the cultivation of the self"`
- description: The formation of mind as a social and moral question. Newman's
  *The Idea of a University* (1852, enlarged 1873), Arnold's *Culture and Anarchy*
  (1869) and his lecture "On the Study of Celtic Literature" (1867) give it the
  theory; the public-school story (Hughes's *Tom Brown's School Days*, 1857), the
  school-board and pupil-teacher novel, and the autodidact's memoir give it the
  institution; the education of the girl — from *Jane Eyre* (1847) to the
  college heroine of the 1890s — is its most argued branch.

**T9**
- name: `"Madness, the asylum, and the diagnosis of the will"`
- description: Insanity as plot, as medicine and as metaphor. Sensation fiction
  makes the private asylum a machine of dispossession in *The Woman in White*
  (1859–60), *Lady Audley's Secret* (1862) and *Armadale* (1866); the
  "monomania" and the hereditary taint pass into the naturalist case history
  (Norris's *McTeague*, 1899) and into the diagnosis of the self-destructive
  will in *The Picture of Dorian Gray* (1890). Behind the fiction are the Lunacy
  Acts of the 1840s, the rapidly growing county and private asylum, and the new
  clinical psychology of the diagnosis.

**T10**
- name: `"Money, credit, speculation, and the joint-stock imagination"`
- description: Finance as a moral and narrative force. Dickens's *Little Dorrit*
  (serialised 1855–57) makes the joint-stock mania and its official
  "Circumlocution" a single system; *The Egoist* (1879) treats money as a
  property of the will; Trollope's *Phineas Finn* (1867) and its sequel put the
  share and the election on the same page; and the commercial panic and the ruin
  of the speculator are stock plots of Gissing's *New Grub Street* (1891) and of
  the finance novel of the 1890s.

**T11**
- name: `"Leisure class, the idle rich, and the unearned income"`
- description: The rentier, the "lady of means" and moneyed idleness as a social
  type and a moral problem. The unearned income of the country house and the
  London season is the material of Trollope's *Phineas Finn* (1867) and of
  Meredith's *The Egoist* (1879), and the "idle class" of the agricultural
  novel; the American branch is the millionaire comedy of the 1870s and 1880s —
  Twain and Warner's *The Gilded Age* (1873) — and the "conspicuous consumption"
  of Thorstein Veblen's analysis (1899).

**T12**
- name: `"Art versus life, and the romance of the artist"`
- description: The quarrel between the demands of art and the demands of living,
  conducted in the novel and the memoir of the artist. Its instances are the
  professional writer's dilemma of the 1860s, Pater's "hard, gemlike flame" in
  the Renaissance studies of 1873 and the artist-hero of *Marius the Epicurean*
  (1885), Morris's artist-craftsman of the 1870s and 1880s, and Gissing's
  *New Grub Street* (1891) as the commercial case of the same quarrel.

**T13**
- name: `"Self-destruction, melancholy, and the coroner's verdict"`
- description: Suicide as plot, as disease and as public question. The
  drownings, poisonings and falls of sensation and realist fiction, the ruin
  endings of Hardy and of the naturalists, and the self-willed destruction of
  *The Picture of Dorian Gray* (1890) give it its narrative forms; its social
  documents are the coroner's inquest and its verdict and the statistical
  discussion of suicide in the 1860s and 1880s. The American instance is
  Chopin's ambiguous walk into the sea in *The Awakening* (1899).

**T14**
- name: `"Sexuality, the double standard, and the literature of the social evil"`
- description: Regulated sex, prostitution, venereal disease and the sexual
  double standard as public subjects. The Contagious Diseases Acts and their
  repeal (the protest literature of 1885–86) create the "social evil" debate; the
  "fallen woman" novel of the 1850s and 1860s and its late-century
  counterparts — Hardy's *Tess of the d'Urbervilles* (1891), the New Woman
  fiction of the 1890s and the "white slavery" panic of the same decade — give it
  its fiction.

**T15**
- name: `"The machinery of print: the serial, the magazine, and the book trade"`
- description: The period's own publishing apparatus as a subject of its
  writing. The monthly part and the weekly serial, the three-volume library
  novel and the railway bookstall, *Household Words* (1850–59) and
  *All the Year Round* (1859–69), the American monthlies from *The Atlantic*
  (1857) onward, and the "conditions of letters" novel of the 1890s make the
  trade itself a theme.

**T16**
- name: `"Childhood, the child labourer, and the sentimental child"`
- description: The child as economic unit, as sentimental icon and as narrator.
  The child-labour commission evidence of the 1840s, the "factory child" of
  *Mary Barton* (1848) and *Hard Times* (1854), the sentimental and holy child
  of *The Water-Babies* (1863) and the fairy tale, and the boy narrators of the
  1870s to 1890s make the theme one of the period's most persistent.

**T17**
- name: `"The American wilderness and the myth of the forest"`
- description: The forest as a moral and national space, after Cooper's
  eighteenth-century "Leather-Stocking" of the 1820s. In Transcendentalist
  writing it becomes a system of symbols — Emerson's *Nature* (1836) and Thoreau's
  *Walden* (1854) — and in Melville's and Hawthorne's romance it is a scene of
  guilt and of terror; the later regionalists keep it as a landscape of
  memory. The survey and the settlement, not the sublimity alone,
  govern the American writing.

**T18**
- name: `"Democracy, individualism, and the American experiment"`
- description: The relation of the individual to the democratic whole. Emerson's
  "Self-Reliance" (1844) and "The American Scholar" (1837) state the ideal;
  Whitman's *Leaves of Grass* (1855) makes it poetic; the anti-democratic
  diagnosis runs from Melville's *The Confidence-Man* (1857) to Twain's
  political tales of the 1870s to 1890s. Tocqueville's *Democracy in America*
  (French 1835–40; the English translation from the later 1830s) is the
  period's standard description of the same problem.

**T19**
- name: `"Slavery, emancipation, and the unfinished Reconstruction"`
- description: The literature of American slavery, its destruction and its
  aftermath. Douglass's *Narrative* (1845), Jacobs's *Incidents in the Life of a
  Slave Girl* (1861) and the anti-slavery lecture platform give the testimony;
  Stowe's *A Key to Uncle Tom's Cabin* (1853) and her later novels make the
  argument a popular one; after the war, Tourgée's *A Fool's Errand* (1879),
  Dunbar's poems and prose of the 1890s, Chesnutt's tales of the colour line of
  1899 to 1901 and Twain's *Adventures of Huckleberry Finn* (1884/85) register
  emancipation's incompleteness.

**T20**
- name: `"The closing of the American frontier"`
- description: The settlement line, the "empty" West and its declared end. The
  emigrant generation wrote the trail narrative in the 1840s — Parkman's prairie
  and Rocky Mountain sketches of 1849 — and after the census declaration of a
  settled frontier line in the early 1890s, the essay "The Significance of the
  Frontier in American History", delivered in 1893, made the closing an official
  theme. Frederick Jackson Turner's "frontier thesis" is the interpretation of
  American character built on it, and the regionalist and imperial writing of the
  1890s are its literary consequences.

**T21**
- name: `"The American city, the machine, and the moneyed metropolis"`
- description: The great city, its wealth and its mechanisms, as the new
  American scene. Howells's *A Hazard of New Fortunes* (1890) puts the strike,
  the newspaper and the fashionable quarter on one page; Crane's *Maggie* (1893)
  makes the slum and the machine a destiny; and the skyscraper city of the
  1890s — its elevated railway, its electric light and its crowded ward — is the
  setting of the naturalists and of the Chicago Bohemia of the later decade.

**T22**
- name: `"Innocence, experience, and the lost American Eden"`
- description: The American theme of an innocence discovered to be
  knowledge. It runs from the "education" of Twain's and James's innocents —
  James's *Daisy Miller* (1878–79) and *The Portrait of a Lady* (1881) — to
  the lost country of the post-bellum regional tale and to the innocence
  of the child before the fact of race in *Adventures of Huckleberry Finn*
  (1884/85).

**T23**
- name: `"Regional identity and the American sectional character"`
- description: The belief that a "section" makes a character, and the literature
  that markets it. Harte's California stories of the late 1860s, Jewett's Maine
  coastal village in *The Country of the Pointed Firs* (1896), the New England
  village tales of the 1880s and 1890s, Harris's Georgia of the 1880s and Cable's
  Louisiana all define the American self by a scene, a speech and a type,
  and the sectional "survey" of the 1880s gives the theme its taxonomy.

**T24**
- name: `"Industrial wealth, accumulation, and the gospel of accumulation"`
- description: The American millionaire, the trust and the moral justification
  of wealth. Carnegie's essay "The Gospel of Wealth" (1889) and the
  "Gilded Age" — the name given to the 1870s by Twain and Warner's novel
  of that title (1873) — provide the vocabulary; Howells's *The Rise of Silas
  Lapham* (1885) makes the paint manufacturer a tragicomic figure, and
  the "money versus labour" quarrel of the 1890s is the naturalists' subject.

**T25**
- name: `"Race, voice, and the dialect of freedom"`
- description: American writing in or about black speech after emancipation.
  Harris's dialect tales, published as *Uncle Remus, His Songs and His Sayings*
  (1880), and the recited dialect verse of the 1880s and 1890s, of which Dunbar
  is the standard example, make dialect a national medium; Chesnutt's
  *The Conjure Woman* (1899) uses the same frame to interrogate it,
  and the race-and-lineage plots of American fiction of the 1890s give the theme
  its tragic form.

**T26**
- name: `"The machine age, speed, and technical modernity"`
- description: The machine, railway, telegraph, telephone, electric light and
  camera as literary subjects. The railway and the accident are plots from the
  1840s onward — the train in *The Woman in White* (1859–60) and the railway
  collision of the sensation and later sensation drama; the telephone and
  the phonograph, the skyscraper's lift and the electric city are the
  equipment of the 1890s; in fiction the machine is the figure of
  determinism in Norris and of the future in Bellamy (1888) and Wells.

**T27**
- name: `"Bohemia, the professional writer, and the Grub Street market"`
- description: Literature as a trade and the writer as a paid professional.
  Borrow's *Lavengro* (1851) makes the learned vagabond a figure of letters, the
  "Grub Street" novel of the 1890s — Gissing's *New Grub Street* (1891) is its
  classic and Du Maurier's *Trilby* (1894) its Bohemian parody — records the
  market, and the little magazine, the recital and the lecture circuit, together
  with the American authors' fight over international copyright in the 1880s and
  1890s, make the trade itself the theme.

## 5. CROSS-LINK NOTES (movement → genres / themes)

Convention for the importer: names below are copied byte-for-byte from §§2–4 above
(including the en dash in the period name and the commas inside theme names). No name
appears here that is not proposed as a row above. The payload shape follows
`data/relationships/installment_06_relationships_authors.json`:

* `period_movements` → `[{"period": "<period name>", "movements": ["<movement>", …]}]`
* `movement_genres` / `movement_themes` (name-resolved, `OR IGNORE`, as with `author_genres`)
  → `[{"movement": "<movement name>", "genres": [...], "themes": [...]}]`

### 5.1 `period_movements` — the single Victorian period row carries all 21 movements

```json
[
  {
    "period": "Victorian Period (1832–1901)",
    "movements": [
      "Victorian High Seriousness and the Public Poet",
      "Tractarian Prose and the Oxford Movement",
      "Carlyle and the Hero-Worship Lecture",
      "Chartism and the Condition-of-England Novel",
      "Sensation Fiction and the Serial Plot",
      "Pre-Raphaelitism and the Truth to Nature",
      "Ruskin and the Political Economy of Art",
      "Arnold and the Criticism of Culture",
      "Muscular Christianity and the Schoolboy Tale of Empire",
      "The Dramatic Monologue and the Masked Voice",
      "Aestheticism and the Decadent Decade",
      "The New Woman and the Fin-de-Siècle Problem Novel",
      "Transcendentalism and the Concord Lyceum",
      "Dark Romance and the Puritan Inheritance",
      "The Second American Renaissance and the Whitman-Dickinson Lyric",
      "Mark Twain and the Vernacular Performance",
      "American Realism and the Howells Program",
      "Local Colour and the Regionalist School",
      "American Naturalism and the Determinist Tragedy",
      "South-Western Humour and the Tall-Tale Sketch",
      "The Aesthetic Turn in 1890s America"
    ]
  }
]
```

### 5.2 Detailed notes — 12 movements (2–4 genres, 3–4 themes each)

**(1) Victorian High Seriousness and the Public Poet** (Tennyson, Browning, Clough, Arnold; 1830–1885)
* Genres: `Idyll and Domestic Narrative Poem`, `Pastoral Elegy and the Mourning Sequence`, `Dramatic Monologue and Masked Lyric`, `Sonnet Revival and Sequenced Sonnet`
* Themes: `Science, religion, and the question of design`, `Bereavement, immortality, and the argument from grief`, `Doubt, agnosticism, and the Broad Church conscience`, `Education, the schools, and the cultivation of the self`
* Rationale: the poet-laureateship instalment sequence is what makes the elegy and the domestic narrative poem the load-bearing Victorian forms; the grief-and-design pairing is the corpus's single densest thematic cluster (In Memoriam 1850, Origin of Species 1859).

**(2) Tractarian Prose and the Oxford Movement** (Newman, Manning, Pusey, Keble, Faber; 1833–1890)
* Genres: `Review Essay and Quarterly Argument`, `Novel of Development and the Growth Story`, `Victorian Verse Drama and Revived Tragedy`
* Themes: `Doubt, agnosticism, and the Broad Church conscience`, `Science, religion, and the question of design`, `Art versus life, and the romance of the artist`
* Rationale: the Tracts for the Times (1833–41) and the Anglican hymnody revival (Keble's Christian Year, 1827, as hinge antecedent) push religious argument into the quarterly review and into the conscience novel; Newman's own development-of-doctrine argument is a growth narrative before the term existed.

**(3) Carlyle and the Hero-Worship Lecture** (Carlyle, Sterling, Mill in discussion; 1830–1881)
* Genres: `Lecture and Popular Address`, `Social Inquiry and the Documented Survey`, `Review Essay and Quarterly Argument`
* Themes: `Wage labour, the strike, and the two nations`, `Education, the schools, and the cultivation of the self`, `The machinery of print: the serial, the magazine, and the book trade`
* Rationale: French Revolution (1837), Chartism (1839) and Heroes and Hero-Worship (1840) invent the serialized social diagnosis delivered as a lecture; the Exeter Hall/Hall of Commerce lecture circuit is the venue that makes the period's public prose.

**(4) Chartism and the Condition-of-England Novel** (Disraeli, Gaskell, Kingsley, Dickens; 1837–1860)
* Genres: `Industrial and Condition-of-England Novel`, `Serial and Monthly-Part Novel`, `Realist Novel of Common Life`
* Themes: `Wage labour, the strike, and the two nations`, `Childhood, the child labourer, and the sentimental child`, `The metropolis, the crowd, and the imperial capital`, `Education, the schools, and the cultivation of the self`
* Rationale: Sybil (1845), Mary Barton (1848), Alton Locke (1850) and Hard Times (serialized 1854) all stage the factory town and the schoolroom; the 1834 and 1870 Education Acts and the Ten Hours Acts give the cluster its documentary spine.

**(5) Sensation Fiction and the Serial Plot** (Collins, Braddon, Henry Wood, Dickens; 1859–1868)
* Genres: `Sensation Novel`, `Serial and Monthly-Part Novel`, `Detective Story and the Tale of Detection`, `Sensation Drama and the Domestic Stage`
* Themes: `Madness, the asylum, and the diagnosis of the will`, `Sexuality, the double standard, and the literature of the social evil`, `Money, credit, speculation, and the joint-stock imagination`, `The machinery of print: the serial, the magazine, and the book trade`
* Rationale: The Woman in White (1859–60) and The Moonstone (1868) fix the asylum-plot and the detective plot; Wilkie Collins's own stage adaptation of The Woman in White (1871) makes the novel-to-sensation-drama migration a documented corpus link.

**(6) Pre-Raphaelitism and the Truth to Nature** (Rossetti, Millais, Holman Hunt, Morris, Elizabeth Siddal; 1848–1882)
* Genres: `Sonnet Revival and Sequenced Sonnet`, `Idyll and Domestic Narrative Poem`, `Pastoral Elegy and the Mourning Sequence`, `Early Scientific Romance and Utopian Speculation`
* Themes: `Art versus life, and the romance of the artist`, `The woman question, married disability, and the New Woman`, `Bereavement, immortality, and the argument from grief`
* Rationale: The Germ (1850) is the movement's only periodical, so the doctrine travels in the poems: The House of Life (sonnet sequence, published 1881), Morris's The Earthly Paradise (1868) and the mourning poems written after Elizabeth Siddal's death in 1862. Morris's News from Nowhere (1890) is the reason the utopian-speculation genre is linked here: the romance of the made thing turns into the romance of the made society.

**(7) Ruskin and the Political Economy of Art** (Ruskin, and the Carlyle–Mill debate around him; 1843–1900)
* Genres: `Social Inquiry and the Documented Survey`, `Lecture and Popular Address`, `Review Essay and Quarterly Argument`, `Victorian Verse Drama and Revived Tragedy`
* Themes: `Wage labour, the strike, and the two nations`, `Art versus life, and the romance of the artist`, `Industrial wealth, accumulation, and the gospel of accumulation`, `The machine age, speed, and technical modernity`
* Rationale: Modern Painters vol. I (1843), Unto This Last (1860), Munera Pulveris (1862–63) and Sesame and Lilies (1865) supply the art-criticism-as-social-economy genre; the Slade Professorship lectures given at Oxford from 1870 are the documented lecture corpus.

**(8) Arnold and the Criticism of Culture** (Matthew Arnold, and his critics Froude, Pattison, Huxley; 1853–1888)
* Genres: `Lecture and Popular Address`, `Review Essay and Quarterly Argument`, `Pastoral Elegy and the Mourning Sequence`
* Themes: `Education, the schools, and the cultivation of the self`, `Doubt, agnosticism, and the Broad Church conscience`, `Wage labour, the strike, and the two nations`, `Art versus life, and the romance of the artist`
* Rationale: Culture and Anarchy (1869) and Arnold's later education lectures are lectures before they are books; Dover Beach (published 1867, composed earlier) and The Scholar-Gipsy (1853) are the poems that carry the Broad-Church theme forward.

**(9) Muscular Christianity and the Schoolboy Tale of Empire** (Hughes, Kingsley, G. A. Henty, Froude's influence; 1849–1889)
* Genres: `Novel of Development and the Growth Story`, `Imperial Adventure Romance`, `Children's Fantasy and the Dream-Region Tale`
* Themes: `Empire, jingoism, and the literature of the metropole`, `Education, the schools, and the cultivation of the self`, `Childhood, the child labourer, and the sentimental child`
* Rationale: Tom Brown's School Days (1857) and Two Years Ago (1857) set the template; Westward Ho! (1855) supplies the imperial schoolboy geography, and Kingsley's The Water-Babies (1863) is the same muscular gospel translated into the child's fantasy. The cluster's real output is the growth story, the adventure tale and the child's tale, and nothing else in the corpus fits it.

**(10) The Dramatic Monologue and the Masked Voice** (Browning, Clough, Rossetti, Bridges, Hardy's later experiments; 1841–1889)
* Genres: `Dramatic Monologue and Masked Lyric`, `Victorian Verse Drama and Revived Tragedy`, `Idyll and Domestic Narrative Poem`
* Themes: `Madness, the asylum, and the diagnosis of the will`, `The woman question, married disability, and the New Woman`, `Self-destruction, melancholy, and the coroner's verdict`, `Art versus life, and the romance of the artist`
* Rationale: Pippa Passes (1841), Dramatic Lyrics (1842), Men and Women (1855) and The Ring and the Book (1868–69) anchor the form; My Last Duchess and Porphyria's Lover give the masked-voice/ homicide-and-insanity overlap that the themes encode.

**(11) Aestheticism and the Decadent Decade** (Pater, Wilde, Symons, Dowson, the Rhymers' Club circle; 1866–1897)
* Genres: `Novel of Development and the Growth Story`, `Problem Play and Well-Made Drama`, `Sonnet Revival and Sequenced Sonnet`, `Nonsense Verse and the Parody of Rule`
* Themes: `Art versus life, and the romance of the artist`, `Sexuality, the double standard, and the literature of the social evil`, `Self-destruction, melancholy, and the coroner's verdict`, `Bohemia, the professional writer, and the Grub Street market`
* Rationale: Marius the Epicurean (1885), The Picture of Dorian Gray (1890), Salomé (1891) and the comedies of 1892–95 make the artist-novel and the problem play the movement's vessels. Nonsense Verse is included because the movement consolidated itself against its parodists.

**(12) The New Woman and the Fin-de-Siècle Problem Novel** (Schreiner, Grand, Ella Hepworth Dixon, George Egerton, Thomas Hardy's Sue Bridehead, Ibsen in translation; 1883–1899)
* Genres: `New Woman and Marriage-Question Novel`, `Problem Play and Well-Made Drama`, `Sensation Novel`, `Realist Novel of Common Life`
* Themes: `The woman question, married disability, and the New Woman`, `Sexuality, the double standard, and the literature of the social evil`, `Education, the schools, and the cultivation of the self`, `The machinery of print: the serial, the magazine, and the book trade`
* Rationale: The Story of an African Farm (1883), The Heavenly Twins (1893), The Story of a Modern Woman (1894) and The Beth Book (1897), with Tess (1891) and The Awakening (1899) on the American side, make marriage-law the fin-de-siècle topic; the New Woman periodicals give the print-machinery link.
### 5.3 Detailed notes — the 9 American movements (2–4 genres, 3–4 themes each)

**(13) Transcendentalism and the Concord Lyceum** (Emerson, Thoreau, Alcott, Margaret Fuller, Channing; 1836–1860)
* Genres: `Lecture and Popular Address`, `Social Inquiry and the Documented Survey`, `Review Essay and Quarterly Argument`
* Themes: `Education, the schools, and the cultivation of the self`, `Democracy, individualism, and the American experiment`, `Science, religion, and the question of design`, `The American wilderness and the myth of the forest`
* Rationale: Nature (1836), the Address before the Senior Class in Divinity College, Cambridge (1838), the Dial (1840–44) and Walden (1854) make the lecture and the surveyed walk the movement's forms; A Week on the Concord and Merrimack Rivers (1849) supplies the documentary travel frame.

**(14) Dark Romance and the Puritan Inheritance** (Hawthorne, Melville, Poe; 1830–1860)
* Genres: `Ghost Story and Scientific Supernatural Tale`, `Imperial Adventure Romance`, `Novel of Development and the Growth Story`
* Themes: `Doubt, agnosticism, and the Broad Church conscience`, `Self-destruction, melancholy, and the coroner's verdict`, `Madness, the asylum, and the diagnosis of the will`, `Innocence, experience, and the lost American Eden`
* Rationale: Twice-Told Tales (1837), The Scarlet Letter (1850), Moby-Dick (1851) and Pierre (1852) define the dark romance; Poe's Tales of the Grotesque and Arabesque (1840) grounds the ghost-story link, Melville's sea quest grounds the romance of adventure, and Hawthorne's Eden-and-fall plots ground the lost-American-Eden theme.

**(15) The Second American Renaissance and the Whitman-Dickinson Lyric** (Whitman, Dickinson, and the post-war generation; 1855–1891)
* Genres: `Dramatic Monologue and Masked Lyric`, `Pastoral Elegy and the Mourning Sequence`, `Idyll and Domestic Narrative Poem`
* Themes: `Bereavement, immortality, and the argument from grief`, `Democracy, individualism, and the American experiment`, `The machinery of print: the serial, the magazine, and the book trade`, `Self-destruction, melancholy, and the coroner's verdict`
* Rationale: Leaves of Grass (1855, rewritten in the 1860 and 1867 editions), the Drum-Taps cluster (1865) and its two public elegies, When Lilacs Last in the Dooryard Bloom'd and O Captain! My Captain! (both 1865), anchor the public side; the hand-copied fascicle and homework-book lyric of the 1860s, first collected in 1890, is the private counter-form.

**(16) Mark Twain and the Vernacular Performance** (Twain, Bret Harte's western strand, Bill Nye, Petroleum V. Nasby; 1865–1894)
* Genres: `Tall Tale and South-Western Humour Sketch`, `Dialect Poem and Vernacular Performance`, `Novel of Development and the Growth Story`
* Themes: `Race, voice, and the dialect of freedom`, `Regional identity and the American sectional character`, `Money, credit, speculation, and the joint-stock imagination`, `The machinery of print: the serial, the magazine, and the book trade`
* Rationale: The Celebrated Jumping Frog of Calaveras County (1865), Roughing It (1872), The Gilded Age (1873, with Charles Dudley Warner), Life on the Mississippi (1883) and Pudd'nhead Wilson (1894) give the vernacular line; the subscription-book campaign that placed A Tramp Abroad (1880) and Adventures of Huckleberry Finn (1884/85) in the home market is the print-machinery link.

**(17) American Realism and the Howells Program** (Howells, James in the American strand, Freeman, Woolson, Chopin; 1871–1895)
* Genres: `Realist Novel of Common Life`, `Local-Colour Sketch and the Regional Portrait`, `New Woman and Marriage-Question Novel`
* Themes: `The woman question, married disability, and the New Woman`, `Money, credit, speculation, and the joint-stock imagination`, `The American city, the machine, and the moneyed metropolis`, `Bohemia, the professional writer, and the Grub Street market`
* Rationale: Their Wedding Journey (1872), A Modern Instance (1882), The Rise of Silas Lapham (1885) and A Hazard of New Fortunes (1890) anchor the programme, with James's The Portrait of a Lady (1881) as its international companion; Howells's editorship of the Atlantic Monthly through the 1870s supplies the professional-writing link, and the domestic breakdown plotted in A Modern Instance supplies the woman-question link.

**(18) Local Colour and the Regionalist School** (Harte, Freeman, Murfree, Cable, Wilkins; 1852–1895)
* Genres: `Local-Colour Sketch and the Regional Portrait`, `Dialect Poem and Vernacular Performance`, `Tall Tale and South-Western Humour Sketch`
* Themes: `Regional identity and the American sectional character`, `The closing of the American frontier`, `Slavery, emancipation, and the unfinished Reconstruction`, `Childhood, the child labourer, and the sentimental child`
* Rationale: The Luck of Roaring Camp and Other Sketches (1868), Old Creole Days (1879) and The Country of the Pointed Firs (1896) are the dated anchors; Murfree's Kentucky mountaineer sketches of the 1880s and Freeman's Maine village tales of the 1880s–90s are cited as bodies of work rather than as single titles. The mining camp, the Creole quarter and the coastal village are the three regional matrices, and each is a dialect problem, which is why the sketch, the dialect poem and the tall tale travel together.

**(19) American Naturalism and the Determinist Tragedy** (Crane, Norris, Dreiser, the young London, Chopin in the determinist register; 1891–1901)
* Genres: `Naturalist and Determinist Novel`, `War Narrative of the Common Soldier`, `New Woman and Marriage-Question Novel`
* Themes: `Money, credit, speculation, and the joint-stock imagination`, `The American city, the machine, and the moneyed metropolis`, `Sexuality, the double standard, and the literature of the social evil`, `Self-destruction, melancholy, and the coroner's verdict`
* Rationale: Maggie: A Girl of the Streets (1893), The Red Badge of Courage (1894/95), McTeague (1899), Sister Carrie (1900) and The Awakening (1899) fix the determinist plot — the slum, the machine economy and the failed marriage as three fates. Frank Norris is cited as a body of work rather than by title, since the later volumes of his wheat epic fall after 1901; the war-genre link is Crane's, not the movement's whole.

**(20) South-Western Humour and the Tall-Tale Sketch** (Longstreet, Hooper, George Poe, the Crockett almanac wits, later Bill Nye and Petroleum V. Nasby; 1833–1885)
* Genres: `Tall Tale and South-Western Humour Sketch`, `Local-Colour Sketch and the Regional Portrait`, `Dialect Poem and Vernacular Performance`
* Themes: `The American wilderness and the myth of the forest`, `Democracy, individualism, and the American experiment`, `Race, voice, and the dialect of freedom`, `The closing of the American frontier`
* Rationale: Georgia Scenes (1835) is the movement's founding statement of method, and the Crockett almanac series of the 1830s and 1840s is its publishing engine; Hooper's and Poe's border sketches are cited as bodies of work rather than by title. The stump-orator and the backwoods brag are what Twain inherits, which is why the tall tale, the local-colour sketch and the dialect poem are linked to the same movement.

**(21) The Aesthetic Turn in 1890s America** (Whistler as the imported spokesman, Stedman as the anthologist-critic, the Chicago and Boston little magazines, Bret Harte's and Thomas Bailey Aldrich's verse of the "artistic" register; 1880–1901)
* Genres: `Nonsense Verse and the Parody of Rule`, `Problem Play and Well-Made Drama`, `Sonnet Revival and Sequenced Sonnet`
* Themes: `Art versus life, and the romance of the artist`, `Leisure class, the idle rich, and the unearned income`, `Bohemia, the professional writer, and the Grub Street market`, `The machinery of print: the serial, the magazine, and the book trade`
* Rationale: Whistler's Ten O'Clock Lecture (1885) is the creed imported into the American debate, The Chap-Book (Chicago, 1894) is its magazine, and Stedman's critical anthologies of the 1880s are its attempt to make a national verse repertoire; the Gilded-Age decorative interior supplies the leisure-class theme. Nonsense verse is linked because the American response to aestheticism ran through its parody.
### 5.4 Coverage check and the `movement_sources` convention

Every one of the 27 genres and 27 themes proposed above is linked from at least one
movement, and every movement carries 2–4 genres and 3–4 themes. No link uses a name
that is not proposed as a row in §§1–4.

For `movement_sources` the importer's shape is `movement -> [source]` with composite
keys resolved by name and `OR IGNORE`. **No source records are proposed in this draft**:
a source row must carry a verifiable author, title, year and publisher, and the memory
note for this project requires edition facts to be web-verified before anything is
written under `data/`. Each movement's `historical_significance` field above names the
scholarly anchors (by author, title and year, or by body of work where a year is not
certain) that the source rows should later be built from.

## 6. NAME INDEX — all 76 exact `name` strings, bare, one per line

Copy each line verbatim as the `name` value; strip the enclosing double quotes only.

### 6.1 Period (1)

Victorian Period (1832–1901)

### 6.2 Movements (21)

Victorian High Seriousness and the Public Poet
Tractarian Prose and the Oxford Movement
Carlyle and the Hero-Worship Lecture
Chartism and the Condition-of-England Novel
Sensation Fiction and the Serial Plot
Pre-Raphaelitism and the Truth to Nature
Ruskin and the Political Economy of Art
Arnold and the Criticism of Culture
Muscular Christianity and the Schoolboy Tale of Empire
The Dramatic Monologue and the Masked Voice
Aestheticism and the Decadent Decade
The New Woman and the Fin-de-Siècle Problem Novel
Transcendentalism and the Concord Lyceum
Dark Romance and the Puritan Inheritance
The Second American Renaissance and the Whitman-Dickinson Lyric
Mark Twain and the Vernacular Performance
American Realism and the Howells Program
Local Colour and the Regionalist School
American Naturalism and the Determinist Tragedy
South-Western Humour and the Tall-Tale Sketch
The Aesthetic Turn in 1890s America

### 6.3 Genres (27)

Novel of Development and the Growth Story
Sensation Novel
Industrial and Condition-of-England Novel
Realist Novel of Common Life
Naturalist and Determinist Novel
New Woman and Marriage-Question Novel
Imperial Adventure Romance
Detective Story and the Tale of Detection
Ghost Story and Scientific Supernatural Tale
Early Scientific Romance and Utopian Speculation
Children's Fantasy and the Dream-Region Tale
War Narrative of the Common Soldier
Serial and Monthly-Part Novel
Dramatic Monologue and Masked Lyric
Victorian Verse Drama and Revived Tragedy
Problem Play and Well-Made Drama
Sensation Drama and the Domestic Stage
Pastoral Elegy and the Mourning Sequence
Sonnet Revival and Sequenced Sonnet
Nonsense Verse and the Parody of Rule
Idyll and Domestic Narrative Poem
Local-Colour Sketch and the Regional Portrait
Tall Tale and South-Western Humour Sketch
Dialect Poem and Vernacular Performance
Lecture and Popular Address
Review Essay and Quarterly Argument
Social Inquiry and the Documented Survey

### 6.4 Themes (27)

Science, religion, and the question of design
Doubt, agnosticism, and the Broad Church conscience
Bereavement, immortality, and the argument from grief
The woman question, married disability, and the New Woman
Wage labour, the strike, and the two nations
The metropolis, the crowd, and the imperial capital
Empire, jingoism, and the literature of the metropole
Education, the schools, and the cultivation of the self
Madness, the asylum, and the diagnosis of the will
Money, credit, speculation, and the joint-stock imagination
Leisure class, the idle rich, and the unearned income
Art versus life, and the romance of the artist
Self-destruction, melancholy, and the coroner's verdict
Sexuality, the double standard, and the literature of the social evil
The machinery of print: the serial, the magazine, and the book trade
Childhood, the child labourer, and the sentimental child
The American wilderness and the myth of the forest
Democracy, individualism, and the American experiment
Slavery, emancipation, and the unfinished Reconstruction
The closing of the American frontier
The American city, the machine, and the moneyed metropolis
Innocence, experience, and the lost American Eden
Regional identity and the American sectional character
Industrial wealth, accumulation, and the gospel of accumulation
Race, voice, and the dialect of freedom
The machine age, speed, and technical modernity
Bohemia, the professional writer, and the Grub Street market
## 7. COLLISION CHECK

Checked against every line of `scripts/_i07_taxonomy_names.txt` (its own 15 movements,
24 genres and 24 themes, the cumulative `EXISTING DB MOVEMENTS/GENRES/THEMES`
vocabularies of 49 / 102 / 91 names, and the 6 existing `PERIODS` rows listed there —
which do not yet include installment 7's own `Romantic Period`, then being imported).
A programmatic pass confirms: **76 proposed
names, 0 exact duplicates, 0 case-insensitive duplicates** against that file. What
follows are the near-synonyms that were deliberately renamed, refused or re-scoped.

### 7.1 Period name

* `"Victorian Period (1832–1901)"` — the existing periods are `Old English Period (Anglo-Saxon)`,
  `Middle English Period`, `Renaissance and Early Tudor Period`, `Elizabethan and Jacobean
  Period`, `Caroline, Commonwealth, and Restoration Period`, `Augustan and Eighteenth-Century
  Period`, plus installment 7's `Romantic Period`. A bare `"Victorian Period"` would have
  clashed in style with `Romantic Period` (which carries no years) while the house style for
  dated rows is `Augustan and Eighteenth-Century Period`; the parenthetical year span follows
  `Old English Period (Anglo-Saxon)`'s precedent of a parenthetical qualifier. `"Victorian"`
  alone was refused as too generic for a controlled vocabulary.

### 7.2 Movements renamed or refused because of installment 7 / cumulative names

| Rejected near-synonym | Kept instead | Reason |
|---|---|---|
| "Victorian high seriousness" (user's suggested form) | `Victorian High Seriousness and the Public Poet` | house style names the institution, not the slogan; also avoids a bare-adjective movement row |
| "the condition-of-power novel" (user's suggested form) | `Chartism and the Condition-of-England Novel` | "condition of England question" is Carlyle's actual phrase (Chartism, 1839); "condition of power" is not attested |
| "Aestheticism and Decadence" | `Aestheticism and the Decadent Decade` | avoids the flat double-noun pattern of existing `Gothic and the Literature of Terror` |
| "Naturalism and the New Woman" (single row) | split into `American Naturalism and the Determinist Tragedy` + `The New Woman and the Fin-de-Siècle Problem Novel` | the two clusters have different corpora, decades and nations |
| "Muscular Protestantism" | `Muscular Christianity and the Schoolboy Tale of Empire` | "Muscular Christianity" is the documented term (derived from Kingsley); the variant would be a near-duplicate in the vocabulary |
| "Carlylean hero-worship" | `Carlyle and the Hero-Worship Lecture` | matches the `Keats and the Sensuous Ode` / `Austen and the Novel of Manners` pattern used throughout installments 6–7 |
| "L'art pour le rire" | folded into `Nonsense Verse and the Parody of Rule` (genre) | a slogan, not a movement; also a near-synonym of the Aestheticism row |
| "The American Lecture" | merged into `Transcendentalism and the Concord Lyceum` + genre `Lecture and Popular Address` | would have double-counted the Lyceum movement |
| "The Lyric Anthology and the National Verse Repertoire" | dropped; carried by genre `Review Essay and Quarterly Argument` and theme `The machinery of print…` | anthology-as-movement overlaps existing genre `Anthology, Reliques, and Editorial Collection` |
| verse drama as a separate movement | dropped as a movement; kept as genre `Victorian Verse Drama and Revived Tragedy` | would have collided with existing `Closet Drama` and `Heroic Drama`/`Revenge Tragedy` genre rows |
| `Abolitionist and Anti-Slavery Writing` (EXISTING DB MOVEMENT) | refused; slavery is carried as theme `Slavery, emancipation, and the unfinished Reconstruction` | the movement already exists; re-proposing it would be a duplicate |
| `Gothic and the Literature of Terror` / `Charles Brockden Brown and the American Gothic` (existing) | `Dark Romance and the Puritan Inheritance` | different genealogy (Hawthorne/Melville, not the 1790s Gothic) and different name |
| `Romantic Essay, Criticism and the Review` (i07) | `Arnold and the Criticism of Culture`, `Review Essay and Quarterly Argument` (genre) | the essayistic movement row exists; installment 8 needs the institutional-criticism row and a genre row instead |
| `The Knickerbocker Group and the American Sketch` / `Cooper and the American Romance of Forest and Sea` / `Bryant and the American Nature Lyric` (i07) | `Local Colour and the Regionalist School`, `South-Western Humour and the Tall-Tale Sketch`, `Dark Romance and the Puritan Inheritance` | the American 1832–1900 strand is post-Knickerbocker; the sketch rows are pushed down to genre level |

### 7.3 Genres renamed or refused

* `Sonnet Revival and Sequenced Sonnet` ← renamed from "Romantic Sonnet Revival" (i07 genre)
  and from bare "Sonnet Sequence" / "English Sonnet" (both existing genre rows).
* `Victorian Verse Drama and Revived Tragedy` ← renamed to avoid existing `Closet Drama`,
  `Revenge Tragedy`, `Tragedy`, `History Play`.
* `Pastoral Elegy and the Mourning Sequence` ← renamed to avoid existing `Elegy` and
  `Pastoral Poetry`, and i07's elegiac rows.
* `Imperial Adventure Romance` ← renamed to avoid existing `Prose Romance`, `Romance`,
  `Historical Novel and Romance`, `Frontier and Maritime Romance` (i07).
* `Children's Fantasy and the Dream-Region Tale` ← renamed to avoid i07 `Fairy Tale and
  Romantic Legend` and existing `Dream Vision`; the row is scoped to the fantasy and
  dream-country children's writing of 1862–1901 and names no post-1901 anchor.
* `Local-Colour Sketch and the Regional Portrait` ← renamed to avoid i07 `The Sketch and
  Character Tale` and `Familiar Essay and Character Sketch`.
* `Social Inquiry and the Documented Survey` ← renamed to avoid i07 `Local Guide and
  Topographical Prose` and existing `Travel and Wonders Literature`; it holds the
  municipal and parliamentary-survey prose that the travel genre cannot.
* `Novel of Development and the Growth Story` ← renamed to avoid existing
  `Sentimental and Domestic Novel`, `Prose Fiction and the Early Novel`, and i07
  `Novel of Manners and Fashion`.
* Dropped outright because an installment-7 or cumulative row already owns them:
  `Literary Annual and Keepsake Verse` (i07), `Memoir and Autobiographical Prose`,
  `Prose Biography`, `Letters`, `Critical Treatise and Dissertation`, `Periodical Essay
  and Spectator Paper`, `Diary and Journal`, `Essay`, `Lyrical Ballad and Popular Stanza`.
* Dropped as unsupportable by the corpus: "Household Magazine and Illustrated Weekly"
  (periodicals are barely titled in `scripts/_i07_existing_works.txt`), "Overland Trail
  and Emigrant Narrative", "Descriptive Art Criticism", "Musical Burlesque and
  Extravaganza", "The Country House Poem" — the last survives only as the theme
  `Leisure class, the idle rich, and the unearned income`.
* Trimmed 29 candidate genre rows to 27 to stay inside the 24–28 budget.

### 7.4 Themes renamed or refused

* `Science, religion, and the question of design` and `Doubt, agnosticism, and the Broad
  Church conscience` ← the single i07 theme `Doubt, faith, and secular questioning` was
  split, because the Victorian corpus distinguishes the design argument from the
  Broad-Church/Tractarian conscience crisis; neither new name duplicates the i07 string.
* `Bereavement, immortality, and the argument from grief` ← renamed from i07
  `Early death and the mourning of poets` and cumulative `Death, mourning, and the
  graveyard meditation`, `Time, death, and immortality through verse`.
* `The woman question, married disability, and the New Woman` ← renamed from i07
  `The marriage market and the limited estate`, `Marriage and women's conduct`,
  `Women's experience and the feminine voice`, `Female authorship and the woman writer`.
* `Wage labour, the strike, and the two nations` ← renamed from i07 `Industry, enclosure,
  and the changed countryside` and cumulative `Poverty, dependence, and the professional
  writer`, `Rural labour, depopulation, and the deserted village`.
* `Bohemia, the professional writer, and the Grub Street market` ← deliberately kept
  distinct from cumulative `Poverty, dependence, and the professional writer` and
  `Patronage and the literary marketplace`: the Victorian/1890s row is about the market
  for the person, not about dependence.
* `Money, credit, speculation, and the joint-stock imagination` ← renamed from cumulative
  `Commerce, luxury, and commercial society`.
* `The metropolis, the crowd, and the imperial capital` and `The American city, the
  machine, and the moneyed metropolis` ← cumulative `The city and urban life` was split
  by nation, since the corpus's London rows and New York rows carry different evidence.
* `Childhood, the child labourer, and the sentimental child` and `Education, the schools,
  and the cultivation of the self` ← cumulative `Childhood, innocence, and education` was
  split in two; the Victorian Factory Acts and the 1870/1880 Education Acts are separate
  documentary problems from the sentimental child.
* `The American wilderness and the myth of the forest` ← renamed from i07 `The wilderness,
  settlement, and Indian removal` (a different political argument) and from Cooper's
  `Frontier and Maritime Romance` genre row; it names the *myth*, and the frontier-closing
  theme carries the historian's claim.
* `The closing of the American frontier` ← kept as a theme, not a movement, to avoid
  duplicating `Cooper and the American Romance of Forest and Sea` and i07's removal theme.
* `Slavery, emancipation, and the unfinished Reconstruction` ← renamed from cumulative
  `Slavery, empire, and the Atlantic world`, `The slave trade and abolition`, and to stay
  distinct from the existing `Abolitionist and Anti-Slavery Writing` movement.
* `Self-destruction, melancholy, and the coroner's verdict` ← renamed against cumulative
  `Melancholy and self-analysis` and `Death, the soul, and the afterlife`: the Victorian
  coroner's inquest and the temporary-lunacy writ are its documented evidence base, which
  the two older rows do not cover.
* `Innocence, experience, and the lost American Eden` ← kept clear of cumulative
  `Childhood, innocence, and education`; this is the American pastoral-loss theme, not
  the Romantic child.
* `Race, voice, and the dialect of freedom` ← kept distinct from `Slavery, emancipation,
  and the unfinished Reconstruction`: the first is about ventriloquy and dialect in the
  text, the second about the political institution.
* Refused outright (already owned by installments 1–7): `Doubt, faith, and secular
  questioning`, `Early death and the mourning of poets`, `Puritan inheritance and the
  secret sin` (i07 theme — note this is *not* the same string as the movement
  `Dark Romance and the Puritan Inheritance`, which is a movement row in a different
  table; no theme duplicate is proposed), `The annual, the keepsake, and the gift-book
  economy`, `Natural history, science, and the poetic eye`, `Memory and the growth of the
  poet's mind`, `Country retirement and the estate poem`, `The public sphere, print, and
  the periodical` (carried instead as `The machinery of print: the serial, the magazine,
  and the book trade`, scoped to the Victorian serial and magazine trade).
* `The machinery of print: the serial, the magazine, and the book trade` is the only
  proposed name containing a colon; no existing theme name uses a colon, so no clash.

### 7.5 Internal consistency

* `- name:` strings in §§1–4 are byte-identical to the §6 index (verified by script:
  76/76, same order).
* Every name used in §5 cross-links exists as a proposed row (verified by script: 0
  unknown names; 27/27 genres and 27/27 themes each linked from at least one movement;
  each movement links 2–4 genres and 3–4 themes).
* No row is named for a single author's slogan where a documented contemporary term
  exists; no name reuses an installment-7 or cumulative vocabulary string.
