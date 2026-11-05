"""Installment 8: works of the essayists, the social-problem novelists and the
imperial romance (part 14)."""

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

LINTON = wks("Eliza Lynn Linton", [
 dict(title="The Girl of the Period and Other Social Essays", year="1868",
   gb="Social Inquiry and the Documented Survey, Review Essay and Quarterly Argument",
   tb=WOM + ", " + SEX + ", " + LEIS,
   mb="The New Woman and the Fin-de-Siècle Problem Novel, Arnold and the Criticism of Culture",
   comp=["1865", "1868"], form="Collected essays",
   desc="Published in 1868 and the book that named the modern young woman: a collection of satirical essays on the fashionable girl, marriage, dress and the woman question.",
   plot="The title essay attacks the 'Girl of the Period' — the young woman who paints her face, dresses in the latest fashion, speaks slang and thinks of nothing but pleasure and money — as a false and degraded modern type; the other essays consider the fashionable marriage, the education of girls, the woman of business and the 'shrieking sisterhood' of the feminists.",
   ctx="1865-68: the London periodical press of the 1860s, the controversy over women's dress and employment, and the rise of the woman's movement after the 1867 Reform Act.",
   sig="'The Girl of the Period' was the most discussed magazine essay of the 1860s and it set the terms of the Victorian debate over the modern woman: Linton's attack made the 'Girl of the Period' a national figure and provoked a decade of argument about fashion, work and female independence."),
 dict(title="The Rebel of the Family", year="1880",
   gb="New Woman and Marriage-Question Novel, Realist Novel of Common Life",
   tb=WOM + ", " + SEX + ", " + LEIS,
   mb="The New Woman and the Fin-de-Siècle Problem Novel, Sensation Fiction and the Serial Plot",
   comp=["1879", "1880"], form="Novel",
   desc="Published in 1880 and Linton's most searching novel of the woman question: a young woman who rebels against her family and finds that freedom has its own price.",
   plot="Perdita Morley, a strong-willed girl of the upper middle class, rejects the marriage her family has planned and insists on earning her living as a journalist; the novel follows her affair with a married man, her ostracism, her illness and the compromise by which she makes her peace with the world she had defied.",
   ctx="1880: the London of the women's colleges and the new professional openings, the feminist debates in the periodical press, and Linton's own complicated position between feminism and anti-feminism.",
   sig="The Rebel of the Family is the most interesting of Linton's novels and a key text of the 1880s debate on the New Woman: it takes the feminist case seriously and then tests it against experience, and it is far more ambivalent than the essays for which Linton was notorious."),
 dict(title="The True History of Joshua Davidson", year="1872",
   gb="Industrial and Condition-of-England Novel, Realist Novel of Common Life",
   tb=LAB + ", " + DOUBT + ", " + IND,
   mb="Carlyle and the Hero-Worship Lecture, Chartism and the Condition-of-England Novel",
   comp=["1871", "1872"], form="Novel (Christian Socialist parable)",
   desc="Published in 1872 and Linton's most original book: the life of a working-class carpenter who tries to live literally by the Sermon on the Mount in modern London.",
   plot="Joshua Davidson, a Somerset carpenter and a member of a small sect, comes to London as a Christian Socialist, preaches the literal gospel to the poor, is hated by the churches and the respectable, and is killed by a mob during a bread riot — a modern repetition of the life of Christ.",
   ctx="1871-72: the Paris Commune, the London of the 1870s, the Christian Socialist movement and the Tichborne case, and the Victorian fascination with the 'historical Jesus'.",
   sig="The True History of Joshua Davidson is one of the boldest religious novels of the century: its application of the gospel literally to Victorian London anticipated the Christian Socialism of the 1880s, and its scandalous success made Linton a figure of national controversy for the second time."),
 dict(title="Under Which Lord?", year="1879",
   gb="Industrial and Condition-of-England Novel, New Woman and Marriage-Question Novel",
   tb=LAB + ", " + SEX + ", " + WOM,
   mb="Chartism and the Condition-of-England Novel, Tractarian Prose and the Oxford Movement",
   comp=["1878", "1879"], form="Novel",
   desc="Published in 1879 and Linton's most ambitious social novel: the conflict between a High Church squire and the Radical workman he has made his son-in-law.",
   plot="Lorne, the young Radical poet whom the old squire has educated and married to his daughter, turns against his patron's Christianity and his class; the novel follows the marriage, the newspaper campaign, the strike and the ruin that the conflict brings on both families.",
   ctx="1878-79: the ritualist controversy in the Church of England, the agricultural labourers' unions, and the Radical press of the 1870s.",
   sig="Under Which Lord? is one of the strongest English novels of class and religion in the 1870s: its portrait of a working-class intellectual and its analysis of the alliance between radicalism and unbelief make it a serious contribution to the condition-of-England tradition."),
 dict(title="My Literary Life", year="1899",
   gb="Review Essay and Quarterly Argument, Serial and Monthly-Part Novel",
   tb=GRUB + ", " + WOM + ", " + PRINT,
   mb="Arnold and the Criticism of Culture",
   comp=["1898", "1899"], form="Autobiography (published posthumously)",
   desc="Published in 1899 after her death and the frank memoir of the first woman to hold a salaried post on the London daily press.",
   plot="Linton recalls her Cumberland childhood, her arrival in London in 1845, her work on the Morning Chronicle, the writers she knew — Dickens, Thackeray, Carlyle, Bulwer-Lytton — her unhappy marriage and her long career of fiction and journalism, and defends her opinions on women with undiminished pugnacity.",
   ctx="1898-99: the London press of the 1840s-90s, the world of the Victorian man and woman of letters, and the retrospect of a literary life at the end of the century.",
   sig="My Literary Life is one of the most valuable Victorian literary memoirs and a central document in the history of women's journalism: it records, with unusual honesty, the professional life of a woman who spent fifty years in the London press."),
])

