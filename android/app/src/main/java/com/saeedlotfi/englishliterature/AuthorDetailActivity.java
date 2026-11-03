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
import com.saeedlotfi.englishliterature.ui.Ui;

/** Author profile: biography, movements, themes, and linked works. */
public final class AuthorDetailActivity extends Activity {

    public static final String EXTRA_AUTHOR_ID = "author_id";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_author_detail);

        int id = getIntent().getIntExtra(EXTRA_AUTHOR_ID, -1);
        final Author author = Library.get().author(id);
        if (author == null) {
            finish();
            return;
        }

        TextView name = findViewById(R.id.name);
        TextView meta = findViewById(R.id.meta);
        LinearLayout chips = findViewById(R.id.chips);
        LinearLayout content = findViewById(R.id.content);

        name.setText(author.name);
        meta.setText(Ui.joinMeta(author.dates, author.nationality, author.identity));

        for (String g : author.genres) chips.addView(Ui.chip(this, g, false));
        for (String m : author.movements) chips.addView(Ui.chip(this, m, true));

        addSection(content, "Biography", author.biography);
        addSection(content, "Literary Profile", author.profile);
        addSection(content, "Style", author.style);
        addSection(content, "Intellectual Concerns", author.concerns);
        addSection(content, "Historical Significance", author.significance);
        if (!author.uncertainty.isEmpty()) {
            addSection(content, "Biographical Uncertainty", author.uncertainty);
        }
        addChipSection(content, "Themes", author.themes);
        addChipSection(content, "Influenced By", author.influencedBy);

        if (!author.works.isEmpty()) {
            Ui.sectionHeader(this, content, "Works (" + author.works.size() + ")");
            LinearLayout card = Ui.card(this, content);
            for (final Author.WorkRef ref : author.works) {
                card.addView(workRow(ref));
            }
        }

        if (!author.sources.isEmpty()) {
            Ui.sectionHeader(this, content, "Sources");
            LinearLayout card = Ui.card(this, content);
            for (String s : author.sources) {
                TextView line = new TextView(this);
                line.setText("•  " + s);
                line.setTextSize(13.5f);
                line.setTextColor(getResources().getColor(R.color.ink_soft));
                line.setPadding(0, Ui.dp(this, 3), 0, Ui.dp(this, 3));
                card.addView(line);
            }
        }
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

    private View workRow(final Author.WorkRef ref) {
        View row = LayoutInflater.from(this).inflate(R.layout.item_work, null, false);
        ((TextView) row.findViewById(R.id.title)).setText(ref.title);
        ((TextView) row.findViewById(R.id.subtitle)).setText(subtitleFor(ref));
        row.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(AuthorDetailActivity.this, WorkDetailActivity.class)
                        .putExtra(WorkDetailActivity.EXTRA_WORK_ID, ref.id));
            }
        });
        return row;
    }

    private String subtitleFor(Author.WorkRef ref) {
        com.saeedlotfi.englishliterature.data.Work w = Library.get().work(ref.id);
        if (w == null) return "";
        return Ui.joinMeta(com.saeedlotfi.englishliterature.data.Work.joinNames(w.authors), w.period, w.dates);
    }
}
