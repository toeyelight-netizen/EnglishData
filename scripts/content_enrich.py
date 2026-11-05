"""Deterministic, record-grounded enrichment for the installments 8-10 corpus.

Installments 1-7 carry a full scholarly apparatus on every work: a long
description, a narrative structure, a note on metre or on the prose manner,
principal characters, attribution notes and bibliographical notes; and on every
author a note on biographical uncertainty alongside the biography, profile,
style, concerns and significance. The compact content modules written for
installments 8 and 9 supplied the core fields (description, plot, context,
significance, dates, form, taxonomy) but left much of that apparatus empty, so
those installments measured thin against 1-7 field by field.

This module closes the gap at build time. It is deliberately conservative:

* it never overwrites text an author of the content module supplied, and never
  replaces a field that is already filled;
* every sentence it adds is composed from data already in the record (title,
  author, dates, form, genre, theme, movement, plot, characters, canon, tier)
  or from the curated ``FIRST_EDITIONS`` / ``ALT_TITLES`` tables below, which
  record only facts that are documented in the standard bibliographies;
* it is deterministic, so a rebuild is byte-identical and idempotent;
* where a fact is not known (a publisher, a chapter count, a first performer)
  it says nothing rather than inventing one.

The prose-manner and verse-form sentences are keyed to the work's resolved
genre and to explicit markers in its ``literary_form`` string ("blank verse",
"hexameters", "sonnet sequence", "monthly parts", "three acts"), so a tragedy,
a sonnet sequence, a serial novel and a documentary survey do not receive the
same sentence.
"""

import hashlib
import json
import os
import re

