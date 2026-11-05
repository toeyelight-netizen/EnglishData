package com.saeedlotfi.englishliterature.data;

import android.content.Context;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.text.Normalizer;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * In-memory library loaded once from the bundled JSON asset.
 * Search is diacritic-insensitive (so "caedmon" finds Cædmon and
 * "meihhad" finds Hali Meiðhad) and instant.
 */
public final class Library {

    public static final int TYPE_AUTHOR = 0;
    public static final int TYPE_WORK = 1;

    /** Significance tiers, in descending order of standing. Author records
     *  carry one of these strings (or "" when not yet graded); a work inherits
     *  the highest tier among its authors. */
    public static final String TIER_MAJOR = "Major / canonical";
    public static final String TIER_SECONDARY = "Significant / secondary";
    public static final String TIER_MINOR = "Minor / lesser-known";
    public static final String TIER_OBSCURE = "Obscure / historically neglected";

    /** Tier options for the filter, in display order ("" = no filter). */
    public static final String[] TIER_FILTERS = {
            "", TIER_MAJOR, TIER_SECONDARY, TIER_MINOR, TIER_OBSCURE};

    /** Rank of a tier name: 0 = ungraded, 1 = obscure ... 4 = major. */
    public static int tierRank(String tier) {
        if (tier == null) return 0;
        String t = tier.trim();
        if (t.equals(TIER_MAJOR)) return 4;
        if (t.equals(TIER_SECONDARY)) return 3;
        if (t.equals(TIER_MINOR)) return 2;
        if (t.equals(TIER_OBSCURE)) return 1;
        return 0;
    }

    /** Short human-readable label for a tier, e.g. "Major canon". */
    public static String tierLabel(String tier) {
        if (tierRank(tier) == 4) return "Major canon";
        if (tierRank(tier) == 3) return "Secondary canon";
        if (tierRank(tier) == 2) return "Minor";
        if (tierRank(tier) == 1) return "Neglected";
        return "";
    }

    /** Short label for the filter bar, where space is tight:
     *  All / Major / Significant / Minor / Neglected. */
    public static String tierFilterLabel(String tier) {
        int rank = tierRank(tier);
        if (rank == 4) return "Major";
        if (rank == 3) return "Significant";
        if (rank == 2) return "Minor";
        if (rank == 1) return "Neglected";
        return "All";
    }

    /** True when the tier names something at or above {@code floor}. */
    public static boolean tierAtLeast(String tier, String floor) {
        if (floor == null || floor.isEmpty()) return true;
        return tierRank(tier) >= tierRank(floor);
    }

    public static final class Entry {
        public final int type;
        public final int id;
        public final String label;
        public final String sub;
        public final int score;

        Entry(int type, int id, String label, String sub, int score) {
            this.type = type;
            this.id = id;
            this.label = label;
            this.sub = sub;
            this.score = score;
        }
    }

    private static final Library INSTANCE = new Library();
    private static final ExecutorService EXECUTOR = Executors.newSingleThreadExecutor();

    private final List<Author> authors = new ArrayList<>();
    private final List<Work> works = new ArrayList<>();
    private final Map<Integer, Author> authorById = new HashMap<>();
    private final Map<Integer, Work> workById = new HashMap<>();
    /** Highest author tier for each work ("" when no author is graded). */
    private final Map<Integer, String> workTier = new HashMap<>();
    private final List<Entry> index = new ArrayList<>();
    private final Object lock = new Object();
    private volatile boolean loaded = false;

    public static Library get() {
        return INSTANCE;
    }

    private Library() {
    }

    public void ensureLoaded(final Context context, final Runnable onDone) {
        if (loaded) {
            if (onDone != null) onDone.run();
            return;
        }
        EXECUTOR.execute(new Runnable() {
            @Override
            public void run() {
                try {
                    load(context);
                    if (onDone != null) onDone.run();
                } catch (Exception ignored) {
                    // Corrupt asset: leave loaded=false; splash still proceeds.
                    if (onDone != null) onDone.run();
                }
            }
        });
    }

    public boolean isLoaded() {
        return loaded;
    }

