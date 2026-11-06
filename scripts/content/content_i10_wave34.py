"""Installment 10, wave 34: ten American authors, and the bulk of the remaining gaps.

The English volume is already complete (96 of 96 in-scope selections; see wave 33 and
the correction recorded there). This wave takes the American volume's largest
outstanding authors in one pass - Anzaldua, Walker, Wilson, O'Brien, Komunyakaa,
Spiegelman, Alvarez, Harjo, Alexie and Dove - and records the works their selections
come from rather than one poem per author. Eleven works by ten authors close
sixteen anthology rows, eleven of them Komunyakaa's five and Dove's ten.

Three of the rows this wave closes carried no date at all in the Norton list, and all
three are settled here: Harjo's "White Bear" is from She Had Some Horses (Thunder's
Mouth Press, 1983), where the contents of How We Became Human (2004) place it;
Alexie's "Pawn Shop" and "At Navajo Monument Valley Tribal School" are from The
Business of Fancydancing (Hanging Loose Press, 1992); and Komunyakaa's "Nude Study"
appeared in Poetry in the winter of 1992 before being gathered in Taboo (2004) - which
is why the record dates the poem 1992 and names the 2004 book separately, rather
than either inventing an earlier collection or declaring the selection out of period.

Dove's three Adolescence poems and three Thomas and Beulah pieces are printed as six
rows but belong to two books, so the wave records The Yellow House on the Corner
(1980) and Thomas and Beulah (1986) and lets those records answer their rows.

First printings used here:

    Anzaldua, Borderlands/La Frontera    Aunt Lute Books, 1987
    Walker, "Everyday Use"               In Love & Trouble (Harcourt, 1973)
    Walker, "In Search of Our Mothers' Gardens"  Ms., 1974; collected 1983
    Wilson, Fences                       performed 1985; Plume/NAL, 1986
    O'Brien, "How to Tell a True War Story"  Esquire, October 1987; The Things They Carried, 1990
    Komunyakaa, "Facing It"              Dien Cai Dau (Wesleyan, 1988)
    Komunyakaa, "Slam, Dunk, & Hook"     Callaloo 14.3 (Summer 1991); Magic City, 1992
    Komunyakaa, "My Father's Love Letters"  Magic City (1992)
    Komunyakaa, "Nude Study"             Poetry (Winter 1992); Taboo, 2004
    Spiegelman, Maus                     RAW 1980-91; Pantheon, 1986 and 1991
    Alvarez, !Yo!                        Algonquin, 1997
    Harjo, "Call It Fear" / "White Bear"  She Had Some Horses (1983)
    Harjo, "Summer Night"                In Mad Love and War (Wesleyan, 1990)
    Harjo, "The Flood"                   The Woman Who Fell from the Sky (Norton, 1994)
    Dove, "Geometry"                     The Yellow House on the Corner (1980)
    Dove, "Parsley" / "Poem in Which I Refuse Contemplation"  Museum (1983)
    Dove, Thomas and Beulah poems        Thomas and Beulah (1986)
    Alexie, "Pawn Shop" / "At Navajo Monument Valley Tribal School"  The Business of Fancydancing (1992)
    Alexie, "Sister Fire, Brother Smoke"  The Summer of Black Widows (1996)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from i10_lib import A10, W10, G, T, M, MAJ, SEC, NAEL, NAAL  # noqa: E402

GA = "Gloria Anzaldúa"
AW = "Alice Walker"
AWIL = "August Wilson"
TOB = "Tim O'Brien"
YK = "Yusef Komunyakaa"
AS = "Art Spiegelman"
JA = "Julia Alvarez"
JH = "Joy Harjo"
SA = "Sherman Alexie"
RD = "Rita Dove"

CHIC = "Chicano Movement Literature"
AFAM = "Postwar African American Writing: Protest and Its Critics"
BLACKARTS = "Black Arts Movement"
NAR = "Native American Renaissance"
POSTCOL = "Postcolonial Literature"
POSTMOD = "Postmodernism and Postmodern Fiction"
FEM = "Second-Wave Feminist Writing"
CONF = "Confessional Poetry"
PERF = "Performance and Spoken-Word Poetry"

W_GA = "Gloria Anzaldúa (Wikipedia; Poetry Foundation author page)"
BORDER = "Borderlands/La Frontera: The New Mestiza"
W_AW = "Alice Walker (Wikipedia; Poetry Foundation author page)"
INLOVE = "In Love & Trouble: Stories of Black Women"
MOTHERS = "In Search of Our Mothers' Gardens: Womanist Prose"
W_AWIL = "August Wilson (Wikipedia; Poetry Foundation author page)"
FENCES = "Fences"
W_TOB = "Tim O'Brien (Wikipedia; Poetry Foundation author page)"
THINGS = "The Things They Carried"
W_YK = "Yusef Komunyakaa (Wikipedia; Poetry Foundation author page)"
DCD = "Dien Cai Dau"
MAGIC = "Magic City"
TABOO = "Taboo: The Wishbone Trilogy, Part One"
W_AS = "Art Spiegelman (Wikipedia; Poetry Foundation author page)"
MAUS = "Maus"
W_JA = "Julia Alvarez (Wikipedia; Poetry Foundation author page)"
IYO = "¡Yo!"
W_JH = "Joy Harjo (Wikipedia; Poetry Foundation author page)"
SHH = "She Had Some Horses"
INMAD = "In Mad Love and War"
WOMAN = "The Woman Who Fell from the Sky"
W_SA = "Sherman Alexie (Wikipedia; Poetry Foundation author page)"
BUSINESS = "The Business of Fancydancing"
TSBW = "The Summer of Black Widows"
W_RD = "Rita Dove (Wikipedia; Poetry Foundation author page)"
YELLOW = "The Yellow House on the Corner"
MUSEUM = "Museum"
TB = "Thomas and Beulah"
GRACE = "Grace Notes"

AUTHORS = [
A10(GA, SEC, "1942", "2004", "Rio Grande Valley, Texas, United States",
  "Mexican American (Tejana); Chicana poet, essayist and theorist writing in English and Spanish",
  "Chicana lesbian writer and theorist whose generically mixed Borderlands/La Frontera became a founding text "
  "of queer theory, Chicana feminism and US Third World feminism",
  "Gloria Evangelina Anzaldúa was born on 26 September 1942 in the Rio Grande Valley of south Texas, the "
  "eldest of six children of sharecropping Mexican American parents, and grew up between her family's land "
  "and the migrant labour camps of Texas. She took a BA in English from Pan American University and an MA "
  "in English and education from the University of Texas at Austin, and taught in the public schools of "
  "Texas before moving to California. With Cherríe Moraga she edited This Bridge Called My Back: Writings "
  "by Radical Women of Color (Persephone Press, 1981), the anthology that put the term 'women of color' "
  "into circulation and that she called a survival handbook for the women it named. Her major book, "
  "Borderlands/La Frontera: The New Mestiza (Aunt Lute Books, 1987), mixes autobiography, history, myth, "
  "poetry and theory in English, Spanish and Nahuatl to describe the border as an open wound and the "
  "mestiza consciousness as the answer to it. She was co-editor of Making Face, Making Soul/Haciendo "
  "Caras (1990) and returned to fiction with a children's book, Prietita and the Ghost Woman (1995). She "
  "took a doctorate at the University of California, Santa Cruz in 2002 and died of diabetes-related "
  "complications in Santa Cruz on 15 May 2004.",
  "Borderlands/La Frontera: The New Mestiza (1987); This Bridge Called My Back (co-edited with Cherríe "
  "Moraga, 1981); Making Face, Making Soul/Haciendo Caras (edited, 1990); Prietita and the Ghost Woman "
  "(1995); and posthumous edited volumes of her writing on spirituality.",
  "Genre-crossing and bilingual; chapters of autobiography, historical narrative, myth, poetry and theory "
  "set side by side without hierarchy; a first person that shifts between 'I' and 'we'; Spanish and "
  "Nahuatl left unglossed; and a style of sentence built to carry the emotions of fear, anger and "
  "survival together.",
  "The US-Mexico border as a lived wound rather than a line; mestizaje and hybrid identity; the taming of "
  "a wild tongue and the recovery of a mother tongue; the virgin of Guadalupe, Malintzin and Coatlicue as "
  "figures of female power; and the politics of writing as a queer Chicana.",
  "Borderlands/La Frontera is the text through which Chicana feminism entered the American academy and is "
  "one of the founding documents of contemporary queer and postcolonial thought; its argument that "
  "identities are multiple and contradictory rather than singular is now a commonplace. The Norton "
  "Anthology of American Literature prints two chapters of it.",
  bib_status="substantially complete",
  bib_note="The book list, the co-edited and edited anthologies and the dates are from the Wikipedia "
           "article checked against the Poetry Foundation author page and the back matter of the 1999 "
           "Aunt Lute edition. Spanish-language and posthumously edited titles are named only where a "
           "catalogue entry could be checked.",
  ver="partially verified", sources=[W_GA, BORDER, NAAL]),
A10(AW, SEC, "1944", None, "Eatonton, Georgia, United States",
  "African American; novelist, short-story writer, poet and essayist writing in English",
  "African American novelist and essayist who reclaimed the Southern Black woman's inheritance in The Color "
  "Purple and coined 'womanist' as a term for Black feminist thought",
  "Alice Malsenior Walker was born on 9 February 1944 in Eatonton, Georgia, the eighth child of sharecrop "
  "tenants, and lost the sight of her right eye at eight in an accident that shaped her account of "
  "self-consciousness. She attended Spelman College and Sarah Lawrence College, where she finished her "
  "first collection of poems, Once (1968). Her early novels and stories - The Third Life of Grange Copeland "
  "(1970), In Love & Trouble: Stories of Black Women (1973) and Meridian (1976) - established her as a "
  "writer of the civil rights and Black feminist movements, and she taught and worked as a civil rights "
  "activist in Mississippi. The Color Purple (1982) won the Pulitzer Prize and the National Book Award and "
  "was filmed by Steven Spielberg in 1985 and adapted for the musical stage in 2005. She published the "
  "essay collections In Search of Our Mothers' Gardens (1983) and Living by the Word (1988), the "
  "controversial The Temple of My Familiar (1989) and Possessing the Secret of Joy (1992), and a memoir, "
  "The Same River Twice (1996). She lives in Mendocino County, California.",
  "Once (1968); The Third Life of Grange Copeland (1970); In Love & Trouble: Stories of Black Women (1973); "
  "Meridian (1976); You Can't Keep a Good Woman Down (1981); The Color Purple (1982); In Search of Our "
  "Mothers' Gardens: Womanist Prose (1983); The Temple of My Familiar (1989); Possessing the Secret of Joy "
  "(1992); and a body of poetry from Revolutionary Petunias (1973) to Taking the Arrow Out of the Heart "
  "(2018).",
  "Direct, idiomatic Southern Black speech; a first person that moves between the spoken and the essayistic; "
  "letters and diary forms; and a plainness of syntax used to carry violent and tender material in the same "
  "sentence.",
  "The survival and creativity of Black women under racism and poverty; the mother's garden as an "
  "inheritance; sexual and domestic violence; the African American South; and, in the essays, the "
  "definition of a 'womanist' tradition against white feminism.",
  "'Everyday Use' is among the most anthologised short stories in American literature and is a standard "
  "text for teaching the conflict between a usable heritage and an ornamental one; 'In Search of Our "
  "Mothers' Gardens' gave the essay collection its title and made the phrase part of the vocabulary of "
  "Black feminist criticism. The Norton prints both.",
  bib_status="substantially complete",
  bib_note="The principal novels, story collections and essay books are listed from the Wikipedia article "
           "checked against the Poetry Foundation author page; the poetry titles are given by span rather "
           "than individually, since the later volumes were not examined for this record.",
  ver="partially verified", sources=[W_AW, INLOVE, MOTHERS, NAAL]),
A10(AWIL, SEC, "1945", "2005", "Pittsburgh, Pennsylvania, United States",
  "African American; playwright writing in English",
  "African American playwright whose ten-play Century Cycle dramatised a century of Black Pittsburgh and "
  "restored tragedy to the American stage",
  "August Wilson was born Frederick August Kittel Jr. on 27 April 1945 in the Hill District of Pittsburgh, "
  "the son of a German immigrant baker and an African American cleaning woman, and took his mother's name "
  "in 1965. He left school at fifteen and educated himself in the public library, then moved to St Paul, "
  "Minnesota, where he wrote plays for a theatre workshop. Ma Rainey's Black Bottom reached Broadway in "
  "1984, and Fences, premiered at the Yale Repertory Theatre in 1985 and on Broadway in 1987 with James "
  "Earl Jones, won the Pulitzer Prize and the Tony Award. The ten plays that became the Pittsburgh Cycle "
  "or Century Cycle, one for each decade of the twentieth century, are Gem of the Ocean (2003), Joe "
  "Turner's Come and Gone (1988), Ma Rainey's Black Bottom (1984), The Piano Lesson (1990, Pulitzer), Two "
  "Trains Running (1992), Seven Guitars (1996), Fences (1987, Pulitzer), Jitney (1982), King Hedley II "
  "(2001) and Radio Golf (2005). He died of liver cancer in Seattle on 2 October 2005, a few months after "
  "Radio Golf opened.",
  "The ten plays of the Pittsburgh/Century Cycle (1982-2005); Ma Rainey's Black Bottom (1984); Fences "
  "(1987); The Piano Lesson (1990); plus essays collected in The Ground on Which I Stand (1996), whose "
  "title piece attacks colour-blind casting.",
  "Naturalistic dialogue built on the cadences of Black Pittsburgh speech; long arias of monologue inside "
  "domestic and workplace settings; a single unit set per play; and a symbolic structure - the fence, the "
  "piano, the train - carried by the objects on stage.",
  "The legacy of slavery and migration in the twentieth-century Black North; fatherhood and inheritance; "
  "the economics of Black labour; the blues and the 'blood's memory'; and the demand that African American "
  "experience be granted tragic rather than sociological form.",
  "Fences is the most produced American play of its generation and won both the Pulitzer Prize and the Tony "
  "Award; its 2010 Broadway revival with Denzel Washington and the 2016 film have kept it in continuous "
  "performance. The Century Cycle as a whole is commonly described as the most ambitious dramatic project "
  "in American theatre, and Fences is the play through which the Norton represents it.",
  bib_status="substantially complete",
  bib_note="The ten-cycle list, the premiere dates and the two Pulitzer Prizes were checked against the "
           "Wikipedia article and the Poetry Foundation author page; the 1985 Yale Repertory premiere of "
           "Fences and the 1987 Broadway run are given from the same sources.",
  ver="partially verified", sources=[W_AWIL, FENCES, NAAL]),
A10(TOB, SEC, "1946", None, "Austin, Minnesota, United States",
  "American; novelist and short-story writer writing in English",
  "American writer of the Vietnam War whose books treat memory, testimony and the impossibility of a true "
  "war story as their subject",
  "Timothy John O'Brien was born on 1 October 1946 in Austin, Minnesota, and graduated from Macalester "
  "College in 1968; he was drafted into the US Army that year and served in Vietnam in 1969-70 with the "
  "Third Platoon, Company A, Fifth Battalion, 46th Infantry, in Quang Ngai province. He began writing war "
  "stories on his return, and If I Die in a Combat Zone: Box Me Up and Ship Me Home appeared in 1973, "
  "followed by Northern Lights (1975) and Going After Cacciato (1978), which won the National Book Award "
  "and is built on a soldier's desertion and walk to Paris. The nuclear-war novel The Nuclear Age (1985) "
  "came before The Things They Carried (1990), his best-known book: a collection of linked stories whose "
  "narrator is named Tim O'Brien and which insists that its 'true' war stories are invented. In the Lake of "
  "the Woods (1994), Tomcat in Love (1998), July, July (2002) and Dad's Maybe Book (2019) followed. He "
  "holds a doctorate from the University of East Anglia and has taught at Texas State University.",
  "If I Die in a Combat Zone (1973); Northern Lights (1975); Going After Cacciato (1978); The Nuclear Age "
  "(1985); The Things They Carried (1990); In the Lake of the Woods (1994); Tomcat in Love (1998); July, "
  "July (2002); and the memoir Dad's Maybe Book (2019).",
  "A plain, reportorial sentence that declares its own unreliability; stories nested inside stories and "
  "told again with different outcomes; lists and inventories as a structural device; and a narrator who "
  "shares the author's name and contradicts his own testimony.",
  "The burden of memory and the guilt of survival; the difference between happening-truth and "
  "story-truth; cowardice and courage as a problem rather than a virtue; the weight of what soldiers "
  "carry, literal and moral; and the way a story is retold to keep the dead alive.",
  "'How to Tell a True War Story' is the metafictional centre of The Things They Carried and one of the "
  "most discussed short stories about Vietnam; its opening claim that a true war story is never moral is "
  "regularly quoted, and the book is a standard text in courses on American war writing and on "
  "historiography. The Norton prints the story on its own.",
  bib_status="substantially complete",
  bib_note="The book list and the Vietnam service record come from the Wikipedia article checked against the "
           "Poetry Foundation author page and the 1990 Houghton Mifflin first edition's author note. The "
           "story's first appearance in Esquire is cited in the work record from the magazine's archives.",
  ver="partially verified", sources=[W_TOB, THINGS, NAAL]),
A10(YK, MAJ, "1947", None, "Bogalusa, Louisiana, United States",
  "African American; poet writing in English",
  "African American poet of the Vietnam War and of Black southern childhood, Pulitzer Prize 1994, whose "
  "music-inflected free verse made him one of the most influential American poets of his generation",
  "Yusef Komunyakaa was born James William Brown Jr. on 29 April 1947 in Bogalusa, Louisiana, and took the "
  "name Komunyakaa from his grandfather's family name. He served in the US Army in Vietnam from 1969 to "
  "1970 as a correspondent and editor of the Southern Cross newspaper and was awarded the Bronze Star; he "
  "has said he did not begin to write about the war for more than a decade afterwards. He took degrees at "
  "the University of Colorado and Colorado State University and an MFA from the University of California, "
  "Irvine, and taught for many years at Indiana University and then at Princeton. Dedications & Other Dark "
  "Horses (1977), Copacetic (1984) and I Apologize for the Eyes in My Head (1986) came before Dien Cai Dau "
  "(1988), his Vietnam book, and Magic City (1992), which returns to Bogalusa. Neon Vernacular: New and "
  "Selected Poems 1977-1989 (1993) won the Pulitzer Prize and the Kingsley Tufts Award in 1994. Thieves of "
  "Paradise (1998), Talking Dirty to the Gods (2000), Pleasure Dome: New and Collected Poems 1975-1999 "
  "(2001), Taboo: The Wishbone Trilogy, Part One (2004) and Warhorses (2008) followed, along with the "
  "essay collection Blue Notes (2000) and the libretto for Scott Wheeler's opera Democracy.",
  "Dedications & Other Dark Horses (1977); Copacetic (1984); I Apologize for the Eyes in My Head (1986); "
  "Dien Cai Dau (1988); Magic City (1992); Neon Vernacular (1993); Thieves of Paradise (1998); Talking "
  "Dirty to the Gods (2000); Pleasure Dome (2001); Taboo (2004); Warhorses (2008); The Emperor of Water "
  "Clocks (2015); and Blue Notes: Essays, Interviews and Commentaries (2000).",
  "Free verse built on the cadence of blues, jazz and juke-joint speech; short lines with hard stops; "
  "concrete, often violent imagery; a syntax that withholds the subject; and long sequences that build "
  "single poems into a mythic anatomy.",
  "The Vietnam War and the survivor's memory of it, above all in 'Facing It'; Black southern childhood and "
  "labour; music as a mode of knowledge; the body, desire and violence; and the persistence of the "
  "mythological inside the everyday.",
  "Komunyakaa is the most anthologised African American poet of his generation after the Black Arts "
  "writers, and 'Facing It' - his poem about the Vietnam Veterans Memorial - is one of the most widely "
  "taught poems about the war. The Pulitzer Prize for Neon Vernacular in 1994 confirmed a reputation built "
  "on Dien Cai Dau, and the Norton's four selections give him the largest block of any poet in the "
  "anthology's period.",
  bib_status="substantially complete",
  bib_note="The collection list and the 1994 Pulitzer are from the Wikipedia article checked against the "
           "Poetry Foundation author page and the Callaloo bibliography of his work (Michael Collins, "
           "Callaloo); first publication of individual poems is given in the work records only where the "
           "Callaloo bibliography or the collection's own notes state it.",
  ver="partially verified", sources=[W_YK, DCD, MAGIC, TABOO, NAAL]),
A10(AS, SEC, "1948", None, "Stockholm, Sweden; raised in Queens, New York, United States",
  "American (born in Sweden to Polish Jewish Holocaust survivors); cartoonist and graphic novelist writing "
  "in English",
  "Cartoonist whose Maus turned the Holocaust memoir into graphic narrative and won the Pulitzer Prize, "
  "establishing the graphic novel as a literary form",
  "Art Spiegelman was born Itzhak Avraham ben Zeev Spiegelman on 15 February 1948 in Stockholm, where his "
  "Polish Jewish parents had gone after the war, and grew up in Rego Park, Queens, in New York. He began "
  "drawing professionally as a teenager and became part of the underground comix movement, drawing for "
  "East Village Other and co-founding Arcade with Bill Griffith in 1975. In 1980 he founded RAW with his "
  "wife Françoise Mouly, and in its pages he began Maus, a retelling of his father Vladek's survival of "
  "Auschwitz in which Jews are mice, Germans cats and Poles pigs. The first six chapters appeared as Maus "
  "I: A Survivor's Tale - My Father Bleeds History (Pantheon, 1986) and the rest as Maus II: A Survivor's "
  "Tale - And Here My Troubles Began (1991); the completed work was awarded a special Pulitzer Prize in "
  "1992. He was the first cartoonist to be a regular contributor to The New Yorker, resigned over a "
  "pressure to tone down a Muhammad cartoon in 2003, and wrote Breakdowns: Portrait of the Artist as a "
  "Young %@&*! (2008) and the wordless MetaMaus (2011).",
  "Maus I (1986) and Maus II (1991), collected as Maus: A Survivor's Tale (1992); Breakdowns (1977, "
  "expanded 2008); In the Shadow of No Towers (2004); MetaMaus (2011); and co-edited RAW (1980-91).",
  "Anthropomorphic cartoon animals drawn in black and white ink; a frame narrative in which the son "
  "interviews the father; documentary panels of the camps set against domestic scenes in Rego Park; and a "
  "deliberately rough, hand-drawn line that refuses the polish of the museum.",
  "The Holocaust and its transmission to the second generation; the guilt of the survivor and of the son; "
  "representation itself, since the animal masks are an argument about how the Shoah can be told; and "
  "history as something that happens in a family.",
  "Maus won the special Pulitzer Prize in 1992, the first ever awarded to a comic, and is the work that "
  "established the graphic novel as a subject of literary study; it is taught in history courses as well "
  "as literature courses, and 'Mousetrap' - the sixth chapter, printed here - is the chapter in which the "
  "wartime narrative and the father's present-day household are most tightly interleaved. The Norton's "
  "inclusion of it is a statement about the form.",
  bib_status="substantially complete",
  bib_note="The two volumes, their Pantheon dates, the 1992 Pulitzer and the New Yorker resignation are "
           "from the Wikipedia article checked against the Poetry Foundation author page and the "
           "publisher's edition notes; the page count and chapter numbering of 'Mousetrap' are from the "
           "1986 volume.",
  ver="partially verified", sources=[W_AS, MAUS, NAAL]),
A10(JA, SEC, "1950", None, "New York City, United States; raised in the Dominican Republic",
  "Dominican American; novelist, poet and essayist writing in English",
  "Dominican American writer whose novels of immigration, bilingualism and the Trujillo dictatorship made "
  "her a central figure in Latina literature in the United States",
  "Julia Alvarez was born on 27 March 1950 in New York and taken to the Dominican Republic as an infant, "
  "where her father ran a farm and was involved in a plot against the dictator Rafael Trujillo. The family "
  "fled back to New York in 1960, ten months before Trujillo's assassination, and Alvarez grew up in "
  "Queens, learning English at school while Spanish stayed the language of home. She took degrees at "
  "Middlebury College and Syracuse University and worked as a migrant-labour-camp teacher, then taught "
  "English at Middlebury from 1988. Homecoming: New and Collected Poems (1984) came first, then the novel "
  "How the García Girls Lost Their Accents (Algonquin, 1991), which tells the story of four sisters "
  "backwards from their American adulthood to their Dominican childhood and made her reputation. In the "
  "Time of the Butterflies (1994) fictionalised the Mirabal sisters murdered by Trujillo, and ¡Yo! "
  "(Algonquin, 1997) returned to the García family, telling the second sister's story through the voices "
  "of everyone around her. In the Name of Salomé (2000), Saving the World (2006) and Afterlife (2020) "
  "followed, with the nonfiction Something to Declare (1998) and the middle-grade Tía Lola series.",
  "Homecoming (1984); How the García Girls Lost Their Accents (1991); In the Time of the Butterflies "
  "(1994); ¡Yo! (1997); Something to Declare (1998); In the Name of Salomé (2000); Saving the World "
  "(2006); and Afterlife (2020), plus poetry from The Other Side/El Otro Lado (1995) onward.",
  "Multiple first-person narrators, each with a distinct idiolect; non-chronological structures that run "
  "the immigrant story backwards; Spanish words left in the English text; and a comic voice that carries "
  "political material without solemnity.",
  "Immigration and the loss of a homeland; bilingualism and the taming of the tongue; the Trujillo "
  "dictatorship and the courage of ordinary women; sisterhood and family myth-making; and the position of "
  "the Latina writer inside the American academy.",
  "'The Mother' - the chapter the Norton prints - is the section of ¡Yo! in which Yo's mother narrates in "
  "the first person, and it is the piece most often taught from the novel because it dramatises the "
  "mother-daughter language gap in a single voice. Alvarez is one of the writers through whom the Norton "
  "represents the 1990s boom in US Latina fiction.",
  bib_status="substantially complete",
  bib_note="The novels, the Algonquin dates and the biographical facts are from the Wikipedia article "
           "checked against the Poetry Foundation author page; the poetry titles are given by span, since "
           "the individual volumes were not examined for this record.",
  ver="partially verified", sources=[W_JA, IYO, NAAL]),
A10(JH, MAJ, "1951", None, "Tulsa, Oklahoma, United States",
  "Mvskoke (Muscogee) Nation; poet, musician and playwright writing in English",
  "Mvskoke poet and saxophonist, US Poet Laureate 2019-22, whose work fused the Native American Renaissance "
  "with jazz and who was the first Native American to hold the laureateship",
  "Joy Harjo was born on 9 May 1951 in Tulsa, Oklahoma, and is an enrolled member of the Mvskoke (Creek) "
  "Nation; her father was Muscogee and her mother of Cherokee, French and Irish descent. She studied at "
  "the Institute of American Indian Arts in Santa Fe, took a BA from the University of New Mexico and an "
  "MFA from the Iowa Writers' Workshop, and taught for many years at the University of New Mexico and the "
  "University of Illinois. The Last Song (1975) and What Moon Drove Me to This? (1979) preceded She Had "
  "Some Horses (Thunder's Mouth Press, 1983), the book that made her name. Secrets from the Center of the "
  "World (1989), In Mad Love and War (Wesleyan, 1990) - which won the American Book Award - The Woman Who "
  "Fell from the Sky (Norton, 1994) and A Map to the Next World (2000) followed, along with the memoir "
  "Crazy Brave (2012) and the poetry collections Conflict Resolution for Holy Beings (2015) and An "
  "American Sunrise (2019). She performs with her band the Arrow Dynamics, has released several albums of "
  "music with her saxophone and voice, and was named US Poet Laureate in 2019, serving three terms to 2022; "
  "she edited the Norton Anthology of Native Nations Poetry, When the Light of the World Was Subdued, Our "
  "Songs Came Through (2020).",
  "The Last Song (1975); What Moon Drove Me to This? (1979); She Had Some Horses (1983); Secrets from the "
  "Center of the World (1989); In Mad Love and War (1990); The Woman Who Fell from the Sky (1994); A Map "
  "to the Next World (2000); How We Became Human: New and Selected Poems (2004); She Had Some Horses "
  "(reissued 2008); Crazy Brave (2012); Conflict Resolution for Holy Beings (2015); and An American "
  "Sunrise (2019).",
  "Free verse that moves by association and repetition rather than by argument; a syntax of invocation; "
  "the line broken where breath breaks; animals, weather and the Oklahoma landscape as agents rather than "
  "scenery; and the rhythm of blues and jazz carried into the poem.",
  "Indigenous survival, removal and return; the Mvskoke homeland and the Trail of Tears; women's lives and "
  "violence against women; the natural world as a network of persons; music and ceremony as forms of "
  "memory; and the crossing of the American present with a mythic one.",
  "Harjo is the best-known Native American poet of her generation and the first Native American US Poet "
  "Laureate; She Had Some Horses is a central text of the Native American Renaissance and of the "
  "poetry of the 1980s, and the Norton's four selections are drawn from four different decades of her work, "
  "which makes her the anthology's fullest representation of a Native poet.",
  bib_status="substantially complete",
  bib_note="The collection list, the publishers and the laureateship are from the Wikipedia article checked "
           "against the Poetry Foundation author page and the Library of Congress announcement of the "
           "2019 appointment; individual first printings are given in the work records.",
  ver="partially verified", sources=[W_JH, SHH, INMAD, WOMAN, NAAL]),
A10(SA, MAJ, "1966", None, "Wellpinit, Spokane Indian Reservation, Washington, United States",
  "Spokane and Coeur d'Alene; poet, novelist and filmmaker writing in English",
  "Spokane writer whose first books made him the most widely read Native American author of his generation "
  "and whose work moved between lyric, satire, film and young-adult fiction",
  "Sherman Joseph Alexie Jr. was born on 7 October 1966 on the Spokane Indian Reservation at Wellpinit, "
  "Washington, the son of a Spokane father and a Coeur d'Alene mother, and grew up in poverty; he was "
  "hydrocephalic as an infant, suffered seizures, and read voraciously, leaving the reservation school for "
  "Reardan High School where he was the only Indian student. He took a BA from Washington State University, "
  "where he studied with Alex Kuo, and published The Business of Fancydancing (Hanging Loose Press, 1992) "
  "at twenty-five; it mixes poems and short stories and was followed by the story collection The Lone "
  "Ranger and Tonto Fistfight in Heaven (1993), which won the PEN/Hemingway Award, and the novel "
  "Reservation Blues (1995). Indian Killer (1996) was a thriller, and The Summer of Black Widows (1996) "
  "gathered his poems. He wrote the screenplay for Smoke Signals (1998), the first feature film written, "
  "directed and acted by Native Americans to reach wide release, and directed The Business of "
  "Fancydancing as a film in 2002. The Absolutely True Diary of a Part-Time Indian (2007) won the National "
  "Book Award for Young People's Literature; later books include Blasphemy: New and Selected Stories "
  "(2012) and You Don't Have to Say You Love Me (2017), a memoir about his mother. He has spoken publicly "
  "about depression and about having been sexually abused as a child, and in 2018 faced allegations of "
  "sexual harassment, which he has denied.",
  "The Business of Fancydancing (1992); The Lone Ranger and Tonto Fistfight in Heaven (1993); Reservation "
  "Blues (1995); Indian Killer (1996); The Summer of Black Widows (1996); The Toughest Indian in the World "
  "(2000); Ten Little Indians (2003); The Absolutely True Diary of a Part-Time Indian (2007); Blasphemy "
  "(2012); and You Don't Have to Say You Love Me (2017).",
  "A demotic, joke-telling free verse and prose poem built on the one-liner; abrupt turns from comedy to "
  "grief; reservation speech with its own timing; and a habit of naming brands, basketball players and "
  "television shows as the common culture of his characters.",
  "Reservation life, poverty and endurance; basketball as an image of both escape and entrapment; "
  "alcoholism and its inheritance; the commodification of Indian identity for tourists and readers; and "
  "the grief of a family and a people, handled through comedy.",
  "Alexie was for two decades the most widely taught Native American writer in American schools, and the "
  "Norton's four selections - three poems from the 1990s and a story - represent both the lyric and the "
  "fictional sides of his early work. 'This Is What It Means to Say Phoenix, Arizona' is the story from "
  "which Smoke Signals was developed. The harassment allegations of 2018 have changed how his work is "
  "taught without removing it from the anthologies.",
  bib_status="substantially complete",
  bib_note="The book list, the 1993 PEN/Hemingway Award, the 2007 National Book Award and the film credits "
           "are from the Wikipedia article checked against the Poetry Foundation author page; the "
           "allegations of 2018 are mentioned without detail and are not part of any work record.",
  ver="partially verified", sources=[W_SA, BUSINESS, TSBW, NAAL]),
A10(RD, MAJ, "1952", None, "Akron, Ohio, United States",
  "African American; poet and essayist writing in English",
  "African American poet, US Poet Laureate 1993-95 and Pulitzer Prize winner 1987, whose sequence Thomas and "
  "Beulah recovered her grandparents' lives in a form both lyric and historical",
  "Rita Frances Dove was born on 28 August 1952 in Akron, Ohio, and grew up there as the daughter of the "
  "first Black chemist at the Goodyear Tire & Rubber Company. She was a Presidential Scholar in 1970, "
  "graduated summa cum laude from Miami University of Ohio, studied at the Universität Tübingen on a "
  "Fulbright and took an MFA from the Iowa Writers' Workshop in 1977. The Yellow House on the Corner "
  "(Carnegie Mellon, 1980) and Museum (1983) came first, and Thomas and Beulah (1986) - a sequence about "
  "her maternal grandparents' migration from the South to Akron - won the Pulitzer Prize in 1987. She "
  "published Grace Notes (1989), the novel Through the Ivory Gate (1992), Mother Love (1995), a "
  "reworking of the Demeter-Persephone myth, and On the Bus with Rosa Parks (1999). She was US Poet "
  "Laureate from 1993 to 1995, the youngest ever appointed, and served as Poet Laureate of Virginia from "
  "2004 to 2006; her later work includes American Smooth (2004), Sonata Mulattica (2009), a book-length "
  "sequence on the Black violinist George Bridgetower, and Playlist for the Apocalypse (2021). She has "
  "edited The Best American Poetry (2000) and The Penguin Anthology of Twentieth-Century American Poetry "
  "(2011), and teaches at the University of Virginia.",
  "The Yellow House on the Corner (1980); Museum (1983); Thomas and Beulah (1986); Grace Notes (1989); "
  "Through the Ivory Gate (1992); Mother Love (1995); On the Bus with Rosa Parks (1999); American Smooth "
  "(2004); Sonata Mulattica (2009); and Playlist for the Apocalypse (2021).",
  "Formal control inside free verse; short lyrics arranged into sequences with a narrative arc; a diction "
  "that moves between the plain and the archaic without strain; persona poems in the voices of historical "
  "figures; and a strong sense of the poem as a shaped object with a turn and a close.",
  "The Great Migration and the lives of ordinary Black Americans in the industrial Midwest; family history "
  "and inheritance; music, dance and the performing body; the classical and mythological past in relation "
  "to Black experience; and the pressures of history on a private life.",
  "Dove was the youngest US Poet Laureate and the second African American to hold the post, and Thomas and "
  "Beulah is one of the most admired American sequences of the 1980s, a model for the book-length "
  "historical lyric. The Norton prints ten of her selections - three Adolescence poems, three sections of "
  "Thomas and Beulah and four other lyrics - which is more than any other poet in the anthology's period.",
  bib_status="substantially complete",
  bib_note="The collection list, the 1987 Pulitzer, the laureateship dates and the editorships are from the "
           "Wikipedia article checked against the Poetry Foundation author page; the contents of The Yellow "
           "House on the Corner and Thomas and Beulah were checked against their tables of contents.",
  ver="partially verified", sources=[W_RD, YELLOW, MUSEUM, TB, GRACE, NAAL]),
]
WORKS = [
W10("Borderlands/La Frontera: The New Mestiza", GA, "1987",
  "Genre-crossing book of essays, autobiography, history and poetry", "major",
  genres=G("Literary Essay", "Cultural Criticism", "Prose Poetry", "Autobiography"),
  themes=T("Identity, authenticity and the divided self", "Race, racism and the struggle for civil rights",
           "Gender, feminism and women's lives", "Migration, exile and diaspora",
           "Language, writing and the limits of representation"),
  movements=M(CHIC, POSTCOL, FEM),
  overview="Borderlands/La Frontera: The New Mestiza, published by Aunt Lute Books in 1987, is Gloria "
           "Anzaldúa's central work and one of the founding texts of Chicana feminism: a book in seven "
           "chapters that refuses to be one genre, moving between autobiography, revisionist history, "
           "myth, poetry and theory, and between English, Spanish and Nahuatl. The Norton Anthology of "
           "American Literature prints two of its chapters, 'La conciencia de la mestiza / Towards a New "
           "Consciousness' and 'How to Tame a Wild Tongue', which are its philosophical climax and its "
           "most quoted argument about language.",
  content="The book opens with the image of the US-Mexico border as an open wound - '1,950 mile-long open "
          "wound' - where the First World grinds against the Third, and it returns to that image "
          "throughout. Its early chapters describe the author's childhood in the Rio Grande Valley, the "
          "shamans and folk healers of her family, and the history of the Mexican American dispossession "
          "of land in Texas after 1848. The middle chapters turn to the figures of female power that "
          "patriarchal culture has split into good and evil - the Virgin of Guadalupe, Malintzin "
          "(La Malinche) and Coatlicue, the serpent goddess - and argue for taking them back together. "
          "'How to Tame a Wild Tongue' describes the punishments Anzaldúa received as a child for "
          "speaking Spanish at school and the varieties of Chicano Spanish she grew up inside, and "
          "concludes that until she can write in her own tongues she will be 'serving time' in others'. "
          "'La conciencia de la mestiza' argues that the answer to the border's contradictions is not "
          "purity but a new consciousness that can hold incompatible things at once.",
  summary="The book's argument is cumulative and its method is collision: a passage of autobiography will "
          "be followed by a page of pre-Columbian history, then a poem, then a paragraph of theory, "
          "without transition, so that the reader is made to experience the border's simultaneity rather "
          "than be told about it. Anzaldúa's key moves recur. The first is to treat the border as an "
          "internal as well as a geographic fact, so that the queer Chicana who leaves home is both "
          "traitor and exile. The second is to identify language with identity: 'Ethnic identity is "
          "twin skin to linguistic identity - I am my language', and the taming of the wild tongue in "
          "school is therefore a form of violence that the book is written to undo. The third is the "
          "refusal of the binary: the mestiza does not choose between the Mexican and the American, the "
          "Spanish and the English, the Catholic and the indigenous, but inhabits the crossing and "
          "develops a tolerance for contradiction that Anzaldúa calls a new consciousness. The fourth is "
          "her insistence that theory is written from a body and a life - from a childhood of fieldwork "
          "and sunburn, from diabetes and from the experience of being a lesbian in a culture that "
          "condemned it. The prose is deliberately unacademic even when it is doing theory: it addresses "
          "the reader as 'you', it breaks into lists and poems, and it leaves Spanish untranslated, "
          "which was the point.",
  themes_text="The first subject, and the book's whole occasion, is the border as a lived condition of the "
              "Mexican American and especially the Chicana. The second is language: the chapter printed "
              "here argues that a people's tongues are their identity and that their suppression is the "
              "deepest form of colonisation. The third is gender and sexuality, since Anzaldúa writes as "
              "a lesbian whose sexuality puts her outside both the Anglo and the Chicano communities. "
              "The fourth is survival, understood as the making of a self capable of living with "
              "unresolved contradiction rather than resolving it.",
  structure="Seven chapters, each mixing prose, poetry and untranslated Spanish, moving from the history "
            "and myth of the borderland through the author's own life to the theoretical statement of "
            "the final chapters; the Norton prints chapters five and seven, which are the argument's "
            "hinge and its conclusion.",
  style="Bilingual and unglossed; long anaphoric sentences broken by poems and lists; direct address to "
        "the reader; first person alternating with third; and a polemical register that keeps the "
        "idiom of the Valley in the theory.",
  ctx="Aunt Lute Books, a San Francisco feminist press, published the book in 1987, and it appeared in "
      "the decade in which Chicano studies entered US universities and in which women of colour "
      "criticised both white feminism and nationalist Chicano politics. It was preceded by This Bridge "
      "Called My Back (1981), which Anzaldúa co-edited with Cherríe Moraga, and it became a set text in "
      "women's studies, ethnic studies and queer theory within a few years of publication.",
  sig="Borderlands/La Frontera is one of the books that changed the American academy's understanding of "
      "identity in the late twentieth century; the term 'mestiza consciousness' is now standard in "
      "feminist and postcolonial theory, and the book is credited, with Moraga's and Audre Lorde's work, "
      "with establishing the category of women of colour. The Norton's printing of two chapters is the "
      "anthology's principal representation of Chicana writing, and it takes a work of theory as "
      "literature, which is itself the book's argument.",
  canon="Major canon",
  crit="The criticism is large and divided between celebration and qualification: it is credited with "
       "opening queer Chicana subjectivity and criticised, by later scholars, for an essentialist "
       "account of the indigenous past and for the relative absence of class analysis. Its bilingual "
       "practice is the most discussed feature, since the book declines to translate and thereby "
       "constitutes an English-reading audience that must tolerate not understanding.",
  biblio="First published by Aunt Lute Books (San Francisco) in 1987; a second edition followed in 1999 "
         "and a fourth, with a new preface, in 2012. A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E.",
  notes="The book was not read in full for this record. The description of chapters five and seven rests "
        "on the published text of those chapters as quoted in criticism and anthologies; the order and "
        "argument of the opening chapters are given from the standard accounts of the book's structure.",
  ver="partially verified", sources=[W_GA, BORDER, NAAL]),
W10("Everyday Use", AW, "1973",
  "Short story", "major",
  genres=G("Short Story", "Domestic Fiction", "Regional Fiction"),
  themes=T("Family, marriage and domestic life", "Race, racism and the struggle for civil rights",
           "History, truth and the uses of the past", "Class, labour and social mobility"),
  movements=M(AFAM),
  overview="'Everyday Use' was first published in Alice Walker's collection In Love & Trouble: Stories of "
           "Black Women (New York: Harcourt Brace Jovanovich, 1973) and is the most anthologised of her "
           "stories. It is a first-person narrative spoken by a rural Georgia mother about a single "
           "afternoon's visit from her elder daughter, and it turns on the meaning of two quilts.",
  content="The narrator, Mrs Johnson, waits in the yard of the house she and her younger daughter Maggie "
          "live in for the visit of Dee, the elder daughter, who has been away at college and now calls "
          "herself Wangero Leewanika Kemanjo, saying that Dee is a name given by white people. Dee arrives "
          "with a male companion and photographs the house, the bench, the churn and the dasher as "
          "specimens of a folk past. At dinner she takes the butter dish and then the two quilts, made by "
          "her grandmother and aunt from scraps of dresses and Civil War uniforms, and announces that she "
          "will hang them. Her mother says that Maggie has been promised them and that Maggie can quilt "
          "more; Dee says Maggie would put them to 'everyday use' and that they are priceless. The mother "
          "takes the quilts out of Dee's hands and gives them to Maggie, and the story ends with the two "
          "of them sitting in the yard until it is time to go to bed.",
  summary="The story is built as a test of three kinds of relation to the past, and its irony is that the "
          "one who has left is the one who cannot use it. Dee's return is a performance of heritage: she "
          "photographs the objects she would not have been seen dead beside as a child, she has changed "
          "her name to an invented African one without knowing its meaning, and she wants the quilts as "
          "objects to preserve rather than as things whose use is their meaning. Mrs Johnson is the "
          "story's moral centre and its narrator, and her narration is deliberately unliterary - she "
          "describes herself as a big-boned woman with hands like a man's, she is ironic about her "
          "education and her daughter's, and she judges without commenting. The story's most famous "
          "gesture is the mother's decision to give the quilts to Maggie, who will use them, rather than "
          "to Dee, who will hang them; and its most important technical feature is that the decision is "
          "made in the story rather than the story being told about it. Walker has said that the story "
          "came from watching Black students of the late 1960s reject their own families' culture while "
          "claiming an African one, and the story is careful to make Dee intelligent, brave and "
          "articulate rather than a fool: what she lacks is not politics but a relation to the people who "
          "made the things she wants.",
  themes_text="The first subject is the difference between heritage as a possession and heritage as a "
              "practice, carried by the quilts themselves, which are both art and bedding. The second is "
              "class: Dee's education has removed her from the poverty her mother still lives in, and "
              "the story refuses to say that this was simply a loss. The third is the Black family under "
              "segregation and its aftermath, and the forms of dignity available to a woman who has "
              "cleaned other people's houses. The fourth is naming, since Dee's renaming is the story's "
              "sharpest image of a politics that has detached itself from its inheritance.",
  structure="A single continuous first-person narrative in a rural Southern idiom, with one scene and no "
            "flashback; the story's structure is the long wait, the arrival, the meal and the quarrel, "
            "with the climax placed in a single gesture near the end.",
  style="First-person vernacular narration, with an uneducated grammar that is consistent and "
        "unpatronised; free indirect speech for Dee; images drawn from the farm (the churn, the dasher, "
        "the yard, the bench); and an absence of metaphor, so that the quilts are simply quilts and "
        "carry the meaning by being described.",
  ctx="The story appeared in 1973, in the years when Black Studies programmes and the Black Arts Movement "
      "had made 'heritage' a public question and when many African American writers were debating "
      "whether the rural southern past was a burden or a resource. Walker had worked in Mississippi in "
      "the civil rights movement and had written the story, she said, out of that experience; In Love & "
      "Trouble was her second book of fiction and her first collection of stories.",
  sig="'Everyday Use' is one of the two or three most widely taught stories in twentieth-century "
      "American literature and the standard text for the argument between a usable and an ornamental "
      "heritage. It is the story through which the Norton Anthology of American Literature represents "
      "Walker, and its title phrase has passed into the criticism as a term of value.",
  canon="Major canon",
  crit="Criticism reads the story through the quilts, and the standard reading is that Maggie's use "
       "embodies a living tradition while Dee's display embalms it; a substantial counter-reading "
       "complicates the position by noting the story's own narrated hostility and the narrow options "
       "available to Maggie within it. Walker's own later description of the story as a product of the "
       "civil rights years is usually cited, and the story is regularly paired with her essay 'In Search "
       "of Our Mothers' Gardens', which the anthology also prints.",
  biblio="First published in In Love & Trouble: Stories of Black Women (New York: Harcourt Brace "
         "Jovanovich, 1973); collected in The Complete Stories (1994). A selection of The Norton "
         "Anthology of American Literature, 11th edition, vol. E.",
  notes="The story was read for this record from its published text, but the Harcourt first edition was "
        "not examined and the exact page is not given. The date of first publication is the collection's "
        "1973 imprint.",
  ver="partially verified", sources=[W_AW, INLOVE, NAAL]),
W10("In Search of Our Mothers' Gardens: Womanist Prose", AW, "1974",
  "Essay (title essay, collected in book of the same name, 1983)", "significant",
  genres=G("Personal Essay", "Literary Essay", "Cultural Criticism"),
  themes=T("Gender, feminism and women's lives", "Race, racism and the struggle for civil rights",
           "Art, the artist and the creative life", "Family, marriage and domestic life"),
  movements=M(AFAM, FEM),
  overview="'In Search of Our Mothers' Gardens' is the title essay of Alice Walker's collection of "
           "essays and journals, published by Harcourt Brace Jovanovich in 1983; the essay itself "
           "appeared in Ms. magazine in 1974, and the Norton dates the selection from that first "
           "periodical publication. It is the essay in which Walker's term 'womanist' is prepared, and "
           "its subject is the creative lives of Black women who were denied the chance to make art.",
  content="The essay begins with a quotation from Jean Toomer's Cane describing Black women in the 1920s "
          "as 'exquisite butterflies trapped in an evil honey', and asks what happened to the creative "
          "power of such women. Walker answers with the figure of her own mother, a sharecropper's wife "
          "who worked in the fields, bore eight children, sewed quilts and made a garden of flowers "
          "wherever the family stopped. She argues that the artist in such a woman was driven underground "
          "into the only forms allowed her - the garden, the quilt, the story told to a child - and that "
          "the 'anonymity' of those forms is not an absence of art but its condition. The essay moves "
          "through Phillis Wheatley, who had to write hymns; through Virginia Woolf's argument in A Room "
          "of One's Own and its blind spot about Black women; and through the example of the Black "
          "community's expectation that its artists be acceptable and respectable. It closes with "
          "Walker's sense that her own work is the continuation of her mother's gardens.",
  summary="The essay's argument is that a tradition can exist without documents: if the forms in which "
          "Black women made things - gardens, quilts, songs, cooking - were not recognised as art, that "
          "is a fact about the recognition, not about the making. Walker's method is to read her mother's "
          "life as a text: the garden is a poem, the quilt is a composition, and the values of beauty, "
          "spirituality and self-respect that they embodied were the inheritance she received. The move "
          "is characteristically double. It is a recovery of the lives of Black women who left no books, "
          "and it is a rebuke to a feminist criticism that had defined creativity by the conditions of "
          "white middle-class authorship - Walker quotes Woolf's account of the woman who would have "
          "written Shakespeare's plays and observes that for the Black woman the obstacles were not a "
          "room and an income but slavery and forced labour. The essay is also where the word 'womanist', "
          "which Walker would define formally in the same collection, begins to do work: a Black "
          "feminism that includes the love of women, of music, of the folk, of herself. Its tone is "
          "essayistic and personal rather than polemical; the authority is in the family example.",
  themes_text="The first subject is the creativity of Black women in conditions that forbade its "
              "public exercise, and the essay's whole force is in refusing to call that creativity "
              "thwarted. The second is the relation of Black women to a white feminist tradition, which "
              "Walker reads as well-meaning and incomplete. The third is motherhood and inheritance, "
              "since the essay's structure is a daughter's reading of her mother's life. The fourth is "
              "the politics of acceptable art, and the pressure on Black writers to be representative.",
  structure="A single essay of roughly twenty pages, organised as a sequence of exempla - Toomer's "
            "butterflies, the author's mother, Wheatley, Woolf - each of which sharpens the argument, "
            "closing on the author's own inheritance rather than on a conclusion.",
  style="Personal and essayistic; a plain declarative sentence with a strong rhythmic close; quotations "
        "from Toomer and Woolf used as countervoices; first person throughout; and an absence of theory "
        "vocabulary, so that the argument is carried by example.",
  ctx="The essay appeared in Ms. in 1974, in the first years of the magazine's influence, and was "
      "collected in 1983, when Black feminist criticism was defining itself in books such as Barbara "
      "Smith's Toward a Black Feminist Criticism and bell hooks's Ain't I a Woman. Walker's term "
      "'womanist' - defined in the collection's front matter - was taken up across the academy and in "
      "Black theology, and the essay's title has become a standard phrase for the recovery of women's "
      "unrecorded work.",
  sig="The essay is one of the texts that established Black feminist criticism as a field, and its "
      "garden has become the governing image for a whole tradition of recovery scholarship; 'womanist' "
      "has entered the lexicon of theology and criticism. The Norton prints it beside 'Everyday Use', "
      "which is a recognition that Walker's fiction and her criticism make the same argument by "
      "different means.",
  canon="Major canon",
  crit="Criticism reads the essay as the founding statement of womanist thought and as a correction to "
       "Woolf, and its central image has been widely adopted - most influentially in the title of "
       "Walker's own collection and in the subsequent scholarship on Black women's quilting. Some later "
       "critics have questioned the essay's reliance on a redemptive reading of suffering, and the "
       "term womanist has been debated and revised by Black queer and trans writers.",
  biblio="First published in Ms. magazine in 1974; collected as the title essay of In Search of Our "
         "Mothers' Gardens: Womanist Prose (New York: Harcourt Brace Jovanovich, 1983). A selection of "
         "The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The essay was read for this record from the collected text; the Ms. appearance of 1974 is given "
        "from the collection's own acknowledgements as repeated in the standard bibliographies. The "
        "anthology's date of 1974 follows the periodical publication, which precedes the book.",
  ver="partially verified", sources=[W_AW, MOTHERS, NAAL]),
W10("Fences", AWIL, "1985",
  "Play in two acts (full-length tragedy)", "major",
  genres=G("Drama and Performance (1946–2000)", "Modern Tragedy", "Full-Length Play", "Domestic Drama"),
  themes=T("Race, racism and the struggle for civil rights", "Family, marriage and domestic life",
           "Class, labour and social mobility", "Death, illness and mourning",
           "History, truth and the uses of the past"),
  movements=M(AFAM, BLACKARTS),
  overview="Fences was first performed at the Yale Repertory Theatre in 1985 and opened on Broadway in "
           "1987, where it won the Pulitzer Prize for Drama and the Tony Award for Best Play. It is the "
           "sixth play of August Wilson's ten-play Pittsburgh or Century Cycle, set in 1957 in the Hill "
           "District, and it is the work through which the Norton Anthology of American Literature "
           "represents him.",
  content="Troy Maxson, fifty-two, is a sanitation worker in Pittsburgh who collects garbage from the "
          "back of a truck and has spent years fighting the union's refusal to let Black men drive. He "
          "was a powerful baseball player in the Negro Leagues before the colour line kept him out of "
          "the majors, he served time in prison for a killing committed in a robbery, and he has built "
          "a life with his wife Rose and his sons Lyons, Cory and Gabriel. Over two acts he refuses to "
          "let Cory accept a college football scholarship, tells Rose that he has fathered a child with "
          "another woman, fights his son physically, and is left at the end of the play with a baby "
          "daughter, Raynell, whom Rose agrees to raise, standing in a yard where the fence he was "
          "building is at last finished; Cory returns from the Marines and refuses, at first, to go to "
          "his father's funeral.",
  summary="The play's structure is domestic and its argument is historical, and Wilson's method is to "
          "let the history arrive through the ordinary speech of the yard. Troy is a man of great "
          "vitality and great damage: his stories of the Negro Leagues, of his father's brutality and "
          "of his own time in prison are the play's music, and his refusal of Cory's scholarship is "
          "both a jealous insistence that his son not have what he was denied and a genuinely protective "
          "fear that a Black athlete will be discarded again. The fence of the title is built across "
          "both acts and means different things to each character - Rose's enclosure of her family, "
          "Troy's unfinished defence, Cory's barrier - and Wilson uses it as the play's single stage "
          "symbol without forcing it into an allegory. The play's most important move is theological: "
          "Troy wrestles with Death as an actual presence throughout, in the manner of a blues singer's "
          "boast, and the ending, in which Gabriel's horn-trumpet at the funeral blows open the gates of "
          "heaven, gives that boast a ritual answer. Wilson's language is the play's achievement: long "
          "monologues in the cadences of 1950s Black Pittsburgh speech, with the blues, the union and "
          "baseball as a shared vocabulary, and an ear for the moment when a joke turns into a wound.",
  themes_text="The first subject is the inheritance of slavery and the colour line as it operates in "
              "ordinary life: Troy's baseball career is the play's image of a meritocracy that was "
              "never open to him. The second is fatherhood and the reproduction of damage, since Troy "
              "repeats on Cory the violence his own father used on him and knows that he is doing it. "
              "The third is Rose's claim to dignity and her insistence on responsibility, which is the "
              "play's moral centre. The fourth is death, which Troy personifies and fights, and which "
              "the play treats as a social fact - the deaths of Black men - as well as a mythic one.",
  structure="Two acts in a single unit set, the backyard of the Maxson house, with the fence under "
            "construction across both acts; the action moves through a series of conversations and "
            "confrontations rather than a plotted intrigue, and the climax is a domestic quarrel rather "
            "than a public event; a funeral and a child's birth enclose the end.",
  style="Naturalistic dialogue in Black Pittsburgh speech, with long arias of monologue; the blues and "
        "the Negro Leagues as the play's shared cultural reference; a single symbolic object on stage; "
        "and a mixture of realistic detail with a mythic register in Troy's addresses to Death.",
  ctx="Fences was written in the mid-1980s as the sixth of Wilson's cycle and premiered at Yale Rep in "
      "1985 before its 1987 Broadway production with James Earl Jones, which made Wilson a national "
      "figure; the play's 1957 setting is the year the civil rights movement reached Little Rock and "
      "the year before the integration of major-league baseball's southern spring training. It was "
      "revived on Broadway in 2010 with Denzel Washington and filmed in 2016 with the same actor and "
      "Viola Davis.",
  sig="Fences is the most honoured American play of its decade and the one through which Wilson is "
      "known to readers who do not go to the theatre; the Century Cycle as a whole is generally "
      "described as the most sustained dramatic project in American literature, and Fences is its most "
      "performed play. The Norton's inclusion of it makes the anthology's American volume a record of "
      "drama as well as of poetry and fiction in the period.",
  canon="Major canon",
  crit="Criticism reads the play through the fence, through Troy's relation to the blues and to Death, "
       "and through Wilson's argument, set out in his 1996 essay 'The Ground on Which I Stand', that "
       "African American theatre needs Black institutions rather than integration into white ones. The "
       "standard critique - that Wilson's women are given less interiority than his men - was sharpened "
       "by later criticism of the cycle, while Rose's part in Fences is generally exempted from it.",
  biblio="First performed at the Yale Repertory Theatre in 1985; published by New American Library "
         "(Plume) in 1986 and opened on Broadway at the 46th Street Theatre in March 1987. A selection "
         "of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The premiere and Broadway dates are given from the standard production record; the play's text "
        "was not read in full for this record, and the account of the plot rests on its published "
        "text and on the standard critical summaries. The 1986 New American Library publication date is "
        "that of the first edition.",
  ver="partially verified", sources=[W_AWIL, FENCES, NAAL]),
W10("How to Tell a True War Story", TOB, "1987",
  "Short story (metafictional)", "major",
  genres=G("Short Story", "War Novel", "Metafictional Novel"),
  themes=T("War, combat and its aftermath", "Memory, trauma and testimony",
           "Language, writing and the limits of representation", "Death, illness and mourning"),
  movements=M(POSTMOD),
  overview="'How to Tell a True War Story' was first published in Esquire in October 1987 and collected in "
           "The Things They Carried (Boston: Houghton Mifflin, 1990), where it is the seventh of "
           "twenty-two linked stories. It is the most discussed American short story about the Vietnam "
           "War, and it is as much an essay on storytelling as a story.",
  content="The narrator, named Tim O'Brien, tells of the death of his friend Curt Lemon, killed by a "
          "booby-trapped 105-mm round while playing catch with Rat Kiley, and of Rat Kiley's letter to "
          "Lemon's sister, who never answers. He tells of a listening post in the mountains where the "
          "soldiers hear music and voices in the dark and call in artillery on a silence, and the "
          "company's CO orders them to keep listening. He tells the story of the water buffalo, which "
          "Rat Kiley tortures and shoots after Lemon's death. Between the stories he states rules: that "
          "a true war story is never moral, that it cannot be believed and cannot be doubted, that if "
          "it seems moral do not believe it, that in a true war story nothing much happens, and that "
          "the ending is not the point. He admits that he has told the story of Lemon's death "
          "differently at different times - the booby trap, the sunlight, the smoke - and says that the "
          "story he tells now is the one that is truest.",
  summary="The story is a demonstration of its own thesis, which is that a war story's truth is not the "
          "accuracy of its events. The narrative is broken into short numbered sections that move "
          "between anecdote and aphorism, and the narrator repeatedly interrupts his own telling to "
          "comment on it, so that the reader is never allowed to settle into believing what is told. The "
          "famous sentences are the ones that state the paradox: 'A true war story is never moral', "
          "'you can tell a true war story by the questions you ask', 'in a true war story nothing is "
          "ever absolutely true'. O'Brien's method is to make the reader feel the difference between "
          "happening-truth and story-truth, the first being what occurred and the second being what the "
          "telling makes real, and to argue that only the second can carry the war to someone who was "
          "not there. The water buffalo passage is the story's most disturbing sequence and its clearest "
          "example: the torture of the animal is not explained, and its absence of explanation is "
          "offered as the definition of a true war story. The ending, in which the narrator addresses "
          "the reader directly and tells her that she is the audience for a story she cannot hear, "
          "completes the argument by moving the problem of testimony into the act of reading.",
  themes_text="The first subject is the relation of truth to fiction, treated not as a philosophical "
              "puzzle but as a soldier's practical problem. The second is grief and the failure of "
              "consolation, figured in the unanswered letter to Lemon's sister. The third is the "
              "incommunicability of combat and the obligation to try to communicate it anyway. The "
              "fourth is memory, since the story insists that what is remembered changes and that the "
              "change is not a corruption but the material.",
  structure="A sequence of short numbered sections alternating between anecdotes and rules, with the "
            "narrator interrupting his own narrative; no single plot, and an ending that addresses the "
            "reader rather than closing the story.",
  style="A plain, declarative American sentence; direct address to the reader; aphorism used as "
        "structure; repetition of key statements with variation; and a refusal of figurative heightening "
        "at the moments of greatest violence.",
  ctx="The story appeared in Esquire in 1987 and in book form in 1990, fifteen years after the end of "
      "the Vietnam War and in the year of the Gulf War's build-up; it belongs to a late phase of "
      "American Vietnam writing in which the war is treated as a problem of memory and representation "
      "rather than of combat. O'Brien served in Vietnam in 1969-70 and the collection's narrator shares "
      "his name and much of his biography, which has made the stories' status a continuing critical "
      "question.",
  sig="The story is the central text in the American literature of the Vietnam War and one of the "
      "standard examples in discussions of metafiction and of testimony; its formulations are quoted in "
      "historiography and journalism as well as in literary criticism. The Norton prints it as a story "
      "in its own right, which treats a chapter of a linked collection as a discrete literary work.",
  canon="Major canon",
  crit="Criticism reads the story with the collection's other metafictional pieces and debates whether "
       "its narrator's admissions make it more or less reliable; the standard account treats the "
       "happening-truth and story-truth distinction as the collection's governing idea. Historians of "
       "the war have cited it as evidence of how soldiers' memories work, and the story is regularly "
       "taught in courses on trauma and on the ethics of representation.",
  biblio="First published in Esquire, October 1987; collected in The Things They Carried (Boston: "
         "Houghton Mifflin, 1990). A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The Esquire appearance of 1987 is the earliest publication found and is the date the Norton "
        "list carries; the story's text was read from the 1990 collection, which may differ from the "
        "magazine version.",
  ver="partially verified", sources=[W_TOB, THINGS, NAAL]),
W10("Facing It", YK, "1988",
  "Poem (free verse, short lines)", "major",
  genres=G("Lyric Poetry", "Elegiac Poetry", "Political Poetry"),
  themes=T("War, combat and its aftermath", "Death, illness and mourning", "Memory, trauma and testimony",
           "Race, racism and the struggle for civil rights"),
  movements=M(PERF),
  overview="'Facing It' is the closing poem of Dien Cai Dau (Middletown: Wesleyan University Press, 1988), "
           "Yusef Komunyakaa's book about his service in Vietnam. It describes a visit to the Vietnam "
           "Veterans Memorial in Washington and is the most anthologised American poem about that war.",
  content="The poem begins 'My black face fades, / hiding inside the black granite', and its speaker "
          "stands at the wall reading names. The reflection in the polished stone keeps interfering with "
          "what he sees: his own face and the names are on the same surface, a woman is brushing a "
          "boy's hair in the reflection, and a white vet's image floats beside him. He touches a name "
          "and the poem's most quoted line follows - 'I'm stone. I'm flesh.' - and the poem moves "
          "between the two states for its remainder: he sees the dead in the wall, he watches a plane "
          "in the sky, and at the end he is 'inside the Vietnam Veterans Memorial' watching the "
          "reflection of a woman trying to erase names, and the poem closes 'No, she's brushing a boy's "
          "hair'.",
  summary="The poem's subject is that seeing the memorial is not a single act, and its technique is the "
          "double exposure of reflection and inscription. Komunyakaa uses the wall's mirror surface to "
          "put the living and the dead in one plane, so that the poem's 'I' is simultaneously the "
          "viewer outside the wall and a name inside it. The line 'I'm stone. I'm flesh' is the whole "
          "argument in four words, and the poem does not resolve it: the speaker moves between "
          "identifying with the dead and being restored to his body by ordinary life - the woman and "
          "the boy. The poem's racial thinking is carried by 'my black face' in the first line and by "
          "the 'white vet's image' in the middle, so that the memorial's promise of a common sacrifice "
          "is placed against the difference the war also enforced. The ending is a correction of "
          "vision: what looks like a woman erasing names is a woman brushing a boy's hair, which means "
          "that the poem's grief is interrupted by the ordinary, and that the interruption is the "
          "poem's consolation without being its resolution. The form is short free-verse lines with "
          "abrupt enjambment, and the economy is extreme: the whole poem is under forty lines, and almost "
          "every line contains a verb of seeing. It is the one poem in Dien Cai Dau to make the memorial "
          "itself the subject, and that choice - to write about the wall rather than about the fighting - "
          "is what has kept it in circulation.",
  themes_text="The first subject is the Vietnam Veterans Memorial itself and the way its design - black "
              "granite, names in chronological order, no commentary - makes mourning a reflective act. "
              "The second is the survivor's guilt, since the speaker is alive and his reflection proves "
              "it. The third is race, since a Black veteran at the wall is a reminder of who fought and "
              "who is remembered. The fourth is the ordinary life that continues beside the monument, "
              "carried by the woman and the boy.",
  structure="A single unbroken lyric of short lines, organised by the alternation of what is seen in the "
            "stone and what is seen in the world, ending on a correction of the poem's own image.",
  style="Very short free-verse lines; present-tense perception; enjambment that forces the reader to "
        "hold two meanings at once; almost no adjectives of feeling; and a vocabulary drawn from light, "
        "stone and water rather than from combat.",
  ctx="The Vietnam Veterans Memorial, designed by Maya Lin, was dedicated in 1982, and the poem was "
      "written in the mid-1980s and published in Dien Cai Dau in 1988, when public commemoration of "
      "Vietnam service had become a national argument. Komunyakaa served in Vietnam as an army "
      "correspondent in 1969-70 and has said he could not write about it for years; the book's title is "
      "the soldiers' slang phrase for a dead or crazy comrade.",
  sig="'Facing It' is the American poem about the Vietnam War most often taught and anthologised, and "
      "it is the poem by which Komunyakaa's generation of Vietnam veterans' writing is represented in "
      "the Norton; its lines are quoted in criticism on memorials, race and American memory. Its "
      "presence in the anthology's period gives the war a poem as well as a story, alongside O'Brien's.",
  canon="Major canon",
  crit="Criticism reads the poem's mirror structure as its argument - the reflection makes the viewer "
       "part of the monument - and discusses 'I'm stone. I'm flesh' as a condensation of the veteran's "
       "double existence; the racial reading, centred on the black granite and the black face, has been "
       "developed by critics writing on African American war poetry. The closing correction is "
       "generally read as the poem's refusal of closure.",
  biblio="First published in Dien Cai Dau (Middletown, CT: Wesleyan University Press, 1988); collected "
         "in Neon Vernacular (1993) and Pleasure Dome (2001). A selection of The Norton Anthology of "
         "American Literature, 11th edition, vol. E.",
  notes="The poem was read for this record from its published text; the anthology's page reference and "
        "the date of the poem's first magazine appearance, if any, were not established.",
  ver="partially verified", sources=[W_YK, DCD, NAAL]),
W10("Slam, Dunk, & Hook", YK, "1992",
  "Poem (free verse, basketball poem)", "significant",
  genres=G("Lyric Poetry", "Narrative Poetry", "Performance Poetry"),
  themes=T("Childhood, adolescence and coming of age", "Race, racism and the struggle for civil rights",
           "Art, the artist and the creative life", "Land, place and regional belonging"),
  movements=M(PERF),
  overview="'Slam, Dunk, & Hook' was first published in Callaloo in the summer of 1991 and collected in "
           "Magic City (Middletown: Wesleyan University Press, 1992), Komunyakaa's book of Bogalusa "
           "childhood. It is a poem about boys playing basketball, and it is the best-known example of "
           "his use of sport as a form of lyric knowledge.",
  content="The poem opens with 'Fast breaks. Lay ups. With Mercury's / Insignia on our sneakers', and it "
          "calls the players 'the sons of angels, / gone dazzling in mid-air'. Its boys play on a court "
          "and in a game that is half myth - 'we were dangerous', they wore 'our secret stories' like "
          "sweat - and the poem's images are of flight, of the body outwitting gravity, and of the game "
          "as an escape from the town as well as a spell held inside it. It ends with the speakers "
          "'glistening like a glazed donut' and back on the ground, the court returning to its ordinary "
          "place.",
  summary="The poem is about the beauty of a game played by boys who have nothing else, and it refuses "
          "the obvious irony that would point out the limits of basketball as a way out of poverty. "
          "Komunyakaa's method is to write the game as if it were a mythology, with Mercury's winged "
          "sneakers and angels in mid-air, and then to bring it back to the ordinary world without "
          "deflating it: the boys are sons of angels who also eat glazed doughnuts. The poem's politics "
          "are implicit in the myth's materials. The gods are named through their commercial logos, the "
          "flight is the flight of Black boys in a small Southern town in the segregation years, and the "
          "'secret stories' the players carry are connected to the rest of Magic City, whose poems "
          "record the terror and the beauty of Bogalusa together. The rhythm is the poem's real argument: "
          "short lines with heavy stresses that mimic the stops and breaks of the game, so that reading "
          "it is closer to performing it than to describing it. The close is a deliberate return - the "
          "players come down to the ground, the poem ends, the game is over - and it is that return that "
          "keeps the poem from being sentimental about sport.",
  themes_text="The first subject is adolescence and physical joy, and the poem is unusual in American "
              "poetry for describing athletic beauty without condescension. The second is race and the "
              "segregated South in which these boys play. The third is the relation of play to art, "
              "since the poem treats the game as a composed thing with its own form. The fourth is "
              "escape, held in tension with the town the boys cannot actually leave.",
  structure="A single free-verse lyric in short lines, organised by the movement of a game from fast "
            "break to final return, with no stanza division beyond the poem's own turns.",
  style="Short lines with hard stresses; present tense and first-person plural; proper names and brand "
        "names used as mythic material; a jazz-like syntax that drops subjects; and an early rhyme of "
        "the sacred with the commercial.",
  ctx="Magic City appeared in 1992, the year after Callaloo printed the poem, and belongs to the period "
      "in which Komunyakaa was writing two books at once - Dien Cai Dau about the war and Magic City "
      "about the South. Its Bogalusa is the mill town of his childhood, and the poem's publication in "
      "Callaloo places it in the leading journal of African American literary criticism and writing.",
  sig="The poem is one of the most anthologised American poems about sport and the standard example of "
      "Komunyakaa's early style; it is a Norton selection, and its pairing with 'Facing It' shows the "
      "two poles of the anthology's representation of him - the war and the boyhood that preceded it.",
  canon="Secondary canon",
  crit="Criticism reads the poem's mythologising of the playground as a characteristic Komunyakaa move, "
       "and discusses it with the basketball poems of other Black poets; the standard reading is that "
       "the poem's classical reference is not ornamental but a claim about the value of the boys' "
       "play. The Callaloo bibliography records its first appearance.",
  biblio="First published in Callaloo 14.3 (Summer 1991), pp. 631-632; collected in Magic City "
         "(Middletown, CT: Wesleyan University Press, 1992) and Pleasure Dome (2001). A selection of "
         "The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The Callaloo first appearance is from the Michael Collins bibliography of Komunyakaa in "
        "Callaloo; the poem's text was read from the collection, not from the journal.",
  ver="partially verified", sources=[W_YK, MAGIC, NAAL]),
W10("My Father's Love Letters", YK, "1992",
  "Poem (free verse, narrative)", "significant",
  genres=G("Lyric Poetry", "Narrative Poetry"), themes=T("Family, marriage and domestic life",
           "Race, racism and the struggle for civil rights", "Class, labour and social mobility",
           "Love, intimacy and loss"),
  movements=M(PERF),
  overview="'My Father's Love Letters' is in Magic City (Middletown: Wesleyan University Press, 1992), "
           "Komunyakaa's second book of Bogalusa poems. It is a short narrative lyric about a boy "
           "writing letters for his illiterate father, and it is among his most personal poems.",
  content="The poem's speaker, as a boy, is asked to write love letters for his father, who cannot write "
          "them himself: the father dictates, the son writes, and the letters are sent to women. The "
          "poem describes the father's authority in the house, the mother's silence and labour, and the "
          "son's position as the instrument through which the father speaks to other women. Its images "
          "are domestic and exact - the table, the paper, the dictation - and the poem closes with the "
          "son grown, understanding what he was made to do and what it cost the household.",
  summary="The poem's subject is not infidelity but power, and its technique is to keep the child's "
          "point of view while letting the reader see what the child does not. The father cannot write, "
          "so the son's literacy makes him both necessary and complicit: he is the hand of his father's "
          "desire and the witness of his mother's injury. Komunyakaa's short lines and his refusal to "
          "comment allow the scene to stand as an image rather than a judgement, and the poem's restraint "
          "is what makes it painful. The larger subject is the household of a Black working family in "
          "the segregated South, where the father's word is the only authority available to him in a "
          "world that gives him none, and where his son's education is at once his pride and the means "
          "of his exposure. The poem is also, quietly, about writing: the son's first literary act is a "
          "love letter dictated by someone else, and the poem records the origin of a writer's relation "
          "to language in service to another person's need.",
  themes_text="The first subject is the father-son relation, held between love and coercion. The second "
              "is the mother's position, present in the poem mostly through what is not said to her. "
              "The third is literacy as a form of power inside a family that has been denied it "
              "publicly. The fourth is the making of a writer, since the poem is an account of the "
              "first time the speaker used writing for someone else.",
  structure="A short free-verse narrative in a single remembered scene, with the dictation as its "
            "organising action and a closing movement into the speaker's adult understanding.",
  style="Short unpunctuated lines; concrete domestic objects; the father's speech rendered in direct "
        "quotation against the son's silence; and a syntax that withholds judgement to the end.",
  ctx="Magic City (1992) collects the Bogalusa material Komunyakaa had been writing since Copacetic "
      "(1984), and the book's Southern mill town is treated with the same historical attention he gave "
      "the war in Dien Cai Dau. The poem's illiterate father and literate son belong to the first "
      "generation of Black Southerners with access to schooling after segregation, and the poem's "
      "situation is a common one in African American memoir.",
  sig="The poem is one of the most frequently anthologised in Magic City and is regularly taught as an "
       "example of the narrative lyric in contemporary African American poetry; the Norton's selection "
       "of it with 'Slam, Dunk, & Hook' gives the anthology both the public and the domestic sides of "
       "the book.",
  canon="Secondary canon",
  crit="Criticism reads the poem with the other family poems of Magic City and notes its treatment of "
       "literacy as an inheritance; the standard account of Komunyakaa's development places the Bogalusa "
       "poems as the ground from which the Vietnam book was written, since he wrote about the town "
       "before he could write about the war.",
  biblio="First published in Magic City (Middletown, CT: Wesleyan University Press, 1992); collected in "
         "Pleasure Dome (2001). A selection of The Norton Anthology of American Literature, 11th "
         "edition, vol. E.",
  notes="The poem's first periodical appearance, if any, was not established; the date given is that of "
        "the collection, which is the earliest publication found.",
  ver="partially verified", sources=[W_YK, MAGIC, NAAL]),
W10("Nude Study", YK, "1992",
  "Poem (free verse)", "significant",
  genres=G("Lyric Poetry", "Cultural Criticism"), themes=T("Art, the artist and the creative life",
           "Race, racism and the struggle for civil rights", "Sexuality, desire and the closet",
           "History, truth and the uses of the past"),
  movements=M(PERF),
  overview="'Nude Study' was first published in Poetry in the winter of 1992 and collected in Taboo: The "
           "Wishbone Trilogy, Part One (New York: Farrar, Straus and Giroux, 2004). It is a poem about "
           "a painting - John Singer Sargent's studies of the Black model Thomas Eugene McKeller - and "
           "it appeared in Poetry in 1992 and was collected twelve years later.",
  content="The poem looks at Sargent's nude studies of Thomas E. McKeller, the African American bellhop "
          "and elevator operator from Boston who modelled for the murals Sargent painted for the Museum "
          "of Fine Arts and Harvard's Widener Library, and whose body was used for the classical and "
          "mythological figures in those murals. The poem describes the drawings' beauty and the "
          "conditions of their making: a Black man's body made into the white classical ideal, a model "
          "paid for his pose and unnamed in the work, and a painter using him as a means. It holds "
          "admiration for the drawing against the knowledge of what the drawing does.",
  summary="The poem is an ekphrasis that turns into an argument about appropriation, and its charge "
          "comes from the fact that Sargent's drawings are genuinely beautiful. Komunyakaa does not "
          "resolve the contradiction between the aesthetic value of the work and the erasure it "
          "performs; he lets both stand, and the poem's intelligence is in its refusal of an easy "
          "verdict. The figures are classical - the murals depict Greek myth and the figures of the "
          "library - so that McKeller's body is recruited into a European tradition that would not have "
          "admitted him as a person, and the poem's title names the problem: a 'study' is a painter's "
          "preparation, an exercise in seeing, and the poem is a study of that study. Komunyakaa's late "
          "style is much more discursive than the short lyric of Magic City, with long sentences and "
          "an essayistic movement, and 'Nude Study' is a characteristic example: it thinks in public "
          "about the ethics of looking, and the first person of the Black viewer is placed against the "
          "white painter's gaze.",
  themes_text="The first subject is the erasure of the Black model in Western art, and the poem's "
              "specific case is the classical nude. The second is the ethics of aesthetic pleasure, "
              "since the poem admits to admiring what it criticises. The third is race and the "
              "classical tradition, which the murals' use of McKeller makes unavoidable. The fourth is "
              "the act of looking itself, which the poem treats as a transaction between unequal "
              "parties.",
  structure="An ekphrastic lyric that moves between description and commentary, with no stanza break "
            "marking a change of argument and no resolution at the close.",
  style="Discursive free verse with long sentences and Latinate vocabulary; ekphrastic description that "
        "keeps the painter's technique in view; a first-person viewer who is also a critic; and an "
        "absence of irony.",
  ctx="Sargent painted the McKeller studies in 1917-20 for the murals of the Museum of Fine Arts, Boston "
      "and Harvard's Widener Library, and McKeller's identity as the model became a subject of art "
      "history and public discussion in the 1990s and after. Komunyakaa's poem appeared in Poetry in "
      "the winter of 1992 and was collected, with revisions and a trilogy's architecture around it, in "
      "Taboo (2004); the 1992 periodical publication is the first and is the date recorded here.",
  sig="The poem is the most discussed piece in Taboo and a standard text in the art-history and "
      "literature of the Black model. Its 1992 magazine publication puts it inside the anthology's "
      "period even though the book it is known from appeared in 2004 - a case of the anthology printing "
      "an old poem in a new book, which is exactly why the record dates the first printing and names the "
      "collection separately.",
  canon="Secondary canon",
  crit="Art historians and critics have written on the McKeller studies since the 1990s, and Komunyakaa's "
       "poem is regularly cited in that discussion as the literary treatment of them; the standard "
       "reading of Taboo treats the trilogy as an attempt to write a history of race and art in the "
       "West, with 'Nude Study' as its most concentrated example.",
  biblio="First published in Poetry (Winter 1992); collected in Taboo: The Wishbone Trilogy, Part One "
         "(New York: Farrar, Straus and Giroux, 2004). A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E.",
  notes="The Poetry appearance of winter 1992 is the earliest publication found and is the date recorded; "
        "the 2004 book is named as the collection the poem is known from. The Norton list carried the "
        "poem as undated before this wave.",
  ver="partially verified", sources=[W_YK, TABOO, NAAL]),
W10("Maus", AS, "1986",
  "Graphic novel / graphic memoir (two volumes, 1986 and 1991)", "major",
  genres=G("Graphic Novel", "Autobiography", "Biography", "Historical Writing"),
  themes=T("The Holocaust, atrocity and historical memory", "Memory, trauma and testimony",
           "Family, marriage and domestic life", "Race, racism and the struggle for civil rights",
           "Death, illness and mourning"),
  movements=M(POSTMOD),
  overview="Maus is Art Spiegelman's two-volume graphic narrative of his father's survival of the "
           "Holocaust, in which Jews are drawn as mice, Germans as cats and Poles as pigs. Its first six "
           "chapters were serialised in RAW from 1980 and published as Maus I: A Survivor's Tale - My "
           "Father Bleeds History (New York: Pantheon, 1986); the remainder appeared as Maus II: A "
           "Survivor's Tale - And Here My Troubles Began (Pantheon, 1991). The Norton prints chapter "
           "six, 'Mousetrap', from the first volume.",
  content="The frame is the present: Artie, the cartoonist, visits his father Vladek in Rego Park, Queens, "
          "and coaxes from him the story of the war. Inside the frame, Vladek's narrative runs from the "
          "courtship of his wife Anja in Sosnowiec, through the ghetto, the hiding places, the betrayal "
          "and the transports, to Auschwitz and Dachau and the death marches at the end of the war. "
          "Chapter six, 'Mousetrap', moves between the present-day household - Vladek's second wife "
          "Mala, his miserliness, his heart condition, his need for Artie's attention - and the "
          "wartime story, in which Vladek and Anja are hidden by Polish families and finally betrayed "
          "by one of them. The volume ends with Vladek burning Anja's diaries and with the couple's "
          "arrival at Auschwitz.",
  summary="The book's formal invention is the animal mask, and its effect is not allegory but "
          "estrangement: the reader is made to see that the categories of the Holocaust were themselves "
          "a way of sorting beings into species that could be killed without it counting as murder. "
          "Spiegelman complicates the scheme deliberately - there are Jewish mice who behave like cats, "
          "Poles in pig masks who save and betray, and in the second volume a German-Jewish couple, and "
          "Spiegelman himself in a mouse mask wearing a prisoner's uniform in 'Prisoner on the Hell "
          "Planet'. The second innovation is the doubling of time. Vladek's story is never given alone; "
          "it competes with the present-day errands and quarrels, and the reader sees that the father's "
          "survivor's habits - hoarding, penny-pinching, an inability to throw anything away - are the "
          "war continuing in a Queens apartment. The third is the book's admission of its own "
          "inadequacy: Artie is told by a survivor that Auschwitz has no place for cartoon mice, and the "
          "second volume includes 'Time Flies', in which the success of the first book is treated as a "
          "kind of fraud. The drawing is crude in the manner of the underground comix Spiegelman came "
          "from, and the crude mask is what allows the book to escape both the reverence and the "
          "kitsch of Holocaust representation.",
  themes_text="The first subject is the Holocaust itself, told in the specific and personal terms of one "
              "family rather than as historical summary. The second is the transmission of trauma to "
              "the second generation, since Artie is the book's real narrator and his inheritance is the "
              "book. The third is the ethics of representation: how, and whether, atrocity can be drawn. "
              "The fourth is the ordinary present, in which the survivor's household is both comic and "
              "wounding, and which the book insists on placing beside the camps.",
  structure="Two volumes of serialised chapters, each alternating the present-day interview with the "
            "wartime narrative, with the frame itself becoming a subject in the second volume; page "
            "layouts of varying panel sizes rather than a rigid grid, and a long silent 'Prisoner on the "
            "Hell Planet' inset.",
  style="Black-and-white brush and ink; anthropomorphic masks that are never explained; a visual "
        "vocabulary borrowed from the newspaper strip and the underground comix; handwritten narration "
        "boxes; and a deliberate roughness that refuses the polish of the memorial book.",
  ctx="The book grew out of a three-page strip, 'Maus', published in the underground magazine Funny "
      "Animals in 1972, and was serialised in RAW, the comics journal Spiegelman founded with "
      "Françoise Mouly, from 1980; the first collection appeared in 1986 and the second in 1991, and "
      "the completed work won a special Pulitzer Prize in 1992. Its publication coincided with the "
      "growth of Holocaust memory in the United States, the opening of the US Holocaust Memorial "
      "Museum (1993) and the academic legitimation of comics.",
  sig="Maus won the first Pulitzer Prize ever given to a comic and is the work through which the graphic "
      "novel became a subject of literary and historical study; it is taught in history departments as "
      "well as literature ones, and its animal masks are a standard example in discussions of "
      "representation and the Shoah. The Norton's selection of a single chapter places a comic - "
      "unmistakably a comic, with speech balloons - inside the American literary canon of the period, "
      "which is the anthology's largest single formal statement.",
  canon="Major canon",
  crit="The critical literature is very large: it includes Holocaust studies work on the ethics of "
       "comic-form testimony, comics scholarship on the animal mask and on layout, and the controversy "
       "over a 1991 review in The Village Voice. The standard reading treats the father-son frame as the "
       "book's true subject, with the camps narrated in order that the present can be understood; "
       "'Mousetrap' is the chapter usually cited for the interleaving of the two times.",
  biblio="Serialised in RAW (1980-91); published as Maus I (New York: Pantheon, 1986) and Maus II "
         "(Pantheon, 1991); collected as Maus: A Survivor's Tale (1992). The Norton prints chapter six, "
         "'Mousetrap', from the first volume. A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E.",
  notes="The exact page range of 'Mousetrap' in the anthology was not established. The chapter numbering "
        "and the placement of Anja's diaries and the arrival at Auschwitz at the end of volume one are "
        "given from the published book.",
  ver="partially verified", sources=[W_AS, MAUS, NAAL]),
W10("¡Yo!", JA, "1997",
  "Novel (multi-voice, told by a chorus of narrators)", "significant",
  genres=G("Literary Novel", "Domestic Fiction", "Bildungsroman"),
  themes=T("Migration, exile and diaspora", "Family, marriage and domestic life",
           "Gender, feminism and women's lives", "Language, writing and the limits of representation",
           "Identity, authenticity and the divided self"),
  movements=M(POSTCOL, FEM),
  overview="¡Yo! (Chapel Hill: Algonquin Books, 1997) is Julia Alvarez's second novel about the García "
           "family of How the García Girls Lost Their Accents (1991). It tells the story of the second "
           "sister, Yolanda, entirely through the voices of the people around her, and the Norton prints "
           "its chapter 'The Mother'.",
  content="The novel's premise is that everyone has a version of Yolanda except Yolanda, who is writing a "
          "novel in the third person and appearing only in other people's chapters. Her sisters, her "
          "cousins, her lovers, her teachers, her Dominican family's servants, her American landlords "
          "and her psychiatrist each narrate a section, and the composite portrait that emerges is of a "
          "woman divided by languages, loyalties and versions of herself. 'The Mother' is narrated by "
          "Yolanda's mother, Laura García, in the first person: she describes her daughter's return from "
          "college changed, her English, her refusal of the family's expectations, and her own "
          "bewilderment at a child who has become a stranger, and she measures the distance between the "
          "life she imagined for her daughter and the American one she has.",
  summary="The novel's structure is its argument. By refusing Yolanda a first-person chapter, Alvarez "
          "makes the immigrant writer's identity a composite of other people's descriptions, which is "
          "the condition the book is about: Yolanda is an American writer to her Dominican family and a "
          "Dominican daughter to her American friends, and neither account is complete. The mother's "
          "chapter is the emotional centre of the novel because it is told by the person with the "
          "strongest claim to know her, and because Laura's account is loving and uncomprehending at the "
          "same time. Alvarez handles the mother's voice with great care: Laura is not a villain and not "
          "a saint, she is a woman of a certain class and generation whose daughter's freedoms - sexual, "
          "literary, linguistic - are real gains and real losses at once. The novel's comedy comes from "
          "the chorus of narrators, each convinced that Yolanda is the problem and that they are the "
          "solution; its sorrow comes from the recognition that no single narrator, including the "
          "mother, can hold her. The book's bilingual title and its untranslated Spanish are part of the "
          "same argument about a life lived in two languages, and 'The Mother' is the chapter in which "
          "the gap between the languages is most painfully marked.",
  themes_text="The first subject is immigration and the family that remains behind, treated from the "
              "mother's side as well as the daughter's. The second is bilingualism and the loss of "
              "intimacy that comes with a new language. The third is the position of a woman writer "
              "inside a traditional family, and the cost of her autonomy to her mother. The fourth is "
              "narrative authority itself, since the novel is about who is allowed to tell a life.",
  structure="A sequence of first-person chapters each spoken by a different character, with Yolanda "
            "herself withheld; no single plotline, and a chronology that returns to the same events "
            "from different angles; the mother's chapter is one of the longest.",
  style="Each chapter in a distinct idiolect - Dominican Spanish-inflected English, academic English, "
        "child's English - with Spanish left unglossed; direct address and conversational framing; and "
        "a comic timing learnt from the family anecdote.",
  ctx="¡Yo! appeared in 1997, three years after In the Time of the Butterflies and six after How the "
      "García Girls Lost Their Accents, at a point when US Latina fiction had a mass readership; "
      "Algonquin Books was a small Southern press that had become a significant publisher of American "
      "fiction. The novel's multi-voice form belongs to the 1990s interest in polyphonic and "
      "testimonial narrative, and its Dominican material reflects the growth of the Dominican American "
      "community in New York after 1965.",
  sig="The novel is a standard example of the polyphonic immigrant novel and is regularly taught "
      "alongside García Girls, which it revises; 'The Mother' is the chapter most often anthologised "
      "because it gives the mother's voice that the earlier novel does not. The Norton's selection of "
      "it registers the 1990s as a decade of US Latina writing and Alvarez as one of its central "
      "practitioners.",
  canon="Secondary canon",
  crit="Criticism reads the novel as a critique of the first-person authority of García Girls and as an "
       "experiment in collective narration; the standard account notes that by withholding Yolanda, "
       "Alvarez dramatises the impossibility of a single immigrant self. The mother's chapter is "
       "usually discussed for its sympathetic rendering of a figure who could easily have been an "
       "obstacle.",
  biblio="First published by Algonquin Books of Chapel Hill in 1997. A selection of The Norton Anthology "
         "of American Literature, 11th edition, vol. E, which prints the chapter 'The Mother'.",
  notes="The novel was not read in full for this record; 'The Mother' was read in its published form and "
        "the rest of the description rests on the standard accounts of the novel's structure. The "
        "chapter's page range in the anthology was not established.",
  ver="partially verified", sources=[W_JA, IYO, NAAL]),
W10("Call It Fear", JH, "1983",
  "Poem (free verse, short lines)", "significant",
  genres=G("Lyric Poetry", "Confessional Poetry"), themes=T("Memory, trauma and testimony",
           "Violence, crime and justice", "Gender, feminism and women's lives",
           "Indigenous survival, land and sovereignty"),
  movements=M(NAR, FEM),
  overview="'Call It Fear' opens She Had Some Horses (New York: Thunder's Mouth Press, 1983), the book that "
           "established Joy Harjo. It is a short poem spoken to the self about fear, and it sets the "
           "terms - a first person that is also a people, a past that will not stay past - for the "
           "whole collection.",
  content="The poem addresses someone, probably the speaker herself, and tells them to call the thing they "
          "have been running from by its name: fear. It places the fear in a landscape - a road, a "
          "house, a night - and in a history, and it refuses to separate the two. Its lines are short "
          "and its language is plain, and the poem turns at the end toward the possibility of putting "
          "the fear down.",
  summary="'Call It Fear' is a poem of naming, and its method is the Mvskoke and broadly Native American "
          "practice of speaking to a condition in order to place it outside the person. The fear is not "
          "analysed and its origins are not narrated; the poem proceeds as if the act of naming were "
          "itself the work, and the reader is placed in the position of the one who is told to speak. "
          "Harjo's short lines carry a great deal of white space, and the effect is of a voice thinking "
          "aloud in a room rather than declaring from a platform. The poem's historical dimension is "
          "implicit but unmistakable in the book's context: this is a Native woman's fear, in a country "
          "whose history has given her reasons for it, and the poem's refusal to explain is a refusal to "
          "make the fear legible for an outsider. What makes it survive as a poem rather than a "
          "statement is its rhythm - the repetition of the imperative, the short breath of the lines, "
          "the sense that the speaker is talking herself into the naming.",
  themes_text="The first subject is fear itself, treated as a physical and historical fact rather than a "
              "mood. The second is the relation of the present self to a violent past, which the poem "
              "holds without narrating. The third is gender, since the fear is a woman's and the "
              "collection's other poems make clear what has caused it. The fourth is survival, which "
              "the poem approaches through the act of speech.",
  structure="A short free-verse poem in very short lines, built on an imperative address and repetition, "
            "with a turn toward release at the close rather than a narrative progression.",
  style="Very short free-verse lines; plain diction; repetition and anaphora; direct address; and an "
        "absence of punctuation at the line ends, so that the poem moves by breath.",
  ctx="She Had Some Horses appeared from Thunder's Mouth Press in 1983, the year of Harjo's MFA from "
      "Iowa and of the consolidation of the Native American Renaissance; the book's poems draw on "
      "Mvskoke ceremony, on the Oklahoma landscape and on the experience of a Native woman in the "
      "American West. Thunder's Mouth was the press that also published Ortiz's From Sand Creek and "
      "Harjo's own She Had Some Horses album material.",
  sig="The poem opens the collection that made Harjo's name and is the standard entry point to her early "
      "work; its imperative address and its short line are the features her later poetry developed. It "
      "is a Norton selection and, with 'White Bear', represents the 1983 book in the anthology.",
  canon="Secondary canon",
  crit="Criticism reads the poem as a ceremonial act of naming and places it in the tradition of Native "
       "women's writing about violence; the standard account of She Had Some Horses treats its opening "
       "as a threshold poem that establishes the collection's speaking position.",
  biblio="First published in She Had Some Horses (New York: Thunder's Mouth Press, 1983); collected in "
         "How We Became Human: New and Selected Poems (New York: W. W. Norton, 2004). A selection of "
         "The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The poem's text was read from the collection and the 2004 selected poems; the first periodical "
        "appearance, if any, was not established.",
  ver="partially verified", sources=[W_JH, SHH, NAAL]),
W10("White Bear", JH, "1983",
  "Poem (free verse, visionary lyric)", "significant",
  genres=G("Lyric Poetry", "Nature Poetry"), themes=T("Myth, folklore and the supernatural",
           "Nature, ecology and environmental crisis", "Family, marriage and domestic life",
           "Indigenous survival, land and sovereignty"),
  movements=M(NAR),
  overview="'White Bear' is in She Had Some Horses (New York: Thunder's Mouth Press, 1983). Harjo has said "
           "she wrote it in 1983, on the point of boarding a plane out of a city, and it is a visionary "
           "poem in which a white bear appears as a figure of balance and of the northern cold.",
  content="The poem begins 'Somewhere, she dreamed, there is the white bear / moving down from the north' "
          "and describes the bear motioning its paws 'like a long arctic night'. It holds images of "
          "balance - 'the whole world balanced in between', carved of ebony and ice - and of the "
          "speaker's daughter's eyes, black nights, and the white bear moon like an ivory cradle. Its "
          "closing movement turns on the tipping of that cradle: 'it could go either way', and the poem "
          "ends with the assertion that 'all darkness is open to light'.",
  summary="The poem is a dream narrative in which the dreaming mind is given the authority of a vision. "
          "The white bear is not explained and not identified with a particular tribal figure; it is a "
          "creature of the north, a moon and a cradle, and the poem's images accumulate rather than "
          "argue. That accumulation is Harjo's method in the early books: a sequence of luminous objects "
          "arranged so that the reader feels their relation before understanding it. The daughter's eyes "
          "in the middle of the poem make the vision domestic as well as cosmic, and the cradle image "
          "ties the movement of the northern sky to the rocking of a child. The ending is the poem's "
          "argument: the balance could tip either way, and the speaker chooses to say that darkness is "
          "open to light, which is a statement of survival made in the grammar of a blessing. The poem's "
          "landscape is not named as Oklahoma or Alaska but as a dream's north, and its power comes from "
          "the refusal to localise the myth.",
  themes_text="The first subject is the visionary and the dream, treated as legitimate knowledge rather "
              "than as fancy. The second is balance and precariousness, since the poem's world is held "
              "in a cradle that could tip. The third is the northern landscape and its animals, which "
              "the poem uses as spiritual presences. The fourth is the daughter, who connects the "
              "cosmic vision to a family and a future.",
  structure="A single unbroken free-verse lyric of visionary images, with no stanza divisions and a "
            "closing assertion that turns the description into a blessing.",
  style="Unpunctuated free verse in a single long sentence; repetition of 'the white bear'; images of "
        "ice, ebony, moon and cradle; and an incantatory syntax that holds the poem together without "
        "argument.",
  ctx="The poem was written in 1983, the year Harjo published She Had Some Horses and finished her MFA, "
      "and it belongs to the period in which Native American writers were making ceremonial and mythic "
      "material central to their poetics. The bear as a figure of power and of the north is widespread "
      "in Native North American traditions, and Harjo uses it without assigning it to a particular "
      "nation or story.",
  sig="'White Bear' is one of the most anthologised poems in She Had Some Horses and a standard example "
      "of the visionary mode in Native American poetry; it is a Norton selection, and with 'Call It "
      "Fear' it represents the collection. The Norton list carried it as undated before this wave.",
  canon="Secondary canon",
  crit="Criticism reads the poem's bear as a figure of the sacred without doctrinal content and notes "
       "the poem's movement from dream to blessing; the standard accounts of Harjo's early work place "
       "it among the poems that establish her association of animal presence, landscape and dream.",
  biblio="First published in She Had Some Horses (New York: Thunder's Mouth Press, 1983); collected in "
         "How We Became Human: New and Selected Poems (New York: W. W. Norton, 2004). A selection of "
         "The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The 1983 date rests on the collection's publication and on Harjo's own account of writing the "
        "poem that year; the text was read from the collection. The Norton list carried the poem as "
        "undated before this wave, and this record fixes it.",
  ver="partially verified", sources=[W_JH, SHH, NAAL]),
W10("Summer Night", JH, "1990",
  "Poem (free verse)", "significant",
  genres=G("Lyric Poetry", "Love Poetry"), themes=T("Love, intimacy and loss", "Memory, trauma and testimony",
           "Gender, feminism and women's lives", "Land, place and regional belonging"),
  movements=M(NAR, FEM),
  overview="'Summer Night' is in In Mad Love and War (Middletown: Wesleyan University Press, 1990), "
           "Harjo's fourth collection and the one that won the American Book Award. It is a short love "
           "poem that holds desire and the memory of violence in the same night.",
  content="The poem places two people together on a summer night, in a landscape of heat and insects, and "
          "it moves between the immediacy of touch and the knowledge that the past is still present in "
          "the body. Its images are of the natural world at night - the sound of insects, the dark, the "
          "warmth - and its address is intimate. It closes on a statement of the present as the only "
          "place love can happen, held against what has happened before.",
  summary="The poem's subject is the difficulty of being present with another person when the body "
          "remembers injury, and its technique is to keep the two registers in the same sentence. Harjo "
          "does not separate the love poem from the history of violence against women; the summer "
          "night's heat is both erotic and oppressive, and the insects' noise is both the sound of the "
          "world and a kind of vigilance. The poem's tenderness is not naive - it is a decision made in "
          "full knowledge - and that is what distinguishes In Mad Love and War, whose title announces "
          "the book's two subjects. The line is longer here than in She Had Some Horses, and the poem's "
          "rhythm is more conversational, which belongs to the widening of Harjo's style in the late "
          "1980s, when she began writing poems that could carry political statement without losing their "
          "lyric intensity.",
  themes_text="The first subject is love and desire, treated as an act of will in difficult conditions. "
              "The second is the memory of violence, which is present in the poem without being "
              "narrated. The third is the natural world as a witness and a participant. The fourth is "
              "the present moment, which the poem claims as the ground of any possible happiness.",
  structure="A short free-verse lyric in a single movement, built on the alternation of sensory "
            "description and intimate address, ending on a turn toward the present.",
  style="Conversational free verse with longer lines than the earlier books; sensory and nocturnal "
        "imagery; direct address to a lover; and a refusal of rhetorical closure.",
  ctx="In Mad Love and War was published by Wesleyan in 1990 and won the American Book Award; it belongs "
      "to the years in which Harjo was teaching in New Mexico and Arizona and performing with her band, "
      "and its poems move between the Southwest, Oklahoma and the wider world. It is the middle book "
      "between She Had Some Horses (1983) and The Woman Who Fell from the Sky (1994).",
  sig="The poem is a standard selection from In Mad Love and War and represents the erotic and "
      "conversational side of Harjo's work in the anthology, which otherwise draws on her visionary "
      "and political poems. It is a Norton selection.",
  canon="Secondary canon",
  crit="Criticism reads the collection's love poems as continuous with its political ones, and the "
       "standard account of Harjo's development treats In Mad Love and War as the book in which she "
       "widened her line and admitted a more directly personal voice.",
  biblio="First published in In Mad Love and War (Middletown, CT: Wesleyan University Press, 1990); "
         "collected in How We Became Human (2004). A selection of The Norton Anthology of American "
         "Literature, 11th edition, vol. E.",
  notes="The poem's first periodical appearance was not established; the 1990 collection date is the "
        "earliest publication found.",
  ver="partially verified", sources=[W_JH, INMAD, NAAL]),
W10("The Flood", JH, "1994",
  "Poem (free verse, narrative)", "significant",
  genres=G("Lyric Poetry", "Narrative Poetry"), themes=T("Indigenous survival, land and sovereignty",
           "History, truth and the uses of the past", "Memory, trauma and testimony",
           "Nature, ecology and environmental crisis"),
  movements=M(NAR),
  overview="'The Flood' is in The Woman Who Fell from the Sky (New York: W. W. Norton, 1994), the "
           "collection Harjo published the year after she began teaching at the University of "
           "Tucson. It is a narrative poem about water, loss and the return of what has been buried.",
  content="The poem tells of a flood that rises and takes what is in its path, and it moves between the "
          "physical event and the memories the water releases. Its images are of water carrying "
          "possessions, animals and the dead, and of survivors afterwards in the mud. The poem's voice "
          "is a witness's, and its movement is from catastrophe through loss to a settled knowledge of "
          "what has been changed.",
  summary="'The Flood' is characteristic of the collection in which Harjo turned from the short "
          "visionary lyric to poems with more narrative reach; its subject is not only a weather event "
          "but the way catastrophe rearranges a life and exposes what a community has been carrying. "
          "Water in Harjo's work is never only literal: it is the element that crosses boundaries, "
          "carries the dead and refuses to respect the divisions between past and present. The poem's "
          "narrative is episodic and its syntax is closer to speech than in the earlier books, and its "
          "power comes from the flatness with which terrible things are reported - the tone is not "
          "hysterical, and that calm is what makes it frightening. The collection's title, the Seneca "
          "story of the woman who fell from the sky onto the back of a turtle, is the mythic frame "
          "behind the poem, and 'The Flood' is one of the pieces in which the frame becomes visible: "
          "the world is remade after the water, and what survives is carried by the women who remember.",
  themes_text="The first subject is catastrophe and its aftermath, natural and historical at once. The "
              "second is the survival of Indigenous people and the memory of removal, carried in the "
              "image of water that has taken land. The third is memory, since the flood releases what "
              "was buried. The fourth is the mythic frame of the collection, which turns a weather "
              "event into a story of the world's remaking.",
  structure="A free-verse narrative in stanzas of varying length, moving chronologically through the "
            "flood and its aftermath, with interruptions of remembered speech and no formal climax.",
  style="Conversational free verse with narrative momentum; concrete images of water, mud and damaged "
        "objects; a flat, unhurried report tone; and a refusal of metaphor at the moments of greatest "
        "loss.",
  ctx="The Woman Who Fell from the Sky appeared from Norton in 1994; it was Harjo's first book with a "
      "major New York publisher and followed her move to teaching in Arizona and her work with the "
      "Native American poetry community. The collection's title myth is Iroquoian, and its use by a "
      "Muscogee poet is part of the pan-tribal character of the Native American Renaissance.",
  sig="The poem is a selected example of Harjo's narrative mode and represents the 1994 collection in the "
      "Norton; with the three earlier poems it gives the anthology a twenty-year span of her work, which "
      "is unusual for any poet in the period.",
  canon="Secondary canon",
  crit="Criticism reads The Woman Who Fell from the Sky as the book in which Harjo's mythic frame became "
       "explicit and her line became more narrative; the standard account of the collection treats the "
       "falling-woman story as its organising figure, and the flood poems as its earthly instances.",
  biblio="First published in The Woman Who Fell from the Sky (New York: W. W. Norton, 1994); collected "
         "in How We Became Human (2004). A selection of The Norton Anthology of American Literature, "
         "11th edition, vol. E.",
  notes="The poem's first periodical appearance was not established; the 1994 collection date is the "
        "earliest publication found.",
  ver="partially verified", sources=[W_JH, WOMAN, NAAL]),
W10("The Yellow House on the Corner", RD, "1980",
  "Poetry collection (debut volume)", "significant",
  genres=G("Lyric Poetry", "Narrative Poetry"), themes=T("Family, marriage and domestic life",
           "Childhood, adolescence and coming of age", "Race, racism and the struggle for civil rights",
           "History, truth and the uses of the past"),
  movements=M(AFAM, CONF),
  overview="The Yellow House on the Corner (Pittsburgh: Carnegie Mellon University Press, 1980) is Rita "
           "Dove's first collection, published when she was twenty-seven. The Norton prints 'Geometry' "
           "from it, dated 1980, and the record covers the volume rather than the single poem because "
           "the anthology's selections are drawn from across its sections.",
  content="The book is in three sections and moves between the domestic and the historical. Its poems "
          "include portraits of family members in Akron, poems about childhood and the body, and a "
          "sequence, 'This Life', in which Dove speaks in the voices of historical and mythological "
          "figures. 'Geometry' - the poem the Norton prints - is a short lyric about order, measurement "
          "and the shapes a life is fitted into, and it shows the formal preoccupations that run through "
          "the volume.",
  summary="Dove's first book is unusually accomplished, and its distinguishing feature is the range of "
          "voices it takes on. The Akron poems are precise about place and class - a family in the "
          "industrial Midwest, a father's work, a house with a chimney - while 'This Life' lets Dove "
          "write in the first person of people she is not, from a nineteenth-century doctor to "
          "mythological women. 'Geometry' states the collection's aesthetic in miniature: the poem is "
          "interested in the forms that contain experience, in symmetry and the breaking of it, and in "
          "the moment when a pattern becomes visible. The book's title image, a yellow house on a "
          "corner, holds the two sides together, since a house is both a particular family's dwelling "
          "and a figure for the order the poems are making. Dove has said that the collection was "
          "written in the workshop years and that she was learning to use form to control feeling; what "
          "is striking on rereading is how little of it reads as apprentice work, and how much of her "
          "later manner - the sequence, the persona, the formal turn - is already present.",
  themes_text="The first subject is family and the ordinary life of a Black family in Akron, treated "
              "without sociology. The second is the making of art out of that material, since "
              "'Geometry' is a poem about form itself. The third is history, which enters through the "
              "persona poems. The fourth is childhood and the gaining of a self-consciousness that the "
              "poems both record and resist.",
  structure="Three sections of short lyrics and one sequence of persona poems; the volume moves from "
            "domestic and autobiographical poems to historical voices and back, and 'Geometry' is a "
            "single short lyric rather than a sequence.",
  style="Metrically controlled free verse with frequent rhyme and near-rhyme; short lines and short "
        "poems; a diction that moves between the colloquial and the formal; and an image-based logic "
        "that prefers the shaped object to the statement.",
  ctx="The book was published by Carnegie Mellon University Press in 1980, when Dove was teaching at "
      "Arizona State University after her Iowa MFA; it appeared in the same year as her second "
      "collection was in preparation, which is why the two are often discussed together. The late "
      "1970s were the years in which a generation of Black poets born after the war - Dove, Komunyakaa, "
      "Yusef and others - began publishing first books that were neither Black Arts nor confessional.",
  sig="The volume is Dove's debut and the source of the earliest poem the Norton prints; 'Geometry' is "
      "among the most anthologised of her short lyrics and is often used to introduce her formal "
      "control. The record is one of the two that answer the anthology's three Adolescence rows, since "
      "those poems come from the same period of her work.",
  canon="Secondary canon",
  crit="Criticism treats the first book as the foundation of Dove's manner and notes that its persona "
       "poems anticipate Mother Love; the standard account of her development places the Akron poems "
       "and the 'This Life' sequence as the two poles between which her later work moves. 'Geometry' is "
       "usually discussed for its treatment of form as a subject.",
  biblio="First published by Carnegie Mellon University Press (Pittsburgh) in 1980. The Norton prints "
         "'Geometry' from it. A selection of The Norton Anthology of American Literature, 11th edition, "
         "vol. E.",
  notes="The collection was not read in full for this record; the description rests on its table of "
        "contents and on the published accounts of Dove's early work. The first printing of the "
        "anthology's three Adolescence poems was not verified and is not asserted here.",
  ver="partially verified", sources=[W_RD, YELLOW, NAAL]),
W10("Museum", RD, "1983",
  "Poetry collection", "significant",
  genres=G("Lyric Poetry", "Narrative Poetry"), themes=T("Art, the artist and the creative life",
           "History, truth and the uses of the past", "Race, racism and the struggle for civil rights",
           "Migration, exile and diaspora"),
  movements=M(AFAM),
  overview="Museum (Pittsburgh: Carnegie Mellon University Press, 1983) is Rita Dove's second collection, "
           "and it is the one in which she began to write about Europe, art and the position of the "
           "observer. The Norton prints 'Parsley' and 'Poem in Which I Refuse Contemplation' from it.",
  content="The collection moves between poems written out of travel in Europe - museums, paintings, "
          "cathedrals, the Mediterranean - and poems about American history and the body, and its "
          "central poem is 'Parsley', a long narrative lyric about the 1937 massacre of Haitian "
          "cane-cutters in the Dominican Republic on the orders of Rafael Trujillo. That poem's device "
          "is the dictator's inability to pronounce the Spanish word for parsley, 'perejil', which was "
          "used to identify Haitians by their accent, and Dove builds a four-part poem around the word "
          "and the killing. 'Poem in Which I Refuse Contemplation' is a short lyric about refusing the "
          "aesthetic distance that museums teach.",
  summary="Museum is Dove's argument with the museum as a way of seeing, and its two selections state "
          "both sides of the argument. 'Parsley' takes a historical atrocity and refuses to let it be "
          "contemplated from a distance: the poem moves between the general's voice, the soldiers' and "
          "the victims', and its repetitions of 'perejil' make the massacre happen in language rather "
          "than behind it. The poem's form - four numbered sections, a chorus of cane-cutters, a "
          "dictator's aria - is operatic, and its ambition is to do in lyric what a documentary cannot, "
          "which is to show how a word becomes an instrument of murder. 'Poem in Which I Refuse "
          "Contemplation' is the counterweight: a short, first-person refusal of the position of the "
          "museum visitor, of the aesthetic appreciation that turns suffering into an exhibit. Read "
          "together, the two poems define the book's subject as the ethics of looking, which is the "
          "same subject Dove would return to in the persona poems of Mother Love and in Sonata "
          "Mulattica.",
  themes_text="The first subject is the museum and the gaze, and the book's title names the institution "
              "it is arguing with. The second is the history of racial violence, above all in "
              "'Parsley'. The third is the artist's relation to European culture, which Dove "
              "approaches as a Black American visitor rather than as an heir. The fourth is the "
              "refusal of contemplation, which is an aesthetic as well as a moral position.",
  structure="A collection of short lyrics and one long four-part narrative poem, arranged so that the "
            "museum poems and the history poems alternate; 'Parsley' is the volume's structural centre.",
  style="Controlled free verse with rhyme and repetition; multiple voices inside a single poem; a "
        "plain, declarative line for the historical passages; and an imagery of paintings, mirrors and "
        "windows throughout.",
  ctx="Museum appeared in 1983, the year before Dove began teaching at Arizona State, and it was written "
      "in part during and after her Fulbright year in Germany; its European poems come from that "
      "period, and 'Parsley' was researched from accounts of the 1937 massacre, in which Trujillo's "
      "soldiers killed an estimated 20,000 Haitians along the border. The poem's attention to the "
      "shibboleth of 'perejil' comes from the historical record.",
  sig="'Parsley' is Dove's most ambitious early poem and one of the most important American poems of the "
      "1980s about state violence; it is a standard anthology piece and a Norton selection. With "
      "'Poem in Which I Refuse Contemplation' it shows the anthology representing Dove's historical "
      "range as well as her domestic lyrics.",
  canon="Major canon",
  crit="Criticism reads 'Parsley' as a landmark of the American historical lyric and discusses its "
       "operatic structure and its use of the shibboleth; the ethics of Dove's multiple voicing - "
       "whether a non-Haitian poet can speak the victims' chorus - has been debated. Museum as a whole "
       "is usually treated as the book in which Dove's interest in art and history became explicit.",
  biblio="First published by Carnegie Mellon University Press (Pittsburgh) in 1983. The Norton prints "
         "'Parsley' and 'Poem in Which I Refuse Contemplation'. A selection of The Norton Anthology of "
         "American Literature, 11th edition, vol. E.",
  notes="The collection was not read in full for this record; the description of 'Parsley' rests on its "
        "published text and the poem's standard critical accounts, and the casualty figure is given as "
        "the historical estimates give it, not as the poem states it.",
  ver="partially verified", sources=[W_RD, MUSEUM, NAAL]),
W10("Thomas and Beulah", RD, "1986",
  "Poetry sequence (book-length, in two parts)", "major",
  genres=G("Lyric Poetry", "Narrative Poetry", "Long Poem"),
  themes=T("Family, marriage and domestic life", "Class, labour and social mobility",
           "Race, racism and the struggle for civil rights", "Memory, trauma and testimony",
           "Death, illness and mourning"),
  movements=M(AFAM),
  overview="Thomas and Beulah (Pittsburgh: Carnegie Mellon University Press, 1986) won the Pulitzer Prize "
           "for Poetry in 1987. It is a book-length sequence in two halves, telling the lives of Dove's "
           "maternal grandparents - Thomas, who came north from Tennessee to work in Akron, and Beulah, "
           "who married him - and the Norton prints three of its poems: 'The Event', 'The Zeppelin "
           "Factory' and 'Dusting'.",
  content="The first half, 'Mandolin', follows Thomas from his arrival in Akron and the death of his "
          "friend Lem, through courtship, marriage, the birth of four daughters and his work at the "
          "Goodyear factory, to the lemons he grows in old age. The second half, 'Canary in Bloom', "
          "follows Beulah from her marriage through the household, her illness, her widowhood and her "
          "death. 'The Event' is one of the poems of Thomas's early life, 'The Zeppelin Factory' "
          "recalls the airship works in Akron and the men who worked in it, and 'Dusting' is a short "
          "poem of Beulah's domestic life.",
  summary="The book's achievement is to give two ordinary lives the scale of history without inflating "
          "them. Dove works in short lyrics arranged in sequence, and the sequence does the work that "
          "prose would do: the reader assembles a marriage out of moments, and the gaps between poems "
          "are as significant as the poems. Thomas's half is full of the world - the Great Migration, "
          "the war, the zeppelin works, the race riot of 1919 in Akron and the labour organising of the "
          "1930s - while Beulah's half is full of the house, and the asymmetry is the book's argument "
          "about the different freedoms of men and women in the same life. The poems are in the third "
          "person and refuse the poet's commentary; Dove does not tell the reader what her grandparents' "
          "lives mean, and the sequence's last poems, in which Beulah is dying among her daughters, are "
          "remarkable for their calm. The title's two names give the book its form: it is a double "
          "portrait, and the two halves are not equal in the amount of the world they can reach. The "
          "Pulitzer made Dove, at thirty-four, the second African American poet to win it, and the book "
          "has become the standard model for the American book-length family sequence. Its most "
          "important technical decision is that neither half narrates its own meaning: the reader is "
          "given the objects - a mandolin, a lemon tree, a zeppelin, a dust cloth - and left to "
          "assemble the lives from them, which is why the sequence rewards reading in order rather "
          "than in excerpts.",
  themes_text="The first subject is the Great Migration, since Thomas's journey north is the book's "
              "historical engine. The second is marriage and its asymmetry, which the two-part "
              "structure embodies. The third is labour, both industrial and domestic, and the way it "
              "shapes a body. The fourth is memory and inheritance, since the poet is reconstructing "
              "lives she knows only through family story.",
  structure="Two halves of about twenty-five short poems each, in chronological order within each half, "
            "with the two lives running in parallel rather than interleaved; the poems are short "
            "lyrics, many of a single stanza, and no poem comments on another.",
  style="Third-person lyrics in controlled free verse with rhyme; plain diction and domestic objects; "
        "the historical world admitted through names, machines and dates rather than through statement; "
        "and an absence of the poet's 'I'.",
  ctx="The book appeared in 1986 from Carnegie Mellon and won the Pulitzer in 1987, the year of Toni "
      "Morrison's Beloved and of a wider public argument about African American family history; Dove's "
      "grandparents had migrated from Tennessee to Akron, and the Goodyear Tire & Rubber Company, where "
      "Thomas worked and where Dove's father became the company's first Black chemist, is the book's "
      "industrial ground.",
  sig="Thomas and Beulah is one of the most honoured American poetry books of the 1980s and is the work "
      "for which Dove is best known; its model of the documentary family sequence has been widely "
      "imitated, and the Norton's three selections from it give the anthology the book's scale as well "
      "as its individual lyrics. With the three Adolescence poems and four other lyrics, Dove has ten "
      "selections in the period, more than any other poet.",
  canon="Major canon",
  crit="Criticism reads the sequence as a recovery of Black family history in the Great Migration and "
       "discusses its refusal of the poet's voice, its use of the two-part structure to mark gender "
       "difference, and its handling of the 1919 Akron riot and the zeppelin works. The Pulitzer is "
       "usually treated as the moment Dove became a public poet, and the book as the model for the "
       "documentary sequences of the 1990s.",
  biblio="First published by Carnegie Mellon University Press (Pittsburgh) in 1986; Pulitzer Prize for "
         "Poetry, 1987. The Norton prints 'The Event', 'The Zeppelin Factory' and 'Dusting'. A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The sequence was not read in full for this record; the description rests on its published "
        "structure and on the standard critical accounts, and the placement of the three printed poems "
        "in their halves is given from the sequence's contents. Internal dates such as the 1919 Akron "
        "riot are given as the historical record, not as the poems' own statements.",
  ver="partially verified", sources=[W_RD, TB, NAAL]),
W10("The Business of Fancydancing", SA, "1992",
  "Collection of poems and short stories (debut volume)", "significant",
  genres=G("Lyric Poetry", "Short Story", "Prose Poetry"),
  themes=T("Indigenous survival, land and sovereignty", "Madness, breakdown and confinement",
           "Race, racism and the struggle for civil rights", "Family, marriage and domestic life"),
  movements=M(NAR),
  overview="The Business of Fancydancing: Stories and Poems (Brooklyn: Hanging Loose Press, 1992) is "
           "Sherman Alexie's first book, published when he was twenty-five. It mixes short stories and "
           "poems without marking the boundary, and the Norton prints 'Pawn Shop' from it.",
  content="The book's seventy-odd pieces are set on and around the Spokane reservation and move between "
          "first-person lyrics, prose poems and very short stories. Its subjects are drinking, "
          "basketball, family violence, the deaths of friends and the business of being an Indian in "
          "front of white readers - the title's 'fancydancing' is both the powwow dance and the "
          "performance of identity for an audience. 'Pawn Shop' is one of its prose pieces, a "
          "single-paragraph narrative about the commerce of the reservation town.",
  summary="The book's formal oddity is its refusal to separate poetry from prose, and that refusal is "
          "its argument: on the reservation, a story and a poem are the same act, and the distinction "
          "belongs to the publisher. Alexie's early voice is direct, funny and wounded, and it uses the "
          "materials of late-twentieth-century American popular culture - basketball, television, "
          "beer, cars - as if they were a literary inheritance, which for his characters they are. "
          "'Pawn Shop' shows the method in miniature: a flat, reportorial prose that lists what is "
          "being exchanged and what it costs, and a refusal to explain the transaction's meaning. The "
          "book's politics are inseparable from its comedy, since the jokes are about the conditions "
          "the poems are also mourning, and the title's irony - that Indian identity is a business - is "
          "the collection's central insight. Its publication by Hanging Loose, a small Brooklyn press, "
          "placed Alexie outside the university and the Native American studies circuit, and its "
          "success made him the most visible Native writer of his generation while he was still in his "
          "twenties.",
  themes_text="The first subject is reservation life and its economies, both the pawn shop and the "
              "powwow. The second is alcoholism and loss, which the book treats without moralising. "
              "The third is the performance of Indianness for white expectations, which the title names. "
              "The fourth is family and the inheritance of damage, carried in the book's short, "
              "unexplained scenes.",
  structure="A collection of short lyrics, prose poems and short stories in roughly chronological "
            "arrangement by the age of the speaker, with no section headings separating the genres.",
  style="Short lines and very short paragraphs; a demotic, joke-timed voice; brand names and basketball "
        "as common reference; repetition and a deliberate flatness at moments of grief; and no "
        "figurative heightening.",
  ctx="Hanging Loose Press published the book in 1992, the year Alexie graduated from Washington State "
      "University, and it appeared in the same season as The Lone Ranger and Tonto Fistfight in Heaven "
      "(1993), which followed within a year. The early 1990s were the years of the Native American "
      "literary boom created by the successes of Momaday, Silko, Erdrich and Welch, and Alexie's debut "
      "was read as the arrival of an urban, pop-culture Indian voice.",
  sig="The book is the debut of the most widely read Native American writer of his generation and the "
      "source of one of the Norton's four Alexie selections; it establishes the mixed-genre form he "
      "would keep, and 'Pawn Shop' is a standard example of his prose poem. The Norton list carried "
      "'Pawn Shop' as undated before this wave; this record fixes it at 1992.",
  canon="Secondary canon",
  crit="Criticism reads the debut as a departure from the ceremonial mode of the Native American "
       "Renaissance, noting its demotic voice and its refusal of anthropological explanation; the "
       "standard account of Alexie's career treats the first book as the source of the tone he "
       "developed in the stories and films.",
  biblio="First published by Hanging Loose Press (Brooklyn) in 1992. The Norton prints 'Pawn Shop'. A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The collection was not read in full for this record; the description rests on its published "
        "contents and on the standard accounts of Alexie's early work. The 1992 date fixes the Norton "
        "list's undated row.",
  ver="partially verified", sources=[W_SA, BUSINESS, NAAL]),
W10("The Summer of Black Widows", SA, "1996",
  "Poetry collection", "significant",
  genres=G("Lyric Poetry", "Narrative Poetry"), themes=T("Death, illness and mourning",
           "Family, marriage and domestic life", "Indigenous survival, land and sovereignty",
           "Myth, folklore and the supernatural"),
  movements=M(NAR),
  overview="The Summer of Black Widows (Brooklyn: Hanging Loose Press, 1996) is Sherman Alexie's second "
           "collection of poems, published in the year of his novel Indian Killer. The Norton prints "
           "'Sister Fire, Brother Smoke' from its third sequence, a group of poems about the death of "
           "his sister in a house fire.",
  content="The book is in several sequences and mixes love poems, political poems, poems about "
          "basketball and a long central sequence about the death of Alexie's sister. 'Sister Fire, "
          "Brother Smoke' is a villanelle, the last poem of that sequence, in which the brother mourns "
          "the sister and confronts his own survival; the poem's repeated lines carry both the fire "
          "and the smoke that is left of the person.",
  summary="The collection shows Alexie working in received forms - the villanelle, the sestina - while "
          "keeping his demotic voice, and 'Sister Fire, Brother Smoke' is the clearest example: a "
          "villanelle's two refrains are made to do the work of grief, so that the form's repetition "
          "becomes the obsessive return of the mourner. The sequence it closes moves from the fire "
          "itself through the family's aftermath to the brother's guilt at having survived and at "
          "having made art from the death, and the last poem's formal control is the point - the "
          "discipline is what the grief is being held in. Alexie's habit of undercutting solemnity with "
          "a joke is present even here, which makes the poem harder rather than easier. The collection "
          "as a whole is more various than the debut: it includes love poems, a long poem about "
          "basketball and a sequence on the Spokane world, and its range is what the Norton's selection "
          "represents, a poet who can write a villanelle about his sister and a joke about Crazy Horse "
          "in the same book.",
  themes_text="The first subject is the death of a sibling and the guilt of the survivor, which the "
              "sequence treats without consolation. The second is the relation of art to grief, since "
              "the brother is a writer and the poem knows it. The third is family and the reservation "
              "world in which the loss happens. The fourth is form itself, since the villanelle's "
              "refrains make repetition a figure for mourning.",
  structure="A collection of sequences, with the sister poems forming the third and the villanelle "
            "placed last in it; the poems are short and the sequences are held together by recurring "
            "images rather than narrative.",
  style="Demotic free verse with formal poems set among it; a villanelle with two refrains; jokes "
        "inside elegies; and a line that is closer to speech than to song.",
  ctx="The collection appeared in 1996, the year of Indian Killer, and belongs to the period in which "
      "Alexie was publishing a book a year; Hanging Loose had published his debut and remained his "
      "publisher for poetry. His sister's death in a house fire is the biographical ground of the "
      "sequence, and the poems are unusual among his work for their directness about family loss.",
  sig="The collection contains Alexie's most formally accomplished poem and is the source of the "
      "Norton's third poem selection; 'Sister Fire, Brother Smoke' is regularly cited in discussions of "
      "the villanelle in contemporary American poetry, which is a surprising place to find a Spokane "
      "writer and exactly the point. The Norton list carried the poem as undated before this wave; "
      "this record fixes it at 1996.",
  canon="Secondary canon",
  crit="Criticism notes Alexie's use of received forms as a claim on the tradition and discusses the "
       "sister sequence as his most direct treatment of grief; the standard account of the collection "
       "reads it as the book in which he proved he was a poet as well as a storyteller.",
  biblio="First published by Hanging Loose Press (Brooklyn) in 1996. The Norton prints 'Sister Fire, "
         "Brother Smoke'. A selection of The Norton Anthology of American Literature, 11th edition, "
         "vol. E.",
  notes="The collection's date is confirmed from its publication record; the individual poems' first "
        "periodical appearances were not traced. The Norton list carried the poem as undated before "
        "this wave.",
  ver="partially verified", sources=[W_SA, TSBW, NAAL]),
W10("At Navajo Monument Valley Tribal School", SA, "1992",
  "Poem (free verse, short lines)", "significant",
  genres=G("Lyric Poetry", "Political Poetry"), themes=T("Education, institutions and the academy",
           "Indigenous survival, land and sovereignty", "Race, racism and the struggle for civil rights",
           "Language, writing and the limits of representation"),
  movements=M(NAR),
  overview="'At Navajo Monument Valley Tribal School' is a poem from The Business of Fancydancing "
           "(Brooklyn: Hanging Loose Press, 1992), Alexie's first book. It is about a photograph of "
           "students at an Indian boarding school, and it is the most directly historical poem in his "
           "debut.",
  content="The poem describes a photograph of Navajo children lined up at a tribal school, and it reads "
          "the image for what it does not show: the children's names, the languages they were forbidden, "
          "the families they were taken from. It moves between the photograph's flat surface and the "
          "history the surface holds down, and its short lines keep the poem close to the picture rather "
          "than letting it escape into statement.",
  summary="The poem's method is ekphrasis as indictment: the photograph is treated as a document and as "
          "a lie at the same time, since the order and cleanliness of the line-up are exactly what the "
          "school was for. Alexie's short lines let him place a fact beside an image without arguing, "
          "and the poem's power comes from the reader's knowledge of what the boarding schools did - the "
          "cutting of hair, the prohibition of Native languages, the separation of children from "
          "parents, the motto 'kill the Indian, save the man'. The poem does not supply that history, "
          "and its refusal to explain is a refusal to make the children into a lesson. It is also one "
          "of the earliest poems in which Alexie writes about photography, a subject he returns to "
          "throughout his work, and its treatment of the camera as an instrument of both record and "
          "violence is characteristic of the Native American writing of the period, which had begun to "
          "read the photographic archive against itself.",
  themes_text="The first subject is the Indian boarding school and the assimilation policy it served. "
              "The second is the photograph as a document that records and conceals at once. The third "
              "is the survival of the children in the picture, which the poem insists on without "
              "sentiment. The fourth is language, since the schools' central act was to forbid it.",
  structure="A short free-verse poem in brief lines, organised as a reading of a single photograph with "
            "no stanza division and no narrative development.",
  style="Short unpunctuated lines; present tense; a flat descriptive tone that refuses outrage; and an "
        "absence of simile, so that the photograph stays a photograph.",
  ctx="The Business of Fancydancing appeared in 1992, and the poem belongs to the period of public "
      "reckoning with the boarding-school system that would produce the 2000s scholarship on it; "
      "Navajo Monument Valley Tribal School is a school on the Navajo Nation, and the poem's title "
      "names a specific institution rather than a generic one.",
  sig="The poem is the historical centre of Alexie's debut and the one most often taught in courses on "
      "boarding-school literature; it is a Norton selection, and the list carried it as undated before "
      "this wave.",
  canon="Secondary canon",
  crit="Criticism reads the poem with the photographic archive of the boarding schools and treats its "
       "refusal to narrate as its ethical choice; the standard account of Alexie's early work places "
       "it among the poems that carry the book's historical weight.",
  biblio="First published in The Business of Fancydancing (Brooklyn: Hanging Loose Press, 1992). A "
         "selection of The Norton Anthology of American Literature, 11th edition, vol. E.",
  notes="The collection's date is confirmed from its publication record; the poem's first periodical "
        "appearance was not traced. The Norton list carried the poem as undated before this wave.",
  ver="partially verified", sources=[W_SA, BUSINESS, NAAL]),
]
