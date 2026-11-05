"""Installment 8: works of the social-problem, New Woman and imperial romance
writers (part 13)."""

import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _lib import wk, wks  # noqa: F407

WOM = "The woman question, married disability, and the New Woman"
SEX = "Sexuality, the double standard, and the literature of the social evil"
LEIS = "Leisure class, the idle rich, and the unearned income"
ART = "Art versus life, and the romance of the artist"
EDU = "Education, the schools, and the cultivation of the self"
LAB = "Wage labour, the strike, and the two nations"
IND = "gospel of accumulation"
ECON = "credit, speculation, and the joint-stock imagination"
EMPIRE = "Empire, jingoism, and the literature of the metropole"
MET = "The metropolis, the crowd, and the imperial capital"
DOUBT = "Doubt, agnosticism, and the Broad Church conscience"
GRIEF = "Bereavement, immortality, and the argument from grief"
CHILD = "child labourer, and the sentimental child"
MEL = "Self-destruction, melancholy, and the coroner's verdict"
MAD = "Madness, the asylum, and the diagnosis of the will"
PRINT = "machinery of print"
GRUB = "Bohemia, the professional writer, and the Grub Street market"
SCI = "question of design"
RACE = "Race, voice, and the dialect of freedom"

OLIPHANT = wks("Margaret Oliphant", [
 dict(title="Miss Marjoribanks", year="1866",
   gb="Realist Novel of Common Life, Novel of Development and the Growth Story",
   tb=WOM + ", " + LEIS + ", " + EDU,
   mb="American Realism and the Howells Program, Sensation Fiction and the Serial Plot",
   comp=["1865", "1866"], form="Novel (Chronicles of Carlingford)",
   desc="Published in 1866 and the masterpiece of the Carlingford series: the comic history of Lucilla Marjoribanks, who returns from school to her provincial town determined to be its social centre.",
   plot="Lucilla Marjoribanks comes home to Carlingford to keep her widowed father's house, and sets about reorganising the town's society with the serene confidence of a natural ruler; the novel follows her dinners, her campaigns, her refusal of several eligible men and her eventual marriage to the one man who understands her management.",
   ctx="1860s: the provincial town of the English midlands, the social economy of the dinner party, and the serial publication of the Carlingford chronicles in Blackwood's Magazine.",
   sig="Miss Marjoribanks is one of the great comic novels of the century and the finest study of a woman's exercise of power within the narrow sphere allowed her: Lucilla is a complete original, and the novel's irony makes it a quiet masterpiece of English realism.",
   canon="Major canon"),
 dict(title="The Doctor's Family", year="1861",
   gb="Realist Novel of Common Life, Serial and Monthly-Part Novel",
   tb=WOM + ", " + LAB + ", " + CHILD,
   mb="Sensation Fiction and the Serial Plot",
   comp=["1861"], form="Novella (Chronicles of Carlingford)",
   desc="Published in 1861 and the first of the Carlingford stories: the arrival in the town of the feckless Fred Ridgely and his family, and the doctor's hopeless love.",
   plot="Dr Rider, a hard-working Carlingford physician, is burdened with the worthless Fred Ridgely and his helpless family; the story turns on the doctor's love for Nettie, Fred's capable sister, and on the discipline of charity that his profession demands.",
   ctx="1861: the early Carlingford series, and the market for short serial fiction in Blackwood's.",
   sig="The Doctor's Family sets the pattern of the Carlingford chronicles and shows Oliphant's characteristic subject at its purest: the ordinary professional life, the burden of dependants, and the hard economy of doing good in a small town."),
 dict(title="Salem Chapel", year="1863",
   gb="Realist Novel of Common Life, Serial and Monthly-Part Novel",
   tb=DOUBT + ", " + MAD + ", " + WOM,
   mb="Sensation Fiction and the Serial Plot, Tractarian Prose and the Oxford Movement",
   comp=["1862", "1863"], form="Novel (Chronicles of Carlingford)",
   desc="Published in 1863 and the most searching of the Carlingford novels: the ministry of a young Dissenting preacher and the ruin of his wife's mind.",
   plot="Arthur Vincent, a gifted young minister, comes to the Salem Chapel in Carlingford and finds his congregation divided and his own faith undermined; his wife, Adelaide, suffers a mental collapse after childbirth, and the novel follows the slow catastrophe of a marriage and a vocation.",
   ctx="1860s: the Dissenting chapels of the English provinces, the tensions of Nonconformist culture, and the Victorian treatment of puerperal insanity.",
   sig="Salem Chapel is the finest Victorian novel of Dissent and one of the earliest English fictions to treat mental illness in marriage with clinical honesty: its portrait of Adelaide Vincent is a landmark in the Victorian novel of the mind."),
 dict(title="Hester", year="1883",
   gb="Realist Novel of Common Life, Novel of Development and the Growth Story",
   tb=WOM + ", " + ECON + ", " + ART,
   mb="Sensation Fiction and the Serial Plot",
   comp=["1882", "1883"], form="Novel",
   desc="Published in 1883 and Oliphant's great novel of the woman of business: the conflict between the old banking family of the Vernonys and the capable young woman who saves it.",
   plot="Hester Vernon, a girl of intelligence and spirit, is brought up by her old-fashioned Quaker relatives after her father's disgrace; she becomes the mainstay of the family bank and must choose between the cousin she loves and the ruin of the house, while the novel follows her growth into a woman of affairs.",
   ctx="1880s: the provincial banking town, the South Sea Bubble speculation and its aftermath, and the Victorian debate on women's work.",
   sig="Hester is Oliphant's finest single novel and one of the great Victorian novels of a woman's professional life: it treats money, work and female independence with a clear-eyed realism that makes it a bridge between the Victorian novel and the New Woman fiction of the 1890s."),
 dict(title="A Beleaguered City", year="1880",
   gb="Ghost Story and Scientific Supernatural Tale, Realist Novel of Common Life",
   tb=DOUBT + ", " + GRIEF + ", " + SCI,
   mb="Victorian High Seriousness and the Public Poet",
   comp=["1879", "1880"], form="Novella",
   desc="Published in 1880 and Oliphant's strange masterpiece of the supernatural: a French cathedral town is besieged by invisible forces after its dead return.",
   plot="The small town of Semur is suddenly evacuated, as its inhabitants find themselves driven out by the presence of the dead; the mayor, the priest and a sceptical official each narrate their account of the visitation, and the town is left changed by the experience of a reality beyond the visible.",
   ctx="1880: the Victorian interest in spiritualism, the French provincial setting, and Oliphant's own bereavements of the 1870s.",
   sig="A Beleaguered City is one of the finest Victorian supernatural tales and a profound meditation on grief and belief: Oliphant turns the ghost story into a theological fiction about the communion of the dead, and it has been recognised as a forerunner of the modern uncanny story."),
 dict(title="Kirsteen", year="1890",
   gb="Novel of Development and the Growth Story, Realist Novel of Common Life",
   tb=WOM + ", " + LAB + ", " + MET,
   mb="Victorian High Seriousness and the Public Poet",
   comp=["1888", "1890"], form="Novel",
   desc="Published in 1890 and Oliphant's last great novel: a Highland girl who leaves home to make her own way in the world rather than marry as her family insists.",
   plot="Kirsteen Douglas, the daughter of an impoverished and tyrannical Highland laird, refuses the marriage he has arranged and runs away to London, where she supports herself as a journal-keeper and then as a businesswoman, returning home only when her father is dying and she has made her own fortune.",
   ctx="1890: the Scottish Highlands and the Clearances' aftermath, the London trade in journals and prints, and the New Woman debate on work and marriage.",
   sig="Kirsteen is the fullest Victorian novel of a woman's independent working life before the New Woman novels of the 1890s: its Scottish heroine, its hard realism about money and its refusal of a conventional marriage plot make it a key text of the Victorian woman's movement."),
 dict(title="The Autobiography of Margaret Oliphant", year="1899",
   gb="Review Essay and Quarterly Argument, Social Inquiry and the Documented Survey",
   tb=GRIEF + ", " + GRUB + ", " + PRINT,
   mb="Victorian High Seriousness and the Public Poet",
   comp=["1885", "1897"], form="Autobiography (published posthumously)",
   desc="Published in 1899 after her death and one of the greatest of Victorian autobiographies: the record of a life spent supporting a family by writing.",
   plot="Oliphant writes of her childhood in Scotland, her marriage and the early death of her husband, the loss of her children, and the unending labour of fiction, criticism and biography by which she kept her household; the book is interrupted by her own outbursts of grief and ends with her unfinished story of the deaths of her sons.",
   ctx="1885-97: the professional literary world of Blackwood's and the Victorian periodical, and the economics of women's authorship.",
   sig="The Autobiography is one of the most moving and most valuable documents of Victorian literary life, a frank account of the cost of a woman's writing career that has become a central text in the history of women's authorship."),
])

