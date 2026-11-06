import com.saeedlotfi.englishliterature.data.Library;

/**
 * Plain-JVM checks for the significance-tier logic in {@link Library}.
 *
 * The Android framework is stubbed in android-all.jar, so anything touching
 * Context/asset loading cannot run here; these assertions cover the pure
 * ranking, floor and label helpers that the filter UI depends on.
 *
 * Run with {@code python3 android/tools/run_tier_tests.py}.
 */
public final class TierLogicTest {

    private static int failures = 0;

    private static void check(String what, boolean ok) {
        if (!ok) {
            System.out.println("FAIL: " + what);
            failures++;
        }
    }

    public static void main(String[] args) {
        // Ranking, including ungraded, null and unknown values.
        check("major ranks 4", Library.tierRank(Library.TIER_MAJOR) == 4);
        check("secondary ranks 3", Library.tierRank(Library.TIER_SECONDARY) == 3);
        check("minor ranks 2", Library.tierRank(Library.TIER_MINOR) == 2);
        check("obscure ranks 1", Library.tierRank(Library.TIER_OBSCURE) == 1);
        check("ungraded ranks 0", Library.tierRank("") == 0);
        check("null ranks 0", Library.tierRank(null) == 0);
        check("unknown ranks 0", Library.tierRank("Canonical-ish") == 0);
        check("rank ignores surrounding space",
                Library.tierRank("  " + Library.TIER_MAJOR + " ") == 4);

        // Filter list: five options, loosest first.
        String[] floors = Library.TIER_FILTERS;
        check("five filter options", floors.length == 5);
        check("first option admits everything", floors[0].isEmpty());
        check("last option is the strictest", floors[4].equals(Library.TIER_OBSCURE));

        // An empty floor admits every author, graded or not.
        for (String t : new String[]{Library.TIER_MAJOR, Library.TIER_SECONDARY,
                Library.TIER_MINOR, Library.TIER_OBSCURE, ""}) {
            check("\"" + t + "\" passes the All floor", Library.tierAtLeast(t, ""));
        }

        // Any grade at all clears the Obscure floor; ungraded never does.
        check("ungraded fails Obscure", !Library.tierAtLeast("", Library.TIER_OBSCURE));
        check("null fails Obscure", !Library.tierAtLeast(null, Library.TIER_OBSCURE));
        check("obscure passes Obscure", Library.tierAtLeast(Library.TIER_OBSCURE, Library.TIER_OBSCURE));

        // Exactly-at-floor and just-below-floor cases.
        for (int i = 1; i < floors.length; i++) {
            check("tier at floor " + i + " passes", Library.tierAtLeast(floors[i], floors[i]));
            if (i + 1 < floors.length) {
                check("tier below floor " + i + " fails",
                        !Library.tierAtLeast(floors[i + 1], floors[i]));
            }
        }

        // Nested: anything admitted by a stricter floor clears every looser one.
        for (int i = 1; i < floors.length - 1; i++) {
            for (String t : floors) {
                if (Library.tierAtLeast(t, floors[i])) {
                    check("nested: " + t + " admitted at " + i + " must clear " + (i + 1),
                            Library.tierAtLeast(t, floors[i + 1]));
                }
            }
        }

        // Labels: short form for the spinner, long form for the detail badges.
        check("All label", Library.tierFilterLabel("").equals("All"));
        check("null label", Library.tierFilterLabel(null).equals("All"));
        check("major filter label", Library.tierFilterLabel(Library.TIER_MAJOR).equals("Major"));
        check("secondary filter label", Library.tierFilterLabel(Library.TIER_SECONDARY).equals("Significant"));
        check("minor filter label", Library.tierFilterLabel(Library.TIER_MINOR).equals("Minor"));
        check("obscure filter label", Library.tierFilterLabel(Library.TIER_OBSCURE).equals("Neglected"));
        check("major badge", Library.tierLabel(Library.TIER_MAJOR).equals("Major canon"));
        check("secondary badge", Library.tierLabel(Library.TIER_SECONDARY).equals("Secondary canon"));
        check("minor badge", Library.tierLabel(Library.TIER_MINOR).equals("Minor"));
        check("obscure badge", Library.tierLabel(Library.TIER_OBSCURE).equals("Neglected"));
        check("ungraded has no badge", Library.tierLabel("").isEmpty());
        check("null has no badge", Library.tierLabel(null).isEmpty());

        System.out.println(failures == 0
                ? "TIER LOGIC OK: all assertions passed"
                : failures + " assertion(s) FAILED");
        if (failures != 0) System.exit(1);
    }
}