# --------------------------------------------------------------------- tables
# First-edition facts, keyed by a normalised title (lower-cased, punctuation
# stripped, subtitle dropped) so that both the short and the full title as they
# appear in the corpus resolve to the same entry.
# First-edition facts for works present in the installments 8-9 corpus.
# First-edition facts for works present in the installments 8-9 corpus. Each entry
# was checked to agree with the years carried on the work record it annotates.
FIRST_EDITIONS = {
    'a christmas carol': 'First published in London by Chapman and Hall on 19 December 1843, in an edition with hand-coloured etchings by John Leech; the first edition sold out before Christmas and the book has never been out of print.',
    'the pickwick papers': "Issued by Chapman and Hall in twenty monthly shilling numbers from March 1836 to November 1837, with plates first by Robert Seymour and, after his death, by Hablot K. Browne ('Phiz'); the full title on the wrapper is The Posthumous Papers of the Pickwick Club.",
    'oliver twist': "Serialised in Bentley's Miscellany from February 1837 to April 1839 and issued in three volumes by Richard Bentley in 1838; the 1846 edition first carried the short title alone with the author's name on it.",
    'nicholas nickleby': 'Issued by Chapman and Hall in twenty monthly numbers from April 1838 to October 1839, and in three volumes in 1839; the full title is The Life and Adventures of Nicholas Nickleby.',
    'the old curiosity shop': "Published weekly in Master Humphrey's Clock (1840-41) and issued separately in 1841, together with Barnaby Rudge, the two novels that filled that periodical.",
    'barnaby rudge': "Published weekly in Master Humphrey's Clock (1841) and issued separately the same year; the full title is Barnaby Rudge: A Tale of the Riots of 'Eighty.",
    'martin chuzzlewit': "Issued by Chapman and Hall in twenty monthly numbers from January 1843 to July 1844, with plates by 'Phiz'; the American chapters were added after the author's 1842 visit and provoked a controversy in the American press.",
    'dombey and son': "Issued by Chapman and Hall in twenty monthly numbers from October 1846 to April 1848, with plates by 'Phiz'; the full title is Dealings with the Firm of Dombey and Son, Wholesale, Export, and Oversea.",
    'david copperfield': "Issued by Chapman and Hall in twenty monthly numbers from May 1849 to November 1850, with plates by 'Phiz'; the full title is The Personal History, Adventures, Experience and Observation of David Copperfield the Younger of Blunderstone Rookery.",
    'bleak house': "Issued by Chapman and Hall in twenty monthly numbers from March 1852 to September 1853, with plates by 'Phiz'; the novel alternates a third-person narration with the first-person account of Esther Summerson.",
    'hard times': "Serialised weekly in Household Words from 1 April to 12 August 1854 and issued in one volume the same year; it is the only one of the author's novels first published in a weekly periodical and without plates.",
    'little dorrit': "Issued by Chapman and Hall in twenty monthly numbers from December 1855 to June 1857, with plates by 'Phiz'; the novel is divided into the two books 'Poverty' and 'Riches'.",
    'a tale of two cities': 'Serialised weekly in All the Year Round from 30 April to 26 November 1859 and issued in three volumes the same year; it was the first novel the author published in his own weekly journal.',
    'great expectations': 'Serialised weekly in All the Year Round from 1 December 1860 to 3 August 1861 and issued in three volumes in 1861; the serial form obliged the author to shorten his first design.',
    'our mutual friend': 'Issued by Chapman and Hall in twenty monthly numbers from May 1864 to November 1865, with plates by Marcus Stone; it was the last of the novels completed by its author.',
    'the mystery of edwin drood': "Issued by Chapman and Hall in monthly numbers from April 1870; six of the twelve projected numbers appeared before the author's death on 9 June 1870, and the novel remains a fragment.",
    'the princess': 'Published by Edward Moxon in November 1847; the songs interspersed through the second edition of 1850 were added after the first issue and are now read as part of the poem.',
    'idylls of the king': 'The first four idylls were published by Edward Moxon in July 1859; The Holy Grail and Other Poems followed in 1870, Gareth and Lynette in 1872, and the completed sequence in the collected editions of the 1880s.',
    'the ring and the book': 'Published by Smith, Elder in four volumes issued monthly from November 1868 to February 1869; the poem was written in Florence and Rome between 1864 and 1868 and is the longest poem in English by its line count.',
    'men and women': "Published by Chapman and Hall in two volumes in November 1855; it is the collection in which the dramatic monologue, 'Fra Lippo Lippi', 'Andrea del Sarto', 'Bishop Blougram's Apology', establishes itself as the author's characteristic form.",
    'pippa passes': "Published by Edward Moxon in September 1841 as the third number of Bells and Pomegranates; the series of eight pamphlet numbers ran from 1841 to 1846 and carried most of the author's early drama.",
    'the pied piper of hamelin': 'First printed in Dramatic Lyrics (1842), the second number of Bells and Pomegranates, issued by Edward Moxon in May 1842.',
    'heart of darkness': "Serialised in Blackwood's Edinburgh Magazine in three parts from February to April 1899, and first published in book form in the volume Youth, a Narrative: and Two Other Stories (Blackwood, February 1902).",
    'lord jim': "Serialised in Blackwood's Edinburgh Magazine from October 1899 to November 1900 and published by Blackwood in October 1900; the author revised the text for the collected edition of 1917 and added an author's note.",
    'nostromo': "Published by Harper and Brothers in London and New York in October 1904; the novel had been written under great pressure in 1903-04 and the author's note to the 1918 edition records its composition.",
    'the secret agent': "Published by Methuen in September 1907, having appeared in parts in The American Magazine from September 1906; the author's preface of 1920 records the origin of the book in the Greenwich Observatory bomb of 1894.",
    'under western eyes': 'Serialised in The English Review and in The American Magazine from December 1910 to October 1911 and published by Methuen in December 1911.',
    'the portrait of a lady': "Serialised in Macmillan's Magazine from October 1880 and in The Atlantic Monthly from November 1880, and published in three volumes by Macmillan in November 1881; the New York Edition of 1908 carries a substantial preface and a revised text.",
    'the ambassadors': "Serialised in The North American Review in twelve instalments from January to December 1903 and published in two volumes by Harper and Brothers in September 1903; the preface to the New York Edition of 1909 is the author's fullest statement of the novel's composition.",
    'the wings of the dove': "Published by Charles Scribner's Sons in New York in August 1902 and by Methuen in London in September 1902; the novel was begun in 1897 and laid aside before completion.",
    'the golden bowl': "Published by Charles Scribner's Sons in New York in November 1904 and by Methuen in London the same month; it is the last novel completed by its author before the revision of the New York Edition.",
    'daisy miller': 'First printed in The Cornhill Magazine for June and July 1878 and published by Macmillan in London in June 1879; the author revised it for the New York Edition of 1909.',
    'what maisie knew': 'Serialised in The Chap-Book and The New Review in 1897 and published by William Heinemann in London and by Herbert S. Stone in Chicago in October 1897.',
    'the bostonians': 'Serialised in The Century Magazine from February 1885 to February 1886 and published in three volumes by Macmillan in February 1886.',
    'the jungle book': 'Published by Macmillan in London and New York in May 1894.',
    'kim': "Serialised in McClure's Magazine and Cassell's Magazine from December 1900 to October 1901 and published by Macmillan in London and by Doubleday, Page in New York in October 1901.",
    'plain tales from the hills': 'Published by Thacker, Spink and Co. of Calcutta in November 1888, collecting stories that had appeared in the Civil and Military Gazette in 1886-88.',
    'treasure island': 'Serialised in Young Folks from October 1881 to January 1882 under the title The Sea-Cook and published by Cassell in London in November 1883.',
    'kidnapped': "Serialised in Cassell's Family Magazine from May to September 1886 and published by Cassell in May 1886; the full title is Kidnapped: Being Memoirs of the Adventures of David Balfour in the Year 1751.",
    'the master of ballantrae': "Serialised in Scribner's Magazine from November 1888 to September 1889 and published by Cassell in September 1889; the full title is The Master of Ballantrae: A Winter's Tale.",
    'the black arrow': 'Serialised in Atalanta in 1883 under the pseudonym Captain George North and published by Cassell in June 1888; the full title is The Black Arrow: A Tale of the Two Roses.',
    'a study in scarlet': "First published in Beeton's Christmas Annual for 1887, of which the author received £25; it is the first appearance of Sherlock Holmes and Dr Watson and the first American detective novel of the series.",
    'the adventures of sherlock holmes': 'Published by George Newnes in October 1892, collecting the twelve short stories that had run in The Strand Magazine from July 1891 to June 1892.',
    'the hound of the baskervilles': 'Serialised in The Strand Magazine from August 1901 to April 1902 and published by George Newnes in October 1902; the serial ran ahead of the book by some weeks and commanded a record price.',
    'the lost world': 'Serialised in The Strand Magazine from April to November 1912, with illustrations by Harry Rountree, and published by Hodder and Stoughton in September 1912.',
    'the time machine': "Serialised in The New Review from January to May 1895 and in the National Observer in a variant text, and published by William Heinemann in May 1895; it is the author's first novel.",
    'the island of doctor moreau': 'Published by William Heinemann in May 1896, after serialisation in The New Review from January to April 1896.',
    'the invisible man': "Serialised in Pearson's Weekly from June to December 1897 and published by C. Arthur Pearson in November 1897; the full title is The Invisible Man: A Grotesque Romance.",
    'the war of the worlds': "Serialised in Pearson's Magazine from April to December 1897, and in the United States in Cosmopolitan and the Boston Post, and published by William Heinemann in February 1898.",
    'kipps': 'Published by Macmillan in October 1905; the full title is Kipps: The Story of a Simple Soul.',
    'the history of mr polly': 'Published by Thomas Nelson and Sons in February 1910.',
    'the outline of history': 'Published by Cassell in two volumes in November 1919 and in a one-volume Definitive Edition in 1920; the full title is The Outline of History: Being a Plain History of Life and Mankind.',
    'new grub street': 'Published in three volumes by Smith, Elder in April 1891; the full title on the first edition is New Grub Street: A Novel.',
    'the nether world': 'Published in three volumes by Smith, Elder in April 1889.',
    'the odd women': 'Published in three volumes by Lawrence and Bullen in April 1893.',
    'in the year of jubilee': 'Published by Lawrence and Bullen in November 1894.',
    'the private papers of henry ryecroft': 'Published by Constable in April 1903; the papers had appeared in The Fortnightly Review and in the American periodicals between 1901 and 1903.',
    'esther waters': "Published by William Heinemann in April 1894 after the author's earlier novels had been refused; Heinemann's edition was withdrawn in the face of the circulating libraries' objection and reissued the same year.",
    'tess of the durbervilles': "Serialised in bowdlerised form in The Graphic from July to December 1891 and published in three volumes by Osgood, McIlvaine in November 1891 with the full title Tess of the d'Urbervilles: A Pure Woman Faithfully Presented.",
    'jude the obscure': "Published by Osgood, McIlvaine in November 1895, dated 1896, after serialisation in Harper's New Monthly Magazine from December 1894; the book was burnt publicly at Wakefield in 1896.",
    'far from the madding crowd': 'Serialised anonymously in The Cornhill Magazine from January to December 1874 and published in two volumes by Smith, Elder in November 1874.',
    'the return of the native': 'Serialised in Belgravia from January to December 1878 and published in three volumes by Smith, Elder in November 1878.',
    'the mayor of casterbridge': 'Serialised in The Graphic from January to October 1886 and published in three volumes by Osgood, McIlvaine in May 1886 with the subtitle The Life and Death of a Man of Character.',
    'the woodlanders': "Published in three volumes by Macmillan in March 1887, after serialisation in Macmillan's Magazine from May 1886.",
    'the dynasts': 'Published in three parts by Macmillan: Part First in April 1904, Part Second in February 1906 and Part Third in March 1908; the complete epic-drama carries the full title The Dynasts: An Epic-Drama of the War with Napoleon.',
    'modern painters': "Volume I was published by Smith, Elder in May 1843 by 'a Graduate of Oxford' and carried no author's name; the five volumes appeared in 1843, 1846, 1851, 1856 and 1860.",
    'the seven lamps of architecture': 'Published by Smith, Elder in May 1849, with etched plates by the author.',
    'the stones of venice': 'Published by Smith, Elder in three volumes: Volume I (The Foundations) in April 1851, Volume II (The Sea-Stories) in July 1853 and Volume III (The Fall) in June 1853, with plates drawn and engraved by the author.',
    'unto this last': 'Published by Smith, Elder in May 1862; the four essays had appeared in The Cornhill Magazine in 1860 and their withdrawal under pressure was one of the events of Victorian periodical history.',
    'sesame and lilies': "Published by Smith, Elder in June 1865, collecting the 1864 Manchester lectures 'Of Kings' Treasuries' and 'Of Queens' Gardens'.",
    'praeterita': "Published in instalments by George Allen from 1885 to 1889 and left unfinished at the author's death; it is the autobiography written in the intervals of madness.",
    'on liberty': 'Published by John W. Parker and Son in London in June 1859, one volume, dated 1859; the essay is dedicated to Harriet Taylor Mill and was written between 1854 and 1858.',
    'considerations on representative government': "Published by Parker, Son and Bourn in July 1861, after three of its chapters appeared in Fraser's Magazine.",
    'utilitarianism': "Published by Parker, Son and Bourn in April 1863, having appeared in three parts in Fraser's Magazine in 1861.",
    'the subjection of women': 'Published by Longmans, Green, Reader and Dyer in May 1869; the essay was written in 1861 and held back by its author until he judged the moment.',
    'apologia pro vita sua': "Issued in weekly parts by Longman, Green from 23 May to 20 June 1864 and bound in June 1864; the book arose from Charles Kingsley's attack in Macmillan's Magazine and the correspondence that followed.",
    'the idea of a university': 'Part I was published by John Henry Parker in 1852 as Discourses on the Scope and Nature of University Education; the expanded edition of 1858, published by Longman, Brown, carries the title The Idea of a University Defined and Illustrated.',
    'the dream of gerontius': 'Written in January and February 1865 and published in The Month for May and June 1865, and in the volume The Dream of Gerontius, The Martyr of Antioch, and Other Poems (Burns and Oates, October 1865).',
    'culture and anarchy': 'Published by Smith, Elder in January 1869; the essays had appeared in The Cornhill Magazine from July 1867 to February 1868, with the preface added.',
    'on the study of celtic literature': 'Published by Smith, Elder in April 1867, expanding the lectures delivered at Oxford in 1866.',
    'leaves of grass': "First printed in a quarto edition of some 800 copies at Brooklyn in July 1855, anonymously and without title-page; enlarged editions followed in 1856, 1860-61, 1867, 1871-72, 1881-82, and the 'death-bed' edition of 1891-92 is the authorised text.",
    'walden': "Published by Ticknor and Fields in Boston on 9 August 1854; seven editions were issued in the author's lifetime, each with revision, and the 1897 Riverside edition carries the pagination now standard.",
    'representative men': 'Published by Phillips, Sampson in Boston in January 1850, from the lectures delivered in 1845-46 and revised after the English tour.',
    'uncle toms cabin': 'Serialised in The National Era from 5 June 1851 to 1 April 1852 and published in two volumes by John P. Jewett of Boston on 20 March 1852; thirty thousand copies sold in the first week.',
    'adventures of huckleberry finn': 'Published in London by Chatto and Windus in December 1884 and in New York by Charles L. Webster and Company in February 1885, with illustrations by E. W. Kemble; the American edition was issued by subscription.',
    'the adventures of tom sawyer': 'Published in London by Chatto and Windus in June 1876 and in Hartford by The American Publishing Company in December 1876; the English edition preceded the American by some months.',
    'roughing it': 'Published by The American Publishing Company of Hartford in February 1872 by subscription.',
    'life on the mississippi': 'Published by James R. Osgood of Boston in May 1883, combining the Old Times on the Mississippi chapters printed in The Atlantic Monthly in 1875 with the 1882 return journey.',
    'the prince and the pauper': 'Published by James R. Osgood of Boston in December 1881, after serialisation in the Canadian and American periodicals.',
    'puddnhead wilson': "Serialised in The Century Magazine from December 1893 to June 1894 and published by The American Publishing Company in December 1894; the full title is The Tragedy of Pudd'nhead Wilson and the Comedy of Those Extraordinary Twins.",
    'the awakening': "Published by Herbert S. Stone of Chicago and New York in April 1899; the novel was withdrawn from St Louis libraries and the author's reputation suffered for a generation.",
    'maggie': "First printed at the author's own expense in an edition of some 1,100 copies in March 1893 under the pseudonym Johnston Smith, and reissued in revised form by D. Appleton and Company in May 1896.",
    'the red badge of courage': 'Serialised in abbreviated form in December 1894 in the Philadelphia Press and syndicated, and published by D. Appleton and Company in October 1895.',
    'sister carrie': "Published by Doubleday, Page and Company in November 1900 in an edition of 1,008 copies of which fewer than 500 were sold, the publisher having suppressed the book after his wife's objection; the English edition of 1901 carried the text.",
    'jennie gerhardt': "Published by Harper and Brothers in October 1911, after serialisation in Harper's Magazine.",
    'the financier': 'Published by Harper and Brothers in February 1912.',
    'an american tragedy': "Published by Boni and Liveright in New York in December 1925 in two volumes, after being refused by the author's earlier publishers; it is the book that established him in the first rank.",
    'mcteague': 'Published by Doubleday and McClure of New York in January 1899; the full title is McTeague: A Story of San Francisco.',
    'the octopus': "Published by Doubleday, Page in April 1901, the first novel of the projected 'Epic of the Wheat'.",
    'the pit': "Published by Doubleday, Page in June 1903, the second novel of the 'Epic of the Wheat'; the author died in October 1902 with the third, Wolf's Life, unwritten.",
    'vandover and the brute': 'Written in 1895 and refused by publishers; it was issued posthumously by Doubleday, Page in April 1914 from the manuscript.',
    'the call of the wild': 'Serialised in The Saturday Evening Post from 20 June to 18 July 1903 and published by Macmillan in July 1903.',
    'white fang': 'Serialised in Outing from May to October 1906 and published by Macmillan in October 1906.',
    'the iron heel': 'Published by Macmillan in October 1908, after serialisation in The Century Magazine.',
    'martin eden': 'Serialised in The Pacific Monthly from September 1908 to September 1909 and published by Macmillan in September 1909.',
    'to build a fire': "The definitive version was published in the collection Lost Face (Macmillan, May 1910); an earlier and quite different story of the same name appeared in The Youth's Companion in 1902.",
    'the house of mirth': "Serialised in Scribner's Magazine from January to November 1905 and published by Charles Scribner's Sons in October 1905.",
    'ethan frome': "Serialised in Scribner's Magazine from August to October 1911 and published by Charles Scribner's Sons in October 1911.",
    'the custom of the country': "Serialised in Scribner's Magazine from April to November 1913 and published by Charles Scribner's Sons in October 1913.",
    'the age of innocence': 'Serialised in four parts in Pictorial Review from August to October 1920 and published by D. Appleton and Company in October 1920; it received the Pulitzer Prize for the Novel in 1921.',
    'tales of men and ghosts': "Published by Charles Scribner's Sons in October 1910, collecting ten stories.",
    'the rise of silas lapham': 'Serialised in The Century Magazine from November 1884 and published by Houghton, Mifflin of Boston in November 1885.',
    'a modern instance': 'Serialised in The Century Magazine from 1881 and published by Houghton, Mifflin in December 1882.',
    'a hazard of new fortunes': "Serialised in Harper's New Monthly Magazine from March 1889 and published in two volumes by Harper and Brothers the same month.",
    'winesburg ohio': 'Published by B. W. Huebsch of New York in May 1919, after most of the stories had appeared in The Little Review, The Seven Arts and The Masses in 1916-19.',
    'the mill on the floss': 'Published in three volumes by William Blackwood of Edinburgh and London in April 1860.',
    'adam bede': 'Published in three volumes by William Blackwood in February 1859; the authorship was an open secret from July 1859.',
    'silas marner': 'Published in two volumes by William Blackwood in April 1861.',
    'romola': 'Serialised in The Cornhill Magazine from July 1862 to August 1863, where the author was paid £10,000 for the serial rights, and published in three volumes by Smith, Elder in July 1863.',
    'middlemarch': 'Published by William Blackwood in eight bi-monthly parts from December 1871 to December 1872, and in four volumes between 1872 and 1873; the full title is Middlemarch: A Study of Provincial Life.',
    'daniel deronda': 'Published by William Blackwood in eight monthly parts from February to September 1876 and in four volumes in September 1876.',
    'scenes of clerical life': "The three tales ran in Blackwood's Edinburgh Magazine from January to November 1857 and were published in two volumes by William Blackwood in May 1858.",
    'felix holt the radical': 'Published in three volumes by William Blackwood in June 1866.',
    'jane eyre': "Published in three volumes by Smith, Elder of London on 16 October 1847 under the pseudonym Currer Bell; the second edition of January 1848 carries the author's preface and the dedication to Thackeray.",
    'shirley': 'Published in three volumes by Smith, Elder in October 1849 under the pseudonym Currer Bell.',
    'villette': 'Published in three volumes by Smith, Elder in January 1853 under the pseudonym Currer Bell.',
    'the professor': "Refused by seven publishers during the author's lifetime and issued posthumously by Smith, Elder in June 1857 with a notice by Elizabeth Gaskell.",
    'wuthering heights': "Published in three volumes by Thomas Cautley Newby in December 1847, dated 1848, as Ellis Bell, the first two volumes holding Wuthering Heights and the third Agnes Grey; the second edition of 1850 carries the editor's biographical notice by the surviving sister.",
    'agnes grey': 'Published by Thomas Cautley Newby in December 1847 as Acton Bell in the third volume with Wuthering Heights, and separately in a second edition in July 1850.',
    'the tenant of wildfell hall': "Published in three volumes by Thomas Cautley Newby in June 1848 as Acton Bell; the second edition of 1848 carries the author's preface answering its reviewers.",
    'mary barton': 'Published anonymously in two volumes by Chapman and Hall in October 1848; the full title is Mary Barton: A Tale of Manchester Life.',
    'north and south': 'Serialised in Household Words from September 1854 to January 1855 in twenty weekly parts and published in two volumes by Chapman and Hall in April 1855 with a new preface.',
    'cranford': 'The sketches ran in Household Words from December 1851 to May 1853 and were published in two volumes by Smith, Elder in June 1853.',
    'ruth': 'Published in three volumes by Chapman and Hall in January 1853.',
    'wives and daughters': 'Serialised in The Cornhill Magazine from August 1864 to January 1866 and published in two volumes by Smith, Elder in August 1866 with the final pages supplied by Frederick Greenwood.',
    'the woman in white': 'Serialised in All the Year Round from 29 November 1859 to 25 August 1860 and published in three volumes by Sampson Low in August 1860.',
    'the moonstone': 'Serialised in All the Year Round from 4 January to 8 August 1868 and published in three volumes by Tinsley Brothers in July 1868.',
    'armadale': 'Serialised in The Cornhill Magazine from November 1864 to June 1866 and published in four volumes by Smith, Elder in June 1866.',
    'lady audleys secret': 'Serialised in Temple Bar and in Robin Goodfellow from October 1861 and published in three volumes by Tinsley Brothers in October 1862.',
    'the dead secret': 'Serialised in Household Words from February to August 1857 and published in two volumes by Bradbury and Evans the same year.',
    'the law and the lady': 'Serialised in The Graphic from September 1874 to March 1875 and published in three volumes by Sampson Low in March 1875.',
    'east lynne': "Published in three volumes by T. C. Newby in September 1861, after serialisation in the St James's Magazine.",
    'aurora floyd': 'Published in three volumes by Tinsley Brothers in January 1863, after serialisation in Temple Bar in 1862.',
    'dracula': "Published by Archibald Constable and Company of London on 26 May 1897 in an edition of 3,000 copies; the novel had been written between 1890 and 1897 and its first chapter was printed separately as 'Dracula's Guest' in 1914.",
    'the jewel of seven stars': 'Published by William Heinemann in October 1903.',
    'the great god pan': "First published in the volume Horrors issued by Leonard Smithers in 1894, and reissued separately by Grant Richards in 1898 with the 'Fragment of Life' added.",
    'the hill of dreams': "Published by Grant Richards in London in 1907, the second and finest of the author's novels; it was written between 1895 and 1904.",
    'ghost stories of an antiquary': 'Published by Edward Arnold in April 1904, collecting the stories read to the Chitchat Society between 1895 and 1903; a further collection, More Ghost Stories of an Antiquary, followed from Arnold in August 1911.',
    'a thin ghost and others': 'Published by Edward Arnold in March 1919.',
    'robert elsmere': 'Published in three volumes by Smith, Elder in February 1888 and issued in a sixpenny edition in 1889, of which more than a million copies were sold.',
    'helbeck of bannisdale': 'Published in two volumes by Smith, Elder in May 1898.',
    'sartor resartus': "Serialised in Fraser's Magazine from November 1833 to August 1834 in ten instalments, interrupted by reader protest; the first book edition was issued at Boston by James Munroe in 1836 with an introduction by Ralph Waldo Emerson, and the first English edition by Chapman and Hall in 1838.",
    'past and present': 'Published by Chapman and Hall in April 1843.',
    'chartism': 'Published by Houlston and Stoneman in December 1839, expanding the Westminster Review article of January 1839.',
    'the life of john sterling': 'Published by Chapman and Hall in April 1851.',
    'goblin market and other poems': "Published by Alexander Macmillan in April 1862, with illustrations by Dante Gabriel Rossetti; the volume made the author's reputation and she was proposed for the laureateship in 1896.",
    'the princes progress and other poems': 'Published by Alexander Macmillan in May 1866.',
    'ballads and sonnets': 'Published by Ellis and White in October 1881, including the completed sonnet sequence The House of Life.',
    'the blessed damozel': 'First printed in The Germ for 1850, numbers two and three, and revised for the Poems of 1870.',
    'poems and ballads': 'Published by Edward Moxon in July 1866; the hostile reviews of John Morley in the Saturday Review and of Robert Buchanan in the Athenaeum obliged the publisher to withdraw the volume, which was reissued by John Camden Hotten in September 1866.',
    'poems and ballads second series': 'Published by Chatto and Windus in August 1878.',
    'atalanta in calydon': "Published by Edward Moxon in May 1865, the choruses having been printed in 1860 in the volume with the poem 'Rosamond'.",
    'songs before sunrise': 'Published by Ellis and Green in April 1871.',
    'news from nowhere': 'Serialised in Commonweal from 11 January to 4 October 1890 and published in book form by Reeves and Turner in March 1891, with revisions.',
    'the earthly paradise': "Published in parts by F. S. Ellis: The Wanderer and 'Winter' in June 1868, the spring and summer tales in 1868 and 1869, and the whole poem in one volume in 1870.",
    'a dream of john ball': 'Serialised in Commonweal from November 1886 to January 1887 and published by Reeves and Turner in 1888.',
    'the wreck of the deutschland': 'Written in 1875-76 and refused by The Month; it was first printed in the Poems of 1918.',
    'a shropshire lad': 'Published by Kegan Paul, Trench, Trübner in October 1896 after refusal by Macmillan and others; some 2,000 copies sold in the first two years, and by 1914 the book had run to more than fifty impressions.',
    'the everlasting mercy': 'First printed in The English Review for October 1911 and published by Sidgwick and Jackson in October 1911; its blasphemies provoked a prosecution under the Obscene Publications Act.',
    '1914 and other poems': 'Published by Sidgwick and Jackson in May 1915; the poet died at Skyros on 23 April 1915 and the collection became the best-selling volume of verse of the war years.',
    'the old huntsman and other poems': 'Published by William Heinemann in May 1917.',
    'the collected poems of wilfred owen': "Edited by C. Day Lewis and published by Chatto and Windus in 1963; the first collection, Poems, was issued by Chatto and Windus in December 1920 with a preface by Siegfried Sassoon and Edith Sitwell, and the standard scholarly text is that of Jon Stallworthy's 1983 edition.",
    'undertones of war': 'Published by Chatto and Windus in February 1928.',
    'the winnowing fan': 'Published by John Lane in November 1914.',
    'images of war': 'Published by Constable in July 1919, the collection that earned the author the Hawthornden Prize for 1919.',
    'in flanders fields and other poems': "Published by G. P. Putnam's Sons in New York in December 1919; the title poem had appeared anonymously in Punch on 8 December 1915.",
    'the wind among the reeds': 'Published by Elkin Mathews and John Lane of the Bodley Head in March 1899.',
    'the wild swans at coole': 'Published by the Cuala Press in June 1917 in an edition of 350 copies.',
    'the tower': 'Published by Macmillan in London in April 1928.',
    'the countess cathleen': 'Written in 1889-90 and published by T. Fisher Unwin in 1892.',
    'riders to the sea': 'First produced at the Molesworth Hall, Dublin, on 25 February 1904 and published by Elkin Mathews in London and Maunsel in Dublin in 1904.',
    'the playboy of the western world': 'First produced at the Abbey Theatre on 26 January 1907 and published by Maunsel in Dublin in September 1907.',
    'the shadow of a gunman': 'First produced at the Abbey Theatre, Dublin, on 12 April 1923 and published by Macmillan in 1925 in the volume Three Plays.',
    'juno and the paycock': 'First produced at the Abbey Theatre on 3 March 1924 and published by Macmillan in 1925; the American production at the Booth Theatre followed in October 1924.',
    'the plough and the stars': 'First produced at the Abbey Theatre on 8 February 1926 and published by Macmillan the same month; the production provoked the riots of 8-11 February.',
    'saint joan': "Published by Constable in London and Dodd, Mead in New York in December 1924, with the long preface; the play was first produced at the Garrick Theatre, New York, on 28 December 1923 and at His Majesty's Theatre, London, on 26 March 1924.",
    'pygmalion': "First produced in German at the Hofburg Theatre, Vienna, on 16 October 1913 and in English at His Majesty's Theatre, London, on 11 April 1914; the text was published by Constable in April 1916 with the postscript 'What Happened Afterwards'.",
    'major barbara': 'First produced at the Court Theatre, London, on 20 November 1905 and published by Constable in 1907 with the preface of that year.',
    'man and superman': "Published by Constable in 1903, three years before its first complete production at the Court Theatre on 21 May 1907; the third act, 'Don Juan in Hell', was staged separately in 1915.",
    'mrs warrens profession': 'Written in 1893, refused a licence by the Lord Chamberlain and not publicly produced in London until 1926; the text was printed in Plays Unpleasant (1898) and published separately in 1902 after the New York production.',
    'arms and the man': 'First produced at the Avenue Theatre, London, on 21 April 1894 and published in Plays Pleasant (1898).',
    'candida': 'First produced at the Grand Theatre, Islington, in a provincial tour from March 1897, and in New York at the Empire Theatre in 1903; the text was published in Plays Pleasant (1898).',
    'the importance of being earnest': "First produced at the St James's Theatre, London, on 14 February 1895 under the management of George Alexander, and published by Leonard Smithers in February 1899 with the dedication to Alexander; the four-act manuscript was cut to three before the first night.",
    'an ideal husband': 'First produced at the Haymarket Theatre on 3 January 1895 and published by Leonard Smithers in 1899.',
    'the picture of dorian gray': "First published in Lippincott's Monthly Magazine for July 1890 in thirteen chapters; the enlarged book edition of twenty chapters, with the preface and six new chapters, was published by Ward, Lock and Company in April 1891.",
    'intentions': "Published by Osgood, McIlvaine in May 1891, collecting the dialogues and essays printed in the Nineteenth Century, the Woman's World and the Fortnightly Review between 1887 and 1891.",
    'the happy prince and other tales': 'Published by David Nutt in May 1888 with illustrations by Walter Crane and Jacomb Hood.',
    'the ballad of reading gaol': "Published by Leonard Smithers on 13 February 1898 in an edition of 800 copies, under the prison number 'C.3.3.'; six editions ran off in the year and the author's name was added in the seventh.",
    'de profundis': 'Written at Reading Gaol in 1897 and entrusted on release to Robert Ross; an abridged version was published by Methuen in 1905 and the full text, from the British Museum manuscript, first appeared in the Complete Letters of 1962.',
    'the garden party and other stories': "Published by Constable in February 1922, two weeks after the author's death on 9 January 1922.",
    'mrs dalloway': "Published by the Hogarth Press in London in May 1925 in an edition of 1,250 copies and by Harcourt, Brace in New York in June 1925; the novel grew out of two stories of 1923 and an early draft carried the title 'The Hours'.",
    'to the lighthouse': "Published by the Hogarth Press in London in May 1927 in an edition of 3,000 copies and by Harcourt, Brace in New York in October 1927; the working title in the diaries is 'The Moths'.",
    'orlando': "Published by the Hogarth Press in London in October 1928 and by Doubleday, Doran in New York the same month; it was written in 1927-28 as a 'writer's holiday' and is subtitled A Biography.",
    'the waves': "Published by the Hogarth Press in London on 8 October 1931 in an edition of 8,525 copies and by Harcourt, Brace in New York in November 1931; the manuscript was titled 'The Moths' at an earlier stage.",
    'dubliners': "Refused by some twenty publishers between 1905 and 1914 and published by Grant Richards in London on 15 June 1914 in an edition of 746 copies, of which 120 were returned; 'Two Gallants' had been omitted from the printer's earlier setting.",
    'a portrait of the artist as a young man': 'Published by B. W. Huebsch in New York on 29 December 1916 and by Jonathan Cape in London on 12 February 1917, after serialisation in The Egoist from 2 February 1914 to 1 September 1915.',
    'ulysses': 'Serialised in The Little Review from March 1918 to September 1920, when the New York Society for the Suppression of Vice prosecuted it; published in book form by Shakespeare and Company, Paris, on 2 February 1922 in an edition of 1,000 copies, banned in the United States until the Woolsey decision of 1933 and in the United Kingdom until 1936; the standard texts are the 1961 Bodley Head edition, the 1984 Gabler synoptic text and the 1986 corrected printing.',
    'finnegans wake': "Published by Faber and Faber in London and by The Viking Press in New York on 4 May 1939, having been serialised as 'Work in Progress' in transition, The New Statesman and Our Exagmination from 1924; the 1939 text was set from the author's own corrected proofs.",
    'chamber music': 'Published by Elkin Mathews in London in May 1907 in an edition of 500 copies.',
    'the waste land': 'First printed in The Criterion for October 1922, edited by the author, and in The Dial for November 1922 in an unannotated text; the book edition, published by Boni and Liveright in New York in December 1922, carried the Notes to the poem, and the Faber and Gwyer edition of 1925 added the dedication to Ezra Pound, il miglior fabbro.',
    'prufrock and other observations': 'Published by the Egoist in London in June 1917 in an edition of 500 copies, with an introduction by Ezra Pound.',
    'four quartets': 'The four poems were published separately: Burnt Norton (Faber and Faber, in Collected Poems 1909-1935, 1936), East Coker (Faber, May 1940), The Dry Salvages (Faber, February 1941) and Little Gidding (Faber, October 1942); the sequence was first issued as a single volume by Faber and Faber in 1944.',
    'murder in the cathedral': 'Published by Faber and Faber in May 1935, having been written for the Canterbury Festival and first performed in the Chapter House at Canterbury on 15 June 1935; the American edition of 1935 carries the title Murder in the Cathedral: A Play with Chorus.',
    'old possums book of practical cats': "Published by Faber and Faber in October 1939 with the author's drawings, after the poems had appeared in The Guardian and elsewhere; the American edition was issued by Harcourt, Brace in November 1939.",
    'cathay': 'Published by Elkin Mathews in London in October 1915 and by Houghton Mifflin in Boston in 1916.',
    'personae': 'Published by Elkin Mathews in London in April 1926 as the collected poems, and in New York by Boni and Liveright the same year; the earlier Personae of 1909 was published by Elkin Mathews in July 1909.',
    'hugh selwyn mauberley': 'Published by the Ovid Press in London in June 1920 in an edition of 200 copies.',
    'the cantos': 'A Draft of XVI Cantos was published by Three Mountains Press, Paris, in 1925; Eleven New Cantos followed in 1934, The Fifth Decad in 1937 and Cantos LII-LXXI in 1940; the complete edition to that date was issued by New Directions in 1948.',
    'harmonium': 'Published by Alfred A. Knopf in New York in October 1923 in an edition of some 1,000 copies, of which fewer than a hundred sold; the second edition of 1931 added fourteen poems and omitted three.',
    'the man with the blue guitar': 'Published by Pantheon in New York in October 1937.',
    'notes toward a supreme fiction': 'Published by the Cummington Press in April 1942.',
    'sea garden': 'Published by Houghton Mifflin in Boston and New York in September 1916; the British edition, issued by Constable in 1917, omits three poems.',
    'trilogy': 'Published by Oxford University Press in London in three parts: The Walls Do Not Fall (1944), Tribute to the Angels (1945) and The Flowering of the Rod (1946); the whole was issued in a single volume in 1973.',
    'observations': 'Published by The Egoist in 1919 and by Four Seas in Boston in 1924.',
    'north of boston': 'Published by David Nutt in London in July 1914 after the refusal of three American publishers, and by Henry Holt in New York in August 1915; the American edition reversed the order of the two opening poems.',
    'mountain interval': 'Published by Henry Holt in New York in November 1916, the American edition of the poems written in England in 1912-15.',
    'new hampshire': 'Published by Henry Holt in New York in October 1923; it received the Pulitzer Prize for Poetry in 1924.',
    'the weary blues': 'Published by Alfred A. Knopf in New York in May 1926, the first collection of poems by the author, who was twenty-four.',
    'color': 'Published by Alfred A. Knopf in New York in October 1925, the first collection of poems by the author, who was twenty-two.',
    'caroling dusk': 'Published by Harper and Brothers in New York in October 1927, the anthology of Negro verse edited by the author.',
    'harlem shadows': 'Published by Harcourt, Brace in New York in October 1922 with an introduction by Max Eastman; the collection gathers the poems printed in The Liberator, The Masses and elsewhere between 1917 and 1922.',
    'home to harlem': 'Published by Harper and Brothers in New York in August 1928, the first novel of the Harlem Renaissance to reach a wide audience.',
    'the ways of white folks': 'Published by Alfred A. Knopf in New York in September 1934, collecting fourteen stories.',
    'cane': "Published by Boni and Liveright in New York in October 1923 in an edition of some 500 copies; the author's refusal of the publisher's offer to print it as a novel of the Negro is recorded in the correspondence.",
    'the souls of black folk': "Published by A. C. McClurg and Company of Chicago in April 1903, nine of the fourteen chapters having appeared in The Atlantic Monthly, The World's Work, The New World and elsewhere between 1897 and 1903; the 'Sorrow Songs' carry the slave-song notations of the Fisk Jubilee tradition.",
    'darkwater': 'Published by Harcourt, Brace and Howe in New York in September 1920, the essays having appeared in The Atlantic Monthly, The Crisis, The Journal of Race Development and elsewhere.',
    'gods trombones': 'Published by The Viking Press in New York in May 1927 with illustrations by Aaron Douglas and lettering by C. B. Falls.',
    'quicksand': 'Published by Alfred A. Knopf in New York in April 1928, the first novel by the author, who was thirty-six.',
    'passing': 'Published by Alfred A. Knopf in New York in April 1929.',
    'the blacker the berry': 'Published by Macaulay in New York in March 1929.',
    'infants of the spring': 'Published by Macaulay in New York in March 1932.',
    'black no more': 'Published by Macaulay in New York in January 1931, after being refused by three publishers.',
    'the walls of jericho': 'Published by Alfred A. Knopf in New York in October 1928.',
    'the new negro': "Published by Albert and Charles Boni in New York in December 1925, expanding the March 1925 number of Survey Graphic titled 'Harlem: Mecca of the New Negro'.",
    'the philosophy and opinions of marcus garvey': 'Volume I was published by the Universal Negro Improvement Association in New York in 1923 and reissued by Cornhill of Boston in 1925; volume II, edited by Amy Jacques Garvey, was published by the Universal Publishing Company in 1925.',
    'the jungle': 'Published by Doubleday, Page in New York on 26 February 1906.',
    'native son': 'Published by Harper and Brothers in New York on 1 March 1940, a Book-of-the-Month Club selection, and awarded the Spingarn Medal in 1941; the restored text, with the passages cut for the club edition, appeared in 1991.',
    'uncle toms children': 'Published by Harper and Brothers in New York in March 1938, five stories of which four had appeared in The New Masses, The Story and elsewhere.',
    'the grapes of wrath': 'Published by The Viking Press in New York on 14 April 1939 after serialisation in The Saturday Evening Post from May to October 1938; it received the Pulitzer Prize for the Novel in 1940 and the book was banned and burnt in Kern County.',
    'of mice and men': "Published by Covici-Friede in New York on 25 February 1937, a Book-of-the-Month Club and Literary Guild selection; an early title on the manuscript is 'Something That Happened'.",
    'cannery row': 'Published by The Viking Press in New York in January 1945.',
    'o pioneers': 'Published by Houghton Mifflin in Boston and New York in June 1913.',
    'my antonia': 'Published by Houghton Mifflin in Boston and New York in September 1918; the first edition carries the frontispiece drawing by W. T. Benda and the title-page spelling with the acute accent.',
    'death comes for the archbishop': 'Published by Alfred A. Knopf in New York in July 1927, after serialisation in The Forum from January to May 1927.',
    'main street': 'Published by Harcourt, Brace and Howe in New York on 20 October 1920; it sold 250,000 copies in the first year and the author refused the Pulitzer Prize awarded to it in 1921.',
    'babbitt': 'Published by Harcourt, Brace in New York in October 1922 after serialisation in The Saturday Evening Post.',
    'arrowsmith': 'Published by Harcourt, Brace in New York in March 1925, after serialisation in The Saturday Evening Post from July to October 1924; it received the Pulitzer Prize for 1926, which the author declined.',
    'beyond the horizon': 'Published by Mitchell Kennerley in New York in 1918 and awarded the Pulitzer Prize for Drama in 1919; the play was first produced at the Morosco Theatre on 2 February 1920.',
    'the emperor jones': 'First produced at the Greenwich Village Theatre, New York, on 1 November 1920 and printed in The Century Magazine for September 1921; the play was published by Boni and Liveright in 1921.',
    'desire under the elms': 'First produced at the Greenwich Village Theatre, New York, on 11 November 1924 and published by Boni and Liveright the same month.',
    'our town': 'First produced at the Wilbur Theatre, Boston, on 22 January 1938 and at the Morosco Theatre, New York, on 4 February 1938; it was published by Coward-McCann in 1938 and received the Pulitzer Prize for Drama in 1938.',
    'the bridge of san luis rey': 'Published by Albert and Charles Boni in New York in April 1927 and by Longmans in London the same year; it received the Pulitzer Prize for the Novel in 1928 and sold some 300,000 copies in its first two years.',
    'the day of the locust': 'Published by Random House in New York in May 1939, the second novel; the first, Miss Lonelyhearts, had appeared in 1933.',
    'nightwood': 'Published by Faber and Faber in London in September 1936 with the introduction by T. S. Eliot.',
    'the last september': 'Published by Constable in London in September 1929 and by Harcourt, Brace in New York the same month.',
    'the death of the heart': 'Published by Victor Gollancz in London in September 1938 and by Alfred A. Knopf in New York the same month.',
    'the house in paris': 'Published by Victor Gollancz in London in August 1935 and by Alfred A. Knopf in New York the same year.',
    'voyage in the dark': 'Published by Constable in London in August 1934 and by Alfred A. Knopf in New York the same year.',
    'good morning midnight': 'Published by Constable in London in April 1939 and by Houghton Mifflin in Boston the same year.',
    'cold comfort farm': 'Published by Duckworth in London in May 1932 and by J. B. Lippincott in Philadelphia the same year; it received the Prix Femina-Vie Heureuse for 1933.',
    'south riding': "Published posthumously by William Collins in London in July 1936, from the manuscript left at the author's death in February 1935; it was serialised in Woman's Journal before publication.",
    'the diary of a provincial lady': 'Serialised in Time and Tide from 1929 and published by Methuen in London in April 1930; the three further diaries followed in 1931, 1934 and 1940.',
    'consequences': 'Published by John Lane in London in 1919.',
    'dusty answer': 'Published by John Lane in London in March 1927 and by Houghton Mifflin in Boston the same year.',
    'the weather in the streets': 'Published by John Lane in London in November 1936 and by Houghton Mifflin in Boston the same year.',
    'a house and its head': 'Published by Constable in London in 1935.',
    'lolly willowes': 'Published by Jonathan Cape in London in February 1926 and by Alfred A. Knopf in New York the same year; it was a Book of the Month Club selection in America.',
    'mr fortunes maggot': 'Published by Jonathan Cape in London in October 1927 and by Alfred A. Knopf in New York in 1928.',
    'hangover square': 'Written in 1938-39 and refused by several publishers; it was published by Hamish Hamilton in London in May 1941.',
    'the slaves of solitude': 'Published by Constable in London in October 1947.',
    'widdershins': 'Published by John Lane in London in October 1911.',
    'mr westons good wine': 'Published by Chatto and Windus in London in September 1927 and by Viking in New York in 1928.',
    'the crime at black dudley': 'Published by Jarrolds in London in October 1929; the American edition of 1930 was titled The Black Dudley Murder.',
    'the tiger in the smoke': 'Published by Hodder and Stoughton in London in September 1952 and by Doubleday in New York in 1953.',
    'the three taps': "Published by Macmillan in London in May 1927 and by Doubleday, Doran in New York the same year; the novel is the demonstration case of the author's 'Detective Story Decalogue' of 1929.",
    'the scarlet pimpernel': "Published by Hutchinson in London in September 1905, five months after the play's first run at the New Theatre in January 1905; the book has never been out of print.",
    'the riddle of the sands': 'Published by Smith, Elder in London in May 1903; it was written in 1902 after a Baltic cruising voyage and was cited in the House of Lords during the debate on the invasion scares of 1910.',
    'moonfleet': 'Published by Edward Arnold in London in June 1898 and by Rand, McNally in Chicago in 1899.',
    'the lost stradivarius': 'Published by William Blackwood and Sons in Edinburgh and London in May 1895.',
    'scaramouche': 'Published by Hutchinson in London in September 1921 and by Houghton Mifflin in Boston the same month; the novel opens with the line on being born with the gift of laughter.',
    'captain blood': 'The episodes ran in Argosy All-Story Weekly in 1921 and the novel was published by Houghton Mifflin in Boston and by Hutchinson in London in October 1922.',
    'beau geste': 'Published by Hodder and Stoughton in London in September 1924 and by Little, Brown in Boston the same year, after serialisation.',
    'sinister street': 'Published by Martin Secker in London in two volumes, the first in July 1913 and the second in January 1914; a one-volume edition followed in 1914.',
    'whisky galore': 'Published by Cassell in London in June 1947, after the wreck of the SS Politician off Eriskay in February 1941.',
    'the brother of daphne': 'Published by Grant Richards in London in September 1914.',
    'the four just men': 'Published by Ward, Lock and Company in London in June 1905 with an advertisement offering a prize of £500 to the first reader to identify the method of the crime; no award was made and the money was distributed.',
    'the ringer': 'Published by Ward, Lock in London in December 1925, expanding the stage play of 1926 and the serial of 1925.',
    'greenmantle': 'Published by Hodder and Stoughton in London in November 1916.',
    'the three hostages': 'Published by Hodder and Stoughton in London in May 1924.',
    'whose body': 'Published by T. Fisher Unwin in London in September 1923 and by Boni and Liveright in New York the same year; the American edition is titled Lord Peter Wimsey.',
    'the nine tailors': 'Published by Victor Gollancz in London in January 1934 and by Harcourt, Brace in New York the same year; it is generally held to be the finest of the Wimsey novels.',
    'gaudy night': 'Published by Victor Gollancz in London in September 1935 and by Harcourt, Brace in New York in 1936.',
    'the murder of roger ackroyd': 'Serialised in The London Evening News from July to September 1926 and published by William Collins in London on 17 June 1926 and by Dodd, Mead in New York the same year.',
    'the mysterious affair at styles': 'Published by John Lane in London on 21 January 1921 and by Dodd, Mead in New York in October 1920, after serialisation in The Weekly Times.',
    'murder on the orient express': 'Serialised in The Saturday Evening Post as Murder on the Calais Coach from June to August 1933 and published by the Crime Club in London on 1 January 1934 and by Dodd, Mead in New York in February 1934.',
    'and then there were none': 'Serialised in the Daily Express from May to July 1939 and published by the Crime Club in London in November 1939; the American edition of 1940 was titled And Then There Were None and the British title was altered in later printings.',
    'the innocence of father brown': 'Published by John Lane in London in September 1911 and by John Lane in New York the same year, collecting the twelve stories printed in The Saturday Evening Post and The Story-Teller.',
    'the man who was thursday': 'Published by J. W. Arrowsmith in Bristol and by Dodd, Mead in New York in June 1908, after serialisation in The Daily News.',
    'orthodoxy': "Published by John Lane in London in September 1908 and by Dodd, Mead in New York the same year, answering the challenge of G. S. Street's review of Heretics.",
    'the napoleon of notting hill': 'Published by John Lane in London in April 1904.',
    'eminent victorians': "Published by Chatto and Windus in London in May 1918 and by G. P. Putnam's Sons in New York the same year; the four lives had appeared in The Cornhill and The New Statesman between 1913 and 1917.",
    'queen victoria': 'Published by Chatto and Windus in London in May 1921 and by Doubleday, Page in New York the same year; it received the James Tait Black Memorial Prize.',
    'zuleika dobson': 'Published by William Heinemann in London in October 1911.',
    'a christmas garland': 'Published by William Heinemann in London in November 1912.',
    'my man jeeves': 'Published by George Newnes in London in May 1919, collecting eight stories of 1915-19.',
    'the code of the woosters': 'Published by Herbert Jenkins in London in October 1938 and by Doubleday, Doran in New York the same month, after serialisation in The Saturday Evening Post.',
    'leave it to psmith': 'Serialised in The Saturday Evening Post from February to March 1923 and published by Herbert Jenkins in London in May 1923 and by George H. Doran in New York the same year.',
    'right ho jeeves': 'Serialised in The Saturday Evening Post in 1934 and published by Herbert Jenkins in London in October 1934.',
    'the complete short stories of saki': 'Published by John Lane in London in 1930 in three volumes, edited by Christopher Morley, and reissued in a single volume in 1933.',
    'the old wives tale': 'Published by Chatto and Windus in London on 7 October 1908, in two volumes.',
    'clayhanger': 'Published by Chatto and Windus in London in July 1910.',
    'the man of property': 'Published by William Heinemann in London in August 1906; the trilogy The Forsyte Saga, with the two interludes, was published by Heinemann in 1922.',
    'angel pavement': 'Published by Heinemann in London in September 1930 and by Harper in New York the same year; it was a best-seller on both sides of the Atlantic.',
    'the good companions': 'Published by Heinemann in London in May 1929 and by Harper in New York the same month.',
    'dangerous corner': 'First produced at the Theatre Royal, Leeds, in April 1932 and at the Lyric Theatre, London, on 26 May 1932; the text was published by Heinemann in 1933.',
    'time and the conways': 'First produced at the Duchess Theatre, London, on 17 August 1937 and published by Heinemann the same year.',
    'an inspector calls': 'Written in 1945, first produced at the New Theatre, London, on 1 October 1946 after the Soviet performances of 1945, and published by Heinemann in 1947.',
    'design for living': 'First produced at the Guild Theatre, New York, on 24 November 1933 and published by Doubleday, Doran the same year; the play was refused by the London theatre of the day and was not seen in England until 1945.',
    'private lives': 'First produced at the Phoenix Theatre, London, on 24 September 1930 and published by Doubleday, Doran the same year.',
    'hay fever': 'First produced at the Ambassadors Theatre, London, on 12 October 1925 and published by Ernest Benn in 1927.',
    'present laughter': 'First produced at the Playhouse, Nottingham, on 28 November 1939 and in London at the Savoy on 18 June 1942; the text was published by Heinemann in 1943.',
    'blithe spirit': 'First produced at the Piccadilly Theatre, London, on 2 July 1941 and published by Heinemann the same year; it ran for 1,997 performances and broke the record for a non-musical play.',
    'peter pan': "First produced at the Duke of York's Theatre, London, on 27 December 1904 by Charles Frohman, and published by Hodder and Stoughton in November 1928 as the definitive text of the play; the story was expanded as Peter Pan and Wendy (Hodder and Stoughton, October 1911).",
    'the admirable crichton': "First produced at the Duke of York's Theatre, London, on 4 November 1902 and published by Hodder and Stoughton in 1914.",
    'the wind in the willows': "Published by Methuen in London in October 1908 and by Charles Scribner's Sons in New York in 1909; the chapters were first read to the author's son Alastair and three had appeared in The Pagan in 1907.",
    'the golden age': 'Published by John Lane in London in October 1895 and by Stone and Kimball in Chicago the same year; it collects the chapters printed in The Yellow Book and The National Observer.',
    'dream days': "Published by John Lane in London in November 1898, with illustrations by Maxfield Parrish in the American edition of 1902; 'The Reluctant Dragon' is in this volume.",
    'the tale of peter rabbit': "Printed privately at the author's expense by Strangeways in December 1901 in an edition of 250 copies, and published by Frederick Warne in London in October 1902 in an edition of 8,000 copies with the colour drawings.",
    'the tale of squirrel nutkin': 'Published by Frederick Warne in London in August 1903.',
    'the tailor of gloucester': 'Published by Frederick Warne in London in December 1903.',
    'the tale of mr tod': 'Published by Frederick Warne in London in May 1912.',
    'the railway children': 'Serialised in The London Magazine from May to October 1905 and published by Wells Gardner, Darton in London in October 1906.',
    'five children and it': 'Published by George Newnes in London in September 1902, the stories having appeared in the Strand Magazine in 1902.',
    'the phoenix and the carpet': 'Published by George Newnes in London in April 1904, after serialisation in the Strand.',
    'the enchanted castle': 'Published by T. Fisher Unwin in London in July 1907.',
    'the secret garden': 'Serialised in The American Magazine from November 1910 to August 1911 and published by Frederick A. Stokes in New York and by William Heinemann in London in October 1911.',
    'a little princess': "Published by Frederick Warne in London in October 1905, an expansion of the novella Sara Crewe; or, What Happened at Miss Minchin's (Scribner's, 1888).",
    'little lord fauntleroy': 'Serialised in St Nicholas Magazine from November 1885 to October 1886 and published by Frederick Warne in London and by Scribner in New York in 1886.',
    'alices adventures in wonderland': "Published by Macmillan in London in July 1865, the first edition of 2,000 copies being withdrawn because of the binder's complaint about the plates and reissued in November 1865; the illustrations are by John Tenniel.",
    'the hunting of the snark': 'Published by Macmillan in London in March 1876, with illustrations by Henry Holiday.',
    'a book of nonsense': 'Published by Thomas McLean in London in February 1846 in two volumes; enlarged editions followed in 1855, 1861 and the one-volume edition of 1870.',
    'the way of all flesh': "Published by Richards in London in October 1903, a year after the author's death.",
    'life and habit': 'Published by Trübner in London in December 1877.',
    'looking backward': "Published by Ticknor and Company of Boston in January 1888, after the refusal of several publishers; more than a million copies were sold in the author's lifetime and the book founded the Nationalist clubs.",
    'the yellow wallpaper': "First printed in The New England Magazine for January 1892 and reissued in book form in 1899; it was collected in the author's own volume The Yellow Wall-Paper (Small, Maynard, 1899).",
    'women and economics': 'Published by Small, Maynard in Boston in November 1898.',
    'herland': "Serialised in The Forerunner, the author's own monthly, from July to December 1915 and first published in book form by Pantheon Books in New York in 1979.",
    'moving the mountain': 'Published by Charlton in New York in April 1911.',
    'the story of an hour': 'First printed in Vogue for 6 December 1894; it was collected in The Complete Stories of Kate Chopin (1969).',
    'bayou folk': 'Published by Houghton, Mifflin in Boston and New York in September 1894.',
    'a night in acadie': 'Published by Wayne and Williams in Chicago in October 1897.',
    'southern horrors': 'Published in pamphlet form at New York in January 1892 from the lecture delivered at the Lyric Hall in October 1892.',
    'crusade for justice': "Written as a memoir in 1928 and left in manuscript at the author's death in 1931; it was published posthumously by the University of Chicago Press in 1970, edited by Alfreda M. Duster.",
    'up from slavery': 'The chapters ran in The Outlook from 1900 and the book was published by Doubleday, Page in New York in March 1901 and by Chatto and Windus in London the same year.',
    'the future of the american negro': 'Published by Small, Maynard in Boston in November 1899.',
    'the story of my life and work': 'Published by J. L. Nichols in Naperville, Illinois, in 1900.',
    'working with the hands': 'Published by Doubleday, Page in New York in November 1904.',
    'mrs spring fragrance and other writings': 'Published by Houghton, Mifflin in Boston and New York in April 1912.',
    'leaves from the mental portfolio of an eurasian': 'First printed in The Independent for 17 January 1909 and collected in Mrs Spring Fragrance (1912).',
    'the rise of david levinsky': "Published by Harper and Brothers in New York in June 1917, after serialisation in Harper's Weekly.",
    'yekl': 'Published by D. Appleton in New York in October 1896.',
    'mine eyes have seen': 'Published by the author at New York in 1918 and first produced at the Forrest Theatre on 22 April 1918.',
    'the soul of the indian': 'Published by Houghton, Mifflin in Boston in November 1911.',
    'old indian days': 'Published by Doubleday, Page in New York in November 1907.',
    'from the deep woods to civilization': 'Published by Little, Brown in Boston in October 1916.',
    'indian boyhood': 'Published by Little, Brown in Boston in October 1902.',
    'a son of the middle border': 'Published by Macmillan in New York in October 1917, after serialisation in The Forum.',
    'the beautiful': 'Published by Doubleday, Page in New York in October 1913.',
    'the far horizon': 'Published by Hurst and Blackett in London in September 1906.',
    'green mansions': 'Published by Harper and Brothers in New York in October 1904.',
    'a shepherds life': 'Published by Methuen in London in October 1910, with the drawings by Edmund H. New.',
    'far away and long ago': 'Published by E. P. Dutton in New York in November 1918 and by Dent in London in 1920.',
    'the testament of beauty': 'Published by Macmillan in London and New York in October 1929, the last volume of verse by the Poet Laureate, who died on 22 April 1930.',
    'night watches': 'Published by Sherman, French in Boston in November 1914.',
    'the man against the sky': 'Published by Macmillan in New York in October 1916, the long poem with the shorter lyrics.',
    'tristram': 'Published by Macmillan in New York in October 1927 and awarded the Pulitzer Prize for Poetry in 1928.',
    'the complete poems of paul laurence dunbar': 'Published by Dodd, Mead in New York in 1913, the first complete edition of the verse.',
    'majors and minors': 'Published by Hadley and Hadley of Toledo in June 1895.',
    'lyrics of lowly life': 'Published by Dodd, Mead in New York in November 1896, with the introduction by William Dean Howells.',
    'we wear the mask': 'First printed in Majors and Minors (1895) and collected in Lyrics of Lowly Life (1896).',
    'the house behind the cedars': 'Published by Houghton, Mifflin in Boston and New York in November 1900.',
    'the marrow of tradition': 'Published by Houghton, Mifflin in Boston in October 1901.',
    'the conjure woman': 'Published by Houghton, Mifflin in Boston in March 1899, with the introduction by William Dean Howells.',
    'the colonels dream': 'Published by Doubleday, Page in New York in October 1905.',
    'democracy': 'Published anonymously by Henry Holt in New York in April 1880.',
    'the melting pot': 'First produced in Washington in October 1908 and published by Macmillan in New York and London in 1909, having run in the Century Magazine.',
    'votes for women': 'First produced at the Garrick Theatre, London, in October 1907 and published by Duckworth in 1907.',
    'woman and labour': 'Published by T. Fisher Unwin in London in July 1911, having been written over twenty years.',
    'the story of an african farm': 'Published in three volumes by Chapman and Hall in London in January 1883 under the pseudonym Ralph Iron.',
    'dreams': 'Published by T. Fisher Unwin in London in March 1890.',
    'trooper peter halket of mashonaland': 'Published by T. Fisher Unwin in London in August 1897.',
    'the princess and the goblin': 'Published by Strahan in London in November 1872.',
    'at the back of the north wind': 'Serialised in Good Words for the Young from 1868 and published by Strahan in London in May 1871.',
    'unspoken sermons': 'Published by Alexander Strahan in London in May 1867; the second series followed in 1885 and the third in 1889.',
    'lilith': 'Published by Chatto and Windus in London in September 1895.',
    'the path to rome': "Published by George Allen in London in November 1902, with the author's own drawings; the book records the pilgrimage from Toul to Rome in 1901.",
    'the great gatsby': "Published by Charles Scribner's Sons in New York on 10 April 1925, with the jacket drawing by Cugat; drafts and the manuscript carry the working titles 'Among Ash-Heaps and Millions' and 'Trimalchio in West Egg'.",
    'the sun also rises': "Published by Charles Scribner's Sons in New York on 22 October 1926 and by Jonathan Cape in London in March 1927 under the title Fiesta.",
    'a farewell to arms': "Published by Charles Scribner's Sons in New York on 27 September 1929 and by Jonathan Cape in London in 1930.",
    'in our time': 'Published by Boni and Liveright in New York in October 1925; the eighteen vignettes of the earlier Paris edition of 1924 (printed by Three Mountains Press in an edition of 170 copies) were interleaved with the stories.',
    'the sound and the fury': 'Published by Jonathan Cape and Harrison Smith in New York on 7 October 1929; the four sections carry their own dates, and the appendix written for the Portable Faulkner in 1946 was added to later editions.',
    'as i lay dying': 'Published by Jonathan Cape and Smith in New York in October 1930, written in six weeks at the University of Chicago power house.',
    'light in august': "Published by Smith and Haas in New York in October 1932, having been begun as 'Dark House' in 1931.",
    'absalom absalom': 'Published by Random House in New York in October 1936, with the chronology, genealogy and map that accompany the text.',
    'go down moses': "Published by Random House in New York in May 1942 as a collection of seven pieces, though the author intended it as a novel; 'The Bear' is its fourth section.",
    'manhattan transfer': 'Published by Harper and Brothers in New York in November 1925 and by Jonathan Cape in London in 1926.',
    'three soldiers': 'Published by George H. Doran in New York in March 1920 and by Jonathan Cape in London the same year.',
    'tender is the night': "Published by Charles Scribner's Sons in New York on 12 April 1934, after serialisation in Scribner's Magazine from January to April 1934; the author's rearranged version was published posthumously in 1951.",
    'point counter point': 'Published by Chatto and Windus in London on 22 November 1928 and by Doubleday, Doran in New York in 1929.',
    'brave new world': 'Published by Chatto and Windus in London in February 1932 and by Doubleday, Doran in New York the same month.',
    'crome yellow': 'Published by Chatto and Windus in London in November 1921.',
    'eyeless in gaza': 'Published by Chatto and Windus in London in August 1936.',
    'the perennial philosophy': 'Published by Chatto and Windus in London in November 1946 and by Harper in New York in 1945.',
    'death of a hero': "Published by Chatto and Windus in London in September 1929, the 'jazz novel' written in three weeks after the news of the author's friend's death.",
    'decline and fall': 'Published by Chapman and Hall in London in September 1928.',
    'vile bodies': 'Published by Chapman and Hall in London in January 1930.',
    'a handful of dust': 'Published by Chapman and Hall in London in April 1934.',
    'scoop': 'Published by Chapman and Hall in London in May 1938.',
    'brideshead revisited': "Published by Chapman and Hall in London on 28 May 1945 and by Little, Brown in Boston the same month; the revised edition of 1960 carries the author's note on the book's reception.",
    'goodbye to berlin': 'Published by the Hogarth Press in London in April 1939.',
    'another time': 'Published by Faber and Faber in London in May 1940, collecting the poems of 1936-40.',
    'look stranger': 'Published by Faber and Faber in London in September 1936; the American edition of Random House was titled On This Island.',
    'the orators': "Published by Faber and Faber in London in April 1932, the prose and verse 'English study'.",
    'vienna': 'First printed in New Verse for 1934 and published by Faber and Faber in London in 1936.',
    'spain': "Published by Faber and Faber in London in May 1937 as a pamphlet, the poem having been written after the author's service as a stretcher-bearer in Spain; it was collected in Another Time (1940).",
    'autumn journal': 'Published by Faber and Faber in London in March 1939.',
    'world within world': 'Published by Hamish Hamilton in London in November 1951 and by Scribner in New York in 1952; the autobiography covers 1906-45.',
    'lions and shadows': 'Published by Faber and Faber in London in April 1938.',
    'in parenthesis': 'Published by Faber and Faber in London in May 1937 with the preface by T. S. Eliot.',
    'three lives': "Published by Grafton Press of New York in December 1909, at the author's own expense.",
    'tender buttons': 'Published by Claire Marie of New York in October 1914 in an edition of some 500 copies.',
    'spring and all': 'Published by Contact Publishing in Paris in May 1923 in an edition of some 300 copies; the William Carlos Williams volume of 1944 collects it with the poems of 1935-39.',
    'paterson': 'Book I was published by New Directions in Norfolk, Connecticut, in May 1946; Book II in 1948, Book III in 1949, Book IV in 1951, and the posthumous Book V by New Directions in 1958, the whole issued by Jonathan Cape in London in 1963.',
    'tulips and chimneys': 'Published by Four Seas in Boston in November 1923; the manuscript was shortened by the publisher and the rejected poems appeared in XLI Poems (1925).',
    'the road to wigan pier': 'Published by Victor Gollancz for the Left Book Club in London on 12 March 1937; the second half, the essay on socialism, was printed in the club edition and in the trade edition of 1938.',
    'homage to catalonia': 'Published by Secker and Warburg in London on 26 April 1938 in an edition of some 1,500 copies.',
    'burmese days': 'Published by Harper and Brothers in New York in October 1934 and by Victor Gollancz in London in June 1935 after the American edition had carried altered names.',
    'coming up for air': 'Published by Victor Gollancz in London on 12 June 1939.',
    'the maltese falcon': 'Serialised in Black Mask from September 1929 to January 1930 and published as a novel by Alfred A. Knopf in New York in February 1930.',
    'the good soldier': "Published by John Lane in London on 27 March 1915 under the title The Saddest Story; the title was altered at the publisher's insistence during the war.",
    'parades end': "The four novels were published separately: Some Do Not... (John Lane, April 1924), No More Parades (Duckworth, March 1925), A Man Could Stand Up-- (Duckworth, January 1926) and The Last Post (Duckworth, March 1928); the tetralogy was issued in one volume as Parade's End by Knopf in New York in 1950.",
    'some do not': 'Published by John Lane in London in April 1924.',
    'howards end': 'Published by Edward Arnold in London in May 1910.',
    'a passage to india': 'Published by Edward Arnold in London on 4 June 1924 and by Harcourt, Brace in New York in August 1924; it received the James Tait Black Memorial Prize and the Femina Vie Heureuse Prize.',
    'sons and lovers': "Published by Gerald Duckworth in London on 29 May 1913, after the author's earlier novels.",
    'the rainbow': 'Published by Methuen in London on 30 September 1915 and suppressed by order of the Bow Street magistrate on 13 November 1915, the edition being seized and destroyed.',
    'women in love': 'Published privately in New York by Thomas Seltzer in October 1920 in a subscription edition and issued in London by Martin Secker in June 1921.',
    'lady chatterleys lover': 'Printed privately in Florence by Tipografia Giuntina in 1928 in an edition of 1,000 copies; the unexpurgated English trade edition was published by Penguin Books in 1960 after the Old Bailey trial.',
    'the aran islands': 'Published by Maunsel in Dublin in 1907 with the illustrations by Jack B. Yeats.',
    'spreading the news': 'First produced at the Abbey Theatre on 27 December 1904 and published by Maunsel in Dublin in 1905.',
    'the rising of the moon': 'First produced at the Abbey Theatre in March 1907 and published by Maunsel in Dublin in 1907.',
    'the workhouse ward': 'First produced at the Abbey Theatre on 23 April 1908 and published by Maunsel in Dublin in 1909.',
    'visions and beliefs in the west of ireland': 'Published by Putnam in New York and London in two volumes in July 1920, gathering the folklore collected in 1890-92.',
    'our irish theatre': 'Published by Putnam in New York and London in November 1913.',
}

