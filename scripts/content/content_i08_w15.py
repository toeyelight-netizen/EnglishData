"""Installment 8: works of the naturalist, ghetto and New Woman novelists
(part 15)."""

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

MOORE = wks("George Moore", [
 dict(title="A Mummer's Wife", year="1885",
   gb="Naturalist and Determinist Novel, Sensation Novel",
   tb=SEX + ", " + MEL + ", " + LAB,
   mb="Aestheticism and the Decadent Decade, Victorian Realism and the Novel of Ordinary Life",
   comp=["1884", "1885"], form="Novel",
   desc="Published in 1885 and the first English naturalist novel: the destruction of a Midland draper's wife by the theatre, drink and desire.",
   plot="Kate Ede, the wife of a consumptive draper in Hanley, falls in love with a travelling actor, leaves her husband and joins the touring company; the novel follows her years on the road, her husband's death, her decline into drink and her death in a London lodging-house, recorded with clinical flatness.",
   ctx="1884-85: the French naturalism of Zola and the Goncourts, the provincial theatre and the touring companies, and the circulating-library censorship of the 1880s.",
   sig="A Mummer's Wife is the first English naturalist novel and a landmark of English fiction: its unsparing record of a woman's decline and its refusal to moralise or console introduced the Zola method into English and prepared the way for Gissing, Hardy and Moore's own Esther Waters.",
   chars="Kate Ede; Ralph Ede; Mrs Ede, Ralph's mother; Dick Lennox"),
 dict(title="Esther Waters", year="1894",
   gb="Naturalist and Determinist Novel, Realist Novel of Common Life",
   tb=WOM + ", " + LAB + ", " + MEL,
   mb="Aestheticism and the Decadent Decade, Victorian Realism and the Novel of Ordinary Life",
   comp=["1892", "1894"], form="Novel",
   desc="Published in 1894 and the finest English novel of domestic service: the life of a servant girl who bears an illegitimate child and fights to keep him.",
   plot="Esther Waters, a kitchenmaid in a racing household, is seduced by the footman William Latch, loses her place when she is pregnant, and raises her son alone through years of service in London and the south coast; she gives up the respectable Fred Parsons to marry the returned William, who keeps a public house and makes a book on the races until gambling and illness ruin him, and the novel ends with Esther back at Woodview with her old mistress, Mrs Barfield, and her son grown into a soldier.",
   ctx="1894: the servant question, the racing world, the workhouse and the lying-in hospital, and the campaign against the Contagious Diseases Acts.",
   sig="Esther Waters is the classic English novel of the servant and one of the greatest novels of the 1890s: its patient, unsentimental record of a working woman's life has been recognised as the English masterpiece of naturalism, and it remains the finest fictional account of domestic service in the language.",
   chars="Esther Waters; William Latch; Mrs Barfield; Mr Barfield; Fred Parsons; Jackie, Esther's son; Mrs Latch; Sarah Tucker; Margaret Gale"),
 dict(title="A Drama in Muslin", year="1886",
   gb="New Woman and Marriage-Question Novel, Realist Novel of Common Life",
   tb=WOM + ", " + LEIS + ", " + SEX,
   mb="The New Woman and the Fin-de-Siècle Problem Novel, Aestheticism and the Decadent Decade, Victorian Realism and the Novel of Ordinary Life",
   comp=["1885", "1886"], form="Novel",
   desc="Published in 1886 and Moore's Irish novel of the marriage market: a group of girls brought out in Dublin to find husbands.",
   plot="Alice Barton and her friends are brought from their convent school to the Dublin season of balls and garden parties, where the girls are sold to the highest bidder; Alice, plain and clever, escapes into a marriage with a Dublin doctor and a life of social conscience, while her beautiful sister Olive is driven through the market by their ambitious mother and her crippled friend Cecilia Cullen retreats into a convent.",
   ctx="1885-86: the Irish landed class in decline, the Dublin Castle season, the Land League agitation, and the Victorian debate on women's education.",
   sig="A Drama in Muslin is the strongest Irish novel of the 1880s and one of the most astringent treatments of the marriage market in English: its picture of the Dublin season and of the destruction of women by the marriage system made it a key text of the New Woman debate and it was banned by the circulating libraries.",
   chars="Alice Barton; Olive Barton; Mrs Barton; Arthur Barton; Cecilia Cullen; May Gould; Violet Scully; Lord Kilcarney; Dr Edward Reed; Captain Hibbert"),
 dict(title="Confessions of a Young Man", year="1888",
   gb="Review Essay and Quarterly Argument, Social Inquiry and the Documented Survey",
   tb=ART + ", " + GRUB + ", " + SEX,
   mb="Aestheticism and the Decadent Decade, Arnold and the Criticism of Culture",
   comp=["1886", "1888"], form="Memoir (fictionalised autobiography)",
   desc="Published in 1888 and the most scandalous memoir of the Aesthetic movement: Moore's account of his years among the painters and poets of Paris.",
   plot="Moore recalls his Irish boyhood, his escape to Paris in 1873, his study of painting and his meetings with Manet, Degas, Zola and the Impressionists, his return to London, his discovery of Wagner and his adoption of the Decadent creed of art for art's sake.",
   ctx="1873-88: the Paris of the Impressionists, the literary Bohemia of London in the 1880s, and the aesthetic movement's cult of the self.",
   sig="Confessions of a Young Man is the liveliest English document of the Aesthetic movement and one of the most influential autobiographies of the century: its brilliant, insolent prose made Decadence a literary programme in English and it gave the movement its most quotable memoir.",
   chars="George Moore, the narrator (Edward Dayne); Marshall, his friend; Manet; Degas; Zola; Mallarmé; Villiers de l'Isle-Adam; Emma, the lodging-house servant"),
 dict(title="The Untilled Field", year="1903",
   gb="Local-Colour Sketch and the Regional Portrait, Realist Novel of Common Life",
   tb=LAB + ", " + DOUBT + ", " + EMPIRE,
   mb="Aestheticism and the Decadent Decade",
   comp=["1899", "1902"], form="Short-story collection",
   desc="Published in 1903 and the founding book of the modern Irish short story: fifteen stories of priest-ridden rural Ireland.",
   plot="The stories follow the parishioners and priests of a Mayo village through emigration, clerical tyranny, the failure of love and the small cruelties of village life, and end with the departure of the young for America.",
   ctx="1899-1902: the Irish Literary Revival, the land agitation and emigration of the 1890s, and the foundation of the Irish Literary Theatre.",
   sig="The Untilled Field invented the modern Irish short story and gave the Irish Revival its most exact prose: its influence on Joyce, O'Connor and the Irish story is direct and acknowledged, and it is the first work in which Moore's Irish subject matter found its proper form.",
   chars="Father Maguire ('Some Parishioners'); Father MacTurnan ('A Letter to Rome'); Biddy M'Hale ('The Window'); James Bryden and Margaret Dirken ('Home Sickness')"),
])

