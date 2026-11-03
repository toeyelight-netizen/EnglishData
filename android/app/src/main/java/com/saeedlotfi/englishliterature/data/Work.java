package com.saeedlotfi.englishliterature.data;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

/** A literary work record. */
public final class Work {

    public final int id;
    public final String title;
    public final List<String> altTitles = new ArrayList<>();
    public final String authorship;
    public final List<String> authors = new ArrayList<>();
    public final List<Integer> authorIds = new ArrayList<>();
    public final String dates;
    public final String compositionStart;
    public final String compositionEnd;
    public final String publicationDate;
    public final String manuscriptDate;
    public final String language;
    public final String form;
    public final String period;
    public final String description;
    public final String summary;
    public final String plot;
    public final String significance;
    public final String meter;
    public final String context;
    public final String characters;
    public final String structure;
    public final String attributionNotes;
    public final String canonicalStatus;
    public final List<String> genres = new ArrayList<>();
    public final List<String> themes = new ArrayList<>();
    public final List<String> movements = new ArrayList<>();
    public final List<String> sources = new ArrayList<>();
    public final List<Edition> editions = new ArrayList<>();

    public static String joinNames(List<String> names) {
        StringBuilder sb = new StringBuilder();
        for (String name : names) {
            if (name == null || name.trim().isEmpty()) continue;
            if (sb.length() > 0) sb.append(", ");
            sb.append(name.trim());
        }
        return sb.toString();
    }

    public static final class Edition {
        public final String title;
        public final String editor;
        public final String publisher;
        public final String year;

        Edition(JSONObject o) {
            title = o.optString("title");
            editor = o.optString("editor");
            publisher = o.optString("publisher");
            year = o.optString("year");
        }
    }

    Work(JSONObject o) {
        id = o.optInt("id");
        title = o.optString("title");
        authorship = o.optString("authorship");
        dates = o.optString("dates");
        compositionStart = o.optString("compositionStart");
        compositionEnd = o.optString("compositionEnd");
        publicationDate = o.optString("publicationDate");
        manuscriptDate = o.optString("manuscriptDate");
        language = o.optString("language");
        form = o.optString("form");
        period = o.optString("period");
        description = o.optString("description");
        summary = o.optString("summary");
        plot = o.optString("plot");
        significance = o.optString("significance");
        meter = o.optString("meter");
        context = o.optString("context");
        characters = o.optString("characters");
        structure = o.optString("structure");
        attributionNotes = o.optString("attributionNotes");
        canonicalStatus = o.optString("canonicalStatus");
        JSONArray arr;
        arr = o.optJSONArray("altTitles");
        if (arr != null) for (int i = 0; i < arr.length(); i++) altTitles.add(arr.optString(i));
        arr = o.optJSONArray("authors");
        if (arr != null) for (int i = 0; i < arr.length(); i++) authors.add(arr.optString(i));
        arr = o.optJSONArray("authorIds");
        if (arr != null) for (int i = 0; i < arr.length(); i++) authorIds.add(arr.optInt(i));
        arr = o.optJSONArray("genres");
        if (arr != null) for (int i = 0; i < arr.length(); i++) genres.add(arr.optString(i));
        arr = o.optJSONArray("themes");
        if (arr != null) for (int i = 0; i < arr.length(); i++) themes.add(arr.optString(i));
        arr = o.optJSONArray("movements");
        if (arr != null) for (int i = 0; i < arr.length(); i++) movements.add(arr.optString(i));
        arr = o.optJSONArray("sources");
        if (arr != null) for (int i = 0; i < arr.length(); i++) sources.add(arr.optString(i));
        arr = o.optJSONArray("editions");
        if (arr != null) for (int i = 0; i < arr.length(); i++) {
            JSONObject e = arr.optJSONObject(i);
            if (e != null) editions.add(new Edition(e));
        }
    }
}