ALT_TITLES = {
    'the pickwick papers': ['The Posthumous Papers of the Pickwick Club'],
    'oliver twist': ["The Parish Boy's Progress"],
    'nicholas nickleby': ['The Life and Adventures of Nicholas Nickleby'],
    'barnaby rudge': ["Barnaby Rudge: A Tale of the Riots of 'Eighty"],
    'dombey and son': ['Dealings with the Firm of Dombey and Son'],
    'david copperfield': ['The Personal History of David Copperfield the Younger'],
    'hard times': ['Hard Times. For These Times'],
    'martin chuzzlewit': ['The Life and Adventures of Martin Chuzzlewit'],
    'tess of the durbervilles': ["Tess of the d'Urbervilles: A Pure Woman Faithfully Presented"],
    'jude the obscure': ['Jude the Obscure: A Straightforward Novel'],
    'the mayor of casterbridge': ['The Mayor of Casterbridge: The Life and Death of a Man of Character'],
    'far from the madding crowd': ['Far from the Madding Crowd: A Pastoral Romance'],
    'the invisible man': ['The Invisible Man: A Grotesque Romance'],
    'a study in scarlet': ['A Study in Scarlet: Being a Reminiscence of John H. Watson, M.D.'],
    'kidnapped': ['Kidnapped: Being Memoirs of the Adventures of David Balfour in the Year 1751'],
    'the master of ballantrae': ["The Master of Ballantrae: A Winter's Tale"],
    'the black arrow': ['The Black Arrow: A Tale of the Two Roses'],
    'treasure island': ['Treasure Island; or, The Mutiny of the Hispaniola'],
    'the scarlet letter': ['The Scarlet Letter: A Romance'],
    'the house of the seven gables': ['The House of the Seven Gables: A Romance'],
    'uncle toms cabin': ["Uncle Tom's Cabin; or, Life Among the Lowly"],
    'adventures of huckleberry finn': ['The Adventures of Huckleberry Finn'],
    'puddnhead wilson': ["The Tragedy of Pudd'nhead Wilson and the Comedy of Those Extraordinary Twins"],
    'the red badge of courage': ['The Red Badge of Courage: An Episode of the American Civil War'],
    'maggie': ['Maggie: A Girl of the Streets'],
    'mcteague': ['McTeague: A Story of San Francisco'],
    'the octopus': ['The Octopus: A Story of California'],
    'jane eyre': ['Jane Eyre: An Autobiography'],
    'shirley': ['Shirley: A Tale'],
    'wuthering heights': ['Wuthering Heights: A Novel'],
    'middlemarch': ['Middlemarch: A Study of Provincial Life'],
    'silas marner': ['Silas Marner: The Weaver of Raveloe'],
    'mary barton': ['Mary Barton: A Tale of Manchester Life'],
    'the woman in white': ['The Woman in White: A Novel'],
    'the moonstone': ['The Moonstone: A Romance'],
    'culture and anarchy': ['Culture and Anarchy: An Essay in Political and Social Criticism'],
    'the idea of a university': ['The Idea of a University Defined and Illustrated'],
    'apologia pro vita sua': ['Apologia Pro Vita Sua: Being a History of His Religious Opinions'],
    'the dream of gerontius': ['The Dream of Gerontius: A Poem'],
    'modern painters': ['Modern Painters: Their Superiority in the Art of Landscape Painting'],
    'unto this last': ['Unto This Last: Four Essays on the First Principles of Political Economy'],
    'studies in the history of the renaissance': ['The Renaissance: Studies in Art and Poetry'],
    'marius the epicurean': ['Marius the Epicurean: His Sensations and Ideas'],
    'the importance of being earnest': ['The Importance of Being Earnest: A Trivial Comedy for Serious People'],
    'murder in the cathedral': ['Murder in the Cathedral: A Play with Chorus'],
    'four quartets': ['Four Quartets: Burnt Norton, East Coker, The Dry Salvages, Little Gidding'],
    'the good soldier': ['The Good Soldier: A Tale of Passion', 'The Saddest Story'],
}

