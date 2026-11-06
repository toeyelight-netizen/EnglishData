package com.saeedlotfi.englishliterature.data;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

/** An author record with its linked works. */
public final class Author {

    public final int id;
    public final String name;
    public final List<String> altNames = new ArrayList<>();
    public final String dates;
    public final String birthplace;
    public final String nationality;
    public final String identity;
    public final String biography;
    public final String profile;
    public final String style;
    public final String concerns;
    public final String significance;
    /** Documented standing: "Major / canonical", "Significant / secondary",
     *  "Minor / lesser-known", "Obscure / historically neglected" or "" when
     *  the author has not been graded (installments 1-7). */
    public final String tier;
    public final String uncertainty;
    public final List<String> genres = new ArrayList<>();
    public final List<String> movements = new ArrayList<>();
    public final List<String> themes = new ArrayList<>();
    public final List<String> influencedBy = new ArrayList<>();
    public final List<String> sources = new ArrayList<>();
    public final List<WorkRef> works = new ArrayList<>();

    public static final class WorkRef {
        public final int id;
        public final String title;

        WorkRef(JSONObject o) {
            id = o.optInt("id");
            title = o.optString("title");
        }
    }

    Author(JSONObject o) {
        id = o.optInt("id");
        name = o.optString("name");
        dates = o.optString("dates");
        birthplace = o.optString("birthplace");
        nationality = o.optString("nationality");
        identity = o.optString("identity");
        biography = o.optString("biography");
        profile = o.optString("profile");
        style = o.optString("style");
        concerns = o.optString("concerns");
        significance = o.optString("significance");
        tier = o.optString("tier");
        uncertainty = o.optString("uncertainty");
        JSONArray arr;
        arr = o.optJSONArray("altNames");
        if (arr != null) for (int i = 0; i < arr.length(); i++) altNames.add(arr.optString(i));
        arr = o.optJSONArray("genres");
        if (arr != null) for (int i = 0; i < arr.length(); i++) genres.add(arr.optString(i));
        arr = o.optJSONArray("movements");
        if (arr != null) for (int i = 0; i < arr.length(); i++) movements.add(arr.optString(i));
        arr = o.optJSONArray("themes");
        if (arr != null) for (int i = 0; i < arr.length(); i++) themes.add(arr.optString(i));
        arr = o.optJSONArray("influencedBy");
        if (arr != null) for (int i = 0; i < arr.length(); i++) influencedBy.add(arr.optString(i));
        arr = o.optJSONArray("sources");
        if (arr != null) for (int i = 0; i < arr.length(); i++) sources.add(arr.optString(i));
        arr = o.optJSONArray("works");
        if (arr != null) for (int i = 0; i < arr.length(); i++) {
            JSONObject ref = arr.optJSONObject(i);
            if (ref != null) works.add(new WorkRef(ref));
        }
    }
}