YONGE = wks("Charlotte M. Yonge", [
 dict(title="The Heir of Redclyffe", year="1853",
   gb="Novel of Development and the Growth Story, Realist Novel of Common Life",
   tb=DOUBT + ", " + GRIEF + ", " + LEIS,
   mb="Tractarian Prose and the Oxford Movement, Victorian High Seriousness and the Public Poet",
   comp=["1851", "1853"], form="Novel",
   desc="Published in 1853 and the most popular religious novel of the Victorian age: the story of two cousins, one generous and one proud, and the discipline of Christian self-sacrifice.",
   plot="Guy Morville, the heir of Redclyffe, is a high-spirited young man wrongly suspected of pride by his cousin Philip; his courtship of Amy Edmonstone, his illness and death abroad, and Philip's slow repentance form the pattern of a novel that made Guy the model of the Christian gentleman for a generation.",
   ctx="1853: the Oxford Movement and the High Church revival, the close-knit world of the English county family, and the Crimean War generation that took the novel to its heart.",
   sig="The Heir of Redclyffe was the most influential religious novel of its decade and is the central text of the Victorian High Church imagination: it shaped the ideal of the Christian gentleman, it was the favourite book of the officers of the Crimean War, and it made Yonge a national figure."),
 dict(title="The Daisy Chain", year="1856",
   gb="Novel of Development and the Growth Story, Realist Novel of Common Life",
   tb=CHILD + ", " + EDU + ", " + GRIEF,
   mb="Tractarian Prose and the Oxford Movement",
   comp=["1855", "1856"], form="Novel (first of the 'Chronicles of the May family')",
   desc="Published in 1856 and the first of Yonge's family chronicles: the eleven May children of a country doctor grow up through loss, school and vocation.",
   plot="The May family of Dr May of Stoneborough loses its mother in the first chapter, and the novel follows the children's education, the invalid Margaret's long illness, Ethel's struggles to manage the household and teach the poor, and the founding of the mission school that becomes Cocksmoor.",
   ctx="1850s: the Victorian country town, the Oxford Movement's parochial work, and the new market for family fiction that parents could give their daughters.",
   sig="The Daisy Chain is the founding text of the Victorian family chronicle and one of the most complete pictures of ordinary genteel life in English fiction: its large cast and its moral seriousness made 'the May family' a household name and founded the dynasty of chronicles that dominated girls' reading for fifty years."),
 dict(title="The Trial: More Links of the Daisy Chain", year="1864",
   gb="Novel of Development and the Growth Story, Realist Novel of Common Life",
   tb=DOUBT + ", " + LEIS + ", " + MEL,
   mb="Tractarian Prose and the Oxford Movement, Sensation Fiction and the Serial Plot",
   comp=["1863", "1864"], form="Novel (sequel to The Daisy Chain)",
   desc="Published in 1864 and the second of the May family chronicles: the trial of a young man for murder and the moral testing of the whole family.",
   plot="Avery May, the cleverest of the May brothers, is tried for the murder of his rival during a poaching affray; the novel follows the suspense of the trial, the family's ordeal and the slow working out of guilt, forgiveness and vocation among the brothers and sisters.",
   ctx="1864: the Victorian criminal trial and the press, the Oxford Movement's casuistry, and the serial market of the 1860s.",
   sig="The Trial shows Yonge at her most ambitious: it uses the machinery of the sensation novel for a sustained examination of conscience, guilt and religious duty, and it is one of the earliest English novels to dramatise a criminal trial as a test of Christian character."),
 dict(title="Pillars of the House", year="1873",
   gb="Novel of Development and the Growth Story, Realist Novel of Common Life",
   tb=CHILD + ", " + LAB + ", " + EDU,
   mb="Tractarian Prose and the Oxford Movement",
   comp=["1871", "1873"], form="Novel (two volumes)",
   desc="Published in 1873 and Yonge's longest and most ambitious family chronicle: the thirteen Underwood children left poor by their father's death.",
   plot="The Underwood family is left in genteel poverty when their father dies, and the novel follows the thirteen children over twenty years as they make their way through school, the church, the army, medicine and marriage, with the eldest daughter Geraldine at the centre of the household.",
   ctx="1870s: the Victorian professional classes and their climb, the High Church parish, and the serial fiction of the 1870s.",
   sig="Pillars of the House is the fullest expression of Yonge's ideal of the Christian family and her largest single work of social portraiture: it is the Victorian chronicle novel at its most comprehensive and the best introduction to the 'Dynasty' that occupied her for half a century."),
 dict(title="The Little Duke", year="1854",
   gb="Novel of Development and the Growth Story, Idyll and Domestic Narrative Poem",
   tb=CHILD + ", " + EDU + ", " + EMPIRE,
   mb="Tractarian Prose and the Oxford Movement, Muscular Christianity and the Schoolboy Tale of Empire",
   comp=["1854"], form="Children's historical novel",
   desc="Published in 1854 and Yonge's classic book for boys: the boyhood of Richard the Fearless, Duke of Normandy, in the tenth century.",
   plot="The ten-year-old Richard succeeds his murdered father as Duke of Normandy and is carried off by King Louis of France; he escapes, holds his duchy against his enemies, and learns the self-command that makes him a ruler, in a story of courage, loyalty and forgiveness.",
   ctx="1854: the Victorian historical novel for children, the vogue for Normandy and the Crusades, and the High Church interest in the medieval past.",
   sig="The Little Duke is one of the great Victorian books for children and a founding text of the historical novel for boys: its picture of a child learning to govern himself has been read by generations and it set the pattern for the moral adventure story of the later century."),
])