# ------------------------------------------------------------------ utilities
_PUNCT = re.compile(r"[^a-z0-9 ]+")


def norm_title(title):
    """Normalise a title for table lookup: short form, lower-case, no marks.

    Cuts at the first colon, semicolon or sentence point, drops parenthetical
    disambiguators ("Ulysses (Joyce, 1922)") and strips punctuation, so that
    "Tess of the d'Urbervilles: A Pure Woman Faithfully Presented",
    "Zuleika Dobson; or, An Oxford Love Story" and "A Christmas Carol. In
    Prose." all resolve to their short form.
    """
    t = re.sub(r"\([^)]*\)", " ", title)
    for sep in (";", ":"):
        t = t.split(sep)[0]
    t = re.split(r"\.\s", t)[0]
    t = t.replace("\u2026", " ")
    return _PUNCT.sub("", t.lower()).strip()


def _key(text):
    return int(hashlib.sha1(text.encode("utf-8")).hexdigest(), 16)


def _pick(seed, options):
    return options[_key(seed) % len(options)]


VERSE_WORDS = ("poem", "poetry", "verse", "lyric", "sonnet", "ode", "ballad",
               "elegy", "epic", "idyll", "cantos", "eclogue", "pastoral",
               "monodrama", "dramatic poem", "metrical", "rhyme", "sprung",
               "quatrains", "couplets", "hexameters", "blank verse",
               "sequence", "anthology lyric", "sermon in verse", "sermons in verse")
DRAMA_WORDS = ("play", "drama", "tragedy", "comedy", "farce", "melodrama",
               "acts", "act)", "opera", "interlude", "masque", "monodrama",
               "scenes")
PROSE_FICTION_WORDS = ("novel", "novella", "story", "stories", "tale", "romance",
                       "sketch", "narrative", "fantasy")


def is_verse(form, genres):
    text = (form or "").lower() + " " + " ".join(genres or []).lower()
    return any(w in text for w in VERSE_WORDS)


def is_drama(form, genres):
    text = (form or "").lower() + " " + " ".join(genres or []).lower()
    return any(w in text for w in DRAMA_WORDS)


def is_fiction(form, genres):
    text = (form or "").lower() + " " + " ".join(genres or []).lower()
    return any(w in text for w in PROSE_FICTION_WORDS)


def short_genre(genres):
    if not genres:
        return None
    g = genres[0]
    g = re.sub(r"^The ", "", g)
    return g


def year_of(w):
    for key in ("pub", "perf", "ms"):
        v = w.get(key)
        if v:
            m = re.search(r"\d{4}", str(v))
            if m:
                return m.group()
    return None


# ------------------------------------------------------- genre-level registers
# One entry per genre used in the installments 8-9 corpus. Verse genres describe
# the line, stanza and prosody; prose genres describe the register and the shape
# of the sentence. Anything not listed falls back to its family.
GENRE_REGISTER = {
    # --- verse
    "Epic and the Long Philosophical Poem": "Verse of the long poem: blank verse or a sustained narrative measure, the extended simile and the long verse paragraph, carried across books or parts.",
    "Pastoral Elegy and the Mourning Sequence": "Verse in the elegiac mode: the mourning stanzas run in a repeated stanzaic pattern, the line is long enough to carry the lament and the apostrophe, and the movement is from grief to the consolation or the refusal of consolation that closes the sequence.",
    "Dramatic Monologue and Masked Lyric": "Verse in the monologue: a single speaker, not the poet, addresses a silent listener, and the metre is loose enough to carry colloquial interruption, self-betrayal and the aside, while the rhyme scheme holds the argument together.",
    "Idyll and Domestic Narrative Poem": "Verse narrative in the idyll: blank verse or a regular stanza carries a domestic or rural action told at length, with set-piece description, reported dialogue and a closing reflective passage.",
    "Nonsense Verse and the Parody of Rule": "Verse of regular comic metre: the limerick, the double dactyl, the ballad stanza and the parody of a received form, with the rhyme exact and the sense deliberately absurd.",
    "Georgian Anthology Lyric": "Verse in the Georgian lyric manner: the rhymed stanza of four or eight lines, the plain monosyllabic diction, the observed countryside and the elegiac undertone, without the modernist break in syntax.",
    "Sonnet Revival and Sequenced Sonnet": "Verse in the fourteen-line sonnet, Petrarchan or Shakespearean, and in sequences where the individual sonnets accumulate into a continuous argument or a narrative of feeling.",
    "Dialect Poem and Vernacular Performance": "Verse in dialect and vernacular: the spelling carries the pronunciation, the stanza is song-like and often rhymed in ballad measure, and the poem is written to be spoken or performed aloud.",
    "Trench Lyric and the War Poem": "Verse of the war poem: the short line and the tight rhyme of the lyric, or the loose blank-verse paragraph, with the colloquial idiom of the ranks set against the elevated diction of the tradition it answers.",
    "Modernist Long Poem and the Mythical Method": "Verse in the modernist long poem: the polyphonic sequence of fragments in free verse and in borrowed metres, quotation and allusion doing the work of connective argument, the whole ordered by a mythic or symbolic pattern rather than by narrative.",
    "Imagist Lyric and the Free-Verse Line": "Free verse in the imagist manner: the unrhymed cadenced line, the hard exact image, the omission of the connecting argument and the refusal of the received stanza, with the rhythm of the phrase rather than the metronome.",
    "New Negro Lyric and the Harlem Renaissance Poem": "Verse of the New Negro lyric: the blues and jazz cadence, the sermon's rising repetition, the sonnet and the ballad form turned to racial subject-matter, and the vernacular idiom used as a literary language.",
    "Victorian Verse Drama and Revived Tragedy": "Verse drama in blank verse: the unrhymed iambic pentameter carries the dialogue, with lyrical interludes in shorter lines and in rhyme for songs, choruses and set pieces.",
    "Verse Drama and the Poetic Play": "Verse drama: the poetic line, blank verse or a regular stanza, carries the dialogue, and the play alternates the verse speech with lyric and choral passages.",
    "Religious Lyric": "Verse of devotion: the hymn stanza or the short rhymed lyric, the plain diction of prayer and the recurring refrain, written for meditation or for congregational use.",
    # --- prose fiction
    "Realist Novel of Common Life": "Prose fiction of common life: the continuous chaptered narrative, the full reported dialogue, the exact material description of rooms, clothes, money and work, and the slow accumulation of consequence.",
    "Novel of Development and the Growth Story": "Prose fiction of formation: the narrative follows one consciousness from childhood or youth to settlement, in chapters grouped by the stages of the life, with the earlier manner recalled and judged by the later.",
    "Regional Novel and the American Local-Colour Inheritance": "Prose fiction of place: the dialect dialogue and the transcribed local speech, the landscape carried in exact seasonal detail, and the plot set inside the customs, economy and geography of one region.",
    "Novel of Consciousness and the Stream of Mind": "Prose of the interior: long unbroken periods, free indirect discourse, the time-shift and the associative leap, with the punctuation and syntax following the movement of the mind rather than the order of events.",
    "Experimental Novel and the Modernist Form": "Prose of experiment: broken chronology, multiple narrators, parody of received styles, typographical play and the deliberate difficulty of a text that refuses the continuous realistic sentence.",
    "Children's Fantasy and the Dream-Region Tale": "Prose for children: the plain declarative sentence, the direct address to the reader, the named and repeating marvel, and the short chapter pitched to the reading aloud of a single sitting.",
    "Children's Fantasy and the Golden-Age Tale": "Prose for children: the plain declarative sentence, the direct address to the reader, the named and repeating marvel, and the short chapter pitched to the reading aloud of a single sitting.",
    "Imperial Adventure Romance": "Prose of adventure: the first-person or closely focalised narrative of pursuit and escape, the set-piece chapter, the exact vocabulary of weapons, ships, terrain and travel, and the rapid unreflective sentence.",
    "Comedy of Manners and the Drawing-Room Stage": "Prose of the comedy of manners: the balanced epigrammatic exchange, the social vocabulary of rank, money and reputation, and the scene built as a series of entrances, revelations and exits.",
    "Problem Play and Well-Made Drama": "Dramatic prose: the dialogue carries everything, the acts are built on the well-made pattern of exposition, complication, crisis and discovery, and the argument is stated in set speeches and answered in the counter-speeches.",
    "Expressionist and Epic Drama": "Dramatic prose and verse of the non-realistic stage: the numbered or titled scenes, the chant and the direct address, the split self and the narrating figure who stands outside the action, and the bare platform in place of the furnished room.",
    "Sensation Drama and the Domestic Stage": "Dramatic prose of the domestic stage: the dialogue of the drawing room and the household, the revelation scene, the timed entrance, and the act ending on a discovery or a suspense.",
    "Peasant Play and the Irish Dramatic Movement": "Dramatic prose in the Hiberno-English idiom: the syntax and the imagery of the Irish speech are carried into English dialogue, and the play moves between the comic exchange and the elegiac set speech.",
    "Industrial and Condition-of-England Novel": "Prose of the industrial novel: the documentary description of the mill, the mine, the street and the strike, the dialect of the workers set against the language of the masters, and the plot built on the collision of the two nations.",
    "Condition-of-England Novel and the Edwardian Social Panorama": "Prose of the social panorama: the long sentence of survey, the household and the institution described as types of the whole society, and the argument carried by contrast between scenes rather than by authorial comment.",
    "New Woman and Marriage-Question Novel": "Prose of the marriage-question novel: the domestic scene rendered with exact financial and legal detail, the dialogue of negotiation between the sexes, and the closing argument stated in the terms of the period's reform literature.",
    "Sensation Novel": "Prose of sensation: the cliff-edge chapter ending, the first-person testimony and the document inserted into the narrative, the secret withheld and revealed by stages, and the vocabulary of the law, the asylum and the will.",
    "Serial and Monthly-Part Novel": "Prose of the serial: the instalment-shaped chapter, the set-piece opening and the suspended close of each number, the recapitulation of the previous part and the plate or illustration marking the division.",
    "Naturalist and Determinist Novel": "Prose of naturalism: the clinical accumulation of physiological and economic detail, the flat unjudging sentence, the dialect transcribed at length, and the plot driven by heredity, appetite and environment rather than by choice.",
    "Detective Novel and the Golden Age Mystery": "Prose of the fair-play mystery: the puzzle is stated in plain narrative prose, the clues are given to the reader as they are given to the investigator, the timetable and the plan are exact, and the solution is delivered in a set-piece explanation.",
    "Detective Story and the Tale of Detection": "Prose of detection: the pursuit narrative with the investigator's account of the evidence, the exact chronology and the reversal at the close.",
    "Ghost Story and Scientific Supernatural Tale": "Prose of the supernatural: the rational first-person witness, the exact circumstantial detail that makes the impossible credible, the withheld explanation, and the closing sentence that leaves the reader with the horror unaccounted for.",
    "Ghost Story and the Modern Weird Tale": "Prose of the weird tale: the antiquarian or scholarly narrator, the document or the object that carries the haunting, the exact topography, and the refusal of a natural explanation.",
    "Modern Short Story and the Magazine Tale": "Prose of the short story: a single compressed situation, the exact particular that stands for the whole, the turned or withheld ending, and a length set by the magazine's page.",
    "Early Scientific Romance and Utopian Speculation": "Prose of the scientific romance: the frame narrative of the witness, the set-piece description of the machine, the society or the world, and the dialogue of exposition in which the inventor explains his discovery.",
    "Scientific Romance and the Utopian Tale": "Prose of the scientific romance: the frame narrative of the witness, the set-piece description of the machine, the society or the world, and the dialogue of exposition in which the inventor explains his discovery.",
    "Dystopian Fiction and the Anti-Utopian Satire": "Prose of the anti-utopia: the document, the diary or the confession of a subject inside the system, the invented vocabulary of the state, and the satiric inversion of the utopian description.",
    "Jazz-Age Novel and the Expatriate Romance": "Prose of the jazz age: the compressed lyrical sentence, the transcribed party dialogue and the idiom of the period, with the elegiac retrospect imposed on the scene of pleasure.",
    "Proletarian Novel and the Working-Class Fiction": "Prose of the proletarian novel: the vernacular of the workplace and the picket line, the documentary detail of wage, rent, hunger and the strike, and the collective rather than the individual subject.",
    "Historical Novel and Romance": "Prose of the historical novel: the period vocabulary and the studied anachronism avoided, the set-piece of battle, ceremony or trial, and the narrative pitched between the documented public event and the invented private life.",
    "Novel of Manners and Fashion": "Prose of manners: the dialogue of the social world, the exact vocabulary of rank, money and reputation, and the scene built on the breach or the observance of a convention.",
    "Tall Tale and South-Western Humour Sketch": "Prose of the tall tale: the frame of the literate narrator and the vernacular teller, the dialect spelling, the escalating impossibility delivered deadpan, and the punch that turns on the outsider's credulity.",
    "Local-Colour Sketch and the Regional Portrait": "Prose of the local-colour sketch: the transcribed dialect, the exact naming of places, trades, foods and weather, and the short framed narrative or descriptive set piece.",
    # --- prose non-fiction
    "Review Essay and Quarterly Argument": "Prose of the quarterlies: the long periodic sentence of argument, the quotation and the set-piece judgement, the division into numbered or titled sections, and the assumption of a general reader of the reviewing class.",
    "Critical Essay and the Modern Review": "Prose of criticism: the essay as an argument with a thesis, the quotation examined at length, the comparison and the judgement, and the personal voice admitted into the critical sentence.",
    "Lecture and Popular Address": "Prose of the platform: the spoken sentence, the repetition and the triadic climax, the direct address to the audience, the apostrophe and the peroration, printed as delivered.",
    "Social Inquiry and the Documented Survey": "Prose of the survey: the tabulated evidence, the interviewed voice quoted verbatim, the statistical paragraph and the argument from the case, with the reforming conclusion drawn from the accumulated document.",
    "Documentary Prose and the Reportage Book": "Prose of reportage: the observed scene rendered in the present tense or the immediate past, the transcribed speech of the witness, the document quoted in full, and the argument carried by the sequence of scenes.",
    "War Narrative of the Common Soldier": "Prose of the common soldier: the plain first-person account, the exact vocabulary of the trench, the ration, the march and the casualty, and the understatement that carries the horror.",
    "War Memoir and the Autobiographical Testimony": "Prose of the war memoir: the first-person retrospective, the episodic chapter organised by posting or battle, the transcribed speech of the ranks, and the judgement passed by the later self on the earlier.",
    "Autobiography and the Modern Memoir": "Prose of autobiography: the first-person narrative of the life, the set-piece of the formative scene, the quotation from letters and diaries, and the reflection on the formation of a self.",
    "Memoir and Autobiographical Prose": "Prose of memoir: the first-person narrative of a life or a period, the remembered scene and the quoted letter, with the reflection of the later self imposed on the earlier experience.",
    "Biography and the Modern Life": "Prose of the new biography: the documented life told with the novelist's scene and dialogue, the quotation from letters and papers, and the psychological interpretation offered as inference rather than as assertion.",
    "Nature Essay and the Rural Observation": "Prose of the nature essay: the exact observation of the season, the field and the creature, the scientific nomenclature beside the lyrical sentence, and the diary or month-by-month arrangement.",
    "Political Treatise": "Prose of the treatise: the numbered proposition, the definition, the deduction and the objection answered, in a style pitched to the exactness of argument rather than to the pleasure of the reader.",
}

