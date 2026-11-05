package com.saeedlotfi.englishliterature;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Spinner;
import android.widget.TextView;

import com.saeedlotfi.englishliterature.data.Library;
import com.saeedlotfi.englishliterature.ui.SearchAdapter;

import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/** Search screen: browse or search authors and works. */
public final class MainActivity extends Activity implements SearchAdapter.Listener {

    private static final long DEBOUNCE_MS = 120;

    private final Handler handler = new Handler(Looper.getMainLooper());
    private final ExecutorService executor = Executors.newSingleThreadExecutor();

    private EditText searchInput;
    private ListView list;
    private SearchAdapter adapter;
    private View emptyState;
    private TextView emptySubtitle;
    private TextView subtitle;
    private Spinner tierFilter;
    private String lastQuery = "";
    /** Current significance-tier floor ("" = all authors and works). */
    private String tierFloor = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        searchInput = findViewById(R.id.search_input);
        list = findViewById(R.id.list);
        emptyState = findViewById(R.id.empty_state);
        emptySubtitle = findViewById(R.id.empty_subtitle);

        subtitle = findViewById(R.id.subtitle);
        Library library = Library.get();
        if (library.isLoaded()) {
            subtitle.setText(buildSubtitle(library));
        }

        adapter = new SearchAdapter(this, this);
        list.setAdapter(adapter);
        list.setOnItemClickListener(null);

        setUpTierFilter();

        searchInput.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
            }

            @Override
            public void afterTextChanged(Editable s) {
                final String query = s.toString();
                handler.removeCallbacksAndMessages(null);
                handler.postDelayed(new Runnable() {
                    @Override
                    public void run() {
                        runSearch(query);
                    }
                }, DEBOUNCE_MS);
            }
        });

        Library.get().ensureLoaded(this, new Runnable() {
            @Override
            public void run() {
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        subtitle.setText(buildSubtitle(Library.get()));
                        runSearch(lastQuery);
                    }
                });
            }
        });
    }

    /**
     * Significance filter. Options are the four documented tiers plus "All";
     * choosing a tier shows only authors graded at or above it, and only works
     * with at least one such author.
     */
    private void setUpTierFilter() {
        tierFilter = findViewById(R.id.tier_filter);
        String[] options = new String[Library.TIER_FILTERS.length];
        for (int i = 0; i < options.length; i++) {
            options[i] = Library.tierFilterLabel(Library.TIER_FILTERS[i]);
        }
        ArrayAdapter<String> tierAdapter = new ArrayAdapter<>(
                this, R.layout.item_spinner_selected, options);
        tierAdapter.setDropDownViewResource(R.layout.item_spinner_dropdown);
        tierFilter.setAdapter(tierAdapter);
        tierFilter.setSelection(0, false);
        tierFilter.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            @Override
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
                String chosen = Library.TIER_FILTERS[position];
                if (chosen.equals(tierFloor)) return;
                tierFloor = chosen;
                runSearch(lastQuery);
            }

            @Override
            public void onNothingSelected(AdapterView<?> parent) {
            }
        });
    }

    private String buildSubtitle(Library library) {
        if (tierFloor.isEmpty()) {
            return "A searchable library of " + library.authorCount()
                    + " authors and " + library.workCount() + " works \u00b7 c. 450\u20132000";
        }
        // Compact when filtered: the full sentence would wrap into two lines
        // and shift the search field down every time the filter changes.
        return library.browseAuthors(tierFloor) + " authors \u00b7 "
                + library.browseWorks(tierFloor) + " works \u00b7 "
                + Library.tierFilterLabel(tierFloor) + " and above";
    }

    private void runSearch(final String query) {
        lastQuery = query;
        executor.execute(new Runnable() {
            @Override
            public void run() {
                final String floor = tierFloor;
                final List<Library.Entry> results = Library.get().search(query, floor);
                final boolean showWorksSection = query.trim().length() < 3;
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        if (!lastQuery.equals(query) || !floor.equals(tierFloor)) {
                            return; // stale result
                        }
                        List<Library.Entry> shown;
                        if (results == null) {
                            shown = Library.get().browse(floor);
                            adapter.setResults(shown, true);
                        } else {
                            shown = results;
                            adapter.setResults(results, showWorksSection);
                        }
                        boolean empty = shown.isEmpty();
                        emptyState.setVisibility(empty ? View.VISIBLE : View.GONE);
                        if (empty) {
                            emptySubtitle.setText(results == null
                                    ? getString(R.string.filter_empty)
                                    : "No matches for \u201c" + query.trim() + "\u201d");
                        }
                        subtitle.setText(buildSubtitle(Library.get()));
                        if (results != null && !results.isEmpty() || results == null) {
                            list.setSelection(0);
                        }
                    }
                });
            }
        });
    }

    @Override
    public void onAuthorClick(int id) {
        startActivity(new Intent(this, AuthorDetailActivity.class)
                .putExtra(AuthorDetailActivity.EXTRA_AUTHOR_ID, id));
    }

    @Override
    public void onWorkClick(int id) {
        startActivity(new Intent(this, WorkDetailActivity.class)
                .putExtra(WorkDetailActivity.EXTRA_WORK_ID, id));
    }

    @Override
    protected void onDestroy() {
        handler.removeCallbacksAndMessages(null);
        super.onDestroy();
    }
}