WARD = wks("Mary Augusta Ward", [
 dict(title="Robert Elsmere", year="1888",
   gb="Novel of Development and the Growth Story, Realist Novel of Common Life",
   tb=DOUBT + ", " + LAB + ", " + ART,
   mb="Arnold and the Criticism of Culture, Victorian High Seriousness and the Public Poet",
   comp=["1885", "1888"], form="Novel",
   desc="Published in 1888 and the central English novel of the Victorian crisis of faith: the story of a clergyman who loses his belief and finds a religion of social service.",
   plot="Robert Elsmere, a young Oxford clergyman of the Broad Church school, falls in love with Catherine Leyburn, a woman of austere Evangelical faith; his reading of the German critics and his visit to the German universities destroy his belief in the resurrection, he resigns his living, and he founds a 'New Brotherhood' of social service in the East End, where he dies of overwork.",
   ctx="1888: the Broad Church and the Lux Mundi group, the higher criticism of the Bible, the university settlement movement, and the Oxford of T. H. Green and Arnold Toynbee.",
   sig="Robert Elsmere was the most discussed novel of the 1880s and the central literary document of the Victorian religious crisis: it sold in enormous numbers, was preached against from pulpits across Britain and America, and its picture of the passage from faith to social service made it the representative novel of its decade."),
 dict(title="Marcella", year="1894",
   gb="New Woman and Marriage-Question Novel, Industrial and Condition-of-England Novel",
   tb=WOM + ", " + LAB + ", " + SEX,
   mb="The New Woman and the Fin-de-Siècle Problem Novel, Chartism and the Condition-of-England Novel",
   comp=["1892", "1894"], form="Novel",
   desc="Published in 1894 and Ward's great novel of the New Woman and the land question: an heiress who refuses her class and must learn to work within it.",
   plot="Marcella Boyce, brought up by a Radical father and educated as an artist, returns to the decaying family estate and falls in love with Aldous Raeburn, the heir of the neighbouring Tory landowner; she breaks off the engagement over a poaching case, trains as a nurse, and finally marries him to work for housing and rural reform from within.",
   ctx="1894: the agricultural depression and the land question, the London poor law and nursing reform, and the New Woman debate at its height.",
   sig="Marcella is one of the most substantial New Woman novels and the finest English novel of the land question: its heroine's conversion from romantic Radicalism to practical social work made it a central text of the 1890s and it was read across the political spectrum."),
 dict(title="Helbeck of Bannisdale", year="1898",
   gb="Realist Novel of Common Life, Novel of Development and the Growth Story",
   tb=DOUBT + ", " + WOM + ", " + GRIEF,
   mb="Tractarian Prose and the Oxford Movement, The New Woman and the Fin-de-Siècle Problem Novel",
   comp=["1896", "1898"], form="Novel",
   desc="Published in 1898 and Ward's most concentrated tragedy: the love of an old Catholic squire and a young woman of the modern world, destroyed by their beliefs.",
   plot="Alan Helbeck, the last of an ancient recusant family, falls in love with Laura Fountain, the daughter of a Cambridge sceptic; their love is destroyed by the conflict between his Catholicism and her inherited unbelief, and Laura drowns herself in the river rather than submit to a faith she cannot accept.",
   ctx="1896-98: the Catholic revival in the north of England, the Victorian debate on education and dogma, and the position of the old Catholic gentry.",
   sig="Helbeck of Bannisdale is the finest of Ward's novels and one of the great English tragedies of religious difference: its portrait of an old Catholic family and its unsparing ending made it a critical favourite and it remains the most accomplished of her works."),
 dict(title="Eleanor", year="1900",
   gb="New Woman and Marriage-Question Novel, Realist Novel of Common Life",
   tb=WOM + ", " + DOUBT + ", " + SEX,
   mb="The New Woman and the Fin-de-Siècle Problem Novel, Arnold and the Criticism of Culture",
   comp=["1899", "1900"], form="Novel",
   desc="Published in 1900 and Ward's most controversial novel: an American girl in Rome, torn between a career of religious scepticism and a Catholic lover.",
   plot="Eleanor Burgoyne, a beautiful and clever American widow, is drawn to the Catholic Church by the aesthetics of Rome and by the love of a Catholic nobleman, but resists conversion; the novel follows her intellectual and emotional struggle, her friendship with a sceptical old priest's son, and her final choice of freedom.",
   ctx="1900: the American colony in Rome, the modernist crisis in the Catholic Church, and the debate over religious authority at the turn of the century.",
   sig="Eleanor was Ward's most discussed late novel and one of the most intelligent treatments of religious choice in English fiction: it dramatises the conflict between the aesthetic appeal of Catholicism and the claims of intellectual freedom, and it shows her at the height of her powers as a novelist of ideas."),
 dict(title="A Writer's Recollections", year="1918",
   gb="Review Essay and Quarterly Argument, Social Inquiry and the Documented Survey",
   tb=GRUB + ", " + DOUBT + ", " + PRINT,
   mb="Arnold and the Criticism of Culture",
   comp=["1917", "1918"], form="Memoir",
   desc="Published in 1918 and Ward's record of her Victorian literary life, her family and the making of Robert Elsmere.",
   plot="Ward remembers her Tasmanian childhood, her father's conversion to Catholicism and return, her Oxford girlhood among the Arnolds, her friendship with George Eliot, the writing of Robert Elsmere and the storm it caused, and the settlement work of her middle years.",
   ctx="1917-18: the last year of the First World War, the retrospect of the Victorian age by one of its survivors, and the Arnold family history.",
   sig="A Writer's Recollections is one of the most readable Victorian literary memoirs and a valuable record of the Arnold family, of George Eliot and of the crisis of faith that produced the greatest religious novel of the century."),
])