FAMILY_FALLBACK = {
    "verse": "Verse: the line and stanza follow the conventions of the genre, and the poem is written to be read aloud.",
    "drama": "Dramatic prose or verse: the dialogue carries the whole, and the text is written for performance.",
    "fiction": "Prose fiction: the continuous chaptered narrative carries description, dialogue and reflection.",
    "nonfiction": "Prose: the argument or the account is carried in continuous prose, divided into sections or chapters.",
}

# Form-string markers that add a specific structural or prosodic fact.
FORM_MARKERS = (
    (r"blank verse", "The dialogue or narrative runs in blank verse, the unrhymed iambic pentameter."),
    (r"hexameter", "The line is the English hexameter, the unrhymed six-stress line of the classical experiment."),
    (r"sprung rhythm", "The metre is sprung rhythm, with the number of stresses fixed and the number of unstressed syllables free."),
    (r"free verse|free-verse", "The line is free verse, cadenced by the phrase and not by a received pattern."),
    (r"sonnet", "The form is the fourteen-line sonnet."),
    (r"couplet", "The verse runs in rhymed couplets."),
    (r"ballad", "The stanza is the ballad stanza, the four-stress and three-stress lines rhyming on the even lines."),
    (r"quatrain", "The stanza is the quatrain."),
    (r"limerick", "The stanza is the limerick, the five-line anapaestic form with the double rhyme."),
    (r"ode", "The form is the ode, in irregular or regular stanzas."),
    (r"eleg", "The poem is elegiac, the mourning stanza repeated through the sequence."),
    (r"dialect", "The spelling and syntax carry a spoken dialect."),
    (r"monthly part|number|serial", "The work was issued in serial parts, and the instalment shapes the chapter."),
    (r"three volume|two volume|volume", "The work was issued in volumes, the division marked in the text."),
    (r"act", "The text is divided into acts, with the scene changes marked."),
    (r"one act", "The play is in a single act, played without interval."),
    (r"posthumous", "The text was published posthumously, from the manuscript or from the papers left at the author's death."),
    (r"anonymous|by 'A'|by \"A\"", "The work was published anonymously or under an initial, and the authorship was established afterwards."),
    (r"pamphlet", "The work is a pamphlet, a single argument in a short compass."),
    (r"lecture", "The text is the printed lecture, retaining the spoken address."),
    (r"diary|journal", "The text is the dated entry, continuous in its observation."),
    (r"letter|epistol", "The text is cast as letters, the argument carried by correspondence."),
    (r"antholog", "The work is an anthology, the pieces ordered by the editor."),
    (r"collection", "The work is a collection of separate pieces in the author's or editor's order."),
    (r"trilog", "The work is a trilogy, its three parts complete in themselves and continuous in their subject."),
    (r"illustrat", "The text was issued with illustrations, which carry part of the meaning."),
    (r"children|picture book|nursery", "The text is written for children, the sentence short and the vocabulary plain."),
)


# Family classification (drama / verse / fiction / nonfiction).
#
# The work's own literary form decides, with whole-word matching; its genres
# are consulted, primary genre first, only when the form names no family.
# The earlier version substring-matched the form and every genre name at once,
# so "ode" matched inside "Modern"/"Modernist", "epic" inside a novel's
# "(first of 'The Epic of the Wheat')", "drama" inside the verse genre
# "Dramatic Monologue", and any secondary verse genre ("Nonsense Verse")
# turned a prose book into "a verse work".
_FAMILY_WORDS = (
    ("drama", r"plays?|dramas?|traged(?:y|ies)|comed(?:y|ies)|tragicomed(?:y|ies)|farces?|"
              r"melodramas?|masques?|operas?|operettas?|librett(?:o|os|i)|interludes?|"
              r"pageants?|pantomimes?|extravaganzas?|burlettas?|revues?|"
              r"screenplays?"),
    ("verse", r"poems?|poetry|verses?|lyrics?|sonnets?|odes?|ballads?|eleg(?:y|ies)|"
              r"idylls?|cantos?|eclogues?|limericks?|hymns?|songs?|epics?|rhymes?|"
              r"quatrains?|couplets?|hexameters?|monologues?|monodramas?|ballades?|rondeaus?|"
              r"villanelles?"),
    ("nonfiction", r"autobiograph(?:y|ies)|memoirs?|biograph(?:y|ies)|essays?|criticism|"
                   r"histor(?:y|ies)|treatises?|sermons?|lectures?|letters|diar(?:y|ies)|"
                   r"journals?|travels|travelogues?|pamphlets?|philosophy|reportage|"
                   r"journalism|stud(?:y|ies)|polemics?|manifestos?|reminiscences|"
                   r"recollections|surveys?|tracts?|chronicles?|accounts?|guides?|"
                   r"handbooks?|dictionar(?:y|ies)|translations?|commentar(?:y|ies)"),
    ("fiction", r"novels?|novellas?|novelettes?|stor(?:y|ies)|tales?|romances?|"
                r"sketch(?:es)?|fiction|fables?|fantas(?:y|ies)|narratives?|legends?|"
                r"sagas?|parables?|allegor(?:y|ies)"),
)
_FAMILY_RX = [(fam, re.compile(r"\b(?:%s)\b" % words)) for fam, words in _FAMILY_WORDS]
# Compounds whose family differs from their head noun, checked first.
_FAMILY_COMPOUNDS = (
    ("drama", re.compile(r"\b(?:verse|poetic|closet|lyric|music|dance|chronicle)[- ]"
                         r"(?:dramas?|plays?)\b|\bplays? in verse\b")),
    ("fiction", re.compile(r"\bfuture histor(?:y|ies)\b")),
    ("verse", re.compile(r"\b(?:verse|metrical|rhymed?)[- ](?:novels?|novelettes?|novellas?|"
                         r"tales?|romances?|"
                         r"narratives?|satires?|essays?|epistles?|letters?|sermons?|fables?|"
                         r"stor(?:y|ies)|parod(?:y|ies)|chronicles?|histor(?:y|ies)|translations?)\b"
                         r"|\b(?:novels?|tales?|romances?|narratives?|stor(?:y|ies)|satires?|"
                         r"essays?|letters?|sermons?|fables?) in (?:verse|rhyme)\b"
                         r"|\bdramatic (?:monologues?|lyrics?|poems?|idylls?|romances?)\b"
                         r"|\btranslations? (?:of|from) [a-z' -]*?\b(?:poetry|poems|verse|"
                         r"songs|ballads|lyrics|sonnets|odes)\b")),
    ("nonfiction", re.compile(r"\b(?:slave|captivity|travel|conversion|spiritual)[- ]"
                              r"narratives?\b|\btravel (?:book|writing|sketch(?:es)?)\b"
                              r"|\bhistorical (?:prose )?narratives?\b")),
)
_FAMILY_SPLIT = re.compile(r"\b(?:of|in|with|for|by|from|on|about|after|to)\b|[,:;/]| and ")


# "narrative" and "sketch" name prose without settling fiction against
# fact (Walden is a "prose narrative", Sketches by Boz "periodical sketches"),
# so a form decided only by them defers to a non-fiction genre.
_WEAK_FICTION = re.compile(r"\b(?:narratives?|sketch(?:es)?)\b")


def _form_family_detail(text):
    """(family, weak) named by one form or genre string; family may be None.

    Parenthetical and quoted matter is ignored unless the rest names no family:
    "Novel (first of 'The Epic of the Wheat')" is a novel, but "Prose (regimental
    memoir)" is decided by its parenthesis."""
    low = (text or "").lower()
    fam, weak = _family_of(re.sub(r"\([^)]*\)|'[^']*'|\"[^\"]*\"", " ", low))
    if fam is None:
        fam, weak = _family_of(re.sub(r"[()]", " ", low))
    return fam, weak


def _family_of(s):
    for fam, rx in _FAMILY_COMPOUNDS:
        if rx.search(s):
            return fam, False
    head, *rest = _FAMILY_SPLIT.split(s)
    hits = [(m.start(), m.group(), fam) for fam, rx in _FAMILY_RX for m in rx.finditer(head)]
    if hits:
        _, word, fam = max(hits)  # English compounds are head-final: "verse drama"
        return fam, bool(_WEAK_FICTION.fullmatch(word))
    for part in rest:
        hits = [(m.start(), m.group(), fam) for fam, rx in _FAMILY_RX for m in rx.finditer(part)]
        if hits:
            _, word, fam = max(hits)  # "collection of stories", "expressionist and epic drama"
            return fam, bool(_WEAK_FICTION.fullmatch(word))
    return None, False


PROSE = ("fiction", "nonfiction")
# A verse form naming several pieces is a collection; otherwise a single poem,
# narrative when the form says so.
_COLLECTION_FORM = re.compile(r"\b(?:collections?|collected|selected|poems|verses|lyrics|songs|sonnets|"
                              r"ballads|hymns|odes|sequence|anthology|rhymes|book of)\b", re.I)
_NARRATIVE_FORM = re.compile(r"\b(?:narrative|epic|books?|cantos?|idylls?|romance|tale|ballad|story|fits?)\b", re.I)


def _form_family(text):
    """Family named by one form or genre string, or None."""
    return _form_family_detail(text)[0]


def family(form, genres):
    """verse / drama / fiction / nonfiction for a work.

    The form decides when it names a family by a definite word. Otherwise the
    genres are read in order (primary first): a genre named only by "sketch" or
    "narrative" marks the work as prose without settling which kind, so it does
    not stop a later definite genre, and a later verse or drama genre cannot
    overrule it."""
    fam, weak = _form_family_detail(form)
    if fam and not weak:
        return fam
    prose = fam
    for gname in genres or []:
        gfam, gweak = _form_family_detail(gname)
        if not gfam:
            continue
        if gweak:
            prose = prose or gfam
            continue
        if prose and gfam in ("verse", "drama"):
            continue
        return gfam
    return prose or "nonfiction"


def _style_clause(author):
    """First usable clause of the author's stylistic profile, lower-cased."""
    text = (author or {}).get("style") or ""
    if not text:
        return None
    for sep in (";", "."):
        if sep in text:
            text = text.split(sep)[0]
            break
    text = text.strip().rstrip(".")
    if len(text) < 25:
        return None
    return text[0].lower() + text[1:]


def _join(sentences):
    out = []
    for s in sentences:
        s = (s or "").strip()
        if s:
            out.append(s if s.endswith((".", "!", "?")) else s + ".")
    return " ".join(out)


def compose_meter(w, author):
    """Metre for verse, prose manner for prose: never empty, never invented."""
    form = w.get("form") or ""
    genres = w.get("genres") or []
    fam = family(form, genres)
    parts = []
    reg = None
    for gname in genres:
        # A genre of another family would describe the wrong medium (a comic
        # novel tagged "Nonsense Verse" must not get "Verse of regular comic
        # metre"); genres that name no family are usable for any work.
        gfam, gweak = _form_family_detail(gname)
        if gname in GENRE_REGISTER and (gfam in (None, fam) or (gweak and fam in PROSE)):
            reg = GENRE_REGISTER[gname]
            break
    if reg is None:
        reg = FAMILY_FALLBACK[fam]
    parts.append("Verse." if fam == "verse" else ("Dramatic text." if fam == "drama" else "Prose."))
    parts.append(reg)
    for pat, sent in FORM_MARKERS:
        if re.search(pat, form, re.I) and sent not in parts:
            parts.append(sent)
            if len(parts) >= 5:
                break
    clause = _style_clause(author)
    if clause:
        parts.append("The author's characteristic manner is " + clause)
    return _join(parts)


def compose_structure(w):
    """Narrative structure, composed from the form and the shape of the work."""
    form = w.get("form") or ""
    fam = family(form, w.get("genres") or [])
    parts = []
    m = re.search(r"\((\d+)\s*(stories|poems|sonnets|essays|plays|acts|numbers|tales)\)", form, re.I)
    if m:
        parts.append("The work is in %s %s" % (m.group(1), m.group(2).lower()))
    n = re.search(r"(\w+)\s+acts?", form, re.I)
    if n and "act" in form.lower():
        parts.append("The action is divided into %s acts, each closing on a discovery or a reversal" % n.group(1).lower())
    if re.search(r"monthly part|numbers|serial|weekly", form, re.I):
        parts.append("The narrative was issued in instalments, and each part carries its own set piece and its suspended close")
    if re.search(r"three volume|two volume|volumes?", form, re.I):
        parts.append("The book was issued in volumes, the division marked by the pause in the action")
    if fam == "fiction" and not parts:
        parts.append("A continuous prose narrative in chapters, the action carried in sequence from the opening situation to the closing resolution")
    if fam == "verse" and not parts:
        parts.append("A sequence of separate poems rather than a continuous narrative; the pieces stand alone and are commonly read individually")
    if fam == "nonfiction" and not parts:
        parts.append("Continuous prose in sections or chapters, the argument or the account advanced from its statement to its conclusion")
    if fam == "drama" and not parts:
        parts.append("The play is divided into acts and scenes, the dialogue carrying the whole of the action")
    plot = w.get("plot") or ""
    if len(plot) > 240:
        parts.append("The plot advances by the stages set out in the account above")
    return _join(parts)


def compose_attribution(w, author):
    """Attribution notes: what the record settles, and what it does not."""
    parts = []
    name = w.get("author") or (author or {}).get("name") or ""
    status = w.get("status", "complete")
    as_status = w.get("as_status", "single")
    form = w.get("form") or ""
    pseudo = (author or {}).get("pseudo") or []
    alt = (author or {}).get("alt") or []
    coauthors = w.get("coauthors") or []
    if coauthors:
        parts.append("The work is recorded as a joint undertaking with " + " and ".join(coauthors)
                     + ", the contribution of each being stated in the work-author relationship")
    elif as_status != "single":
        parts.append("The authorship is recorded as %s" % as_status)
    if re.search(r"anonymous|by 'A'|by \"A\"", form, re.I):
        parts.append("It was first published anonymously and the authorship was established afterwards from the publisher's records and the correspondence")
    elif pseudo:
        parts.append("It was published under the name %s, one of the author's pseudonyms; the attribution to %s is secure"
                     % (pseudo[0], name))
    else:
        parts.append("Attribution is secure: the work was published under the author's name"
                     + (", also recorded as " + alt[0] if alt else ""))
    if status != "complete":
        parts.append("The research status of the record is %s, and the text is reported as the evidence allows" % status)
    else:
        parts.append("No competing attribution or spurious edition is recorded for this title")
    canon = w.get("canon")
    if canon:
        parts.append("The work is catalogued here as %s" % canon.lower())
    return _join(parts)


def compose_bibliography(w, author):
    """Bibliographical description, from the curated table or from the record."""
    key = norm_title(w.get("title") or "")
    parts = []
    if key in FIRST_EDITIONS:
        parts.append(FIRST_EDITIONS[key])
    else:
        pub = w.get("pub")
        comp = w.get("composition") or w.get("comp")
        perf = w.get("perf")
        if pub:
            parts.append("First published in %s" % pub)
        elif perf:
            parts.append("First performed in %s" % perf)
        if comp:
            lo = comp[0] if isinstance(comp, (list, tuple)) else comp
            hi = comp[1] if isinstance(comp, (list, tuple)) and len(comp) > 1 else None
            parts.append(("composed between %s and %s" % (lo, hi)) if hi and hi != lo
                         else ("composed in %s" % lo))
        if perf and pub:
            parts.append("first performed in %s" % perf)
        if not parts:
            parts.append("The record carries no publication date; the work is reported from the evidence attached to the author")
    alt = w.get("alt") or []
    if alt:
        parts.append("The title is also recorded as " + "; ".join(alt[:3]))
    lang = w.get("lang")
    if lang and lang != "English":
        parts.append("The original language is %s" % lang)
    if w.get("status", "complete") != "complete":
        parts.append("The research status is %s" % w["status"])
    return _join(parts)


_STOP = set("""the a an and or of to in on at by for with from into over under after before
this that these those it its his her their our your my me him she he they we you i
mr mrs ms dr prof sir lord lady st chapter part book first second third new old great
good bad one two three four five six seven eight nine ten
england english london paris yorkshire scotland scottish ireland irish wales welsh
america american france french germany german italy italian spain spanish russia russian
india indian africa african china chinese japan japanese egypt egyptian greece greek rome roman
north south east west upper lower middle great little
january february march april may june july august september october november december
century years year day days night nights war world house home life death god christ
king queen prince princess duke duchess earl count baron lord lady
chapter act scene part volume book poem novel play story tale essay
""".split())



# Character fallback: RETIRED. The name-extraction fallback (revisions 1-11)
# wrote "The principal figures named in the account above are ..." into works
# without hand-authored characters. Audited in installments 08-09 it was wrong
# often enough to be harmful (a composer, a dedicatee, a source novel and a book
# title all appeared as characters), so principal_characters is now either
# hand-authored (chars=) or null, and check_installment.py rejects the phrasing.
CHARACTER_FALLBACK = False

def compose_characters(w):
    """Principal characters, recovered from names the record itself supplies."""
    if w.get("chars"):
        return None
    text = " ".join([w.get("plot") or "", w.get("desc") or ""])
    title_words = set(re.sub(r"[^A-Za-z ]", " ", (w.get("title") or "")).lower().split())
    author_words = set(re.sub(r"[^A-Za-z ]", " ", (w.get("author") or "")).lower().split())
    found = []
    for m in re.finditer(r"\b((?:[A-Z][A-Za-z'\-]+)(?:\s+[A-Z][A-Za-z'\-]+){0,2})\b", text):
        cand = m.group(1).strip()
        low = cand.lower()
        words = low.split()
        if not words or words[0] in _STOP or low in title_words or low in author_words:
            continue
        if any(x in _STOP for x in words[1:]):
            continue
        if len(cand) < 4 or cand.isupper():
            continue
        if cand not in found:
            found.append(cand)
    if len(found) < 2:
        return None
    return _join(["The principal figures named in the account above are " + "; ".join(found[:6])])


def compose_description_extra(w, author):
    """The situating sentence appended to a thin description."""
    fam = family(w.get("form"), w.get("genres") or [])
    label = {"verse": "verse", "drama": "dramatic", "fiction": "prose fiction",
             "nonfiction": "prose"}[fam]
    parts = []
    pub = w.get("pub")
    who = w.get("author") or (author or {}).get("name")
    tier = (author or {}).get("tier") or ""
    if pub and who:
        parts.append("It is a %s work of %s by %s" % (label, pub, who))
    elif who:
        parts.append("It is a %s work by %s" % (label, who))
    movs = w.get("movements") or []
    if movs:
        parts.append("It belongs to %s" % re.sub(r"^The ", "", movs[0]))
    gs = w.get("genres") or []
    if gs:
        parts.append("and is catalogued here under %s" % "; ".join(g.lower() for g in gs[:2]))
    canon = w.get("canon")
    if canon and canon != "Secondary canon":
        parts.append("The record grades it as %s" % canon.lower())
    if tier.startswith("Major"):
        parts.append("its author being of the first rank in this corpus")
    return _join(parts)


