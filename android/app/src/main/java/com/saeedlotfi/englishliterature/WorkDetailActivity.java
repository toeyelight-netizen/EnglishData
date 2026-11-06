package com.saeedlotfi.englishliterature;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.saeedlotfi.englishliterature.data.Author;
import com.saeedlotfi.englishliterature.data.Library;
import com.saeedlotfi.englishliterature.data.Work;
import com.saeedlotfi.englishliterature.ui.Ui;

/** Work profile: summary, plot, editions, and linked authors. */
public final class WorkDetailActivity extends Activity {

    public static final String EXTRA_WORK_ID = "work_id";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_work_detail);

        int id = getIntent().getIntExtra(EXTRA_WORK_ID, -1);
        final Work w = Library.get().work(id);
        if (w == null) {
            finish();
            return;
        }

        TextView title = findViewById(R.id.title);
        TextView meta = findViewById(R.id.meta);
        LinearLayout chips = findViewById(R.id.chips);
        LinearLayout content = findViewById(R.id.content);

        title.setText(w.title);
        String by = Work.joinNames(w.authors);
        meta.setText(Ui.joinMeta(by.isEmpty() ? "" : "By " + by, w.period, w.dates));

        String authorTier = Library.get().workTier(w.id);
        String standing = Library.tierLabel(authorTier);
        if (!standing.isEmpty()) {
            chips.addView(Ui.chip(this, standing, true));
        }
        for (String g : w.genres) chips.addView(Ui.chip(this, g, false));
        for (String m : w.movements) chips.addView(Ui.chip(this, m, true));

        addSection(content, "Summary", firstNonEmpty(w.summary, w.description));
        addSection(content, "Plot & Argument", w.plot);
        addSection(content, "Characters", w.characters);
        addSection(content, "Structure", w.structure);
        addSection(content, "Meter & Prosody", w.meter);
        addSection(content, "Historical Context", w.context);
        addSection(content, "Significance", w.significance);
        addSection(content, "Attribution", w.attributionNotes);
        addDetails(content, w);
        addChipSection(content, "Themes", w.themes);
        addAuthors(content, w);
        addEditions(content, w);
        addBullets(content, "Sources", w.sources);
    }

    private String firstNonEmpty(String first, String second) {
        return first != null && !first.trim().isEmpty() ? first : second;
    }

    private void addSection(LinearLayout content, String title, String text) {
        if (text == null || text.trim().isEmpty()) return;
        Ui.sectionHeader(this, content, title);
        LinearLayout card = Ui.card(this, content);
        Ui.paragraph(this, card, text.trim());
    }

    private void addChipSection(LinearLayout content, String title, java.util.List<String> values) {
        if (values.isEmpty()) return;
        Ui.sectionHeader(this, content, title);
        LinearLayout card = Ui.card(this, content);
        card.setOrientation(LinearLayout.HORIZONTAL);
        for (String v : values) card.addView(Ui.chip(this, v, false));
    }

    private void addDetails(LinearLayout content, Work w) {
        boolean hasDetails = !w.authorship.isEmpty() || !w.form.isEmpty() || !w.language.isEmpty()
                || !w.compositionStart.isEmpty() || !w.compositionEnd.isEmpty()
                || !w.publicationDate.isEmpty() || !w.manuscriptDate.isEmpty()
                || !w.canonicalStatus.isEmpty() || !w.altTitles.isEmpty();
        if (!hasDetails) return;

        Ui.sectionHeader(this, content, "Details");
        LinearLayout card = Ui.card(this, content);
        addDetailLine(card, "Authorship", w.authorship);
        addDetailLine(card, "Form", w.form);
        addDetailLine(card, "Language", w.language);
        addDetailLine(card, "Composition", w.compositionStart.isEmpty() && w.compositionEnd.isEmpty() ? ""
                : w.compositionStart + (w.compositionEnd.isEmpty() ? "" : "\u2013" + w.compositionEnd));
        addDetailLine(card, "First published", w.publicationDate);
        addDetailLine(card, "Manuscript", w.manuscriptDate);
        addDetailLine(card, "Canonical status", w.canonicalStatus);
        addDetailLine(card, "Also known as", Work.joinNames(w.altTitles));
    }

    private void addDetailLine(LinearLayout card, String label, String value) {
        if (value == null || value.trim().isEmpty()) return;
        TextView line = new TextView(this);
        line.setText(label + ": " + value.trim());
        line.setTextSize(13.5f);
        line.setTextColor(getResources().getColor(R.color.ink));
        line.setPadding(0, Ui.dp(this, 3), 0, Ui.dp(this, 3));
        card.addView(line);
    }

    private void addAuthors(LinearLayout content, Work w) {
        if (w.authorIds.isEmpty()) return;
        Ui.sectionHeader(this, content, w.authorIds.size() == 1 ? "Author" : "Authors");
        LinearLayout card = Ui.card(this, content);
        for (Integer authorId : w.authorIds) {
            final Author author = Library.get().author(authorId);
            if (author == null) continue;
            View row = LayoutInflater.from(this).inflate(R.layout.item_author, null, false);
            ((TextView) row.findViewById(R.id.title)).setText(author.name);
            ((TextView) row.findViewById(R.id.subtitle)).setText(
                    Ui.joinMeta(author.dates, author.identity));
            row.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    startActivity(new Intent(WorkDetailActivity.this, AuthorDetailActivity.class)
                            .putExtra(AuthorDetailActivity.EXTRA_AUTHOR_ID, author.id));
                }
            });
            card.addView(row);
        }
    }

    private void addEditions(LinearLayout content, Work w) {
        if (w.editions.isEmpty()) return;
        Ui.sectionHeader(this, content, "Editions (" + w.editions.size() + ")");
        LinearLayout card = Ui.card(this, content);
        for (Work.Edition e : w.editions) {
            TextView line = new TextView(this);
            line.setText("•  " + Ui.joinMeta(
                    e.title,
                    e.editor,
                    e.publisher,
                    e.year));
            line.setTextSize(13.5f);
            line.setTextColor(getResources().getColor(R.color.ink_soft));
            line.setPadding(0, Ui.dp(this, 3), 0, Ui.dp(this, 3));
            card.addView(line);
        }
    }

    private void addBullets(LinearLayout content, String title, java.util.List<String> values) {
        if (values.isEmpty()) return;
        Ui.sectionHeader(this, content, title);
        LinearLayout card = Ui.card(this, content);
        for (String s : values) {
            TextView line = new TextView(this);
            line.setText("•  " + s);
            line.setTextSize(13.5f);
            line.setTextColor(getResources().getColor(R.color.ink_soft));
            line.setPadding(0, Ui.dp(this, 3), 0, Ui.dp(this, 3));
            card.addView(line);
        }
    }
}