CRAIK = wks("Dinah Mulock Craik", [
 dict(title="John Halifax, Gentleman", year="1856",
   gb="Novel of Development and the Growth Story, Realist Novel of Common Life",
   tb=IND + ", " + LAB + ", " + DOUBT,
   mb="Carlyle and the Hero-Worship Lecture, Victorian High Seriousness and the Public Poet",
   comp=["1855", "1856"], form="Novel",
   desc="Published in 1856 and the classic Victorian novel of self-help: the rise of a poor boy to wealth and honour as a manufacturer in a west-country town.",
   plot="John Halifax, an orphan of unknown parentage, is befriended by Phineas Fletcher, the invalid son of a tanner, and works his way from mill-boy to master; the novel follows his marriage to Ursula March, his business struggles during the Napoleonic wars, the death of his children and his own death as a revered citizen.",
   ctx="1850s: the industrial west country, the Victorian gospel of work and self-help, and the Quaker and Unitarian culture of the manufacturing towns.",
   sig="John Halifax, Gentleman was one of the most popular novels of the century and the central Victorian fiction of self-help: its hero became the model of the self-made Christian businessman, and the book's combination of business realism and domestic sentiment made it a standard text of Victorian values."),
 dict(title="A Woman's Thoughts about Women", year="1858",
   gb="Social Inquiry and the Documented Survey, Review Essay and Quarterly Argument",
   tb=WOM + ", " + EDU + ", " + LEIS,
   mb="Victorian High Seriousness and the Public Poet",
   comp=["1857", "1858"], form="Essay collection",
   desc="Published in 1858 and the most practical Victorian book on the single woman's life: twelve essays on work, marriage, friendship and self-support.",
   plot="The essays address the woman who must earn her own living, the daughter at home, the wife, the old maid and the female friend, arguing that work is a duty and a dignity, that marriage is not the only vocation, and that women must be trained for independence of mind and purse.",
   ctx="1858: the surplus-women controversy, the early campaigns for women's employment and education, and the periodical culture of the 1850s.",
   sig="A Woman's Thoughts about Women is a founding text of Victorian feminism: it made the case for women's work and education in the most widely read form of the day, and it shaped the thinking of the generation that produced the women's movement of the 1860s and 70s."),
 dict(title="A Life for a Life", year="1859",
   gb="Sensation Novel, Realist Novel of Common Life",
   tb=SEX + ", " + MEL + ", " + GRIEF,
   mb="Sensation Fiction and the Serial Plot",
   comp=["1858", "1859"], form="Novel",
   desc="Published in 1859 and Craik's most daring novel: a doctor's love for the woman whose brother he killed.",
   plot="Dr Max Urquhart, an army surgeon, falls in love with Dora, the sister of a man he shot in a duel; the novel follows his concealment of the fact, the revelation that destroys their happiness, and the slow expiation of the guilt through years of service and suffering.",
   ctx="1859: the Victorian duel and its disgrace, the Crimean War, the ethics of medical confession, and the sensation market of the late 1850s.",
   sig="A Life for a Life is one of the boldest English novels of the 1850s: it treats duelling, guilt and sexual love with an intensity that anticipates the sensation novel, and it shows Craik's readiness to put a moral problem rather than a courtship at the centre of her fiction."),
 dict(title="The Little Lame Prince and His Travelling Cloak", year="1875",
   gb="Children's Fantasy and the Dream-Region Tale, Novel of Development and the Growth Story",
   tb=CHILD + ", " + EDU + ", " + GRIEF,
   mb="Victorian High Seriousness and the Public Poet",
   comp=["1874", "1875"], form="Children's fantasy",
   desc="Published in 1875 and one of the best-loved Victorian children's books: a crippled prince who is given a magic cloak that carries him over the world.",
   plot="Prince Dolor, robbed of his kingdom and lamed by his wicked uncle, is imprisoned in a tower until his fairy godmother brings him a travelling cloak; he flies across the world, learns the wisdom of the kingdoms he sees, and is restored to his throne as a just and gentle ruler.",
   ctx="1875: the Victorian fairy tale revival, the moral literature for children, and the widespread Victorian experience of childhood illness and disability.",
   sig="The Little Lame Prince is a permanent children's classic and one of the few Victorian fantasies to make physical disability the centre of its meaning: its image of the boy flying over the world in his cloak has entered the common imaginative inheritance."),
 dict(title="Olive", year="1850",
   gb="Novel of Development and the Growth Story, Sensation Novel",
   tb=WOM + ", " + SEX + ", " + ART,
   mb="Sensation Fiction and the Serial Plot",
   comp=["1849", "1850"], form="Novel",
   desc="Published in 1850 and Craik's first major novel: the story of a girl born with a deformity and her struggle for love and work.",
   plot="Olive Rothesay is born with a curved spine and a face disfigured by a birthmark; rejected by her mother and educated by a stern father, she becomes a painter, falls in love with a man who cannot accept her deformity, and finds her vocation in art and in the care of the child she adopts.",
   ctx="1850: the Victorian cult of female beauty, the position of disabled women, and the emergence of the woman artist as a fictional subject.",
   sig="Olive is one of the first English novels to make a disabled woman its heroine and one of the earliest to treat women's art as a vocation: it is a bold forerunner of the Victorian novel of the woman artist and a landmark in the representation of disability."),
])

WORKS = []
for _group in (OLIPHANT, YONGE, CRAIK):
    WORKS.extend(_group)