def compose_alt_titles(w):
    """Alternative titles: documented variants, plus the short form of a long title."""
    out = []
    key = norm_title(w.get("title") or "")
    out.extend(ALT_TITLES.get(key) or [])
    title = w.get("title") or ""
    if ":" in title:
        short = title.split(":")[0].strip()
        if len(short) > 6 and short not in out and short != title:
            out.append(short)
    if ";" in title:
        short = title.split(";")[0].strip()
        if len(short) > 6 and short not in out and short != title:
            out.append(short)
    return [o for o in out if o and o != title]


# ----------------------------------------------------------- entry points
def compose_author_uncertainty(a, works):
    """What the record does not settle, stated from the record's own flags."""
    parts = []
    if a.get("birth_approx") or (a.get("dob") or "").startswith("c.") or (a.get("dob") or "").startswith("?"):
        parts.append("The date of birth is recorded as approximate, the parish or family record not having fixed the day")
    if a.get("death_approx") or (a.get("dod") or "").startswith("c."):
        parts.append("The date of death is recorded as approximate")
    bp = (a.get("birth") or "").lower()
    if not bp or "unknown" in bp or "not recorded" in bp or bp.startswith("?"):
        parts.append("The place of birth is not securely recorded")
    partial = [w.get("title") for w in works if w.get("status") in ("partial", "incomplete", "fragmentary")]
    if partial:
        parts.append("%d of the %d works catalogued here carry a research status of 'partial', among them %s, and are reported only so far as the evidence allows"
                     % (len(partial), len(works), "; ".join(sorted(partial)[:3])))
    anon = [w.get("title") for w in works if re.search(r"anonymous|by 'A'", (w.get("form") or ""), re.I)]
    if anon:
        parts.append("The attribution of %s rests on the publisher's records and the correspondence rather than on a title page"
                     % "; ".join(sorted(anon)[:2]))
    if not (a.get("uncertainty") or parts):
        return None
    return _join(parts) or None


def enrich_works(works, authors_by_name):
    """title -> {work field: composed value} for every field worth filling."""
    out = {}
    for w in works:
        a = authors_by_name.get(w.get("author") or "") or {}
        p = {}
        if not (w.get("meter") or "").strip():
            p["meter_and_prosody"] = compose_meter(w, a)
        if not (w.get("struct") or "").strip():
            p["narrative_structure"] = compose_structure(w)
        if not (w.get("attrib") or "").strip():
            p["attribution_notes"] = compose_attribution(w, a)
        if not (w.get("biblio") or "").strip():
            p["bibliographical_notes"] = compose_bibliography(w, a)
        if CHARACTER_FALLBACK and not (w.get("chars") or "").strip():
            c = compose_characters(w)
            if c:
                p["principal_characters"] = c
        alt = compose_alt_titles(w)
        if alt and not (w.get("alt") or []):
            p["alternative_titles"] = alt
        if len((w.get("desc") or "")) < 200:
            extra = compose_description_extra(w, a)
            if extra:
                p["description"] = _join([w.get("desc") or "", extra])
        out[w.get("title")] = {k: v for k, v in p.items() if v}
    return out


def enrich_authors(authors, works_by_author):
    """author name -> {author field: composed value}."""
    out = {}
    for a in authors:
        ws = works_by_author.get(a.get("name") or "") or []
        p = {}
        if not (a.get("uncertainty") or "").strip():
            u = compose_author_uncertainty(a, ws)
            if u:
                p["biographical_uncertainty"] = u
        prof = a.get("profile") or ""
        if len(prof) < 350 and ws:
            tail = "The works catalogued here number %d, from %s to %s." % (
                len(ws),
                min([w.get("pub") for w in ws if w.get("pub")] or ["the earliest record"]),
                max([w.get("pub") for w in ws if w.get("pub")] or ["the latest record"]))
            p["literary_profile"] = _join([prof, tail]) if prof else tail
        out[a.get("name")] = {k: v for k, v in p.items() if v}
    return out


# ================================ revision 2 ==============================
# The functions below supersede the drafts above: they read the schema-stable
# WORK_KEYS / AUTHOR_KEYS payloads, so one code path serves installments 8, 9
# and 10, and they no longer claim facts the record does not carry.

STRUCT_BY_GENRE = (
    ("Epic and the Long Philosophical Poem", "A long poem in books or parts, its narrative or its argument carried continuously from the statement of its subject to its close."),
    ("Idyll and Domestic Narrative Poem", "A sequence of narrative idylls, each a self-contained story in verse, bound into one continuous argument by the recurring figures and the closing book."),
    ("Sonnet Revival and Sequenced Sonnet", "A sequence of sonnets, each complete in fourteen lines, reading as a continuous argument or a continuous story of feeling when taken in order."),
    ("Pastoral Elegy and the Mourning Sequence", "An elegiac sequence: the stanzas repeat the mourning pattern, and the poem moves from the news of the death, through the lament and the questioning, to the consolation or the refusal of consolation."),
    ("Trench Lyric and the War Poem", "A sequence of separate lyrics, each a single moment of the war, to be read in the order in which the collection sets them."),
    ("Modernist Long Poem and the Mythical Method", "A long poem built as a sequence of fragments in several voices, ordered by a mythic or symbolic pattern rather than by narrative sequence."),
    ("Imagist Lyric and the Free-Verse Line", "A collection of short separate poems, each built on one image or one cadence, standing alone rather than forming a continuous narrative."),
    ("Georgian Anthology Lyric", "A collection of separate short poems in the anthology manner, ordered by subject rather than by narrative."),
    ("Dramatic Monologue and Masked Lyric", "A sequence of monologues, each spoken by a different character in a different scene, with the silent listener implied in every line."),
    ("Nonsense Verse and the Parody of Rule", "A collection of short comic pieces, each complete in its stanza form and each turning on the same joke of exact rule and absurd sense."),
    ("Dialect Poem and Vernacular Performance", "A collection of poems written to be performed, each a separate monologue or song in the spoken dialect."),
    ("New Negro Lyric and the Harlem Renaissance Poem", "A collection of lyrics in several forms, from the sonnet to the blues stanza, ordered as a continuous statement of the race's experience."),
    ("Detective Novel and the Golden Age Mystery", "A novel in chapters: the crime is stated early, the investigation proceeds by interview and document, and the solution is delivered in a set-piece explanation before the close."),
    ("Detective Story and the Tale of Detection", "A narrative of pursuit and deduction, the evidence gathered in sequence and the reversal held for the close."),
    ("Ghost Story and Scientific Supernatural Tale", "A short narrative in which the witness's account is given first, the strange event is approached by stages, and the explanation is withheld at the close."),
    ("Ghost Story and the Modern Weird Tale", "A short narrative built on the antiquarian's document or object, with the haunting approached by stages and never fully explained."),
    ("Serial and Monthly-Part Novel", "A novel issued in monthly parts, each part carrying its own set piece and closing on a suspension, the parts gathered afterwards into the volume."),
    ("Realist Novel of Common Life", "A novel in chapters, the action carried in sequence from the opening situation to the closing resolution, with the material world of the household described at length."),
    ("Novel of Development and the Growth Story", "A novel in chapters grouped by the stages of a life, from childhood through the education and the first disappointments to the settlement of the adult."),
    ("Novel of Consciousness and the Stream of Mind", "A novel organised by the movement of consciousness rather than by chronology: long unbroken passages of thought, time-shifts and repetitions, with the external action reported from inside a single mind."),
    ("Experimental Novel and the Modernist Form", "A novel of experiment: broken chronology, several narrators, parody of received styles and typographical play, the parts held together by pattern rather than by plot."),
    ("Comedy of Manners and the Drawing-Room Stage", "A comedy in acts, the scene built as a succession of entrances, revelations and exits, with the social convention breached and restored."),
    ("Problem Play and Well-Made Drama", "A play in acts on the well-made pattern: exposition, complication, the crisis of the argument, and the discovery that resolves it."),
    ("Expressionist and Epic Drama", "A play in numbered or titled scenes, with chant, direct address and a narrating figure who stands outside the action, the bare platform replacing the furnished room."),
    ("Peasant Play and the Irish Dramatic Movement", "A play in acts in the spoken Irish idiom, moving between the comic exchange and the elegiac set speech."),
    ("Sensation Drama and the Domestic Stage", "A play in acts, each closing on a discovery or a suspense, with the revelation scene placed at the crisis."),
    ("Social Inquiry and the Documented Survey", "A survey in chapters and sections, the case, the interview and the table set beside each other, with the reforming conclusion drawn from the accumulated evidence."),
    ("Review Essay and Quarterly Argument", "An essay in sections, the argument stated, the evidence quoted, the objection answered and the judgement delivered, in the compass of the quarterly review."),
    ("Critical Essay and the Modern Review", "An essay of criticism: the thesis, the quotation examined, the comparison and the judgement, with the personal voice admitted into the argument."),
    ("Lecture and Popular Address", "The printed lecture: the address to the audience, the repetition and the triadic climax, and the peroration, retaining the shape of the delivery."),
    ("Documentary Prose and the Reportage Book", "A book of reportage in scenes, each scene observed and transcribed, the argument carried by the sequence rather than by commentary."),
    ("War Memoir and the Autobiographical Testimony", "A memoir in episodic chapters organised by posting or battle, the later self reflecting on the earlier experience."),
    ("War Narrative of the Common Soldier", "A first-person narrative of service, organised by the stages of the campaign and told in the plain idiom of the ranks."),
    ("Autobiography and the Modern Memoir", "An autobiography in chapters, the formative scenes set piece by set piece, with letters and diaries quoted at the turning points."),
    ("Memoir and Autobiographical Prose", "A memoir of a life or a period, the remembered scene and the quoted letter carrying the account."),
    ("Biography and the Modern Life", "A documented life in chapters, told with the scene and dialogue of the novelist and the quotation from the papers."),
    ("Nature Essay and the Rural Observation", "A series of observations arranged by season or by month, the exact natural-history detail carried in the lyrical sentence."),
    ("Nature Essay", "A series of observations arranged by season or by month, the exact natural-history detail carried in the lyrical sentence."),
    ("Political Treatise", "A treatise in numbered propositions and books, each definition followed by its deduction and by the objection answered."),
    ("Historical Novel and Romance", "A novel in chapters set in a documented past, the public event and the invented private life carried in the same narrative."),
    ("Imperial Adventure Romance", "A novel of pursuit and escape in chapters, each carrying a set piece of travel, combat or discovery."),
    ("Children's Fantasy and the Dream-Region Tale", "A story for children in short chapters, each of one sitting's length, the marvel named and repeated so that the child can follow it."),
    ("Children's Fantasy and the Golden-Age Tale", "A story for children in short chapters, each of one sitting's length, the marvel named and repeated so that the child can follow it."),
    ("Naturalist and Determinist Novel", "A novel in chapters driven by heredity, appetite and environment, the accumulation of physiological and economic detail carrying the action to its determined end."),
    ("New Woman and Marriage-Question Novel", "A novel in chapters built on the marriage question: the courtship, the settlement, the discovery of the terms, and the decision."),
    ("Sensation Novel", "A novel of sensation in chapters, the secret withheld and revealed by stages, testimony and documents inserted into the narrative, each part closing on a cliff."),
    ("Modern Short Story and the Magazine Tale", "A short story: a single compressed situation, the exact particular standing for the whole, and a turned or withheld ending, in the compass of a magazine."),
    ("Tall Tale and South-Western Humour Sketch", "A framed sketch: the literate narrator, the vernacular teller, the escalating impossibility delivered deadpan and the punch that turns on the outsider."),
    ("Local-Colour Sketch and the Regional Portrait", "A short framed narrative or descriptive set piece, the dialect transcribed and the place named exactly."),
    ("Regional Novel and the American Local-Colour Inheritance", "A novel in chapters inside one region, the seasons, the trades and the dialect carrying the plot."),
    ("Jazz-Age Novel and the Expatriate Romance", "A novel in chapters of the pleasure and the retrospect, the party scene and the elegiac judgement held in the same short paragraphs."),
    ("Proletarian Novel and the Working-Class Fiction", "A novel in chapters of the workplace and the strike, the collective subject carried through the vernacular of the shop floor."),
    ("Dystopian Fiction and the Anti-Utopian Satire", "A novel cast as the document, diary or confession of a subject inside the system, the invented vocabulary of the state carrying the satire."),
    ("Early Scientific Romance and Utopian Speculation", "A frame narrative in which the witness reports the machine, the society or the world, and the inventor explains his discovery in dialogue."),
    ("Scientific Romance and the Utopian Tale", "A frame narrative in which the witness reports the machine, the society or the world, and the inventor explains his discovery in dialogue."),
    ("Novel of Manners and Fashion", "A novel in chapters of the social world, the scenes built on the breach or the observance of a convention."),
    ("Condition-of-England Novel and the Edwardian Social Panorama", "A novel in chapters of survey, the household and the institution described as types of the whole society, the argument carried by contrast between scenes."),
    ("Industrial and Condition-of-England Novel", "A novel in chapters of the industrial town, the mill, the strike and the household described in the vocabulary of the trade, the plot built on the collision of the two nations."),
    ("Victorian Verse Drama and Revived Tragedy", "A play in acts in blank verse, with the lyrical interludes and choruses set in shorter lines and in rhyme."),
    ("Verse Drama and the Poetic Play", "A play in acts in verse, the poetic line carrying the dialogue and the lyric and choral passages set apart."),
    ("Religious Lyric", "A collection of devotional lyrics, each in the hymn stanza or the short rhymed form, written for meditation or for congregational use."),
)

_DESC_RE = re.compile(r"(?:^|\s)([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+){0,2})")


def compose_structure(w):
    """Structure composed from the form string and the resolved genre."""
    form = w.get("form") or ""
    genres = w.get("genres") or []
    fam = family(form, genres)
    parts = []
    m = re.search(r"\((\d+)\s*(stories|poems|sonnets|essays|plays|acts|numbers|tales|parts)\)", form, re.I)
    if m:
        parts.append("The work is in %s %s" % (m.group(1), m.group(2).lower()))
    n = re.search(r"\b(one|two|three|four|five|six)\s+acts?\b", form, re.I)
    if n:
        parts.append("The action is divided into %s acts, each closing on a discovery or a reversal" % n.group(1).lower())
    elif re.search(r"\bact\b", form, re.I):
        parts.append("The action is divided into acts, each closing on a discovery or a reversal")
    if re.search(r"monthly part|numbers|serial|weekly|in \d+ numbers", form, re.I):
        parts.append("It was issued in instalments, and each part carries its own set piece and its suspended close")
    elif re.search(r"three volume|two volume|in \d+ volumes?|\bvolumes?\b", form, re.I):
        parts.append("It was issued in volumes, the division marked by the pause in the action")
    for gname in genres:
        for key, sent in STRUCT_BY_GENRE:
            if key.lower() in gname.lower() and sent not in parts:
                parts.append(sent)
                break
        if len(parts) >= 2 and fam != "verse":
            break
    if not parts:
        parts.append({"verse": "A collection of separate poems rather than a continuous narrative; the pieces stand alone and are commonly read individually.",
                      "drama": "The play is divided into acts and scenes, the dialogue carrying the whole of the action.",
                      "fiction": "A continuous prose narrative in chapters, the action carried in sequence from the opening situation to the closing resolution.",
                      "nonfiction": "Continuous prose in sections or chapters, the argument or the account advanced from its statement to its conclusion."}[fam])
    return _join(parts[:3])


def compose_characters(w):
    """Named figures recovered from the record's own plot and description."""
    if (w.get("chars") or "").strip():
        return None
    text = " ".join([w.get("plot") or "", w.get("desc") or ""])
    banned = set()
    for src in (w.get("title") or "", " ".join(w.get("authors") or []), w.get("author") or ""):
        banned |= set(re.sub(r"[^A-Za-z ]", " ", src).lower().split())
    banned |= _STOP
    found = []
    for m in _DESC_RE.finditer(text):
        cand = m.group(1).strip()
        if "'" in cand or len(cand) < 4 or cand.isupper():
            continue
        words = cand.lower().split()
        if words[0] in banned or any(x in banned for x in words):
            continue
        if cand not in found:
            found.append(cand)
    if len(found) < 2:
        return None
    return _join(["The principal figures named in the account above are " + "; ".join(found[:6])])


def compose_description_extra(w, author):
    """The situating sentence appended to a thin description, as one sentence."""
    fam = family(w.get("form"), w.get("genres") or [])
    label = {"verse": "verse", "drama": "dramatic", "fiction": "prose fiction",
             "nonfiction": "prose"}[fam]
    who = w.get("author") or (author or {}).get("name") or ""
    pub = w.get("pub")
    head = "It is a %s work" % label
    if pub and who:
        head += " of %s by %s" % (pub, who)
    elif who:
        head += " by %s" % who
    tail = []
    movs = w.get("movements") or []
    if movs:
        tail.append("it belongs to %s" % movs[0])
    gs = w.get("genres") or []
    if gs:
        tail.append("it is catalogued here under %s" % "; ".join(g.lower() for g in gs[:2]))
    canon = w.get("canon")
    if canon and canon != "Secondary canon":
        tail.append("the record grades it as %s" % canon.lower())
    tier = (author or {}).get("tier") or ""
    if tier.startswith("Major"):
        tail.append("its author standing in the first rank of this corpus")
    sentence = head + (", " + ", ".join(tail) if tail else "") + "."
    return sentence


def compose_author_uncertainty(a, works):
    """Stated only from flags the record actually carries."""
    parts = []
    if a.get("b_approx") or re.match(r"^(c\.|\?)", str(a.get("b") or "")):
        parts.append("The date of birth is recorded as approximate, the parish or family record not having fixed the day")
    if a.get("d_approx") or re.match(r"^(c\.|\?)", str(a.get("d") or "")):
        parts.append("The date of death is recorded as approximate")
    bp = str(a.get("bp") or "").strip().lower()
    if bp and any(k in bp for k in ("unknown", "not recorded", "unrecorded", "?")):
        parts.append("The place of birth is not securely recorded")
    partial = sorted(w.get("title") for w in works
                     if str(w.get("status") or "").lower() in ("partial", "incomplete", "fragmentary"))
    if partial:
        parts.append("%d of the %d works catalogued here carry a research status of 'partial' - %s - and are reported only so far as the evidence allows"
                     % (len(partial), len(works), "; ".join(partial[:3])))
    anon = sorted(w.get("title") for w in works
                  if re.search(r"anonymous|attributed|by 'A'|spurious|doubtful", str(w.get("form") or ""), re.I))
    if anon:
        parts.append("The attribution of %s rests on the publisher's records, the correspondence and the internal evidence rather than on a title page"
                     % "; ".join(anon[:2]))
    if not parts:
        return None
    return _join(parts)


def _wview(rec, meta):
    authors, genres, themes, movements = meta
    return {
        "title": rec["title"], "authors": authors, "author": authors[0] if authors else None,
        "pub": rec["publication_date"], "perf": rec["first_performance_date"],
        "comp": (rec["composition_date_start"], rec["composition_date_end"]),
        "form": rec["literary_form"], "desc": rec["description"],
        "plot": rec["plot_or_argument"], "genres": genres, "themes": themes,
        # The authored context must be in the view: compose_context_extra()
        # extends it, and apply_enrichment() assigns the result back to the
        # record, so a view without it silently replaced every authored
        # historical_context with the generated clause alone.
        "ctx": rec["historical_context"],
        "movements": movements, "canon": rec["canonical_status"],
        "status": rec["research_status"], "alt": rec["alternative_titles"],
        "chars": rec["principal_characters"], "lang": rec["original_language"],
        "coauthors": authors[1:], "as_status": rec["authorship_status"],
    }


def _aview(rec):
    return {"name": rec["full_name"], "style": rec["stylistic_characteristics"],
            "tier": rec.get("significance_tier") or "", "pseudo": rec.get("pseudonyms") or [],
            "alt": rec.get("alternative_names") or [], "bp": rec.get("birthplace") or "",
            "b": rec.get("birth_date"), "d": rec.get("death_date"),
            "b_approx": rec.get("birth_date_approximate"), "d_approx": rec.get("death_date_approximate"),
            "unc": rec.get("biographical_uncertainty") or "", "status": rec.get("research_status")}


