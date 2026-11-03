package com.saeedlotfi.englishliterature.ui;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import com.saeedlotfi.englishliterature.R;
import com.saeedlotfi.englishliterature.data.Library;

import java.util.ArrayList;
import java.util.List;

/** List adapter: section headers + author/work rows. */
public final class SearchAdapter extends BaseAdapter {

    public interface Listener {
        void onAuthorClick(int id);

        void onWorkClick(int id);
    }

    private static final int VIEW_HEADER = 0;
    private static final int VIEW_AUTHOR = 1;
    private static final int VIEW_WORK = 2;

    private final Context context;
    private final LayoutInflater inflater;
    private final Listener listener;
    private final List<Object> items = new ArrayList<>();

    public SearchAdapter(Context context, Listener listener) {
        this.context = context;
        this.inflater = LayoutInflater.from(context);
        this.listener = listener;
    }

    public void setResults(List<Library.Entry> results, boolean grouped) {
        items.clear();
        if (results == null) return;
        if (grouped) {
            boolean haveAuthors = false;
            boolean haveWorks = false;
            for (Library.Entry e : results) {
                if (e.type == Library.TYPE_AUTHOR) haveAuthors = true;
                else haveWorks = true;
            }
            if (haveAuthors) {
                items.add(context.getString(R.string.section_authors));
                for (Library.Entry e : results) {
                    if (e.type == Library.TYPE_AUTHOR) items.add(e);
                }
            }
            if (haveWorks) {
                items.add(context.getString(R.string.section_works));
                for (Library.Entry e : results) {
                    if (e.type == Library.TYPE_WORK) items.add(e);
                }
            }
        } else {
            items.addAll(results);
        }
        notifyDataSetChanged();
    }

    @Override
    public int getCount() {
        return items.size();
    }

    @Override
    public Object getItem(int position) {
        return items.get(position);
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public int getViewTypeCount() {
        return 3;
    }

    @Override
    public int getItemViewType(int position) {
        Object item = items.get(position);
        if (item instanceof String) return VIEW_HEADER;
        Library.Entry e = (Library.Entry) item;
        return e.type == Library.TYPE_AUTHOR ? VIEW_AUTHOR : VIEW_WORK;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        Object item = items.get(position);
        if (item instanceof String) {
            TextView header = (TextView) convertView;
            if (header == null) {
                header = (TextView) inflater.inflate(R.layout.item_section_header, parent, false);
            }
            header.setText((String) item);
            return header;
        }
        final Library.Entry entry = (Library.Entry) item;
        if (entry.type == Library.TYPE_AUTHOR) {
            View row = convertView;
            if (row == null || !(row.getTag() instanceof Integer)
                    || (Integer) row.getTag() != VIEW_AUTHOR) {
                row = inflater.inflate(R.layout.item_author, parent, false);
                row.setTag(VIEW_AUTHOR);
            }
            ((TextView) row.findViewById(R.id.title)).setText(entry.label);
            ((TextView) row.findViewById(R.id.subtitle)).setText(entry.sub);
            row.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    listener.onAuthorClick(entry.id);
                }
            });
            return row;
        }
        View row = convertView;
        if (row == null || !(row.getTag() instanceof Integer)
                || (Integer) row.getTag() != VIEW_WORK) {
            row = inflater.inflate(R.layout.item_work, parent, false);
            row.setTag(VIEW_WORK);
        }
        ((TextView) row.findViewById(R.id.title)).setText(entry.label);
        ((TextView) row.findViewById(R.id.subtitle)).setText(entry.sub);
        row.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                listener.onWorkClick(entry.id);
            }
        });
        return row;
    }
}