ZANGWILL = wks("Israel Zangwill", [
 dict(title="Children of the Ghetto", year="1892",
   gb="Realist Novel of Common Life, Local-Colour Sketch and the Regional Portrait",
   tb=RACE + ", " + LAB + ", " + EDU,
   mb="The New Woman and the Fin-de-Siècle Problem Novel",
   comp=["1891", "1892"], form="Novel",
   desc="Published in 1892 and the first great English novel of the Jewish East End: a year in the life of the immigrant community of London.",
   plot="The novel follows the Ansell family and their neighbours through the synagogue, the workshop, the Board School and the pawnshop: the clever Esther Ansell grows up in poverty and rises into the West End, Reb Shemuel's daughter Hannah is torn between her father's Law and her love for David Brandon, and the community's poverty, piety and humour are recorded in a series of connected scenes.",
   ctx="1891-92: the mass immigration of Russian and Polish Jews after 1881, the Whitechapel ghetto, the Jews' Free School, and the debate on anglicisation.",
   sig="Children of the Ghetto was the first English novel to give the Jewish immigrant community a full literary existence: it made Zangwill famous as the 'Dickens of the Ghetto', it recorded the speech and customs of the East End before they vanished, and it stands at the head of the English-Jewish tradition.",
   chars="Esther Ansell; Moses Ansell; Benjamin Ansell; Reb Shemuel; Hannah Jacobs, Reb Shemuel's daughter; Levi Jacobs; Sam Levine; David Brandon; Raphael Leon; Melchitsedek Pinchas"),
 dict(title="The King of Schnorrers", year="1894",
   gb="Tall Tale and South-Western Humour Sketch, Local-Colour Sketch and the Regional Portrait",
   tb=RACE + ", " + ECON + ", " + LEIS,
   mb="",
   comp=["1893", "1894"], form="Novella",
   desc="Published in 1894 and Zangwill's comic masterpiece: the exploits of Manasseh Bueno Barzillai Azevedo da Costa, the proudest beggar in eighteenth-century London.",
   plot="Manasseh, a Sephardi schnorrer of immense dignity, lives by extracting alms from the rich of Bevis Marks; he outwits a wealthy Ashkenazi on the point of honour, tricks a merchant into supporting his daughter's wedding, and defeats every attempt to humiliate him, in a picaresque comedy of the Jewish community of 1780.",
   ctx="1780s: the Sephardi and Ashkenazi communities of London, the Bevis Marks synagogue, and the Yiddish comic tradition of the schlemiel and the schnorrer.",
   sig="The King of Schnorrers is a comic classic and the first English book to draw on the Yiddish humour of the immigrant world: its portrait of Manasseh is one of the great comic creations in English fiction and it opened the way for the Jewish-American humour of the next century.",
   chars="Manasseh Bueno Barzillai Azevedo da Costa; Joseph Grobstock; Yankele ben Yitzchok; Deborah, Manasseh's daughter"),
 dict(title="Dreamers of the Ghetto", year="1898",
   gb="Review Essay and Quarterly Argument, Local-Colour Sketch and the Regional Portrait",
   tb=RACE + ", " + ART + ", " + DOUBT,
   mb="Arnold and the Criticism of Culture",
   comp=["1897", "1898"], form="Collection of historical portraits",
   desc="Published in 1898 and Zangwill's gallery of Jewish lives: a series of imagined portraits of figures from Spinoza to Heine.",
   plot="The volume presents episodes in the lives of Spinoza, Sabbatai Zevi, Uriel Acosta, Heine, Lassalle, and a company of modern dreamers, each caught at the moment when the vision of the ghetto meets the world outside it.",
   ctx="1897-98: the Zionist movement after the first Congress of 1897, the Jewish Enlightenment, and the debate over assimilation and national identity.",
   sig="Dreamers of the Ghetto is the most ambitious of Zangwill's books and a key text of the early Zionist imagination: its portraits of the great Jewish heretics and dreamers gave the movement a gallery of heroic ancestors and it remains a striking experiment in the historical portrait.",
   chars="Uriel Acosta; Baruch Spinoza; Sabbatai Zevi; the Baal Shem; Heinrich Heine; Ferdinand Lassalle"),
 dict(title="The Melting Pot", year="1908",
   gb="Problem Play and Well-Made Drama, Social Inquiry and the Documented Survey",
   tb=RACE + ", " + MET + ", " + WOM,
   mb="The New Woman and the Fin-de-Siècle Problem Novel",
   comp=["1908"], form="Play (four acts)",
   desc="First performed in 1908 and the play that gave the language its phrase: the love of a Russian-Jewish immigrant and a Christian girl in New York, and the vision of America as the crucible of the races.",
   plot="David Quixano, a composer who survived the Kishinev pogrom, writes an American symphony in a New York settlement house; he falls in love with Vera, the daughter of the Russian baron who commanded the pogrom, and in the last act the two are united in a vision of the great melting pot in which all races are fused into a new American.",
   ctx="1908: the mass immigration through Ellis Island, the settlement houses of New York, the Kishinev pogrom of 1903, and the American debate on assimilation.",
   sig="The Melting Pot gave the English language its most enduring metaphor for American immigrant assimilation: the play was a sensation in the United States and its title became the standard term for the American fusion of peoples, making Zangwill one of the most influential writers on the idea of America.",
   chars="David Quixano; Vera Revendal; Baron Revendal; Baroness Revendal; Mendel Quixano, David's uncle; Frau Quixano, David's grandmother; Quincy Davenport Jr; Kathleen O'Reilly; Herr Pappelmeister"),
])