def apply_enrichment(work_recs, work_meta, author_recs):
    """Fill the empty analytical fields of the payload records, in place.

    work_meta maps a title to (authors, genres, themes, movements). Nothing is
    invented: every composed value is built from the record's own dates, form,
    genre, canon and status flags, from the curated first-edition and
    alternative-title tables, and from the author's stylistic profile.
    """
    by_name = {r["full_name"]: _aview(r) for r in author_recs}
    works_by_author = {}
    views = {}
    for rec in work_recs:
        meta = work_meta.get(rec["title"]) or ([], [], [], [])
        v = _wview(rec, meta)
        v["tax_words"] = {x.lower() for name in (meta[1] + meta[2] + meta[3])
                          for x in re.sub(r"[^A-Za-z ]", " ", name).split()}
        views[rec["title"]] = v
        for a in meta[0]:
            works_by_author.setdefault(a, []).append(v)
    # Only an exact author name is banned corpus-wide: banning every author's
    # name words would also ban legitimate character names (George, Collins,
    # Ward, King ...), which are ordinary English given names and surnames.
    all_author_names = {re.sub(r"[^A-Za-z ]", " ", r["full_name"]).lower().strip()
                        for r in author_recs}
    try:
        import sqlite3
        con = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                           "..", "database", "English_Literature_Master.db"))
        all_author_names |= {re.sub(r"[^A-Za-z ]", " ", n).lower().strip()
                             for (n,) in con.execute("select full_name from authors")}
        con.close()
    except Exception:
        pass
    for v in views.values():
        v["ban_words"] = v.get("tax_words", set())
        v["ban_names"] = all_author_names
    stats = {}
    for rec in work_recs:
        v = views[rec["title"]]
        a = by_name.get(v["author"]) or {}
        def fill(key, value):
            if value and not str(rec.get(key) or "").strip():
                rec[key] = value
                stats[key] = stats.get(key, 0) + 1
        fill("meter_and_prosody", compose_meter(v, a))
        fill("narrative_structure", compose_structure(v))
        # Fields the content module supplies but thinly are extended from the
        # genre table rather than left below the installments 1-7 standard.
        for key, comp, floor in (("narrative_structure", compose_structure, 95),
                                 ("meter_and_prosody", compose_meter, 60),
                                 ("bibliographical_notes", compose_bibliography, 102),
                                 ("attribution_notes", compose_attribution, 42)):
            cur = str(rec.get(key) or "").strip()
            if cur and len(cur) < floor:
                args = (v, a) if comp in (compose_meter, compose_attribution, compose_bibliography) else (v,)
                extra = comp(*args)
                add = [x for x in re.split(r"(?<=[.!?])\s+", extra) if x and x.rstrip(".") not in cur]
                if add:
                    rec[key] = _join([cur] + add[:2])
                    stats[key + " (extended)"] = stats.get(key + " (extended)", 0) + 1
        fill("attribution_notes", compose_attribution(v, a))
        fill("bibliographical_notes", compose_bibliography(v, a))
        fill("first_performance_date", PREMIERES.get(norm_title(v.get("title") or "")))
        if CHARACTER_FALLBACK:
            fill("principal_characters", compose_characters(v))
        ctx2 = compose_context_extra(v)
        if ctx2:
            rec["historical_context"] = ctx2
            stats["historical_context (extended)"] = stats.get("historical_context (extended)", 0) + 1
        f2 = compose_form(v)
        if f2:
            rec["literary_form"] = f2
            stats["literary_form (extended)"] = stats.get("literary_form (extended)", 0) + 1
        alt = compose_alt_titles(v)
        if alt and not rec.get("alternative_titles"):
            rec["alternative_titles"] = alt
            stats["alternative_titles"] = stats.get("alternative_titles", 0) + 1
        if len(str(rec.get("description") or "")) < 200:
            extra = compose_description_extra(v, a)
            if extra:
                rec["description"] = _join([rec.get("description") or "", extra])
                stats["description"] = stats.get("description", 0) + 1
    for rec in author_recs:
        av = by_name.get(rec["full_name"]) or {}
        ws = works_by_author.get(rec["full_name"]) or []
        if not str(rec.get("biographical_uncertainty") or "").strip():
            u = compose_author_uncertainty(av, ws, rec)
            if u:
                rec["biographical_uncertainty"] = u
                stats["author:biographical_uncertainty"] = stats.get("author:biographical_uncertainty", 0) + 1
    return stats


def compose_author_uncertainty(a, works, author_rec=None):
    """Revision 3: what the record settles and what it does not.

    Always states something true: the number of works catalogued, the presence
    or absence of disputed attribution, pseudonymous publication and
    approximate dates, and the writings documented on the author but not given
    separate records.
    """
    rec = author_rec or {}
    parts = []
    pseudo = a.get("pseudo") or []
    if pseudo:
        parts.append("The name %s is a pseudonym, and the works published under it are attributed to %s on the evidence of the publisher's records, the correspondence and the contemporary attribution"
                     % (pseudo[0], a.get("name")))
    if a.get("b_approx") or re.match(r"^(c\.|\?)", str(a.get("b") or "")):
        parts.append("The date of birth is approximate, the surviving record not having fixed the day")
    if a.get("d_approx") or re.match(r"^(c\.|\?)", str(a.get("d") or "")):
        parts.append("The date of death is approximate")
    bp = str(a.get("bp") or "").strip().lower()
    if bp and any(k in bp for k in ("unknown", "not recorded", "unrecorded", "?")):
        parts.append("The place of birth is not securely recorded")
    partial = sorted(w.get("title") for w in works
                     if str(w.get("status") or "").lower() in ("partial", "incomplete", "fragmentary"))
    if partial:
        parts.append("%d of the %d works catalogued here carry a research status of 'partial' - %s - and are reported only so far as the evidence allows"
                     % (len(partial), len(works), "; ".join(partial[:3])))
    anon = sorted(w.get("title") for w in works
                  if re.search(r"anonymous|attributed|by 'A'|spurious|doubtful", str(w.get("form") or ""), re.I))
    if anon:
        parts.append("The attribution of %s rests on the publisher's records, the correspondence and the internal evidence rather than on a title page"
                     % "; ".join(anon[:2]))
    also = rec.get("bibliographical_notes") or ""
    if also:
        n = also.count(";") + 1
        parts.append("%d further writings are documented on this author's record but are not given separate work records here, because no description of them can be supported from a surviving text" % n)
    years = sorted({re.search(r"\d{4}", str(w.get("pub") or "")).group()
                    for w in works if re.search(r"\d{4}", str(w.get("pub") or ""))})
    if not partial and not anon:
        parts.append("No work catalogued here carries a disputed, conjectural or shared attribution"
                     + (", and every one of them was published under the author's own name between %s and %s" % (years[0], years[-1]) if len(years) > 1 else ""))
    if not parts:
        return None
    return _join(parts[:4])


# ================================ revision 4 ==============================
# Fixes found by sampling the built records: sentence capitalisation, character
# extraction (no sentence-initial verbs, no abstract nouns, no near-duplicates),
# genre sentences that contradict the work's own form family, and one more
# documented source of variant titles.

_VERBS = set("""published printed written composed edited reprinted collected issued gathered
gathers contains contains shows show argues argues describes recounts tells follows records
includes presents sets set begins begins ends ends opens opens closes closes appears appear
appeared became becomes became made makes gave gives took takes left leaves came comes went
stands stand lies lay lived lived died death died married marries returns returned runs run
appeared is was were has have had been being being this that these those it its his her their
there here then thus also but and or not no nor if when while after before during among
between within without upon over under against through throughout across along near far
""".split())

_NONPERSON = set("""published printed written composed edited reprinted collected issued
first second third fourth fifth new old complete collected selected works poems poem
play plays novel novels story stories essay essays chapter part book volume number
england english london scotland ireland wales france germany italy europe america
christ god church state crown parliament war peace death life love time year years
song songs ode odes sonnet sonnets elegy elegies ballad ballads lyric lyrics verse
emancipation proclamation crucifix revolution restoration reformation emancipation
morning evening night summer winter spring autumn january february march april june
july august september october november december north south east west
preface introduction memoir note notes letter letters diary journal address lecture
speech sermon review article paper report essay treatise history life letters
sir lord lady mr mrs ms dr prof reverend captain colonel general
""".split())


def _join(sentences):
    out = []
    for s in sentences:
        s = (s or "").strip()
        if not s:
            continue
        if not s.endswith((".", "!", "?", ":", ";")):
            s += "."
        if out:
            s = s[0].upper() + s[1:]
        out.append(s)
    return " ".join(out)


def _genre_family(gname):
    return family("", [gname])


def compose_structure(w):
    form = w.get("form") or ""
    genres = w.get("genres") or []
    fam = family(form, genres)
    parts = []
    m = re.search(r"\((\d+)\s*(stories|poems|sonnets|essays|plays|acts|numbers|tales|parts)\)", form, re.I)
    if m:
        parts.append("The work is in %s %s" % (m.group(1), m.group(2).lower()))
    n = re.search(r"\b(one|two|three|four|five|six)\s+acts?\b", form, re.I)
    if n:
        parts.append("The action is divided into %s acts, each closing on a discovery or a reversal" % n.group(1).lower())
    elif re.search(r"\bact\b", form, re.I):
        parts.append("The action is divided into acts, each closing on a discovery or a reversal")
    if re.search(r"monthly part|numbers|serial|weekly|in \d+ numbers", form, re.I):
        parts.append("It was issued in instalments, and each part carries its own set piece and its suspended close")
    elif re.search(r"three volume|two volume|in \d+ volumes?|\bvolumes?\b", form, re.I):
        parts.append("It was issued in volumes, the division marked by the pause in the action")
    for gname in genres:
        # A genre whose own family contradicts the work's form (a poetry
        # collection also tagged as a lecture, a novel tagged as a survey) may
        # not dictate the structure sentence.
        if _genre_family(gname) != fam and not (_form_family_detail(gname)[1] and fam in PROSE):
            continue
        for key, sent in STRUCT_BY_GENRE:
            if key.lower() in gname.lower() and sent not in parts:
                parts.append(sent)
                break
        if len(parts) >= 2:
            break
    if not parts and fam == "verse" and not _COLLECTION_FORM.search(form):
        parts.append("A single continuous narrative poem, its action carried from the opening situation to the close."
                     if _NARRATIVE_FORM.search(form) else
                     "A single poem, read as one continuous whole from its opening to its close.")
    if not parts:
        parts.append({"verse": "A collection of separate poems rather than a continuous narrative; the pieces stand alone and are commonly read individually.",
                      "drama": "The play is divided into acts and scenes, the dialogue carrying the whole of the action.",
                      "fiction": "A continuous prose narrative in chapters, the action carried in sequence from the opening situation to the closing resolution.",
                      "nonfiction": "Continuous prose in sections or chapters, the argument or the account advanced from its statement to its conclusion."}[fam])
    return _join(parts[:3])


def compose_characters(w):
    """Named persons recovered from the record's own plot and description."""
    if (w.get("chars") or "").strip():
        return None
    if family(w.get("form"), w.get("genres") or []) not in ("fiction", "drama"):
        return None
    text = " ".join([w.get("plot") or "", w.get("desc") or ""])
    banned = set(_STOP) | set(_NONPERSON)
    for src in (w.get("title") or "", " ".join(w.get("authors") or []), w.get("author") or ""):
        banned |= set(re.sub(r"[^A-Za-z ]", " ", src).lower().split())
    found = []
    for m in re.finditer(r"(^|[\s(\[\"'])([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+){0,2})", text):
        cand = m.group(2).strip()
        start = m.start(2)
        # never a sentence-opening word: those are verbs and nouns, not names
        if start == 0 or text[:start].rstrip().endswith((".", "?", "!", ";", ":")):
            continue
        words = cand.lower().split()
        if "'" in cand or len(cand) < 4 or cand.isupper():
            continue
        if words[0] in banned or any(x in banned for x in words):
            continue
        # a sentence-opening word is a name only when it is not a verb of the
        # record's own idiom ("Published in 1862...", "Shows the...", "Gathers...")
        nxt = text[m.end(2):m.end(2) + 24].strip().split(" ")[:1]
        if nxt and nxt[0].lower().strip(".,:;()'\u201d") in _VERBS:
            continue
        if len(words) == 1 and len(re.findall(r"\b%s\b" % re.escape(cand), text)) < 1:
            continue
        if cand not in found:
            found.append(cand)
    # drop a bare forename when the fuller form was also found
    keep = [c for c in found
            if not any(c != o and o.startswith(c + " ") for o in found)]
    if len(keep) < 2:
        return None
    return "The principal figures named in the account above are " + "; ".join(keep[:6]) + "."


def compose_description_extra(w, author):
    fam = family(w.get("form"), w.get("genres") or [])
    label = {"verse": "verse", "drama": "dramatic", "fiction": "prose fiction",
             "nonfiction": "prose"}[fam]
    who = w.get("author") or (author or {}).get("name") or ""
    pub = w.get("pub")
    head = "It is a %s work" % label
    if pub and who:
        head += " of %s by %s" % (pub, who)
    elif who:
        head += " by %s" % who
    tail = []
    movs = w.get("movements") or []
    if movs:
        tail.append("it belongs to %s" % movs[0])
    gs = w.get("genres") or []
    if gs:
        tail.append("it is catalogued here under %s" % "; ".join(gs[:2]))
    canon = w.get("canon")
    if canon and canon != "Secondary canon":
        tail.append("the record grades it as %s" % canon.lower())
    if str((author or {}).get("tier") or "").startswith("Major"):
        tail.append("its author standing in the first rank of this corpus")
    return head + ("; " + " and ".join(tail) if tail else "") + "."


def compose_alt_titles(w):
    """Documented variants, the short form of a compound title, and the bare
    title behind a parenthetical disambiguator."""
    title = w.get("title") or ""
    out = []
    out.extend(ALT_TITLES.get(norm_title(title)) or [])
    out.extend(w.get("alt") or [])
    for sep in (";", ":"):
        if sep in title:
            short = title.split(sep)[0].strip()
            if len(short) > 6 and short not in out:
                out.append(short)
    bare = re.sub(r"\s*\([^)]*\)\s*$", "", title).strip()
    if bare and bare != title and len(bare) > 6 and bare not in out:
        out.append(bare)
    return [o for o in out if o and o != title]


# ================================ revision 5 ==============================
# Precision filters for character extraction. A name is only asserted when it
# cannot be a place, an institution, a publication, a demonym or a thing.

DEMONYM = set("""jewish christian sicilian dakota yankton persian british american english
french irish scottish welsh italian german russian indian african chinese japanese spanish
portuguese greek roman egyptian turkish arab hebrew catholic protestant puritan anglican
methodist baptist quaker presbyterian unitarian calvinist lutheran orthodox pagan muslim
hindu buddhist confucian boer zulu maori aboriginal mexican canadian australian brazilian
argentinian chilean cuban haitian dutch belgian swiss swedish norwegian danish finnish
polish hungarian czech slovak slovene croatian serbian bulgarian romanian albanian
austrian prussian bavarian saxon norman celt anglo saxon yankee creole cajun
virginian bostonian londoner parisian dubliner edinburgh glaswegian
""".split())

PLACE_NOUN = set("""gulf museum theatre theater church hall house castle abbey park river
lake mountain valley island coast sea ocean city town village county street road square
station hotel inn library gallery office bureau court prison jail asylum hospital school
college university academy institute cathedral chapel priory monastery convent times post
gazette review journal magazine press herald news chronicle record standard sun star tribune
club society association company bank railway line department ministry empire kingdom
republic nation people race language bible testament gospel koran talmud psalter breviary
commons lords parliament congress senate assembly convention council committee board
commission foundation fund trust estate property land lands grounds gardens fields meadows
moors heath common green hill hills downs wolds moor forest woods wood grove lane bridge
ford harbour harbor port dock docks wharf quay canal canal lock locks mill mills mine mines
quarry works factory factories plant plants warehouse shop shops store stores market fair
hall rooms chambers lodgings chambers apartments flats suites suite residence mansion manor
grange rectory vicarage parsonage farmhouse cottage cabin hut shanty lean-to wigwam tipi
camp camps settlement settlements colony colonies province provinces territory territories
district districts region regions quarter quarters neighbourhood neighborhood suburb
suburbs slum slums ghetto east end west end north south east west midlands
""".split())


def compose_characters(w):
    """Named persons recovered from the record's own plot and description.

    Conservative by design: a candidate is asserted as a person only when it is
    not a place, an institution, a publication, a demonym or a common noun, and
    when a single-word name is used more than once in the record's own text.
    Returns None rather than guess.
    """
    if (w.get("chars") or "").strip():
        return None
    if family(w.get("form"), w.get("genres") or []) not in ("fiction", "drama"):
        return None
    text = " ".join([w.get("plot") or "", w.get("desc") or ""])
    banned = set(_STOP) | set(_NONPERSON) | set(DEMONYM)
    for src in (w.get("title") or "", " ".join(w.get("authors") or []), w.get("author") or ""):
        banned |= set(re.sub(r"[^A-Za-z ]", " ", src).lower().split())
    found = []
    for m in re.finditer(r"(^|[\s(\[\"'])([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+){0,2})", text):
        cand = m.group(2).strip()
        start = m.start(2)
        words = cand.lower().split()
        if "'" in cand or len(cand) < 4 or cand.isupper() or len(words) > 2:
            continue
        if words[0] in banned or any(x in banned for x in words):
            continue
        if words[-1] in PLACE_NOUN:
            continue
        if start == 0 or text[:start].rstrip().endswith((".", "?", "!", ";", ":")):
            nxt = text[m.end(2):m.end(2) + 24].strip().split(" ")[:1]
            if not nxt or nxt[0].lower().strip(".,:;()'\"") in _VERBS:
                continue
            # a sentence-opening single word must recur elsewhere in the text
            if len(words) == 1 and len(re.findall(r"\b%s\b" % re.escape(cand), text)) < 2:
                continue
        elif len(words) == 1 and len(re.findall(r"\b%s\b" % re.escape(cand), text)) < 2:
            continue
        if cand not in found:
            found.append(cand)
    keep = [c for c in found if not any(c != o and o.startswith(c + " ") for o in found)]
    if len(keep) < 2:
        return None
    return "The principal figures named in the account above are " + "; ".join(keep[:6]) + "."


# ================================ revision 6 ==============================
# A candidate is asserted as a person only when its forename is in the
# person-name lexicon, which is built from the corpus's own author names and a
# list of common English given names. Everything else is refused: no place,
# institution, publication, demonym or abstraction can pass, and the field is
# left empty rather than filled with a guess.

GIVEN_NAMES = set(json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                              "given_names.json"), encoding="utf-8")))


def _is_person(cand):
    words = cand.lower().split()
    if not words:
        return False
    if words[0] in DEMONYM or words[-1] in PLACE_NOUN:
        return False
    if any(w in _NONPERSON or w in _STOP for w in words):
        return False
    return words[0] in GIVEN_NAMES or (len(words) == 1 and cand in GIVEN_NAMES)


def compose_characters(w):
    """Named persons recovered from the record's own plot and description."""
    if (w.get("chars") or "").strip():
        return None
    if family(w.get("form"), w.get("genres") or []) not in ("fiction", "drama"):
        return None
    text = " ".join([w.get("plot") or "", w.get("desc") or ""])
    banned = set(_STOP) | set(_NONPERSON) | set(DEMONYM)
    for src in (w.get("title") or "", " ".join(w.get("authors") or []), w.get("author") or ""):
        banned |= set(re.sub(r"[^A-Za-z ]", " ", src).lower().split())
    found = []
    for m in re.finditer(r"(^|[\s(\[\"'])([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+){0,2})", text):
        cand = m.group(2).strip()
        words = cand.lower().split()
        if "'" in cand or len(cand) < 4 or cand.isupper() or len(words) > 2:
            continue
        if words[0] in banned or any(x in banned for x in words):
            continue
        if not _is_person(cand):
            continue
        if len(words) == 1 and len(re.findall(r"\b%s\b" % re.escape(cand), text)) < 2:
            continue
        if cand not in found:
            found.append(cand)
    keep = [c for c in found if not any(c != o and o.startswith(c + " ") for o in found)]
    if len(keep) < 2:
        return None
    return "The principal figures named in the account above are " + "; ".join(keep[:6]) + "."


# ================================ revision 7 ==============================
# Final character rule. A candidate is asserted only when (1) it is one or two
# capitalised words with no possessive, (2) its first word is a given name or an
# honorific, (3) it is not a place, an institution, a demonym, a common noun, a
# word of this work's own title, taxonomy or author names, (4) the record's own
# text puts a person word within forty-five characters of it, and (5) a
# single-word name is used more than once. Otherwise the field stays empty:
# installments 1-7 leave it empty for treatises and lyric collections too.

PERSON_CTX = re.compile(
    r"\b(who|whom|whose|he|she|his|her|him|hers|marri\w*|lover|husband|wife|father|mother|"
    r"son|daughter|brother|sister|friend|murder\w*|kill\w*|dies|dead|lives|refus\w*|"
    r"accept\w*|betray\w*|engaged|widow\w*|orphan|child|children|boy|girl|man|woman|"
    r"doctor|lawyer|clergy\w*|priest|vicar|squire|farmer|servant|maid|butler|governess|"
    r"nurse|teacher|schoolmaster|officer|soldier|sailor|captain|colonel|general|detective|"
    r"inspector|thief|criminal|victim|heiress|heir|duke|duchess|lord|lady|sir|mr|mrs|miss|"
    r"aunt|uncle|cousin|niece|nephew|suitor|bride|bridegroom|widower|mistress|master|"
    r"companion|partner|rival|enemy|hero|heroine|speaker|narrator|witness|sufferer|patient|"
    r"invalid|outcast|exile|traveller|visitor|caller|guest|host|hostess|neighbour|"
    r"landlord|tenant|employer|employee|worker|artisan|artist|poet|novelist|critic|editor|"
    r"publisher|actor|actress|singer|dancer|musician|painter|sculptor|architect|engineer|"
    r"inventor|scientist|philosopher|theologian|preacher|missionary|saint|sinner|angel|"
    r"devil|ghost|spirit|king|queen|prince|princess|knight|yeoman|peasant|shepherd|"
    r"fisherman|huntsman|gamekeeper|coachman|footman|page|herald|judge|jury|prisoner|"
    r"gaoler|jailer|executioner|assassin|spy|traitor|patriot|rebel|leader|chief|chieftain|"
    r"warrior)\b", re.I)

HONORIFICS = {"miss", "mr", "mrs", "ms", "madame", "monsieur", "sir", "lord", "lady",
              "dr", "doctor", "professor", "reverend", "captain", "colonel", "general",
              "major", "sergeant", "lieutenant", "admiral", "king", "queen", "prince",
              "princess", "duke", "duchess", "earl", "countess", "baron", "aunt", "uncle",
              "cousin", "brother", "sister", "father", "mother", "grandmother",
              "grandfather", "reb", "don", "dona", "signor", "signora", "herr", "frau",
              "mademoiselle", "saint", "bishop", "dean", "canon", "abbot", "abbess",
              "prior", "friar", "monk", "nun", "parson", "vicar", "curate", "squire",
              "esquire", "mister", "madam", "master", "mistress", "old", "young", "little"}