    private void load(Context context) throws Exception {
        String text = readAsset(context, "data/english_literature.json");
        JSONObject root = new JSONObject(text);

        JSONArray authorArr = root.optJSONArray("authors");
        if (authorArr != null) {
            for (int i = 0; i < authorArr.length(); i++) {
                JSONObject o = authorArr.optJSONObject(i);
                if (o == null) continue;
                Author a = new Author(o);
                authors.add(a);
                authorById.put(a.id, a);
            }
        }
        JSONArray workArr = root.optJSONArray("works");
        if (workArr != null) {
            for (int i = 0; i < workArr.length(); i++) {
                JSONObject o = workArr.optJSONObject(i);
                if (o == null) continue;
                Work w = new Work(o);
                works.add(w);
                workById.put(w.id, w);
            }
        }
        synchronized (lock) {
            buildIndex();
            buildWorkTiers();
            loaded = true;
        }
    }

    private void buildIndex() {
        index.clear();
        for (Author a : authors) {
            String sub = joinNonEmpty(a.dates, a.identity, a.nationality);
            index.add(new Entry(TYPE_AUTHOR, a.id, a.name, sub, 0));
        }
        for (Work w : works) {
            String by = w.authors.isEmpty() ? "" : join(", ", w.authors);
            String sub = joinNonEmpty(by, w.period, w.dates);
            index.add(new Entry(TYPE_WORK, w.id, w.title, sub, 0));
        }
        Collections.sort(index, new Comparator<Entry>() {
            @Override
            public int compare(Entry x, Entry y) {
                int byType = Integer.compare(x.type, y.type);
                if (byType != 0) return byType;
                return fold(x.label).compareTo(fold(y.label));
            }
        });
    }

    private void buildWorkTiers() {
        workTier.clear();
        for (Work w : works) {
            String best = "";
            for (int i = 0; i < w.authorIds.size(); i++) {
                Author a = authorById.get(w.authorIds.get(i));
                if (a == null) continue;
                if (tierRank(a.tier) > tierRank(best)) best = a.tier;
            }
            workTier.put(w.id, best);
        }
    }

    /** Highest tier among a work's authors ("" when nobody is graded). */
    public String workTier(int workId) {
        String t = workTier.get(workId);
        return t == null ? "" : t;
    }

    /** All entries in display order (browse mode). */
    public List<Entry> browse() {
        return new ArrayList<>(index);
    }

    /** Browse entries whose author/work standing is at or above {@code floor}.
     *  An ungraded author (installments 1-7) is treated as not-yet-classified
     *  and is admitted only when no filter is set. */
    public List<Entry> browse(String floor) {
        if (floor == null || floor.isEmpty()) return browse();
        List<Entry> out = new ArrayList<>();
        for (Entry e : index) {
            if (e.type == TYPE_AUTHOR) {
                Author a = authorById.get(e.id);
                if (a != null && tierAtLeast(a.tier, floor)) out.add(e);
            } else {
                if (tierAtLeast(workTier(e.id), floor)) out.add(e);
            }
        }
        return out;
    }

    /** Count of authors at or above {@code floor} (for the filter subtitle). */
    public int browseAuthors(String floor) {
        int n = 0;
        for (Author a : authors) {
            if (tierAtLeast(a.tier, floor)) n++;
        }
        return n;
    }

    /** Count of works at or above {@code floor}. */
    public int browseWorks(String floor) {
        int n = 0;
        for (Work w : works) {
            if (tierAtLeast(workTier(w.id), floor)) n++;
        }
        return n;
    }

    /** Ranked matches; empty query returns null to signal browse mode. */
    public List<Entry> search(String query) {
        return search(query, "");
    }