GRAND = wks("Sarah Grand", [
 dict(title="The Heavenly Twins", year="1893",
   gb="New Woman and Marriage-Question Novel, Novel of Development and the Growth Story",
   tb=WOM + ", " + SEX + ", " + CHILD,
   mb="The New Woman and the Fin-de-Siècle Problem Novel",
   comp=["1890", "1893"], form="Novel (three books)",
   desc="Published in 1893 and the central English New Woman novel: the boy-and-girl twins Angelica and Diavolo, three marriages, and the destruction of women by the sexual double standard.",
   plot="Evadne Frayling, learning on her wedding day of her husband Major Colquhoun's dissolute past, refuses to consummate the marriage and lives with him in name only; Angelica Hamilton-Wells, the wilder of the mischievous 'heavenly twins' with her brother Diavolo, proposes to the much older Mr Kilroy and then, disguised as a boy, strikes up a nocturnal friendship with the Tenor, a singer of the cathedral town, who dies after discovering her sex; and Edith Beale, married to the syphilitic Sir Mosley Menteith, dies insane after the birth of a diseased child, which provides the novel's indictment. The last book is narrated by Dr Galbraith, whom Evadne marries after Colquhoun's death.",
   ctx="1890-93: the Contagious Diseases Acts campaign, the sexual ignorance of middle-class girls, the marriage law and the feminist periodicals of the early 1890s.",
   sig="The Heavenly Twins was the most discussed novel of 1893 and it made the New Woman a national figure: its treatment of venereal disease, sexual ignorance and the double standard made it a founding text of the English feminist novel, and Grand's own essay of 1894, 'The New Aspect of the Woman Question', helped put the phrase 'the New Woman' into circulation.",
   chars="Evadne Frayling; Major George Colquhoun; Angelica Hamilton-Wells; Diavolo (Theodore Hamilton-Wells), her twin; Mr Kilroy; the Tenor; Edith Beale; Sir Mosley Menteith; Dr Galbraith"),
 dict(title="The Beth Book", year="1897",
   gb="Novel of Development and the Growth Story, New Woman and Marriage-Question Novel",
   tb=WOM + ", " + ART + ", " + CHILD,
   mb="The New Woman and the Fin-de-Siècle Problem Novel",
   comp=["1896", "1897"], form="Novel",
   desc="Published in 1897 and Grand's finest novel: the growth of a girl of genius into an independent woman against every obstacle of Victorian family life.",
   plot="Beth Caldwell grows up in an Irish and English household of careless parents and brutal schooling, marries Dr Dan Maclure, a mercenary, philandering doctor who runs a lock hospital and practises vivisection, and after years of illness and poverty discovers her vocation as a writer and an orator for women's freedom.",
   ctx="1896-97: the Irish and English provincial middle class, the Victorian education of girls, and the feminist lecture platform of the 1890s.",
   sig="The Beth Book is the most fully realised of the New Woman novels and one of the first English novels to treat a woman's artistic vocation from childhood to fulfilment: its portrait of a girl of genius has made it a key text in the history of women's writing.",
   chars="Beth Caldwell; Captain Caldwell, her father; her mother; Dr Dan Maclure, her husband; Arthur Brock"),
 dict(title="Ideala", year="1888",
   gb="New Woman and Marriage-Question Novel, Realist Novel of Common Life",
   tb=WOM + ", " + SEX + ", " + DOUBT,
   mb="The New Woman and the Fin-de-Siècle Problem Novel",
   comp=["1887", "1888"], form="Novel",
   desc="Published in 1888 and the first of Grand's novels of the woman question: the spiritual history of a wife who cannot accept the double standard.",
   plot="Ideala, a beautiful and spiritual woman unhappily married to a dull and selfish husband, travels through Europe in search of faith and freedom, refuses the love of a good man rather than break the marriage law, and finds at last a vocation of social work among the poor.",
   ctx="1887-88: the Victorian debate on marriage and divorce, the higher education of women, and the spiritual crisis of the 1880s.",
   sig="Ideala was the first of the New Woman novels and a founding text of the genre: its heroine's refusal of the double standard and her search for a life of her own made it a book that Victorian women read as a manifesto.",
   chars="Ideala; Lord Dawne, the narrator; Lorrimer, the doctor who loves her; her husband"),
 dict(title="The New Aspect of the Woman Question", year="1894",
   gb="Review Essay and Quarterly Argument, Lecture and Popular Address",
   tb=WOM + ", " + EDU + ", " + SEX,
   mb="The New Woman and the Fin-de-Siècle Problem Novel, Arnold and the Criticism of Culture",
   comp=["1894"], form="Essay (North American Review)",
   desc="Published in March 1894 and the essay that named the movement: Grand's statement of what the New Woman wanted and why.",
   plot="Grand argues that the woman movement is a claim for the 'new aspect' of an old question: women demand education, economic independence and a single moral standard, and they claim the right to be judged as individuals rather than as members of a sex, in an essay that answers the caricatures of the New Woman in the press.",
   ctx="1894: the North American Review's symposium on the woman question, the suffrage campaigns, and the height of the New Woman controversy in Britain and America.",
   sig="'The New Aspect of the Woman Question' is the manifesto of the New Woman and one of the most influential feminist essays of the century: it defined the movement for its contemporaries, it was reprinted and answered across the English-speaking world, and it remains the clearest statement of what the 1890s meant by the New Woman."),
])