HAGGARD = wks("H. Rider Haggard", [
 dict(title="King Solomon's Mines", year="1885",
   gb="Imperial Adventure Romance, Novel of Development and the Growth Story",
   tb=EMPIRE + ", " + RACE + ", " + IND,
   mb="Muscular Christianity and the Schoolboy Tale of Empire",
   comp=["1885"], form="Novel",
   desc="Published in 1885 and the first great English adventure romance of Africa: Allan Quatermain's expedition into the interior in search of a lost civilisation and a legendary diamond mine.",
   plot="Allan Quatermain, the hunter, is engaged by Sir Henry Curtis and Captain Good to find Curtis's lost brother and the diamond mines of Solomon; the expedition crosses the desert, survives the mountains of Sheba, and reaches the lost Kukuana kingdom, where an Englishman is taken for a god and a civil war is fought before the treasure is found.",
   ctx="1885: the scramble for Africa, the discovery of the Zimbabwe ruins, the South African diamond fields, and the schoolboy market for adventure fiction.",
   sig="King Solomon's Mines invented the modern adventure novel of Africa: its combination of documentary travel detail, a treasure hunt and an encounter with a lost civilisation set the formula for a century of imperial romance, and it made Haggard the most popular storyteller in England."),
 dict(title="She: A History of Adventure", year="1887",
   gb="Imperial Adventure Romance, Early Scientific Romance and Utopian Speculation",
   tb=EMPIRE + ", " + SEX + ", " + MEL,
   mb="Muscular Christianity and the Schoolboy Tale of Empire, Victorian High Seriousness and the Public Poet",
   comp=["1886", "1887"], form="Novel",
   desc="Published in 1887 and Haggard's masterpiece: the discovery of the immortal queen Ayesha in a lost city beneath an African volcano.",
   plot="Leo Vincey and Horace Holly travel to the lost city of Kôr, where Ayesha, who has lived for two thousand years, believes Leo to be the reincarnation of her murdered lover Kallikrates; she bathes him in the flame of life, but the experiment that would make her mortal again destroys her, and the explorers escape the collapsing city.",
   ctx="1887: the archaeology of the ancient world, the Victorian interest in spiritualism and immortality, and the imperial exploration of central Africa.",
   sig="She is one of the foundational books of modern popular fiction: Ayesha became one of the great mythic figures of English literature, the novel invented the lost-world romance that Conan Doyle, Kipling and the cinema would carry into the twentieth century, and it has never been out of print."),
 dict(title="Allan Quatermain", year="1887",
   gb="Imperial Adventure Romance, War Narrative of the Common Soldier",
   tb=EMPIRE + ", " + MEL + ", " + SCI,
   mb="Muscular Christianity and the Schoolboy Tale of Empire",
   comp=["1887"], form="Novel (sequel to King Solomon's Mines)",
   desc="Published in 1887 and the last adventure of Allan Quatermain: the ageing hunter's journey to a hidden white nation beyond the African lakes.",
   plot="Quatermain, now rich and bored, sets out with Sir Henry Curtis and Captain Good to find the lost white race of the Zu-Vendi beyond the central lakes; they become involved in a dynastic war between two royal sisters, Quatermain is wounded, and the novel ends with his death and burial in Africa.",
   ctx="1887: the exploration of the African interior, the Victorian cult of the male adventure, and the market for sequels to a best-seller.",
   sig="Allan Quatermain is the first great adventure sequel and the book that gave the imperial romance a hero capable of death: the passing of Quatermain made Haggard's protagonists mortal, an unusually serious touch in a popular genre, and it prepared the way for the more ambivalent imperial fiction of the 1890s."),
 dict(title="Cleopatra", year="1889",
   gb="Imperial Adventure Romance, Novel of Development and the Growth Story",
   tb=SEX + ", " + EMPIRE + ", " + MEL,
   mb="Victorian High Seriousness and the Public Poet, Muscular Christianity and the Schoolboy Tale of Empire",
   comp=["1888", "1889"], form="Novel",
   desc="Published in 1889 and Haggard's great historical romance of the ancient world: the love of the Greek scholar Harmachis for the last queen of Egypt.",
   plot="Harmachis, the heir of the priests and the destined liberator of Egypt, is sent into the palace at Alexandria to destroy Cleopatra, but falls under her spell; she betrays the conspiracy, he escapes to the desert, and returns years later to see the queen die by the asp before he dies himself.",
   ctx="1889: the Victorian fascination with Cleopatra, the archaeology of Egypt, and the imperial analogy between Rome and Britain.",
   sig="Cleopatra is the finest of Haggard's historical romances and one of the great Victorian recreations of antiquity: its narrative of an Egyptian priest destroyed by the power of a queen made it a best-seller and it remains a landmark of the imperial historical romance."),
 dict(title="Eric Brighteyes", year="1891",
   gb="Imperial Adventure Romance, War Narrative of the Common Soldier",
   tb=EMPIRE + ", " + SEX + ", " + MEL,
   mb="Muscular Christianity and the Schoolboy Tale of Empire, Victorian High Seriousness and the Public Poet",
   comp=["1890", "1891"], form="Novel (Icelandic saga pastiche)",
   desc="Published in 1891 and Haggard's saga of the Viking age: the heroic life and death of an Icelandic warrior and his love for Gudruda the Fair.",
   plot="Eric Brighteyes, the strongest and most generous of the Icelandic heroes, loves Gudruda the Fair but is ensnared by Swanhild, the witch-wife of his enemy Ospakar; the novel follows his outlawry, his voyages, his duel with Ospakar, and his death at the hands of Swanhild's magic.",
   ctx="1890-91: the Victorian enthusiasm for the Icelandic sagas, William Morris's and Eiríkur Magnússon's translations, and the imperial cult of northern courage.",
   sig="Eric Brighteyes is the best of Haggard's historical novels and a remarkable English imitation of the Icelandic saga: its stern style and heroic fatalism made it a favourite of the saga revival and it stands at the head of the English tradition of Northern historical fiction."),
 dict(title="The World's Desire", year="1890",
   gb="Imperial Adventure Romance, Novel of Development and the Growth Story",
   tb=SEX + ", " + GRIEF + ", " + SCI,
   mb="Victorian High Seriousness and the Public Poet",
   comp=["1889", "1890"], form="Novel (with Andrew Lang)",
   desc="Published in 1890 and Haggard's collaboration with Andrew Lang: the wanderings of Odysseus, the last of the heroes, in search of Helen and the world's desire.",
   plot="Odysseus, returned to Ithaca but unable to forget Helen, sets out again and comes to Egypt, where he meets the Queen Meriamun, who believes him to be her destined lover; he is imprisoned, escapes, and dies at last in the desert, while the gods take Helen away.",
   ctx="1889-90: the Victorian Homeric revival, Andrew Lang's anthropology and folklore, and the imperial reading of the Odyssey.",
   sig="The World's Desire is one of the most interesting English continuations of Homer and a key text of the Victorian reimagining of the ancient world: its collaboration between a romancer and a scholar produced a strange and haunting book that influenced the later historical fantasy of the twentieth century."),
 dict(title="Nada the Lily", year="1892",
   gb="Imperial Adventure Romance, Novel of Development and the Growth Story",
   tb=EMPIRE + ", " + MEL + ", " + RACE,
   mb="Muscular Christianity and the Schoolboy Tale of Empire",
   comp=["1891", "1892"], form="Novel",
   desc="Published in 1892 and Haggard's Zulu epic: the rise of a Zulu warrior in the time of Chaka and the tragedy of his love for Nada the Lily.",
   plot="Umslopogaas, a Zulu warrior of royal blood, is raised in hiding from the tyrant Chaka; he becomes a chief, falls in love with Nada the Lily, and loses her to the jealousy of the witch-doctor, in a narrative of Zulu history told by Mopo, the old chief.",
   ctx="1891-92: the Zulu wars of the Victorian imagination, the ethnography of southern Africa, and Haggard's own South African service.",
   sig="Nada the Lily is the most ambitious of Haggard's African romances and one of the few Victorian novels to give a sustained and sympathetic account of Zulu history: its narrative of Chaka's tyranny is a powerful and disturbing piece of historical fiction."),
])

WORKS = []
for _group in (LINTON, WARD, HAGGARD):
    WORKS.extend(_group)