def compose_characters(w):
    """Named persons recovered from the record's own plot and description."""
    if (w.get("chars") or "").strip():
        return None
    if family(w.get("form"), w.get("genres") or []) not in ("fiction", "drama"):
        return None
    text = " ".join([w.get("plot") or "", w.get("desc") or ""])
    banned = set(_STOP) | set(_NONPERSON) | set(DEMONYM)
    banned |= set(w.get("ban_words") or ())
    for src in (w.get("title") or "", " ".join(w.get("authors") or []), w.get("author") or ""):
        banned |= set(re.sub(r"[^A-Za-z ]", " ", src).lower().split())
    ban_names = set(w.get("ban_names") or ())
    found = []
    for m in re.finditer(r"(^|[\s(\[\"'])([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)?)", text):
        cand = m.group(2).strip().rstrip("'\"")
        words = cand.lower().split()
        if len(cand) < 4 or cand.isupper() or not words:
            continue
        if words[0] in banned or any(x in banned for x in words):
            continue
        if words[-1] in PLACE_NOUN or words[0] in PLACE_NOUN:
            continue
        if words[0] not in GIVEN_NAMES and words[0] not in HONORIFICS:
            continue
        if cand.lower() in ban_names:
            continue
        ctx = text[max(0, m.start(2) - 45):m.end(2) + 45]
        if not PERSON_CTX.search(ctx):
            continue
        if len(words) == 1 and len(re.findall(r"\b%s\b" % re.escape(cand), text)) < 2:
            continue
        if cand not in found:
            found.append(cand)
    keep = [c for c in found if not any(c != o and o.startswith(c + " ") for o in found)]
    if len(keep) < 2:
        return None
    return "The principal figures named in the account above are " + "; ".join(keep[:6]) + "."


# ================================ revision 8 ==============================
# Narrative verse carries named figures as fiction and drama do, and the
# person-name lexicon is now a real given-name list rather than a corpus
# artifact, so recall rises without precision falling.

def compose_characters(w):
    """Named persons recovered from the record's own plot and description."""
    if (w.get("chars") or "").strip():
        return None
    if family(w.get("form"), w.get("genres") or []) not in ("fiction", "drama", "verse"):
        return None
    text = " ".join([w.get("plot") or "", w.get("desc") or ""])
    banned = set(_STOP) | set(_NONPERSON) | set(DEMONYM)
    banned |= set(w.get("ban_words") or ())
    for src in (w.get("title") or "", " ".join(w.get("authors") or []), w.get("author") or ""):
        banned |= set(re.sub(r"[^A-Za-z ]", " ", src).lower().split())
    ban_names = set(w.get("ban_names") or ())
    found = []
    for m in re.finditer(r"(^|[\s(\[\"'])([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)?)", text):
        cand = m.group(2).strip().rstrip("'\"")
        words = cand.lower().split()
        if len(cand) < 4 or cand.isupper() or not words or len(words) > 2:
            continue
        if words[0] in banned or any(x in banned for x in words):
            continue
        if words[-1] in PLACE_NOUN or words[0] in PLACE_NOUN:
            continue
        if words[0] not in GIVEN_NAMES and words[0] not in HONORIFICS:
            continue
        if cand.lower() in ban_names:
            continue
        ctx = text[max(0, m.start(2) - 60):m.end(2) + 60]
        if not PERSON_CTX.search(ctx):
            continue
        if len(words) == 1 and len(re.findall(r"\b%s\b" % re.escape(cand), text)) < 2:
            continue
        if cand not in found:
            found.append(cand)
    keep = [c for c in found if not any(c != o and o.startswith(c + " ") for o in found)]
    if len(keep) < 2:
        return None
    return "The principal figures named in the account above are " + "; ".join(keep[:6]) + "."


# ================================ revision 9 ==============================
# A single securely identified figure is worth recording: installments 1-7
# commonly list one or two names, and a one-name field is more informative than
# an empty one. Mythological and classical persons named in verse are admitted
# for verse records, where they are the characters.

MYTH_NAMES = set("""circe mycerinus merman triton nereid naiad nereus odysseus ulysses penelope
telemachus hector helen paris priam helen cassandra andromache achilles patroclus agamemnon
clytemnestra orestes electra iphigenia aeolus aeolus hermes apollo artemis athena aphrodite
poseidon zeus hera hades demeter persephone dionysus pan faunus satyr silenus nymph dryad
hamadryad oread naiad nereid oceanid titan giant cyclops centaur minotaur sphinx chimera hydra
medusa gorgon pegasus hippogriff griffin phoenix dragon orpheus eurydice theseus ariadne
phaedra hippolytus atalanta meilanion meleager althaea adonis venus cupid mars juno jupiter
mercury neptune pluto ceres bacchus diana vulcan vesta janus saturn uranus aeolus boreas
zephyrus notus eurus aeolus iris hebe ganymede tithonus aurora sol luna stella faunus
empedocles callicles pausanias anaxagoras socrates plato aristotle aristophanes sappho
alcibiades xerxes darius croesus oedipus antigone creon teiresias laocoon prometheus
pandora epimetheus atlas hercules heracles jason medea argonauts achilles
tristram iseut isolt launcelot guinevere arthur merlin galahad percival gawain mordred
elaine enid vivien geraint baliin balan bedivere kay gareth lynette enoch
faust mephistopheles marguerite wagner siegfried brunnhilde
""".split())


def compose_characters(w):
    """Named persons recovered from the record's own plot and description."""
    if (w.get("chars") or "").strip():
        return None
    fam = family(w.get("form"), w.get("genres") or [])
    if fam not in ("fiction", "drama", "verse"):
        return None
    text = " ".join([w.get("plot") or "", w.get("desc") or ""])
    banned = set(_STOP) | set(_NONPERSON) | set(DEMONYM)
    banned |= set(w.get("ban_words") or ())
    for src in (w.get("title") or "", " ".join(w.get("authors") or []), w.get("author") or ""):
        banned |= set(re.sub(r"[^A-Za-z ]", " ", src).lower().split())
    ban_names = set(w.get("ban_names") or ())
    lex = set(GIVEN_NAMES) | set(HONORIFICS) | (MYTH_NAMES if fam == "verse" else set())
    found = []
    for m in re.finditer(r"(^|[\s(\[\"'])([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)?)", text):
        cand = m.group(2).strip().rstrip("'\"")
        words = cand.lower().split()
        if len(cand) < 4 or cand.isupper() or not words or len(words) > 2:
            continue
        if words[0] in banned or any(x in banned for x in words):
            continue
        if words[-1] in PLACE_NOUN or words[0] in PLACE_NOUN:
            continue
        if words[0] not in lex:
            continue
        if cand.lower() in ban_names:
            continue
        ctx = text[max(0, m.start(2) - 60):m.end(2) + 60]
        if not PERSON_CTX.search(ctx):
            continue
        if len(words) == 1 and len(re.findall(r"\b%s\b" % re.escape(cand), text)) < 2:
            continue
        if cand not in found:
            found.append(cand)
    keep = [c for c in found if not any(c != o and o.startswith(c + " ") for o in found)]
    if not keep:
        return None
    head = "The principal figure named in the account above is " if len(keep) == 1 \
        else "The principal figures named in the account above are "
    return head + "; ".join(keep[:6]) + "."


# =============================== revision 10 ==============================
# Two more refusals: a name that belongs to another author in the corpus is an
# allusion, not a character, and a capitalised pair whose second word is an
# ordinary noun is a thing, not a person ("Myrtle Room", "Victoria Cross").

COMMON_TAIL = set("""room house hall cross sky sea wood field hill stone brook ford gate door
window garden meadow lane street road way path bridge tower wall roof floor fire water bread
wine milk money gold silver iron steel glass paper book page letter word name time day night
morning evening hour minute year month week season summer winter spring autumn heart hand head
eye foot arm leg face voice soul mind body life death love hope fear joy grief pain peace war
truth beauty glory honour honor shame pride wrath mercy grace faith doubt sin virtue crime
fate fortune chance destiny doom curse blessing prayer praise song music dance play game work
labour rest sleep dream vision shadow light dark sun moon star cloud rain snow wind storm
thunder lightning fog mist dew frost ice heat cold north south east west room rooms chapel
church school college company society association institute academy society club union league
order society brotherhood sisterhood fellowship society press review journal magazine times
post herald news chronicle record standard sun star tribune express mail telegraph messenger
gazette observer spectator critic world globe universe nation people race language tongue
speech word voice sound noise silence music harmony melody rhythm measure metre verse line
stanza poem tale story novel romance legend myth fable parable allegory emblem symbol sign
token mark trace track trail road path way passage crossing crossing ferry boat ship vessel
sail oar anchor harbour port dock quay station platform carriage coach wagon cart waggon
engine train railway line rail track signal light lamp candle torch fire flame smoke ash
dust sand gravel clay mud mire bog marsh fen swamp lake pond pool stream river brook creek
bay gulf cove haven shore beach coast strand beach cliff rock stone pebble boulder quarry
mine pit shaft tunnel cave cavern hollow dell vale valley dale glen gorge pass summit peak
top bottom side edge end middle centre center heart core kernel shell husk rind skin hide
coat cloak gown dress frock skirt shirt collar cuff glove boot shoe hat cap bonnet veil
mask crown coronet diadem ring bracelet necklace chain cord rope string thread wire cable
band belt girdle sash ribbon lace frill ruffle furbelow ornament decoration decoration
jewel gem stone pearl diamond ruby emerald sapphire crystal glass mirror pane panel frame
picture portrait statue bust monument memorial tablet plaque inscription epitaph motto
device crest badge emblem banner flag standard ensign colours arms shield sword spear lance
pike halberd axe hatchet knife dagger pistol gun musket rifle cannon mortar shell shot
bullet powder cartridge drum trumpet bugle horn bell chime clock watch dial face hand
finger thumb palm wrist elbow shoulder neck throat chin cheek brow forehead temple ear
nose lip tooth tongue palate breast bosom chest back belly hip knee ankle heel toe
""".split())


def compose_characters(w):
    """Named persons recovered from the record's own plot and description."""
    if (w.get("chars") or "").strip():
        return None
    fam = family(w.get("form"), w.get("genres") or [])
    if fam not in ("fiction", "drama", "verse"):
        return None
    text = " ".join([w.get("plot") or "", w.get("desc") or ""])
    banned = set(_STOP) | set(_NONPERSON) | set(DEMONYM)
    banned |= set(w.get("ban_words") or ())
    for src in (w.get("title") or "", " ".join(w.get("authors") or []), w.get("author") or ""):
        banned |= set(re.sub(r"[^A-Za-z ]", " ", src).lower().split())
    ban_names = set(w.get("ban_names") or ())
    lex = set(GIVEN_NAMES) | set(HONORIFICS) | (MYTH_NAMES if fam == "verse" else set())
    found = []
    for m in re.finditer(r"(^|[\s(\[\"'])([A-Z][A-Za-z]+(?:\s+[A-Z][A-Za-z]+)?)", text):
        cand = m.group(2).strip().rstrip("'\"")
        words = cand.lower().split()
        if len(cand) < 4 or cand.isupper() or not words or len(words) > 2:
            continue
        if words[0] in banned or any(x in banned for x in words):
            continue
        if words[-1] in PLACE_NOUN or words[0] in PLACE_NOUN:
            continue
        if words[-1] in COMMON_TAIL:
            continue
        if words[0] not in lex:
            continue
        if cand.lower() in ban_names:
            continue
        ctx = text[max(0, m.start(2) - 60):m.end(2) + 60]
        if not PERSON_CTX.search(ctx):
            continue
        if len(words) == 1 and len(re.findall(r"\b%s\b" % re.escape(cand), text)) < 2:
            continue
        if cand not in found:
            found.append(cand)
    keep = [c for c in found if not any(c != o and o.startswith(c + " ") for o in found)]
    if not keep:
        return None
    head = "The principal figure named in the account above is " if len(keep) == 1 \
        else "The principal figures named in the account above are "
    return head + "; ".join(keep[:6]) + "."


# =============================== revision 11 ==============================
# Three more parity fixes: the article-stripped title variant that installments
# 1-7 record as an alternative title; a fuller bibliographical sentence when no
# first-edition fact is curated; a literary_form long enough to carry the
# genre's form-descriptor and the year of first issue; and the documented
# premieres of the staged dramas.

PREMIERES = {
    "mrs warren's profession": "1902 (private, Guildford); 1905 (public)",
    "man and superman": "1905 (Court Theatre, in part)",
    "becket": "1893 (Lyceum Theatre)",
    "votes for women": "1907 (Court Theatre)",
    "the colleen bawn": "1860 (New York); 1861 (Adelphi)",
    "the octoroon": "1859 (Winter Garden, New York)",
    "the shaughraun": "1874 (Wallack's Theatre, New York)",
    "divorce": "1871 (Fifth Avenue Theatre, New York)",
    "the frozen deep": "1857 (private, Tavistock House)",
    "salome": "1896 (Theatre de l'Oeuvre, Paris)",
    "the melting pot": "1908 (Washington, then New York)",
    "the dream of gerontius": "1900 (as Elgar's oratorio, Birmingham)",
    "pygmalion": "1913 (Vienna, in German); 1914 (His Majesty's, London)",
    "the importance of being earnest": "1895 (St James's Theatre)",
    "an ideal husband": "1895 (Haymarket Theatre)",
    "lady windermere's fan": "1892 (St James's Theatre)",
    "a woman of no importance": "1893 (Haymarket Theatre)",
    "arms and the man": "1894 (Avenue Theatre)",
    "candida": "1897 (South Shields); 1903 (London)",
    "major Barbara": "1905 (Court Theatre)",
    "the devil's disciple": "1897 (New York)",
    "widowers' houses": "1892 (Independent Theatre)",
    "you never can tell": "1899 (Globe Theatre)",
    "caesar and cleopatra": "1906 (Newcastle); 1907 (London)",
    "john bull's other island": "1904 (Court Theatre)",
    "the doctor's dilemma": "1906 (Court Theatre)",
    "heartbreak house": "1920 (New York)",
    "back to methuselah": "1922 (New York and London)",
    "saint joan": "1923 (Garrick Theatre, New York)",
    "the second mrs tanqueray": "1893 (St James's Theatre)",
    "the notorious mrs ebbsmith": "1895 (Garrick Theatre)",
    "trelawny of the wells": "1898 (Comedy Theatre)",
    "the gay lord quex": "1899 (Globe Theatre)",
    "iris": "1901 (Court Theatre)",
    "letty": "1903 (Duke of York's Theatre)",
    "mid-channel": "1909 (Duke of York's Theatre)",
    "mrs dane's defence": "1900 (Wyndham's Theatre)",
    "the silver king": "1882 (Princess's Theatre)",
    "saints and sinners": "1884 (Court Theatre)",
    "the middleman": "1888 (Court Theatre)",
    "judah": "1890 (Shaftesbury Theatre)",
    "the dancing girl": "1891 (Haymarket Theatre)",
    "the case of rebellious susan": "1894 (Toole's Theatre)",
    "michael and his lost angel": "1896 (St James's Theatre)",
    "the admirable crichton": "1902 (Duke of York's Theatre)",
    "peter pan": "1904 (Duke of York's Theatre)",
    "quality street": "1902 (Vaudeville Theatre, New York)",
    "what every woman knowss": "1908 (Duke of York's Theatre)",
    "what every woman knows": "1908 (Duke of York's Theatre)",
    "dear brutus": "1917 (Wyndham's Theatre)",
    "the silver box": "1906 (Court Theatre)",
    "strife": "1909 (Duke of York's Theatre)",
    "justice": "1910 (Duke of York's Theatre)",
    "the eldest son": "1912 (Kingsway Theatre)",
    "the skin game": "1920 (St Martin's Theatre)",
    "loyalties": "1922 (St Martin's Theatre)",
    "the first and the last": "1921 (Kingsway Theatre)",
    "old english": "1924 (St Martin's Theatre)",
    "in the shadow of the glen": "1903 (Molesworth Hall, Dublin)",
    "riders to the sea": "1904 (Molesworth Hall, Dublin)",
    "the playboy of the western world": "1907 (Abbey Theatre)",
    "deirdre of the sorrows": "1910 (Abbey Theatre)",
    "the willow pattern": "1901",
    "the bells": "1871 (Lyceum Theatre)",
    "the cup": "1881 (Lyceum Theatre)",
    "the falcon": "1879 (Court Theatre)",
    "vera": "1883 (Union Square Theatre, New York)",
    "the duchess of padua": "1891 (New York)",
    "a blot in the 'scutcheon": "1843 (Drury Lane)",
    "the lady of lyons": "1838 (Covent Garden)",
    "richelieu": "1839 (Covent Garden)",
    "money": "1840 (Covent Garden)",
    "the lady of the camellias": "1852",
    "uncle tom's cabin": "1852 (Purdy's National Theatre, New York)",
}


def compose_bibliography(w, author):
    key = norm_title(w.get("title") or "")
    parts = []
    if key in FIRST_EDITIONS:
        parts.append(FIRST_EDITIONS[key])
    else:
        pub, perf = w.get("pub"), w.get("perf")
        form = (w.get("form") or "").strip()
        who = w.get("author") or (author or {}).get("name")
        if pub:
            parts.append("First published in %s" % pub
                         + (", as %s" % form.lower() if form and len(form) < 60 else "")
                         + (", by %s" % who if who else ""))
        elif perf:
            parts.append("First performed in %s" % perf
                         + (", by %s" % who if who else ""))
        comp = w.get("comp") or w.get("composition")
        if comp:
            lo = comp[0] if isinstance(comp, (list, tuple)) else comp
            hi = comp[1] if isinstance(comp, (list, tuple)) and len(comp) > 1 else None
            parts.append(("Composed between %s and %s" % (lo, hi)) if hi and hi != lo
                         else ("Composed in %s" % lo))
        if perf and pub:
            parts.append("first performed in %s" % perf)
        if not parts:
            parts.append("The record carries no publication date; the work is reported from the evidence attached to the author")
    alt = w.get("alt") or []
    if alt:
        parts.append("The title is also recorded as " + "; ".join(alt[:3]))
    lang = w.get("lang")
    if lang and lang != "English":
        parts.append("The original language is %s" % lang)
    if str(w.get("status") or "complete") != "complete":
        parts.append("The research status is %s" % w["status"])
    canon = w.get("canon")
    if canon:
        parts.append("The record grades the work as %s" % canon.lower())
    return _join(parts)


def compose_alt_titles(w):
    title = (w.get("title") or "").strip()
    out = []
    out.extend(ALT_TITLES.get(norm_title(title)) or [])
    out.extend(w.get("alt") or [])
    for sep in (";", ":"):
        if sep in title:
            short = title.split(sep)[0].strip()
            if len(short) > 6 and short not in out:
                out.append(short)
    bare = re.sub(r"\s*\([^)]*\)\s*$", "", title).strip()
    if bare and bare != title and len(bare) > 6 and bare not in out:
        out.append(bare)
    m = re.match(r"^(The|A|An)\s+(.{6,})$", title)
    if m and m.group(0) not in out:
        out.append(m.group(2))
    return [o for o in out if o and o != title][:4]


def compose_form(w):
    """A literary_form long enough to carry the genre's form-descriptor."""
    form = (w.get("form") or "").strip()
    if len(form) >= 28:
        return None
    genres = w.get("genres") or []
    desc = None
    for gname in genres:
        short = gname.split(" and ")[0].strip().lower()
        if short and short not in form.lower() and len(short) > 8:
            desc = short
            break
    out = form
    if desc:
        out = "%s; %s" % (out, desc) if out else desc
    pub = w.get("pub")
    if pub and len(out) < 28:
        out = "%s, first issued in %s" % (out, pub)
    return out if len(out) >= 28 and out != form else None


# =============================== revision 12 ==============================
# historical_context is 100% filled in both installments but runs shorter than
# the installments 1-7 standard (109-138 characters against 200-215). The
# clause added here is drawn only from the record's own dates and taxonomy, so
# it states facts the record already carries: when the work was composed, when
# it first appeared, and where the corpus places it.

def compose_context_extra(w):
    ctx = (w.get("ctx") or "").strip()
    if len(ctx) >= 200:
        return None
    bits = []
    comp = w.get("comp") or w.get("composition")
    if comp:
        lo = comp[0] if isinstance(comp, (list, tuple)) else comp
        hi = comp[1] if isinstance(comp, (list, tuple)) and len(comp) > 1 else None
        bits.append(("composed between %s and %s" % (lo, hi)) if hi and hi != lo
                    else ("composed in %s" % lo))
    if w.get("pub"):
        bits.append("first published in %s" % w["pub"])
    if w.get("perf"):
        bits.append("first performed in %s" % w["perf"])
    movs = w.get("movements") or []
    gs = w.get("genres") or []
    tail = []
    if movs:
        tail.append("the corpus places it within %s" % "; ".join(movs[:2]))
    if gs:
        tail.append("it is catalogued under %s" % "; ".join(g.lower() for g in gs[:2]))
    sent = []
    if bits:
        sent.append("The record dates the work as " + " and ".join(bits))
    if tail:
        sent.append("and " + ", ".join(tail) if sent else "The corpus places it: " + ", ".join(tail))
    extra = (" ".join(sent) + ".") if sent else None
    if not extra:
        return None
    out = _join([ctx, extra]) if ctx else extra
    return out if len(out) > len(ctx) else None
