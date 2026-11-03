package com.saeedlotfi.englishliterature.ui;

import android.content.Context;
import android.graphics.Typeface;
import android.util.TypedValue;
import android.view.Gravity;
import android.view.ViewGroup;
import android.widget.LinearLayout;
import android.widget.TextView;

import com.saeedlotfi.englishliterature.R;

/** Small view-building helpers shared by the detail screens. */
public final class Ui {

    private Ui() {
    }

    public static String joinMeta(String... parts) {
        StringBuilder sb = new StringBuilder();
        for (String part : parts) {
            if (part == null || part.trim().isEmpty()) continue;
            if (sb.length() > 0) sb.append(" \u00b7 ");
            sb.append(part.trim());
        }
        return sb.toString();
    }

    public static int dp(Context context, float value) {
        return Math.round(TypedValue.applyDimension(
                TypedValue.COMPLEX_UNIT_DIP, value, context.getResources().getDisplayMetrics()));
    }

    public static TextView chip(Context context, String text, boolean accent) {
        TextView chip = new TextView(context);
        chip.setText(text);
        chip.setTextSize(13);
        chip.setGravity(Gravity.CENTER);
        chip.setPadding(dp(context, 12), dp(context, 6), dp(context, 12), dp(context, 6));
        if (accent) {
            chip.setBackgroundResource(R.drawable.bg_chip_accent);
            chip.setTextColor(context.getResources().getColor(R.color.splash_text_soft));
        } else {
            chip.setBackgroundResource(R.drawable.bg_chip);
            chip.setTextColor(context.getResources().getColor(R.color.gold_text));
        }
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.WRAP_CONTENT, ViewGroup.LayoutParams.WRAP_CONTENT);
        lp.setMargins(0, 0, dp(context, 8), 0);
        chip.setLayoutParams(lp);
        return chip;
    }

    public static TextView sectionHeader(Context context, LinearLayout parent, String title) {
        TextView header = new TextView(context);
        header.setText(title.toUpperCase());
        header.setTextSize(12.5f);
        header.setLetterSpacing(0.1f);
        header.setTypeface(Typeface.create("sans-serif-medium", Typeface.NORMAL));
        header.setTextColor(context.getResources().getColor(R.color.gold_text));
        header.setPadding(dp(context, 4), dp(context, 14), dp(context, 4), dp(context, 7));
        parent.addView(header, new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT));
        return header;
    }

    public static TextView paragraph(Context context, LinearLayout parent, String text) {
        TextView view = new TextView(context);
        view.setText(text);
        view.setTextSize(14.5f);
        view.setLineSpacing(dp(context, 3), 1f);
        view.setTextColor(context.getResources().getColor(R.color.ink));
        parent.addView(view, new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT));
        return view;
    }

    public static LinearLayout card(Context context, LinearLayout parent) {
        LinearLayout card = new LinearLayout(context);
        card.setOrientation(LinearLayout.VERTICAL);
        card.setBackgroundResource(R.drawable.bg_card);
        card.setElevation(dp(context, 1));
        card.setPadding(dp(context, 16), dp(context, 13), dp(context, 16), dp(context, 14));
        LinearLayout.LayoutParams lp = new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT);
        lp.setMargins(0, 0, 0, dp(context, 4));
        parent.addView(card, lp);
        return card;
    }

    public static TextView label(Context context, LinearLayout parent, String text) {
        TextView view = new TextView(context);
        view.setText(text);
        view.setTextSize(12.5f);
        view.setLetterSpacing(0.05f);
        view.setTextColor(context.getResources().getColor(R.color.ink_soft));
        parent.addView(view, new LinearLayout.LayoutParams(
                ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.WRAP_CONTENT));
        return view;
    }
}
