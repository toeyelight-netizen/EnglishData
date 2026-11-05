"""Installment 07 (British and American Romantic, c. 1789-1832), batch b1.

MAP_B1 maps each exact work title authored in
``data/works/installment_07_works_batch1.json`` to the tuple
``([authors], [genres], [themes], [movements])`` used by the loader.
Author names are limited to the eight authors owned by this batch, and
every taxonomy name is copied verbatim from ``scripts/_i07_taxonomy_names.txt``.
"""

MAP_B1 = {
    "Lyrical Ballads": (
        ["William Wordsworth", "Samuel Taylor Coleridge"],
        ["Lyrical Ballad and Popular Stanza", "Ballad and Popular Song", "Metrical Tale and Romance in Verse"],
        ["The supernatural ballad and willed belief", "Nature, landscape, and the shaping mind", "Industry, enclosure, and the changed countryside", "Rebellion, guilt, and the outcast hero", "Poverty, dependence, and the professional writer"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "Preface to Lyrical Ballads": (
        ["William Wordsworth"],
        ["Critical Treatise and Dissertation", "Literary Biography and Prefatory Commentary"],
        ["Imagination as a way of knowing", "Memory and the growth of the poet's mind", "Taste, decorum, and the rules of art", "Poverty, dependence, and the professional writer"],
        ["Lyrical Ballads and the Lake Poets", "Romantic Essay, Criticism and the Review"],
    ),
    "Lines Written a Few Miles above Tintern Abbey": (
        ["William Wordsworth"],
        ["Conversation Poem and Lyric Meditation", "Nature Lyric and Meditation", "Meditative Blank Verse"],
        ["Nature, landscape, and the shaping mind", "Memory and the growth of the poet's mind", "Poetic solitude and the conversation with nature", "Consolation and endurance"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "The Thorn": (
        ["William Wordsworth"],
        ["Lyrical Ballad and Popular Stanza", "Ballad and Popular Song"],
        ["Melancholy and self-analysis", "The supernatural ballad and willed belief", "Industry, enclosure, and the changed countryside", "Seduction and the betrayed heroine"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "Michael": (
        ["William Wordsworth"],
        ["Metrical Tale and Romance in Verse", "Meditative Blank Verse", "Pastoral Poetry"],
        ["Industry, enclosure, and the changed countryside", "Nature, landscape, and the shaping mind", "Consolation and endurance", "Love, constancy, and betrayal"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "The Solitary Reaper": (
        ["William Wordsworth"],
        ["Nature Lyric and Meditation", "Lyrical Ballad and Popular Stanza"],
        ["Border, ballad, and national memory", "Poetic solitude and the conversation with nature", "Memory and the growth of the poet's mind", "The literature of the nations: Scotland, Ireland, and Wales"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "I Wandered Lonely as a Cloud": (
        ["William Wordsworth"],
        ["Nature Lyric and Meditation", "Lyrical Ballad and Popular Stanza", "Lyric"],
        ["Nature, landscape, and the shaping mind", "Memory and the growth of the poet's mind", "Poetic solitude and the conversation with nature"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "Composed upon Westminster Bridge": (
        ["William Wordsworth"],
        ["Romantic Sonnet Revival", "English Sonnet"],
        ["The city and urban life", "Nature, landscape, and the shaping mind", "The sublime, terror, and the ruin"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "Intimations of Immortality": (
        ["William Wordsworth"],
        ["Romantic Ode", "Pindaric Ode", "Nature Lyric and Meditation"],
        ["Childhood, innocence, and education", "Memory and the growth of the poet's mind", "Time, death, and immortality through verse", "Nature, landscape, and the shaping mind"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "Resolution and Independence": (
        ["William Wordsworth"],
        ["Romantic Sonnet Revival", "English Sonnet", "Lyrical Ballad and Popular Stanza"],
        ["Poverty, dependence, and the professional writer", "Consolation and endurance", "Memory and the growth of the poet's mind", "Nature, landscape, and the shaping mind"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "The Prelude": (
        ["William Wordsworth"],
        ["Meditative Blank Verse", "Nature Lyric and Meditation", "Vision Literature"],
        ["Memory and the growth of the poet's mind", "Imagination as a way of knowing", "Nature, landscape, and the shaping mind", "Revolutionary hope and its disappointment", "The sublime, terror, and the ruin", "Childhood, innocence, and education"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "The Excursion": (
        ["William Wordsworth"],
        ["Meditative Blank Verse", "Metrical Tale and Romance in Verse", "Nature Lyric and Meditation"],
        ["Poetic solitude and the conversation with nature", "Nature, landscape, and the shaping mind", "Melancholy and self-analysis", "Industry, enclosure, and the changed countryside", "Doubt, faith, and secular questioning"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "The Rime of the Ancient Mariner": (
        ["Samuel Taylor Coleridge"],
        ["Lyrical Ballad and Popular Stanza", "Metrical Tale and Romance in Verse", "Ballad and Popular Song"],
        ["The supernatural ballad and willed belief", "Penance, confession, and sin", "Sea voyage and seafaring", "Rebellion, guilt, and the outcast hero", "Creation and cosmology"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "Kubla Khan": (
        ["Samuel Taylor Coleridge"],
        ["Vision Literature", "Metrical Tale and Romance in Verse", "Lyric"],
        ["Dream, intoxication, and the divided mind", "Imagination as a way of knowing", "Monsters and the marvellous", "Exile, travel, and the southern sojourn"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "Christabel": (
        ["Samuel Taylor Coleridge"],
        ["Metrical Tale and Romance in Verse", "Lyrical Ballad and Popular Stanza", "Ballad and Popular Song"],
        ["Gothic confinement and the pursued heroine", "The supernatural ballad and willed belief", "Seduction and the betrayed heroine", "Penance, confession, and sin", "Appearance, dissembling, and self-fashioning"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "Frost at Midnight": (
        ["Samuel Taylor Coleridge"],
        ["Conversation Poem and Lyric Meditation", "Nature Lyric and Meditation", "Meditative Blank Verse"],
        ["Poetic solitude and the conversation with nature", "Nature, landscape, and the shaping mind", "Childhood, innocence, and education", "Imagination as a way of knowing"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "Dejection: An Ode": (
        ["Samuel Taylor Coleridge"],
        ["Romantic Ode", "Pindaric Ode", "Conversation Poem and Lyric Meditation"],
        ["Melancholy and self-analysis", "Nature, landscape, and the shaping mind", "Imagination as a way of knowing", "Idealized love and the lost beloved"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "The Eolian Harp": (
        ["Samuel Taylor Coleridge"],
        ["Conversation Poem and Lyric Meditation", "Nature Lyric and Meditation", "Meditative Blank Verse"],
        ["Poetic solitude and the conversation with nature", "Creation and cosmology", "Reason, faith, and the limits of understanding", "Idealized love and the lost beloved"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "Biographia Literaria": (
        ["Samuel Taylor Coleridge"],
        ["Literary Biography and Prefatory Commentary", "Critical Treatise and Dissertation", "Memoir and Autobiographical Prose", "Philosophy and Scholastic Writing"],
        ["Imagination as a way of knowing", "Self-knowledge and the philosophy of the mind", "Memory and the growth of the poet's mind", "Poverty, dependence, and the professional writer"],
        ["Romantic Essay, Criticism and the Review", "Lyrical Ballads and the Lake Poets"],
    ),
    "The Friend": (
        ["Samuel Taylor Coleridge"],
        ["Periodical Essay and Spectator Paper", "Critical Review and Periodical Essay", "Moral Philosophy and the Theory of Society"],
        ["Familiar prose and the essayist's persona", "The public sphere, print, and the periodical", "Self-knowledge and the philosophy of the mind", "Conscience and moral self-examination"],
        ["Romantic Essay, Criticism and the Review"],
    ),
    "Aids to Reflection": (
        ["Samuel Taylor Coleridge"],
        ["Moral Philosophy and the Theory of Society", "Natural and Revealed Theology", "Philosophy and Scholastic Writing"],
        ["Reason, faith, and the limits of understanding", "Doubt, faith, and secular questioning", "Self-knowledge and the philosophy of the mind", "Conscience and moral self-examination"],
        ["Romantic Essay, Criticism and the Review"],
    ),
    "Joan of Arc": (
        ["Robert Southey"],
        ["Closet Drama", "Tragedy", "Meditative Blank Verse"],
        ["Warfare and battle", "Tyranny and the abuse of power", "Revolutionary hope and its disappointment", "Religious persecution and martyrdom", "Heroism and the heroic code"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "Thalaba the Destroyer": (
        ["Robert Southey"],
        ["Metrical Tale and Romance in Verse", "National Epic and Didactic Poem", "Philosophical Tale and Oriental Fiction"],
        ["Rebellion, guilt, and the outcast hero", "Tyranny and the abuse of power", "Exile, travel, and the southern sojourn", "Doubt, faith, and secular questioning", "Love, constancy, and betrayal"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "Madoc": (
        ["Robert Southey"],
        ["National Epic and Didactic Poem", "Metrical Tale and Romance in Verse"],
        ["Colonial enterprise and the New World", "The literature of the nations: Scotland, Ireland, and Wales", "Slavery, empire, and the Atlantic world", "Tyranny and the abuse of power", "Warfare and battle"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "The Curse of Kehama": (
        ["Robert Southey"],
        ["National Epic and Didactic Poem", "Metrical Tale and Romance in Verse", "Philosophical Tale and Oriental Fiction"],
        ["Tyranny and the abuse of power", "Doubt, faith, and secular questioning", "Seduction and the betrayed heroine", "Exile, travel, and the southern sojourn", "Slavery, empire, and the Atlantic world"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "Wat Tyler": (
        ["Robert Southey"],
        ["Closet Drama", "Political and Revolutionary Verse", "Tragedy"],
        ["Revolutionary hope and its disappointment", "Tyranny and the abuse of power", "Warfare and battle", "Social satire and estates criticism"],
        ["Lyrical Ballads and the Lake Poets"],
    ),
    "The Life of Nelson": (
        ["Robert Southey"],
        ["Prose Biography", "Literary Biography and Prefatory Commentary"],
        ["Heroism and the heroic code", "Sea voyage and seafaring", "Warfare and battle", "National identity and Englishness"],
        ["Romantic Essay, Criticism and the Review"],
    ),
    "Songs of Innocence": (
        ["William Blake"],
        ["Lyrical Ballad and Popular Stanza", "Lyric", "Hymn and Devotional Song", "Pastoral Poetry"],
        ["Childhood, innocence, and education", "Tyranny and the abuse of power", "Nature, landscape, and the shaping mind", "Poetic solitude and the conversation with nature"],
        ["Blake and the Illuminated Prophecy"],
    ),
    "Songs of Experience": (
        ["William Blake"],
        ["Lyric", "Lyrical Ballad and Popular Stanza", "Pastoral Poetry"],
        ["Tyranny and the abuse of power", "Rebellion, guilt, and the outcast hero", "Seduction and the betrayed heroine", "Penance, confession, and sin", "Childhood, innocence, and education"],
        ["Blake and the Illuminated Prophecy"],
    ),
    "The Marriage of Heaven and Hell": (
        ["William Blake"],
        ["Visionary and Illuminated Prophecy", "Vision Literature", "Polemic, Pamphlet, and Open Letter"],
        ["Rebellion, guilt, and the outcast hero", "Tyranny and the abuse of power", "Doubt, faith, and secular questioning", "Imagination as a way of knowing", "Revolutionary hope and its disappointment", "Enthusiasm and the disease of the imagination"],
        ["Blake and the Illuminated Prophecy"],
    ),
    "Visions of the Daughters of Albion": (
        ["William Blake"],
        ["Visionary and Illuminated Prophecy", "Metrical Tale and Romance in Verse", "Closet Drama"],
        ["Seduction and the betrayed heroine", "Tyranny and the abuse of power", "Slavery, empire, and the Atlantic world", "Exile and homelessness", "Idealized love and the lost beloved"],
        ["Blake and the Illuminated Prophecy"],
    ),
    "America a Prophecy": (
        ["William Blake"],
        ["Visionary and Illuminated Prophecy", "Political and Revolutionary Verse", "Metrical Tale and Romance in Verse"],
        ["Revolutionary hope and its disappointment", "Tyranny and the abuse of power", "Colonial enterprise and the New World", "Warfare and battle", "Rebellion, guilt, and the outcast hero"],
        ["Blake and the Illuminated Prophecy"],
    ),
    "Europe a Prophecy": (
        ["William Blake"],
        ["Visionary and Illuminated Prophecy", "Metrical Tale and Romance in Verse", "Political and Revolutionary Verse"],
        ["Revolutionary hope and its disappointment", "Warfare and battle", "Tyranny and the abuse of power", "Exile and homelessness", "Rebellion, guilt, and the outcast hero"],
        ["Blake and the Illuminated Prophecy"],
    ),
    "The Book of Urizen": (
        ["William Blake"],
        ["Visionary and Illuminated Prophecy", "Vision Literature", "English Epic and Allegorical Romance"],
        ["Creation and cosmology", "Tyranny and the abuse of power", "Rebellion, guilt, and the outcast hero", "Reason, faith, and the limits of understanding", "Doubt, faith, and secular questioning"],
        ["Blake and the Illuminated Prophecy"],
    ),
    "Jerusalem": (
        ["William Blake"],
        ["Visionary and Illuminated Prophecy", "National Epic and Didactic Poem", "Metrical Tale and Romance in Verse"],
        ["Imagination as a way of knowing", "Tyranny and the abuse of power", "Creation and cosmology", "National identity and Englishness", "Exile and homelessness"],
        ["Blake and the Illuminated Prophecy"],
    ),
    "Essays of Elia": (
        ["Charles Lamb"],
        ["Familiar Essay and Character Sketch", "Periodical Essay and Spectator Paper", "Essay"],
        ["Familiar prose and the essayist's persona", "The city and urban life", "Poverty, dependence, and the professional writer", "Consolation and endurance", "Memory and the growth of the poet's mind"],
        ["Romantic Essay, Criticism and the Review"],
    ),
    "The Last Essays of Elia": (
        ["Charles Lamb"],
        ["Familiar Essay and Character Sketch", "Periodical Essay and Spectator Paper", "Essay"],
        ["Familiar prose and the essayist's persona", "Melancholy and self-analysis", "The city and urban life", "Consolation and endurance"],
        ["Romantic Essay, Criticism and the Review"],
    ),
    "Tales from Shakespeare": (
        ["Charles Lamb", "Mary Lamb"],
        ["Juvenile, School and Educational Book", "Prose Fiction and the Early Novel", "Fairy Tale and Romantic Legend"],
        ["Childhood, innocence, and education", "Marriage and women's conduct", "Tyranny and the abuse of power", "Appearance, dissembling, and self-fashioning"],
        ["Romantic Essay, Criticism and the Review"],
    ),
    "Characters of Shakespeare's Plays": (
        ["William Hazlitt"],
        ["Critical Treatise and Dissertation", "Character Writing", "Literary Biography and Prefatory Commentary"],
        ["Imagination as a way of knowing", "Self-knowledge and the philosophy of the mind", "Taste, decorum, and the rules of art", "The public theatre and the players' world"],
        ["Romantic Essay, Criticism and the Review"],
    ),
    "Lectures on the English Poets": (
        ["William Hazlitt"],
        ["Critical Treatise and Dissertation", "Character Writing", "Literary Biography and Prefatory Commentary"],
        ["Taste, decorum, and the rules of art", "Imagination as a way of knowing", "The sublime, terror, and the ruin", "Time, death, and immortality through verse"],
        ["Romantic Essay, Criticism and the Review"],
    ),
    "Lectures on the English Comic Writers": (
        ["William Hazlitt"],
        ["Critical Treatise and Dissertation", "Character Writing", "Familiar Essay and Character Sketch"],
        ["Wit, ridicule, and the war against dullness", "Taste, decorum, and the rules of art", "The city and urban life", "Patronage and the literary marketplace"],
        ["Romantic Essay, Criticism and the Review"],
    ),
    "Lectures on the Dramatic Literature of the Age of Elizabeth": (
        ["William Hazlitt"],
        ["Critical Treatise and Dissertation", "Character Writing", "Literary Biography and Prefatory Commentary"],
        ["The public theatre and the players' world", "Tyranny and the abuse of power", "Revenge and justice", "Ambition and the overreacher"],
        ["Romantic Essay, Criticism and the Review"],
    ),
    "The Spirit of the Age": (
        ["William Hazlitt"],
        ["Familiar Essay and Character Sketch", "Character Writing", "Critical Review and Periodical Essay"],
        ["Self-knowledge and the philosophy of the mind", "Familiar prose and the essayist's persona", "The public sphere, print, and the periodical", "Poverty, dependence, and the professional writer", "Doubt, faith, and secular questioning"],
        ["Romantic Essay, Criticism and the Review"],
    ),
    "Table Talk (Hazlitt)": (
        ["William Hazlitt"],
        ["Familiar Essay and Character Sketch", "Periodical Essay and Spectator Paper", "Essay"],
        ["Familiar prose and the essayist's persona", "The city and urban life", "Imagination as a way of knowing", "Melancholy and self-analysis"],
        ["Romantic Essay, Criticism and the Review"],
    ),
    "Confessions of an English Opium-Eater": (
        ["Thomas De Quincey"],
        ["Inward Confession and Opium Narrative", "Memoir and Autobiographical Prose", "Spiritual Autobiography"],
        ["Dream, intoxication, and the divided mind", "The city and urban life", "Penance, confession, and sin", "Poverty, dependence, and the professional writer", "Enthusiasm and the disease of the imagination"],
        ["Romantic Essay, Criticism and the Review"],
    ),
    "Murder as a Fine Art": (
        ["Thomas De Quincey"],
        ["Critical Review and Periodical Essay", "Familiar Essay and Character Sketch", "Polemic, Pamphlet, and Open Letter"],
        ["Revenge and justice", "Penance, confession, and sin", "Self-knowledge and the philosophy of the mind", "Monsters and the marvellous", "The public sphere, print, and the periodical"],
        ["Romantic Essay, Criticism and the Review"],
    ),
}
