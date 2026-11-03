package com.saeedlotfi.englishliterature;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;

import com.saeedlotfi.englishliterature.data.Library;

/** Loading screen with the app credit, then on to the search screen. */
public final class SplashActivity extends Activity {

    private static final long MIN_SPLASH_MS = 1500;

    private final Handler handler = new Handler(Looper.getMainLooper());
    private boolean finished = false;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);

        final long startedAt = System.currentTimeMillis();
        Library.get().ensureLoaded(this, new Runnable() {
            @Override
            public void run() {
                long remaining = MIN_SPLASH_MS - (System.currentTimeMillis() - startedAt);
                handler.postDelayed(new Runnable() {
                    @Override
                    public void run() {
                        proceed();
                    }
                }, Math.max(0L, remaining));
            }
        });
    }

    private void proceed() {
        if (finished) return;
        finished = true;
        startActivity(new Intent(this, MainActivity.class));
        overridePendingTransition(android.R.anim.fade_in, android.R.anim.fade_out);
        finish();
    }

    @Override
    protected void onDestroy() {
        handler.removeCallbacksAndMessages(null);
        super.onDestroy();
    }
}
