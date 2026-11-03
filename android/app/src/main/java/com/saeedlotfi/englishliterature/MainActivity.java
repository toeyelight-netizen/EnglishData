package com.saeedlotfi.englishliterature;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.EditText;
import android.widget.ListView;
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
    private String lastQuery = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        searchInput = findViewById(R.id.search_input);
        list = findViewById(R.id.list);
        emptyState = findViewById(R.id.empty_state);
        emptySubtitle = findViewById(R.id.empty_subtitle);

        TextView subtitle = findViewById(R.id.subtitle);
        Library library = Library.get();
        if (library.isLoaded()) {
            subtitle.setText(buildSubtitle(library));
        }

        adapter = new SearchAdapter(this, this);
        list.setAdapter(adapter);
        list.setOnItemClickListener(null);

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

    private String buildSubtitle(Library library) {
        return "A searchable library of " + library.authorCount()
                + " authors and " + library.workCount() + " works · c. 450\u20132000";
    }

    private void runSearch(final String query) {
        lastQuery = query;
        executor.execute(new Runnable() {
            @Override
            public void run() {
                final List<Library.Entry> results = Library.get().search(query);
                final boolean showWorksSection = query.trim().length() < 3;
                runOnUiThread(new Runnable() {
                    @Override
                    public void run() {
                        if (!lastQuery.equals(query)) return; // stale result
                        if (results == null) {
                            adapter.setResults(Library.get().browse(), true);
                        } else {
                            adapter.setResults(results, showWorksSection);
                        }
                        boolean empty = results != null && results.isEmpty();
                        emptyState.setVisibility(empty ? View.VISIBLE : View.GONE);
                        if (empty) {
                            emptySubtitle.setText("No matches for \u201c" + query.trim() + "\u201d");
                        }
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