CAIRD = wks("Mona Caird", [
 dict(title="'Marriage' (1888)", year="1888",
   alt=["Marriage"],
   gb="Review Essay and Quarterly Argument, Lecture and Popular Address",
   tb=WOM + ", " + SEX + ", " + LEIS,
   mb="The New Woman and the Fin-de-Siècle Problem Novel, Arnold and the Criticism of Culture",
   comp=["1888"], form="Essay (Westminster Review)",
   desc="Published in August 1888 and the essay that provoked the greatest marriage debate of the century: an argument against the indissolubility of marriage.",
   plot="'Marriage' argues that the legal indissolubility of marriage makes the wife a chattel, that the double standard is enforced by law, that many marriages are legalised prostitution, and that women must be free to leave intolerable unions; the essay calls for equal divorce, for the economic independence of wives and for a single moral standard.",
   ctx="1888: the Westminster Review, the campaign for the custody of children and the Married Women's Property Acts, and the periodical press of the late 1880s.",
   sig="'Marriage' is a founding document of English feminism and the most radical Victorian argument on marriage: it drew over 27,000 replies in the periodical press, it made Caird the most notorious woman in England, and it set the agenda of the New Woman novel for the next decade."),
 dict(title="The Daughters of Danaus", year="1894",
   gb="New Woman and Marriage-Question Novel, Novel of Development and the Growth Story",
   tb=WOM + ", " + ART + ", " + CHILD,
   mb="The New Woman and the Fin-de-Siècle Problem Novel",
   comp=["1892", "1894"], form="Novel",
   desc="Published in 1894 and the most intellectually ambitious New Woman novel: the sacrifice of a woman composer to her family and the maternal 'instinct'.",
   plot="Hadria Fullerton, a gifted composer, is urged by her family to marry and to give up her music for husband and children; she marries Hubert Temperley, bears children she cannot love, escapes to Paris to study composition, and is called home by her mother's illness, which her family uses against her; the novel ends not in reconciliation but in defeat, her music abandoned and her revolt absorbed by a duty she cannot refuse.",
   ctx="1892-94: the debate on the 'maternal instinct', the position of the woman artist, the campaign for the Married Women's Property Acts, and the feminist circles of the early 1890s.",
   sig="The Daughters of Danaus is the most searching of the New Woman novels and the only one to make a woman artist's vocation its central subject: its refusal of the maternal ideal and its unflinching account of the cost of marriage made it the most radical feminist novel of the 1890s, and it has been recovered as a key text of Victorian feminism.",
   chars="Hadria Fullerton; Hubert Temperley, her husband; Algitha Fullerton, her sister; Mrs Fullerton, her mother; Professor Fortescue; Valeria Du Prel; Professor Theobald; Martha, the child she adopts"),
 dict(title="The Wing of Azrael", year="1889",
   gb="New Woman and Marriage-Question Novel, Sensation Novel",
   tb=WOM + ", " + SEX + ", " + MEL,
   mb="The New Woman and the Fin-de-Siècle Problem Novel",
   comp=["1888", "1889"], form="Novel",
   desc="Published in 1889 and the first novel to dramatise Caird's argument against marriage: a wife's revolt against a brutal husband.",
   plot="Viola Sedley, persuaded for her parents' sake to marry Philip Dendraith, the cruel heir of Upton Castle, finds herself trapped in a union of legalised cruelty; after her mother's death she resolves to elope with Harry Lancaster, the man she loves, and when her husband tries to stop her she stabs him with the dagger Harry gave her as a wedding present; repelled by Harry's horror, she flees along the shore and throws herself from the cliffs.",
   ctx="1888-89: the agitation after 'Marriage', the divorce law of 1857, and the Victorian treatment of wives' insanity.",
   sig="The Wing of Azrael is the first novel to put Caird's feminist argument into narrative form: its portrait of a wife's psychological destruction by marriage was one of the most shocking books of 1889 and it prepared the way for the New Woman fiction of the 1890s.",
   chars="Viola Sedley; Philip Dendraith; Harry Lancaster; Mr and Mrs Sedley, Viola's parents"),
 dict(title="The Stones of Sacrifice", year="1915",
   gb="New Woman and Marriage-Question Novel, Social Inquiry and the Documented Survey",
   tb=WOM + ", " + EDU + ", " + DOUBT,
   mb="",
   comp=["1913", "1915"], form="Novel",
   desc="Published in 1915 and Caird's last novel: a study of heredity, education and the sacrifice demanded of women by the family.",
   plot="A young woman of scientific mind is asked to give up her research to nurse the family that has stunted her; the novel examines heredity, the claims of the old and the young, and the ethics of self-sacrifice, and refuses the consolations of conventional piety.",
   ctx="1913-15: the science of heredity, the suffrage campaign at its height, and the pre-war debate on the family.",
   sig="The Stones of Sacrifice is Caird's most concentrated late work and shows the continuity of the feminist argument into the twentieth century: it treats heredity and self-sacrifice with a scientific seriousness rare in fiction and it is an important bridge between Victorian and modern feminism."),
])

WORKS = []
for _group in (MOORE, ZANGWILL, GRAND, CAIRD):
    WORKS.extend(_group)
