"""Installment 10, wave 12: five minor American novelists whose careers began in 1946-1948.

The first wave under the scope decision of 2026-11-06 (British, Irish and American authors,
major and minor; other traditions only for major authors) and the first batch of minor
authors: several authors per wave, each with a complete author record and tiered work
records. The five began publishing between 1946 and 1948:

  Ross Lockridge Jr. (1914-1948): Raintree County (1948), his only book;
  Thomas Heggen (1918-1949): Mister Roberts (1946), his only novel;
  John Horne Burns (1916-1953): The Gallery (1947), Lucifer with a Book (1949) and
      A Cry of Children (1952);
  Dorothy West (1907-1998): The Living Is Easy (1948), The Wedding (1995) and
      The Richer, the Poorer (1995);
  William Gardner Smith (1927-1974): Last of the Conquerors (1948), South Street (1954)
      and The Stone Face (1963).

Lockridge, Heggen and Burns are in the discovery inventory through the Post45 New York Times
bestseller data (and Heggen also through the Pulitzer drama jury lists); West and Smith are
not in the inventory and were taken from the reference sources. None of the books was read.
Plots come from Wikipedia and from contemporary Kirkus reviews (most seen as the full review
text in search results) and, for Lucifer with a Book, the Atlantic. Books whose contents no
consulted source describes (Smith's Anger at Innocence and Return to Black America) and the
play Mister Roberts, which Heggen wrote with Joshua Logan, who has no record yet, are listed in
the bibliography notes and not recorded. Only Smith's first two novels are linked to a
movement ("Postwar African American Writing: Protest and Its Critics", with which Wikipedia
associates him); the others are left without one rather than forced.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MIN, OBS  # noqa: E402

WIKI_LOCKRIDGE = "Ross Lockridge Jr. (Wikipedia)"
WIKI_RAINTREE = "Raintree County (novel) (Wikipedia)"
WIKI_HEGGEN = "Thomas Heggen (Wikipedia)"
WIKI_ROBERTS = "Mister Roberts (novel) (Wikipedia)"
WIKI_ROBERTS_PLAY = "Mister Roberts (play) (Wikipedia)"
WIKI_BURNS = "John Horne Burns (Wikipedia)"
KIRKUS_LUCIFER = "Review of Lucifer with a Book (Kirkus Reviews, 1 March 1949)"
ATLANTIC_LUCIFER = "Review of Lucifer with a Book (The Atlantic, April 1949)"
KIRKUS_CRY = "Review of A Cry of Children (Kirkus Reviews, 1 September 1952)"
WIKI_WEST = "Dorothy West (Wikipedia)"
WIKI_LIVING = "The Living Is Easy (Wikipedia)"
KIRKUS_LIVING = "Review of The Living Is Easy (Kirkus Reviews, 1 May 1948)"
KIRKUS_WEDDING = "Review of The Wedding (Kirkus Reviews, 1 November 1994)"
KIRKUS_RICHER = "Review of The Richer, the Poorer (Kirkus Reviews, 15 May 1995)"
GALE_WEST = "Dorothy West (Gale biographical entries, via Encyclopedia.com)"
WIKI_WGS = "William Gardner Smith (Wikipedia)"
WIKI_CONQUERORS = "Last of the Conquerors (Wikipedia)"
KIRKUS_SOUTH = "Review of South Street (Kirkus Reviews, 1 October 1954)"
KIRKUS_STONE = "Review of The Stone Face (Kirkus Reviews, 1 November 1963)"
NYRB_STONE = "The Stone Face, publisher's description (New York Review Books / Penguin Random House, 2021)"
AMNEWS = "William Gardner Smith: significant Black author in exile (New York Amsterdam News, 2019)"
NYT = "NYT Hardcover Fiction Bestsellers, 1931-2020 (Post45 Data Collective)"
PULITZER_DRAMA = "Pulitzer Prize for Drama (Wikipedia)"

RL = "Ross Lockridge Jr."
TH = "Thomas Heggen"
JHB = "John Horne Burns"
DW = "Dorothy West"
WGS = "William Gardner Smith"

PROTEST = "Postwar African American Writing: Protest and Its Critics"

HISTORY = "History, truth and the uses of the past"
WAR = "War, combat and its aftermath"
LAND = "Land, place and regional belonging"
LOVE = "Love, intimacy and loss"
POWER = "Power, the state and surveillance"
SEX = "Sexuality, desire and the closet"
EDU = "Education, institutions and the academy"
FAMILY = "Family, marriage and domestic life"
CLASS = "Class, labour and social mobility"
RACE = "Race, racism and the struggle for civil rights"
GENDER = "Gender, feminism and women's lives"
CHILD = "Childhood, adolescence and coming of age"
VIOLENCE = "Violence, crime and justice"
CITY = "The city, the suburb and modern space"
EXILE = "Migration, exile and diaspora"
HOLOCAUST = "The Holocaust, atrocity and historical memory"

AUTHORS = [
A10(RL, MIN, "1914", "1948", "Bloomington, Indiana, United States",
  "American; Indiana novelist, author of a single published book, Raintree County (1948)",
  "American novelist whose only published book, Raintree County (1948), an epic of nineteenth-century Indiana "
  "framed by a single day, 4 July 1892, was a bestseller and has been named as a candidate for the Great American "
  "Novel; he took his own life two months after it appeared.",
  "Ross Franklin Lockridge Jr. was born on 25 April 1914 in Bloomington, Indiana, the youngest of four children of "
  "Elsie Shockley and Ross Lockridge Sr., a populist historian and lecturer; the novelist Mary Jane Ward was his "
  "double cousin (Wikipedia). He graduated from Indiana University in 1935 with the highest average then recorded "
  "there, after a year at the Sorbonne, taught English at the university while writing an MA thesis on Byron and "
  "Napoleon, and married Vernice Baker in 1936. In 1940 he went to Harvard on a fellowship and later taught at "
  "Simmons College in Boston; a long poem, The Dream of the Flesh of Iron, was rejected by Houghton Mifflin in "
  "1941. From the summer of 1943 he typed Raintree County on the backs of the pages of a 2,000-page draft about "
  "his mother's family, and finished it as a 600,000-word typescript in April 1946. Houghton Mifflin accepted it, and an MGM prize of "
  "$150,000 and a Book-of-the-Month Club selection followed, each at the price of further cuts. The novel was "
  "published on 5 January 1948 to extravagant reviews and large sales. Suffering from severe depression, "
  "Lockridge died of carbon monoxide poisoning in Bloomington on 6 March 1948, leaving his wife and four young "
  "children. John Leggett paired his life with Thomas Heggen's in Ross and Tom: Two American Tragedies (1974), "
  "and his son Larry Lockridge wrote the biography Shade of the Raintree (1994).",
  "His published work is Raintree County (Houghton Mifflin, 1948). Earlier writing, a long poem rejected in 1941 "
  "and a family novel with the working title American Lives, was not published (Wikipedia).",
  "Raintree County mixes realist chronicle with dream sequences, flashbacks and departures from linear narrative, "
  "and confines its present action to one day, perhaps in emulation of Joyce's Ulysses, as Wikipedia suggests; "
  "Howard Mumford Jones found in it 'a queer amalgam of pattern and formlessness'.",
  "The American myth and the meaning of the Civil War; the Midwest as the heart of the republic; heroism, poetry "
  "and the quest for an ideal, figured in the legendary golden raintree; a marriage across the sectional divide.",
  "Raintree County was a New York Times bestseller (Post45) that the Times reviewer called 'a huge and "
  "extraordinary first novel', while the New Yorker dismissed it as 'the climax of all the swollen, pretentious "
  "human chronicles'; MGM filmed it in 1957. Lockridge's suicide at the height of its success made him, with "
  "Heggen, the subject of Leggett's study of two first novelists destroyed by sudden fame.",
  bib_status="complete",
  bib_note="Bibliography status, 1946-2000: complete for published books. Lockridge published one book, Raintree "
  "County (Boston: Houghton Mifflin, 1948; recorded). An excerpt appeared in Life on 18 September 1947. "
  "Unpublished: The Dream of the Flesh of Iron (a long poem rejected by Houghton Mifflin in 1941), the abandoned "
  "family novel American Lives, on whose typescript the novel was drafted, and his MA thesis on Byron and "
  "Napoleon (Indiana University). Sources: Wikipedia's articles on Lockridge and the novel, and the Post45 New York "
  "Times bestseller data.",
  ver="partially verified", sources=[WIKI_LOCKRIDGE, WIKI_RAINTREE, NYT],
  alt=["Ross Franklin Lockridge Jr.", "Ross Lockridge"]),

A10(TH, MIN, "1918", "1949", "Fort Dodge, Iowa, United States",
  "American; novelist and playwright, born in Iowa, whose family moved to Oklahoma City in 1935; author of Mister "
  "Roberts (1946)",
  "American novelist whose only book, Mister Roberts (1946), a novel of life aboard a US Navy cargo ship in the "
  "rear areas of the Pacific war, sold over a million copies; with Joshua Logan he turned it into the play that "
  "won the Tony Awards for best play and best author in 1948.",
  "Thomas Heggen was born on 23 December 1918 in Fort Dodge, Iowa; in 1935, when his father's business failed in "
  "the Depression, the family moved to Oklahoma City (Wikipedia). He was a cousin of Wallace Stegner. After "
  "Oklahoma City University and Oklahoma State University he took a journalism degree at the University of "
  "Minnesota, where Max Shulman was a classmate, and became an editor at Reader's Digest in New York. He joined the "
  "Navy after Pearl Harbor, was commissioned a lieutenant in August 1942, and served on supply ships in the North "
  "Atlantic, the Caribbean and the Pacific, including fourteen months as assistant communications officer of the "
  "cargo ship USS Virgo, where he wrote vignettes of shipboard tedium and clashed with a martinet captain. "
  "Discharged in December 1945, he reworked them into Mister Roberts (Houghton Mifflin, 1946), which sold over a "
  "million copies despite mixed reviews. A stage adaptation begun with Shulman failed; written instead with the "
  "producer-director Joshua Logan, the play opened at the Alvin Theatre on 18 February 1948 with Henry Fonda and "
  "ran for 1,157 performances. Under pressure to write another bestseller, Heggen suffered from writer's block and "
  "insomnia, which he treated with alcohol and sleeping pills; on 19 May 1949 he drowned in his bath in New York "
  "after taking barbiturates. His death was widely reported as a probable suicide, though he left no note and "
  "friends insisted it was an accident (Wikipedia).",
  "Mister Roberts (novel; Houghton Mifflin, 1946) and, with Joshua Logan, the play Mister Roberts (first performed "
  "in 1948; published by Random House, 1948).",
  "Episodic chapters grown out of separate shipboard stories, mixing barracks comedy with frustration and a tragic "
  "ending; Logan's stage version stressed the farce while keeping the serious undertones (Wikipedia).",
  "The boredom and pettiness of the rear areas of the Pacific war; an officer who shields his men from a "
  "tyrannical captain while longing for combat; the crew's loyalty; men who feel 'left out' of the war.",
  "Mister Roberts sold over a million copies and was a New York Times bestseller (Post45); the play made from it "
  "with Logan won the first Tony Award for Best Play and was filmed in 1955 with Henry Fonda. John Leggett paired "
  "Heggen with Ross Lockridge in Ross and Tom (1974) as two first novelists whose deaths followed sudden success.",
  bib_status="complete",
  bib_note="Bibliography status, 1946-2000: complete for books. Recorded: Mister Roberts (novel; Boston: Houghton "
  "Mifflin, 1946). Listed and not recorded here: Mister Roberts, the play written with Joshua Logan (Alvin "
  "Theatre, New York, 18 February 1948; New York: Random House, 1948, with a foreword by John Mason Brown), which "
  "the Pulitzer drama jury considered for 1948 (Wikipedia's Pulitzer list, via the discovery inventory); it will "
  "be recorded when Logan, who has no record yet, is researched, so that both authors are credited. The shipboard "
  "stories from which the novel grew were not identified separately in the sources consulted.",
  ver="partially verified", sources=[WIKI_HEGGEN, WIKI_ROBERTS, WIKI_ROBERTS_PLAY, NYT, PULITZER_DRAMA],
  alt=["T. O. Heggen"]),

A10(JHB, MIN, "1916", "1953", "Andover, Massachusetts, United States",
  "American; novelist from Massachusetts, of an Irish Catholic family, who lived in Italy from 1950",
  "American novelist, author of three novels: The Gallery (1947), portraits of Allied-occupied Naples in 1944, was "
  "a bestseller praised by Hemingway and Edmund Wilson, while Lucifer with a Book (1949) and A Cry of Children "
  "(1952) were savaged by reviewers, and his reputation faded until The Gallery was reissued in 2004.",
  "John Horne Burns was born on 7 October 1916 in Andover, Massachusetts, the eldest of seven children of an "
  "upper-middle-class Irish Catholic family, and was educated at St Augustine's School, Phillips Academy and "
  "Harvard, where he became fluent in French, German and Italian and wrote the book for a student musical comedy "
  "(Wikipedia). He graduated in 1937 and taught English at the Loomis School in Windsor, Connecticut, writing "
  "several novels that he never published. Drafted in 1942, he was commissioned as a second lieutenant and served "
  "in military intelligence in Casablanca and Algiers and then for eighteen months in Italy, mainly in Naples, "
  "where he censored prisoners' mail. Back at Loomis after his discharge in 1946, he finished The Gallery, which "
  "Harper published in 1947; it became a bestseller. Lucifer with a Book (1949), a satire of a boarding school "
  "like Loomis, was savagely reviewed, and in 1950 he moved to Florence, where he wrote A Cry of Children (1952) "
  "and an article on the city for Holiday, and began a fourth novel. Known for his drinking and his attacks on "
  "other writers, he died of a cerebral haemorrhage after a sailing trip, on 11 August 1953, aged thirty-six, and "
  "was buried in Brookline, Massachusetts. David Margolick wrote his biography, Dreadful: The Short Life and Gay "
  "Times of John Horne Burns (2013), and called him, in the New York Times Magazine, 'the great (gay) novelist "
  "you've never heard of' (Wikipedia).",
  "Three novels, all published by Harper: The Gallery (1947), Lucifer with a Book (1949) and A Cry of Children "
  "(1952). He also wrote book reviews for the New York Times and the Saturday Review, a piece on Florence for "
  "Holiday and, in Harper's Magazine (May 1947), 'Promenade in Naples'; a fourth novel was unfinished at his "
  "death.",
  "The Gallery alternates nine character portraits with eight first-person recollections by an anonymous American "
  "soldier; Paul Fussell said Burns 'relied on discontinuity, like a sort of prose T. S. Eliot' (Wikipedia). "
  "Reviewers of the later novels found the same gift for biting satire and drama turned to caricature and excess "
  "(Kirkus).",
  "Occupiers and occupied in wartime Naples; the soldier's resentment of the military machine; homosexual "
  "servicemen; hypocrisy and venality in American private education; destructive love and a possessive mother; the "
  "veteran as smashed idealist.",
  "The Gallery was called 'the best war book of the year' by the Saturday Review and praised by Hemingway, Edmund "
  "Wilson and John Dos Passos; by 1991 Herbert Mitgang called it 'that forgotten gem of a novel', and New York Review "
  "Books reissued it in 2004 with an introduction by Paul Fussell. Time noted its chapter on 'an evening spent in a "
  "homosexuals' hangout', which other reviewers left unmentioned, and later critics, among them Marisa Escolar, have "
  "read it for its portrayal of homosexual servicemen (Wikipedia).",
  bib_status="complete",
  bib_note="Bibliography status, 1946-2000: complete for books; periodical writing incomplete. Recorded: The "
  "Gallery (New York: Harper & Brothers, 1947); Lucifer with a Book (Harper, 1949); A Cry of Children (Harper, "
  "1952; Wikipedia's list of works gives 1951, its text and Kirkus 1952). Not recorded: reviews in the New York "
  "Times (1949) and the Saturday Review (1948-49); 'Promenade in Naples' (Harper's Magazine, May 1947, seen in "
  "the Unz Review's index as a search extract); a piece on Florence for Holiday; the unfinished fourth novel; and "
  "the unpublished early novels and student work held at the Howard Gotlieb Archival Research Center, Boston "
  "University. The chapter 'Queen Penicillin' from The Gallery was anthologised as a story in The Best Short "
  "Stories of World War II (1957) and American Men at Arms (1964).",
  ver="partially verified", sources=[WIKI_BURNS, KIRKUS_LUCIFER, ATLANTIC_LUCIFER, KIRKUS_CRY, NYT]),

A10(DW, MIN, "1907", "1998", "Boston, Massachusetts, United States",
  "American; African American novelist, short-story writer and journalist of Boston and Martha's Vineyard, "
  "associated with the Harlem Renaissance",
  "African American novelist and short-story writer of the Harlem Renaissance generation and founder of the "
  "magazine Challenge, whose two novels, The Living Is Easy (1948) and The Wedding (1995), satirise and chronicle "
  "the Black middle class of Boston and Martha's Vineyard.",
  "Dorothy West was born in Boston on 2 June 1907, the daughter of Rachel Benson, of Camden, South Carolina, and "
  "Isaac Christopher West, a former slave who built a wholesale fruit business and was known as Boston's 'Black "
  "Banana King'; the family was among the most affluent Black households in the city, and the poet Helene "
  "Johnson was her cousin (Wikipedia). She published her first story at fourteen, attended the Girls' Latin "
  "School, Boston University and the Columbia School of Journalism, and in 1926 tied with Zora Neale Hurston for "
  "second place in Opportunity's contest with 'The Typewriter'. In Harlem she knew Langston Hughes, Countee "
  "Cullen and Wallace Thurman; she took a small part in Porgy and went with it to London in 1929, travelled to the "
  "Soviet Union in 1932 with a group making a film about American racism, founded Challenge in 1934 (six issues, "
  "to 1937) and edited its successor, New Challenge, with Richard Wright. She worked as a welfare investigator "
  "and for the Federal Writers' Project, wrote stories for the New York Daily News, and in the mid-1940s settled "
  "in her family's house at Oak Bluffs on Martha's Vineyard, where she wrote The Living Is Easy (Houghton "
  "Mifflin, 1948). For four decades she wrote for the island's newspaper. The Feminist Press reissued her novel in "
  "1982, and with the encouragement of Jacqueline Kennedy Onassis, her editor at Doubleday, she finished The "
  "Wedding (1995), which Oprah Winfrey adapted for television in 1998; the collection The Richer, the Poorer "
  "followed in 1995. She died in Boston on 16 August 1998 (Wikipedia; Kirkus).",
  "Two novels, The Living Is Easy (Houghton Mifflin, 1948) and The Wedding (Doubleday, 1995); short stories from "
  "the 1920s onwards in Opportunity, The Crisis, the Saturday Evening Quill and the New York Daily News, many collected "
  "with sketches and reminiscences in The Richer, the Poorer (Doubleday, 1995); a weekly column for the Vineyard "
  "Gazette from 1948; and the magazines Challenge (1934-37) and New Challenge, which she edited.",
  "Ironic humour and close social observation: Seymour Krim called The Living Is Easy 'a housewifey novel: a look "
  "at life from the kitchen and the parlor', full of 'abundant and special woman's energy' (Wikipedia), and Kirkus "
  "found her strength as 'a moralist and social observer', with her best stories told from a young girl's point "
  "of view.",
  "Class and colour within Black society, especially among the light-skinned elite Kirkus called the 'blue-white' "
  "Black people of Boston; ambition and the American dream; women's power within the family; poverty and welfare "
  "in Depression Harlem; childhood.",
  "One of the few Black women writers published in major literary magazines in the 1930s and 1940s and, late in "
  "life, celebrated as one of the last surviving members of the Harlem Renaissance (Wikipedia). Cynthia Davis "
  "argues that her concentration on the Black middle class placed her 'outside the black vernacular tradition' of "
  "Petry, Wright and Baldwin and left her less studied; the Feminist Press reissue of 1982 and the success of The "
  "Wedding brought her renewed attention.",
  bib_status="substantially complete",
  bib_note="Bibliography status, 1946-2000: substantially complete for books; periodical work not listed piece by "
  "piece. Recorded: The Living Is Easy (Boston: Houghton Mifflin, 1948; reissued by the Feminist Press, 1982); "
  "The Wedding (New York: Doubleday, 1995); The Richer, the Poorer: Stories, Sketches, and Reminiscences "
  "(Doubleday, 1995). Not recorded individually: her stories of the 1940s for the New York Daily News and, "
  "Wikipedia says, The New Yorker; her Vineyard Gazette columns from 1948; and her essay of 1985 on Sergei "
  "Eisenstein, later collected in The Richer, the Poorer. Before the period, and not recorded by installment 9: "
  "her stories from 'Promise and Fulfillment' (Boston Post) and 'The Typewriter' (Opportunity, 1926) onwards, and "
  "her editorship of Challenge (1934-37) and New Challenge.",
  ver="partially verified", sources=[WIKI_WEST, GALE_WEST, KIRKUS_LIVING, KIRKUS_WEDDING, KIRKUS_RICHER]),

A10(WGS, OBS, "1927", "1974", "Philadelphia, Pennsylvania, United States",
  "American; African American novelist and journalist from Philadelphia, an expatriate in France from 1951",
  "African American novelist and journalist of the postwar protest tradition, author of Last of the Conquerors "
  "(1948), South Street (1954) and The Stone Face (1963), one of the earliest fictional accounts of the Paris "
  "massacre of 17 October 1961; he lived in France from 1951 and worked for Agence France-Presse.",
  "William Gardner Smith was born in Philadelphia on 6 February 1927 and grew up in the South Philadelphia ghetto, "
  "a recurring setting of his novels (Wikipedia, quoting the Dictionary of Literary Biography). With his "
  "high-school principal's help he began reporting part-time for the Pittsburgh Courier, graduated with honours in "
  "January 1944 and joined the paper full-time. Drafted in January 1946, he served as a clerk-typist in occupied "
  "Berlin, the source of his first novel, Last of the Conquerors (1948), published when he was twenty-one. After "
  "his discharge he studied at Temple University, married and wrote Anger at Innocence (1950); after a stay at "
  "Yaddo the couple left for France in late 1951, joining the African American community in Paris that included "
  "Richard Wright, James Baldwin and Chester Himes. The marriage failed. South Street (1954) appeared as he joined "
  "Agence France-Presse, for which he worked as an editor and correspondent, directing its service in Ghana until "
  "Nkrumah's fall in 1966. The Stone Face (1963) drew on the anti-Arab racism of the Algerian War years in Paris, "
  "and Return to Black America (1970) revised reporting from his visits to the United States in the late 1960s, "
  "when French radio and television treated him as an expert on American racial unrest. He was diagnosed with "
  "cancer in October 1973 and died at Thiais, near Paris, on 5 November 1974 (Wikipedia).",
  "Four novels, Last of the Conquerors (Farrar, Straus, 1948), Anger at Innocence (1950), South Street (1954) and "
  "The Stone Face (1963), and the reportage Return to Black America (Prentice-Hall, 1970), with essays and "
  "journalism, among them 'The Negro Writer: Pitfalls and Compensations' (Phylon, 1950) (Wikipedia).",
  "Realist protest fiction, which Kirkus found didactic and flat in prose but capable of 'fine oblique scenes' and "
  "shocking comparisons between ghettos, camps and riots; Wikipedia describes him using fiction, as he used "
  "journalism, to testify to events he witnessed.",
  "Racism in the United States and abroad, from the segregated army of occupation to the Algerian War; interracial "
  "love; exile and the outsider's double view of two countries; the choice between militancy and withdrawal.",
  "Wikipedia links him with the Black social protest novel of Wright, Ellison, Motley and Petry and counts South "
  "Street among the first Black militant protest novels. Kristin Ross notes that The Stone Face, published in the "
  "United States because it could not be published in France, remained one of the few representations of the "
  "massacre of 17 October 1961 until the early 1990s; New York Review Books reissued it in 2021 with an "
  "introduction by Adam Shatz.",
  bib_status="substantially complete",
  bib_note="Bibliography status, 1946-2000: substantially complete for books (Wikipedia's list of major works); "
  "journalism incomplete. Recorded: Last of the Conquerors (New York: Farrar, Straus, 1948; London: Gollancz, "
  "1949); South Street (New York: Farrar, Straus and Young, 1954); The Stone Face (New York: Farrar, Straus, 1963; "
  "New York Review Books, 2021). Listed and not recorded, because no source consulted describes their contents: "
  "Anger at Innocence (Farrar, Straus, 1950; London: Gollancz, 1951; in French as Malheur aux justes, 1952) and "
  "Return to Black America (Englewood Cliffs: Prentice-Hall, 1970; in French as L'Amerique noire, 1972), reportage "
  "revised from his journalism of the late 1960s. Essays and articles include 'The Negro Writer: Pitfalls and "
  "Compensations' (Phylon, 1950) and 'Black Boy in France' (Ebony, July 1953), on Richard Wright in Paris.",
  ver="partially verified", sources=[WIKI_WGS, WIKI_CONQUERORS, KIRKUS_SOUTH, KIRKUS_STONE, NYRB_STONE]),
]

WORKS = [
W10("Raintree County", RL, "1948", "Novel", "significant",
  genres=G("Historical Novel"),
  themes=T(HISTORY, WAR, LAND, LOVE),
  overview="Lockridge's only novel, a 1,066-page epic of nineteenth-century America set in the imaginary Raintree "
  "County, Indiana, and published by Houghton Mifflin on 5 January 1948. Its present action covers one day, 4 July "
  "1892, in the life of the schoolteacher and poet John Wickliff Shawnessy; the rest of his story is told in "
  "flashbacks and dream sequences (Wikipedia).",
  content="The life of John Shawnessy from his youth before the Civil War, through his marriage to an unstable "
  "Southern belle and his service as a Union soldier, to his later years as a teacher, defeated candidate and "
  "would-be playwright, seen from one Fourth of July.",
  summary="On 4 July 1892 John Wickliff Shawnessy, a teacher and poet in the small town of Waycross, lives through a "
  "single day whose events call up his past (Wikipedia's article on Lockridge). As a young man before the Civil "
  "War, 'Johnny' is a lover of literature who measures his life against three ideals: the hero of Greek legend; "
  "the great man foretold in Hawthorne's story 'The Great Stone Face'; and the legendary golden raintree that "
  "Johnny Appleseed is said to have planted somewhere in the county. He meets and marries a beautiful Southern "
  "belle, whose emotional instability destroys the marriage. He serves as a Union soldier, and on his return "
  "learns that he has been reported killed in action and that the woman he loved, believing him dead, has married "
  "his old friend and rival and has died in childbirth. As John he builds a new life: he becomes a teacher, runs "
  "unsuccessfully for political office, goes briefly to New York to try to become a playwright, and comes home to "
  "Indiana, where he remarries and finds contentment, while witnessing the century's turning points from westward "
  "expansion and the slavery debate to industrialisation and the labour movement (Wikipedia's article on the "
  "novel). An outrageous alter ego for the hero, the 'Perfessor' Jerusalem Webster Styles (Wikipedia's spelling), "
  "delivers among other things a blasphemous riff in praise of bastards (Wikipedia's article on Lockridge).",
  themes_text="Wikipedia calls the book an effort to mythologise American history through Shawnessy's eyes, and "
  "Lockridge said he wanted to 'express the American myth' and to 'write the American republic' (quoted from John "
  "Leggett). The Civil War is its defining event, as it was for the country; turning points in the hero's life "
  "fall on the Fourth of July; his search for the golden raintree joins private desire to national legend; and the "
  "Southern marriage carries the sectional conflict into the home.",
  structure="Two parts, before and after the Civil War, framed by one day, 4 July 1892, with flashbacks, dream "
  "sequences and departures from linear narrative; about 400,000 words in the published text. A frontispiece map "
  "shows the meandering Shawmucky River spelling the hero's initials (Wikipedia).",
  style="Expansive, rhapsodic prose that moves between realist chronicle and surreal passages; Howard Mumford Jones "
  "praised its 'jerky and sometimes magnificent vitality' and an 'ingenuity of structure that is at once admirable "
  "and maddening' (Saturday Review, quoted by Wikipedia).",
  ctx="Written in Boston and Bloomington between 1943 and 1947, while Lockridge, found unfit for military service "
  "in 1944, said he let his hero 'bleed for me' in the Civil War. Revisions for the publisher and for MGM reduced "
  "the typescript from 600,000 to 450,000 words, and at the Book-of-the-Month Club's request three words of the "
  "Perfessor's ('Wasn't Jesus God's?') were removed after 5,000 copies of a first printing of 50,000 had been run "
  "off (Wikipedia). Waycross is based on Straughn, Indiana, and the county on Henry County.",
  sig="A New York Times bestseller (Post45) that the Times reviewer called 'a huge and extraordinary first novel ... "
  "an achievement of art and purpose', while Hamilton Basso in the New Yorker called it 'just the sort of plump "
  "turkey that they bake to a turn in Hollywood'. MGM filmed it in 1957 with Montgomery Clift and Elizabeth Taylor, "
  "and some have counted it a 'Great American Novel' (Wikipedia).",
  chars="John Wickliff Shawnessy; the 'Perfessor', Jerusalem Webster Styles",
  biblio="Boston: Houghton Mifflin, 5 January 1948 (released 4 January); 1,066 pages, with a map by John V. Morris "
  "after the author's sketch; first printing of 50,000 copies, of which the first 5,000 keep the three words later "
  "removed (Wikipedia).",
  notes="Not read. Wikipedia's article on the novel carries no footnotes (flagged January 2024); its outline was "
  "accepted only where the sourced article on Lockridge agrees. The names of the hero's wife, first love and rival "
  "are not given in the sources consulted and are not supplied. Whether the long concluding dream sequence planned "
  "in 1943 survived the cuts was not established. The Atlantic's review of February 1948, cited by Wikipedia, "
  "could not be opened (HTTP 403).",
  ver="partially verified", sources=[WIKI_RAINTREE, WIKI_LOCKRIDGE, NYT]),

W10("Mister Roberts", TH, "1946", "Novel", "significant",
  genres=G("War Novel"),
  themes=T(WAR, POWER),
  overview="Heggen's only novel, published by Houghton Mifflin in 1946: a loosely connected sequence of episodes "
  "set almost entirely aboard the USS Reluctant, a Navy cargo ship in the rear areas of the Pacific war, whose "
  "first lieutenant, Douglas Roberts, shields the crew from the petty tyranny of the captain while asking every "
  "month to be transferred to combat (Wikipedia).",
  content="Episodes of shipboard life on the Reluctant, built around Lieutenant (junior grade) Doug Roberts, "
  "Captain Morton and the crew, ending with Roberts's transfer to a destroyer and his death in action.",
  summary="Douglas Roberts joined the Navy expecting to serve on a destroyer or a cruiser, and was assigned first to "
  "a tanker in the Atlantic and then to the USS Reluctant, AK-601, a cargo ship that ferries supplies to backwater "
  "Pacific bases. As first lieutenant he is responsible for the whole ship apart from its engine spaces, and he "
  "hates it. Every month he submits a request for transfer, and every month Captain Morton forwards it without "
  "recommending approval; Roberts is the balance wheel between the captain's unreasonable behaviour and the crew's "
  "frustration at serving in 'this bucket'. The chapters show life on an auxiliary in the rear areas: a very new "
  "ensign finding his feet aboard a casual ship; a feud between two officers bred by months of boredom; what "
  "happens when men who have had no liberty for more than a year anchor off an island whose naval hospital has "
  "nurses and no shades on the windows; and the liberty granted to half the crew when the ship delivers cargo to "
  "the port of Elysium. In the last chapter Roberts's transfer comes through; the crew show their affection as he "
  "leaves for the United States and a new destroyer, on which he is killed in action (Wikipedia).",
  themes_text="The comedy and frustration of men who feel 'left out' of the war, sailing, in Heggen's phrase, 'from "
  "Tedium to Apathy and back again, with an occasional side trip to Monotony'; authority abused by a petty tyrant "
  "and resisted by a decent officer; the loyalty between that officer and his men; and the irony that Roberts, "
  "released at last into the fighting he wanted, is killed.",
  structure="A series of episodes merged from short stories Heggen had written aboard ship, with an introductory "
  "chapter added for the book; Roberts and the ship hold it together (Wikipedia).",
  style="Plain, colloquial narration with barracks humour and comic set pieces, darkening in the final chapter; "
  "Joshua Logan's stage version emphasised its farcical elements while keeping its serious undertones (Wikipedia).",
  ctx="Heggen drew on fourteen months as assistant communications officer of the cargo ship USS Virgo and on "
  "service in the USS Rotanin. The captain of the stage and screen versions was modelled on the Virgo's captain, "
  "the Naval Reserve lieutenant commander Herbert Ezra Randall, who owned two palm trees; Heggen, like the "
  "characters Doug Roberts and Ensign Pulver, threw them over the side (Naval History, quoted by Wikipedia). Houghton Mifflin "
  "replaced his title, The Iron-Bound Bucket.",
  sig="It sold over a million copies despite mixed reviews and was a New York Times bestseller (Post45). The play "
  "Heggen made from it with Joshua Logan won the first Tony Award for Best Play (1948), and the story was filmed "
  "in 1955, made into a television series (1965-66) and remade for television in 1984; Lewis Nichols wrote in the "
  "New York Times that as a novel it 'won a few million friends' (Wikipedia).",
  chars="Lieutenant (junior grade) Douglas Roberts; Captain Morton; the crew of the Reluctant",
  biblio="Boston: Houghton Mifflin, 1946; 189 pages, illustrated by Samuel Hanks Bryant (Wikipedia; OCLC "
  "51762498). The play version, by Heggen and Joshua Logan, was published by Random House, New York, in 1948.",
  notes="Not read. Wikipedia's plot section is unreferenced; the article on Heggen speaks of 'the fictional Captain "
  "Morton of the movie and dramatizations', so whether the novel itself names the captain Morton was not "
  "confirmed. The play, written with Logan, is not recorded until Logan has a record.",
  ver="partially verified", sources=[WIKI_ROBERTS, WIKI_HEGGEN, WIKI_ROBERTS_PLAY, NYT]),

W10("The Gallery", JHB, "1947", "Novel", "significant",
  genres=G("War Novel"),
  themes=T(WAR, SEX, POWER),
  overview="Burns's first novel, published by Harper & Brothers in 1947 and a bestseller: a picture of "
  "Allied-occupied North Africa and Naples in 1944, built from portraits of nine characters, all of whom pass "
  "through the Galleria Umberto I, the Naples shopping arcade of the title, interspersed with eight recollections "
  "narrated by an anonymous American soldier (Wikipedia).",
  content="Nine portraits of soldiers and civilians in and around the Galleria Umberto, alternating with eight "
  "recollections in which an anonymous GI follows a route from North Africa to Naples much like Burns's own.",
  summary="The book moves between two kinds of chapter. In the eight recollections an unnamed American soldier "
  "follows a route through North Africa to Naples much like the one Burns took, and gives his first assessment of "
  "how the Americans treat the Neapolitans, a chapter later reprinted in The Vintage Book of War Fiction (1999). "
  "The nine portraits show characters whose paths cross in the Galleria Umberto, and through them the book takes "
  "up the average man's resentment of the military and his struggle to keep his individuality within the war "
  "effort; the friction between officers and enlisted men; the psychological effects of dislocation; the economic "
  "and social gulf between the Americans and the people they have defeated; the experience of homosexual "
  "servicemen, in a chapter set in what Time called 'a homosexuals' hangout'; and the popular life of Naples under "
  "occupation (Wikipedia, drawing on Andrew Huebner). One chapter, 'Queen Penicillin', was anthologised as a short "
  "story. William Zinsser summed up its moral question: 'who was more degraded: the Italians hustling to feed their "
  "families, or the GIs selling their cheaply bought PX goods at a huge profit?'",
  themes_text="War as the degradation of occupier and occupied alike; the individual against the military machine; "
  "inequality between victors and vanquished; homosexual life in the wartime army; and the American as an "
  "uncomfortable conqueror, a role that, Frederic Morton wrote in 1956, no really distinguished novel except "
  "possibly The Gallery had recorded (Wikipedia).",
  structure="Nine portraits interspersed with eight recollections by an anonymous narrator; the Galleria, through "
  "which all the main characters pass, gives the book its unity of place and its title (Wikipedia).",
  style="Paul Fussell wrote that Burns 'relied on discontinuity, like a sort of prose T. S. Eliot, thus suggesting "
  "incoherence as a contemporary social characteristic'; Charles Poore found 'a rancorously vivid portrait' of 'the "
  "mentally and morally lost', and a 1949 survey in Military Affairs praised its rendering of soldiers' speech "
  "(Wikipedia).",
  ctx="Burns served in military intelligence in Casablanca and Algiers and then in Naples, where he censored "
  "prisoner-of-war mail, and finished the book at the Loomis School in April 1946 (Wikipedia). A plan of 1959-60 "
  "for an Italian neorealist film of it was postponed when its makers argued over its unflattering picture of both "
  "Neapolitans and Americans.",
  sig="The Saturday Review called it 'the best war book of the year'; Hemingway, Edmund Wilson and John Dos Passos "
  "praised it, and it was a New York Times bestseller (Post45). By 1991 Herbert Mitgang called it 'that forgotten "
  "gem of a novel'; New York Review Books reissued it in 2004 with Fussell's introduction, and William Zinsser "
  "called it 'the proto-Vietnam novel' (Wikipedia).",
  biblio="New York: Harper & Brothers, 1947 (Wikipedia). Reissued several times, by New York Review Books Classics "
  "in 2004 with an introduction by Paul Fussell.",
  notes="Not read. The portraits' subjects are not named in the sources consulted and are not supplied; reader "
  "reviews that name them are not used.",
  ver="partially verified", sources=[WIKI_BURNS, NYT]),

W10("Lucifer with a Book", JHB, "1949", "Novel", "minor",
  genres=G("Satirical Fiction"),
  themes=T(EDU, WAR),
  overview="Burns's second novel, published by Harper on 30 March 1949: a satire of an American private school, "
  "Miss Sophia's Academy, much like the Loomis School where he taught, and 'perhaps the most savagely attacked book "
  "of its day', in Gore Vidal's words (Wikipedia; Kirkus).",
  content="Two teachers at Miss Sophia's Academy, the disfigured veteran Guy Hudson and the former WAC Betty "
  "Blanchard, set themselves against the venality and hypocrisy of Mr. Pilkey and his like, among staff and pupils "
  "alike.",
  summary="At Miss Sophia's Academy, a school run, as the Atlantic's reviewer put it, by reactionary trustees and "
  "principals 'as if it were a corporation', two teachers, Guy Hudson, a disfigured veteran and 'a sort of smashed "
  "idealist', and Betty Blanchard, a former WAC and a beautiful language teacher, try to resist the venality, "
  "sadism and bootlicking of staff and students, the toadying to wealthy parents, the glorification of sport over "
  "study and the reliance on tests in place of humane learning. They come to grief, but they find each other and "
  "keep their faith in their vocation, hoping to teach somewhere free of the school's hypocrisy, intolerance, greed "
  "and fear (Kirkus; the Atlantic).",
  themes_text="The corruption of American private education by money, snobbery, athletics and testing; the "
  "returning veteran's disillusion; and adolescent sexuality, which both reviewers found overdrawn. Kirkus missed the "
  "compassion of The Gallery in a book that was 'all anger and violence and hate'.",
  structure="Built around the two teachers' resistance and their love, with a cast of staff and pupils that Kirkus "
  "found 'more than life size in their grotesqueries'.",
  style="Biting, overwritten satire: Kirkus granted Burns 'a sense of drama' and scenes the reader would not forget "
  "but found the characters 'mainly caricatures'; the Atlantic found 'a number of biting portraits' smothered by "
  "stereotypes and 'righteous indignation'.",
  ctx="Burns returned to teach at Loomis after the war, and the novel's school is much like it (Wikipedia). It "
  "appeared to largely unfavourable reviews; James Michener later wrote that never in his memory had critics 'come "
  "so close to total annihilation of an author's work'.",
  sig="A New York Times bestseller (Post45) despite its reviews. Its failure sent Burns back to Italy in 1950, and "
  "Hemingway later dismissed it as 'a stinking book about a prep school' (Wikipedia).",
  chars="Guy Hudson; Betty Blanchard; Mr. Pilkey",
  canon="Minor canon",
  biblio="New York: Harper, 30 March 1949 (Kirkus).",
  notes="Not read. The plot comes from two contemporary reviews, Kirkus (issue of 1 March 1949) and the Atlantic "
  "(April 1949), both seen as search-result text; Kirkus's full review appeared in the result. Mr. Pilkey's post "
  "at the school is not stated.",
  ver="partially verified", sources=[KIRKUS_LUCIFER, ATLANTIC_LUCIFER, WIKI_BURNS, NYT]),

W10("A Cry of Children", JHB, "1952", "Novel", "minor",
  genres=G("Literary Novel"),
  themes=T(LOVE, FAMILY, SEX),
  overview="Burns's third and last novel, written in Florence and published by Harper on 3 September 1952: a love "
  "affair between a young musician and an amoral girl, marketed as 'a merciless novel' of 'young love in the "
  "bohemian fringe-world' (Wikipedia; Kirkus).",
  content="The affair of David, a sensitive, emotionally immature musician restless after the war, and Isobel, told "
  "in turn from his viewpoint, hers and that of his possessive Back Bay mother.",
  summary="David, a young musician, restless after the war, falls into an affair with Isobel, a girl Kirkus calls "
  "cheap, ruthless and utterly amoral. Her brother, who has designs of his own on David's unstable sexuality, "
  "brought the two together and hates himself for it. The story shifts its viewpoint from David to Isobel and "
  "finally to David's mother, an intensely possessive and suspicious Back Bay Boston matron, as the lovers pass "
  "through passion, disillusionment and distaste to the irony of their incompatibility (Kirkus). Wikipedia's "
  "sources think the principal character, a composer and pianist, was modelled on Burns's Harvard classmate Irving "
  "Fine.",
  themes_text="Destructive love and sexual ambiguity; a mother's possessiveness; the 'phoney Bohemianism' Kirkus "
  "found in its milieu; lovers who cannot escape one another, as the title of the New York Times review, 'No Way "
  "Out for Isobel', suggests.",
  structure="Three successive viewpoints, David's, Isobel's and his mother's (Kirkus).",
  style="Kirkus granted Burns 'the gift for biting satire, crude drama' but found the characters puppets moved by "
  "the author 'as deus ex machina'; the New York Times reviewer saw 'excessive malice and nightmarish distortions'.",
  ctx="Written in Florence, where Burns settled in 1950 after the failure of Lucifer with a Book; it was his last "
  "published work, and a fourth novel was unfinished when he died in 1953 (Wikipedia).",
  sig="Badly reviewed, though James Kelly in the New York Times thought it 'reaffirms the author's status as one of "
  "America's gifted young writers' (Wikipedia); Kirkus called it a betrayal of Burns's gifts.",
  chars="David; Isobel; Isobel's brother; David's mother",
  canon="Minor canon",
  biblio="New York: Harper, 3 September 1952 (Kirkus). Wikipedia's list of Burns's works dates it 1951; its text, "
  "the New York Times review of 7 September 1952 and Kirkus give 1952.",
  notes="Not read. The plot comes from Kirkus (read directly); Wikipedia adds the possible model for the hero.",
  ver="partially verified", sources=[KIRKUS_CRY, WIKI_BURNS]),

W10("The Living Is Easy", DW, "1948", "Novel", "significant",
  genres=G("Social Novel", "Domestic Fiction"),
  themes=T(CLASS, RACE, FAMILY, GENDER),
  overview="West's first novel, published by Houghton Mifflin on 13 May 1948. Set in Boston from 1914, it follows "
  "Cleo Jericho Judson, a beautiful, mixed-race Southern woman who dominates her family in pursuit of position "
  "among the city's Black elite, and is often read as a satire of the Black bourgeoisie (Wikipedia; Kirkus).",
  content="Cleo Judson's marriage to Bart, an older, financially secure businessman, her campaign for money and "
  "social standing, and her bringing of her three sisters north to live with her, at the cost of their homes and "
  "marriages.",
  summary="Cleo Judson, a Southern-born beauty with 'sins of pride and power', has married Bart, an older, "
  "financially secure man, and in Boston she sets out to win the money and social position she craves among the "
  "'blue-white' Black people of the city, with their keen sense of caste superiority and gentility (Kirkus; "
  "Wikipedia). She milks her husband insistently and, telling herself it is for their own sakes, brings her three "
  "sisters north from the South with their husbands to live with her; dependent on Cleo, the sisters forfeit their "
  "homes, and all their marriages break apart (Kirkus; Gale entries). Around her move Simeon, a Harvard "
  "intellectual dedicated to his race, who marries 'the Duchess', once the sporting woman of Boston's first "
  "families, and his sister Thea (Kirkus). Cleo's domination brings ruin on the family members under her control "
  "and finally on herself (Gale). The title echoes 'Summertime' from Porgy and Bess (Wikipedia, citing Cynthia "
  "Davis).",
  themes_text="Class and colour in Black Boston: Kirkus called the book 'an uncompromising if often compassionate "
  "portrait of the inheritance of color warring against acquired notions of breeding and betterment', a circle "
  "'hoping for assimilation and advancement'. Cleo's will to power overturns the expected roles of wife and mother; "
  "Trudier Harris praised her complexity as a heroine who 'defies any easy categorization', and Cherene "
  "Sherrard-Johnson's article reads space, property and identity in the novel (Wikipedia).",
  structure="A narrative centred on Cleo and the household she gathers in Boston from 1914, with a wider circle of "
  "the city's Black society around it (Kirkus; Wikipedia).",
  style="Ironic humour, which Wikipedia calls characteristic of West; Seymour Krim wrote in the New York Times that "
  "it was 'a housewifey novel' whose characters were women first and Black second, with 'abundant and special "
  "woman's energy and beat'. Harris found West's writing stylistically limited.",
  ctx="Written at Oak Bluffs on Martha's Vineyard, where West settled in the mid-1940s, and drawn from her own "
  "affluent Boston family: Cleo is thought to be modelled on her mother, Rachel (Wikipedia). It was well reviewed; "
  "Wikipedia says it sold few copies, while one Gale entry calls it a modest financial success. West published no "
  "other novel for almost fifty years.",
  sig="Reissued by the Feminist Press in 1982, it has since been studied by Trudier Harris, Cherene "
  "Sherrard-Johnson and Jewelle Gomez for its nuanced portrayal of Black womanhood and of an upper-middle-class "
  "Black community (Wikipedia). Cynthia Davis attributes its long neglect to a subject that places it 'outside the "
  "black vernacular tradition' of Petry, Wright and Baldwin.",
  chars="Cleo Jericho Judson; Bart Judson; Cleo's three sisters; Simeon; the Duchess; Thea",
  biblio="Boston: Houghton Mifflin, 13 May 1948 (Kirkus); reissued New York: Feminist Press, 1982 (Wikipedia; one "
  "of the Gale entries gives a Feminist Press paperback of 1987).",
  notes="Not read. Wikipedia's article has no plot section; the plot comes from Kirkus's review of 1948 (seen as "
  "search-result text) and Gale entries on Encyclopedia.com (search extracts only). Kirkus places the story at the "
  "turn of the century, Wikipedia in 1914. Details found only in blogs and in an unauthorised online copy of a "
  "biography are not used.",
  ver="partially verified", sources=[WIKI_LIVING, KIRKUS_LIVING, GALE_WEST, WIKI_WEST]),

W10("The Wedding (Dorothy West)", DW, "1995", "Novel", "significant",
  genres=G("Family Saga", "Social Novel"),
  themes=T(RACE, CLASS, FAMILY, LOVE),
  overview="West's second novel, published by Doubleday on 6 January 1995, almost fifty years after her first and "
  "when she was in her late eighties. It is set over a weekend in 1953 in the Oval, a Black bourgeois community "
  "on Martha's Vineyard, as Shelby Coles prepares to marry a white jazz musician, and it recounts the Coles "
  "family's history across generations (Kirkus; Wikipedia).",
  content="The eve of Shelby Coles's wedding to a white musician: the dismay of the Oval and of her family, the "
  "family history, and the intervention of Lute McNeil, who wants to marry Shelby himself.",
  summary="It is 1953, and in the Oval, a community of the Black bourgeoisie on Martha's Vineyard, Shelby Coles is "
  "preparing to marry a white jazz musician; the Oval's residents are dismayed that someone 'who could have had "
  "her pick of the best of breed in her own race' should marry outside it (Kirkus). West then recounts the Coles "
  "family history. As a child Shelby once got lost, and because of her light skin the people who found her could "
  "not tell that she was the child being sought; asked point-blank whether she was 'colored', she answered, 'I "
  "don't know.' Her sister Liz has married a dark-skinned doctor and borne an equally dark daughter, whom their "
  "light-skinned grandmother spurns. Their father has kept up a long affair while maintaining appearances with his "
  "wife, but his mistress, about to turn forty, has decided to marry someone else. Another islander, Lute McNeil, "
  "who has three daughters by three different white women, decides that he should be the one to marry Shelby. Her "
  "father has reproached her for never seriously considering Black men; on the night before the wedding she agrees "
  "to meet Lute, and a tragedy follows, which Kirkus found random (Kirkus). Although the action occupies a "
  "weekend, the novel traces the family's history over centuries (Wikipedia).",
  themes_text="Colour and class within Black America, where shades of skin decide standing even inside one family; "
  "marriage across the colour line in the early 1950s; the weight of family history; and the wish to belong that "
  "drives Lute, whose reasons Kirkus found 'never clear beyond a vague desire to be a legitimate part of the "
  "Oval'.",
  structure="The present action covers the weekend of the wedding; long retrospective sections recount the "
  "family's history over generations before the story returns to the eve of the wedding (Kirkus; Wikipedia).",
  style="Kirkus found it 'written with the sure hand of a practiced short-story writer', its episodes 'full of "
  "interesting detail', but lacking 'the resonance of a deeply layered novel'.",
  ctx="West dedicated the book to Jacqueline Kennedy Onassis, who as an editor at Doubleday had encouraged her to "
  "finish it; the attention that followed the Feminist Press reissue of The Living Is Easy (1982) and her "
  "inclusion in Margaret Busby's anthology Daughters of Africa (1992) led to its completion (Wikipedia).",
  sig="Its success made West, one of the last surviving members of the Harlem Renaissance, a public figure in her "
  "late eighties; Oprah Winfrey adapted it as a two-part television miniseries in 1998, and Doubleday followed it "
  "with The Richer, the Poorer (Wikipedia; Gale entries).",
  chars="Shelby Coles; Liz; their parents; Lute McNeil",
  alt=["The Wedding"],
  biblio="New York: Doubleday, 6 January 1995; 208 pages; ISBN 0-385-47143-2 (Kirkus).",
  notes="Not read. The title is qualified with the author's name because James Shirley's play The Wedding (1626) "
  "is already in the database. The plot comes from Kirkus's review (issue of 1 November 1994, seen as search-result "
  "text). The fiance's name is given only by reader reviews and catalogue blurbs, which are not used.",
  ver="partially verified", sources=[KIRKUS_WEDDING, WIKI_WEST, GALE_WEST]),

W10("The Richer, the Poorer: Stories, Sketches, and Reminiscences", DW, "1995", "Short-story collection", "minor",
  genres=G("Short-Story Collection", "Personal Essay"),
  themes=T(CLASS, RACE, CHILD),
  overview="A collection of thirty stories, sketches and reminiscences spanning almost seventy years of West's "
  "writing, from 'The Typewriter' (1926) onwards, published by Doubleday on 1 July 1995 after the success of The "
  "Wedding; some pieces had not been published before (Kirkus; Gale entries).",
  content="Stories, many told from a child's point of view, of Black families in Boston, Harlem and Martha's "
  "Vineyard, with autobiographical sketches and portraits.",
  summary="The fiction includes 'The Typewriter', the prize-winning story West wrote at seventeen, and the widely "
  "anthologised 'Jack in the Pot' (1940) (Gale); 'The Five-Dollar Bill', whose young protagonist, with parents "
  "living apart, sees childhood as 'full of unrequited love, and suffering, and tears'; 'Funeral', a child's view "
  "of the greed and guilt on show at an uncle's funeral; and 'The Happiest Year, The Saddest Year', about a girl's "
  "anger at the death of her dark-complexioned cousin. Shades of blackness and their social consequences recur. "
  "The nonfiction portrays West's entrepreneurial father and the women of her family, recounts an encounter with "
  "Sergei Eisenstein and profiles Wallace Thurman (Kirkus); pieces from the Vineyard Gazette are included (Gale).",
  themes_text="Colour and class within Black families; poverty and the indignities of relief; children's discovery "
  "of adult failings; and memory of family and of the Harlem Renaissance.",
  structure="Thirty pieces, fiction and nonfiction, written over almost seventy years (Kirkus).",
  style="Kirkus praised West as 'a moralist and social observer, sensitive to the slippery slope of vice and the "
  "indignities of poverty', at her best in stories told from a young girl's point of view.",
  ctx="Doubleday published it in the wake of The Wedding, gathering early stories with unpublished work (Gale "
  "entries).",
  sig="Kirkus called it 'a first-rate collection'; a Gale entry describes it as the cross-section of the short "
  "fiction that was the mainstay of her career.",
  canon="Minor canon",
  alt=["The Richer, the Poorer"],
  biblio="New York: Doubleday, 1 July 1995; 272 pages; ISBN 0-385-47145-9 (Kirkus).",
  notes="Not read. The contents come from Kirkus (search-result text) and Gale entries (search extracts). One Gale "
  "entry dates the collection 1998, against 1995 in Kirkus and the other entries. Its pieces first published "
  "before 1946 are not recorded individually in installment 9.",
  ver="partially verified", sources=[KIRKUS_RICHER, GALE_WEST]),

W10("Last of the Conquerors", WGS, "1948", "Novel", "minor",
  genres=G("Social Novel"),
  themes=T(RACE, WAR, LOVE),
  movements=M(PROTEST),
  overview="Smith's first novel, published by Farrar, Straus in 1948, when he was twenty-one, and drawn from his "
  "service as a clerk-typist in occupied Berlin: an African American soldier's love affair with a German woman in "
  "the segregated US Army of occupation (Wikipedia).",
  content="Hayes Dawkins, a Black GI in occupied Germany, and Ilse, a white German woman, struggle to sustain their "
  "relationship against racist officers and Army policy.",
  summary="Hayes Dawkins, an African American GI serving in the racially segregated US Army in occupied Germany "
  "after the Second World War, has an affair with Ilse, a white German woman. The two struggle against racist Army "
  "officers and policies to keep up a relationship that some white soldiers condemn, though many friendly whites "
  "help them. The novel presents post-Nazi Germany as more racially tolerant than the United States (Wikipedia).",
  themes_text="Racism in the American army and at home set against the apparent tolerance of defeated Germany; "
  "Wikipedia reads the book as a critique of Marshall Plan rhetoric presenting American society as a model for the "
  "world while African Americans lived under Jim Crow.",
  structure="The story follows Dawkins's service and love affair in occupied Germany; its narrative form is not "
  "described in the sources consulted.",
  style="Realist fiction of the protest tradition with which Wikipedia associates Smith; Kirkus reviewed it on 1 "
  "June 1948, as its review of South Street records, but that review was not seen.",
  ctx="Smith was drafted in January 1946 and posted to Berlin as a clerk-typist; Gollancz published the novel in "
  "London in 1949 (Wikipedia). It appeared in the year President Truman ordered the desegregation of the armed "
  "forces (general historical date).",
  sig="The book that began Smith's career; Wikipedia names it with The Stone Face as his notable works, and Alexa "
  "Weik von Mossner wrote its entry in the Literary Encyclopedia (2009).",
  chars="Hayes Dawkins; Ilse",
  canon="Minor canon",
  biblio="New York: Farrar, Straus, 1948; London: Gollancz, 1949 (Wikipedia).",
  notes="Not read. Wikipedia's article is a stub flagged for more citations; it cites Weik von Mossner's Literary "
  "Encyclopedia entry, which was not consulted.",
  ver="partially verified", sources=[WIKI_CONQUERORS, WIKI_WGS]),

W10("South Street", WGS, "1954", "Novel", "minor",
  genres=G("Social Novel", "Political Novel"),
  themes=T(RACE, VIOLENCE, LOVE, CITY),
  movements=M(PROTEST),
  overview="Smith's third novel, published by Farrar, Straus and Young on 11 October 1954: a portrait of the Black "
  "community of Philadelphia's South Street, drawn from the neighbourhoods of his childhood, that Wikipedia counts "
  "among the first Black militant protest novels (Wikipedia; Kirkus).",
  content="Lives in South Street's Black community, among them the blues singer Lil and the three Bowers brothers, "
  "sworn to avenge their father's death by hating whites, one of whom marries a white violinist.",
  summary="On Philadelphia's South Street the paths of a Black community's members cross: Lil, a blues singer whose "
  "anger has led her to live off men, and who finally commits murder when her true loyalties are roused; and the "
  "Bowers brothers, pledged to avenge their father's death by actively hating whites: Michael, the desperate one, "
  "Philip, the dreamer, and Claude, the famous one, whose own people plague him as much as the more threatening "
  "whites do when he marries Kristin, a white girl and a violinist. Their love faces pressures impossible to "
  "withstand, and, still loving each other, they part, Claude to work for his people and Kristin to play her "
  "violin (Kirkus).",
  themes_text="Interracial contact and strain, the subject Kirkus saw it share with Last of the Conquerors; hatred "
  "as a pledge of loyalty; the cost of interracial love; and individuals caught up in group conflict.",
  structure="Several strands follow members of the community, with the Bowers brothers and Claude's marriage at the "
  "centre (Kirkus).",
  style="Kirkus found that 'tenderness and violence commingle' in a novel with 'some measure of force in its "
  "characters and its relentless portrayal of individuals caught up in group conflicts'.",
  ctx="Published in 1954, as Smith, by then in Paris, joined Agence France-Presse; it draws on his childhood in the "
  "Black neighbourhoods of Philadelphia (Wikipedia).",
  sig="Wikipedia counts it among the first Black militant protest novels; the New York Amsterdam News recalls "
  "lukewarm reviews, after which Smith felt he had 'come to a dead end' on 'the road of protest' (search extract).",
  chars="Lil; Michael, Philip and Claude Bowers; Kristin",
  canon="Minor canon",
  biblio="New York: Farrar, Straus and Young, 11 October 1954 (Kirkus; Wikipedia).",
  notes="Not read. The plot comes from Kirkus (search-result text). The New York Amsterdam News describes the book "
  "as about a Black radical returned from Africa, which matches nothing in Kirkus's account and is not followed.",
  ver="partially verified", sources=[KIRKUS_SOUTH, WIKI_WGS, AMNEWS]),

W10("The Stone Face", WGS, "1963", "Novel", "significant",
  genres=G("Political Novel"),
  themes=T(RACE, EXILE, VIOLENCE, HOLOCAUST),
  overview="Smith's fourth and last novel, published by Farrar, Straus on 7 November 1963 and described by its "
  "publisher in 2021 as a roman a clef: an African American journalist who has fled racist violence in "
  "Philadelphia finds freedom in Paris, then recognises in the treatment of Algerians the racism he escaped. It is "
  "one of the earliest published accounts of the Paris massacre of 17 October 1961 (Kirkus; New York Review "
  "Books; Wikipedia).",
  content="Simeon Brown, a Black American journalist who lost an eye in a racist attack as a teenager, settles in "
  "Paris, falls in love with a Polish actress who survived the concentration camps, befriends Algerians, joins "
  "them in a riot, and finally leaves to become a teacher.",
  summary="As a teenager in Philadelphia Simeon Brown lost an eye in a racist attack, and the young journalist has "
  "lived ever since in a state of agonising tension; after a violent encounter with white sailors he moves to "
  "Paris, known as a haven for Black artists and intellectuals, where he can go where he pleases without fear (New "
  "York Review Books). Through Babe, another Black American emigre, he makes friends among the interracial "
  "expatriates and falls in love with a Polish actress, who proves to be Jewish and to have spent her childhood in "
  "concentration camps (NYRB; Kirkus). Through chance-met Algerians, treated more brutally in Paris than Black "
  "people in America, he slowly comes to see race hatred, the 'stone face' of the title, as universal and "
  "irrational rather than personal, its victims changing from country to country, and his expatriate friends begin "
  "to pall. Simeon joins the Algerians in a riot; finally, 'no longer an escapist nor a member of a separate race', "
  "he leaves to become a teacher (Kirkus). Wikipedia, citing Kristin Ross, calls the novel's account of the Paris "
  "massacre of 17 October 1961 one of the earliest eyewitness representations of it, though fictionalised.",
  themes_text="The universality of race hatred, seen by a Black American who finds that in France he is simply an "
  "American while the Algerians bear the racism he fled; bystander guilt and solidarity, the subject of Alexa Weik "
  "von Mossner's chapter on Smith; the memory of the Holocaust carried by his lover; and the choice between "
  "personal freedom and political engagement.",
  structure="Follows Simeon from the violence that drives him out of Philadelphia, through his life among "
  "expatriates and Algerians in Paris, to his decision to leave (Kirkus; NYRB).",
  style="Kirkus called it 'somewhat didactic, naive, but basically quite interesting', its 'rather flat prose' "
  "redeemed by 'some fine oblique scenes and a few shocking comparisons between various ghettos, concentration "
  "camps, riots and tortures'.",
  ctx="Smith began the novel in 1961, when the Algerian War had inflamed passions in France, and drew on the "
  "anti-Arab racism he witnessed as a journalist and in the streets of Paris; Kristin Ross writes that it was "
  "published in the United States because it could not be published in France (Wikipedia).",
  sig="Ross notes that it remained one of the few representations of 17 October 1961 available until the early "
  "1990s, when the children of North African immigrants began to demand information about the event. Kirkus called "
  "it 'a thought-provoking and an oddly humanizing and liberating book', and New York Review Books reissued it in "
  "2021 with an introduction by Adam Shatz (Wikipedia; Kirkus).",
  chars="Simeon Brown; Babe; the Polish actress; Simeon's Algerian friends",
  biblio="New York: Farrar, Straus, 7 November 1963 (Kirkus; Wikipedia); New York Review Books Classics, 2021, "
  "introduction by Adam Shatz (ISBN 978-1-68137-516-8).",
  notes="Not read. The plot comes from Kirkus (issue of 1 November 1963; search-result text) and the 2021 "
  "publisher's description (search extract). Kirkus's web page heads the review 'HE STONE FACE', a typing error. "
  "The novel is not linked to the protest movement entry, whose span (1945-1965) it falls within but whose "
  "American focus it leaves behind.",
  ver="partially verified", sources=[KIRKUS_STONE, NYRB_STONE, WIKI_WGS]),
]