    /** Ranked matches restricted to the given tier floor ("" = no filter). */
    public List<Entry> search(String query, String floor) {
        boolean filtered = floor != null && !floor.isEmpty();
        String q = fold(query).trim();
        if (q.isEmpty()) return null;
        String[] tokens = q.split("\\s+");
        List<Entry> hits = new ArrayList<>();
        for (Author a : authors) {
            if (filtered && !tierAtLeast(a.tier, floor)) continue;
            int score = scoreFor(q, tokens, a.name, a.altNames, join(" ", a.genres, a.movements, a.identity));
            if (score > 0) {
                hits.add(new Entry(TYPE_AUTHOR, a.id, a.name,
                        joinNonEmpty(a.dates, a.identity), score));
            }
        }
        for (Work w : works) {
            if (filtered && !tierAtLeast(workTier(w.id), floor)) continue;
            int score = scoreFor(q, tokens, w.title, w.altTitles,
                    join(" ", w.description, w.summary, w.plot, w.period, w.authors));
            if (score > 0) {
                hits.add(new Entry(TYPE_WORK, w.id, w.title,
                        joinNonEmpty(join(", ", w.authors), w.period, w.dates), score));
            }
        }
        Collections.sort(hits, new Comparator<Entry>() {
            @Override
            public int compare(Entry x, Entry y) {
                int byScore = Integer.compare(y.score, x.score);
                if (byScore != 0) return byScore;
                return fold(x.label).compareTo(fold(y.label));
            }
        });
        return hits;
    }

    private static int scoreFor(String q, String[] tokens, String label, List<String> aliases, String extra) {
        String l = fold(label);
        int best = 0;
        if (l.equals(q)) best = Math.max(best, 100);
        else if (l.startsWith(q)) best = Math.max(best, 90);
        else if (l.contains(q)) best = Math.max(best, 60);
        for (String alias : aliases) {
            String al = fold(alias);
            if (al.equals(q)) best = Math.max(best, 85);
            else if (al.startsWith(q)) best = Math.max(best, 72);
            else if (al.contains(q)) best = Math.max(best, 52);
        }
        if (best == 0 && tokens.length > 1 && containsAll(l, tokens)) {
            best = Math.max(best, 48);
        }
        String ex = fold(extra);
        if (ex.contains(q)) best = Math.max(best, 28);
        if (best == 0 && tokens.length > 1 && containsAll(ex, tokens)) {
            best = Math.max(best, 18);
        }
        return best;
    }

    private static boolean containsAll(String haystack, String[] tokens) {
        for (String t : tokens) {
            if (!haystack.contains(t)) return false;
        }
        return true;
    }

    public Author author(int id) {
        return authorById.get(id);
    }

    public Work work(int id) {
        return workById.get(id);
    }

    public int authorCount() {
        return authors.size();
    }

    public int workCount() {
        return works.size();
    }

    /**
     * Case- and diacritic-folding for search: "Cædmon" -> "caedmon",
     * "Meiðhad" -> "meithhad", "þ" -> "th".
     */
    public static String fold(String value) {
        if (value == null) return "";
        String nfd = Normalizer.normalize(value.toLowerCase(Locale.ROOT), Normalizer.Form.NFD);
        StringBuilder out = new StringBuilder(nfd.length());
        for (int i = 0; i < nfd.length(); i++) {
            char c = nfd.charAt(i);
            if (Character.getType(c) == Character.NON_SPACING_MARK) continue;
            if (c == '\u00fe' || c == '\u00f0') out.append("th");
            else out.append(c);
        }
        return out.toString();
    }

    private static String readAsset(Context context, String path) throws Exception {
        InputStream in = context.getAssets().open(path);
        try {
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(in, StandardCharsets.UTF_8));
            StringBuilder sb = new StringBuilder();
            char[] buf = new char[8192];
            int n;
            while ((n = reader.read(buf)) != -1) sb.append(buf, 0, n);
            return sb.toString();
        } finally {
            in.close();
        }
    }

    private static String join(String sep, Object... groups) {
        StringBuilder sb = new StringBuilder();
        for (Object g : groups) {
            if (g == null) continue;
            if (g instanceof List) {
                for (Object s : (List<?>) g) append(sep, sb, String.valueOf(s));
            } else {
                append(sep, sb, String.valueOf(g));
            }
        }
        return sb.toString();
    }

    private static void append(String sep, StringBuilder sb, String s) {
        if (s == null || s.isEmpty()) return;
        if (sb.length() > 0) sb.append(sep);
        sb.append(s);
    }

    private static String joinNonEmpty(String... parts) {
        StringBuilder sb = new StringBuilder();
        for (String s : parts) {
            if (s == null || s.isEmpty()) continue;
            if (sb.length() > 0) sb.append(" · ");
            sb.append(s);
        }
        return sb.toString();
    }
}
