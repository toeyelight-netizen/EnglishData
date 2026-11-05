# English Literature — Android App

A fast, offline Android app for browsing and searching the English Literature
Database (c. 450–2000). Built entirely with the Android framework (Java 8) —
no AndroidX, no Kotlin, no external libraries — so the APK is small (≈3.7 MB)
and starts instantly.

## Features

- **Search bar** — search authors or their works; diacritic-insensitive, so
  `caedmon` finds *Cædmon* and `meihhad` finds *Hali Meiðhad*. Results are
  ranked (exact > prefix > contains) and appear as you type.
- **Browse** — clear the search to browse all 579 authors and 2226 works,
  grouped by section. Installment 8 (Victorian and American nineteenth
  century, 1832-1901) contributes 161 authors and 771 works, including the
  whole British Victorian canon and the American strand from Emerson to
  Edith Wharton.
- **Canon filter** — a `Canon` spinner above the list narrows the library to
  authors at or above a significance tier: **Major** (45 authors, 287 works),
  **Significant** (106 / 564), **Minor** (157 / 756) or **Neglected**
  (161 / 771), plus **All** (579 / 2226). Each level is a floor, not a single
  tier, so Major is nested inside Significant and so on; the filter applies to
  search as well as browse, and the header shows the live counts ("45 authors
  · 287 works · Major and above"). Ungraded authors appear only under **All**.
  The database grades 161 of 579 authors — the whole of installment 8 — so the
  filter is most useful on Victorian material.
- **Author pages** — biography, literary profile, style, themes, movements,
  sources, the author's works, and a standing badge when the author is graded.
- **Work pages** — summary, plot, characters, structure, meter, editions,
  sources, and tappable author links.
- **Splash screen** — medieval-fantasy logo and the credit
  **"Developed by Saeed Lotfi"**.
- **Medieval fantasy app logo** — golden dragon, open book, quill and castle
  in burgundy and gold; adaptive icons (API 26+) plus a system splash
  (API 31+).
- **Dark mode** — a parchment-and-ink night theme via `values-night`.
- **Offline** — the whole dataset ships inside the APK as a compressed JSON
  asset (no network access ever needed).

## Requirements to build

- Windows x64, Python 3.10+, and the toolchain in `~/.android-build/`:

| File | Source (verified URLs) |
|---|---|
| `dl/jdk17.zip` | Adoptium: <https://api.adoptium.net/v3/binary/latest/17/ga/windows/x64/jdk/hotspot/normal/eclipse?project=jdk> |
| `dl/aapt2.jar` | Aliyun Google mirror: `https://maven.aliyun.com/repository/google/com/android/tools/build/aapt2/8.5.2-11315950/aapt2-8.5.2-11315950-windows.jar` |
| `dl/r8.jar` | Aliyun Google mirror: `https://maven.aliyun.com/repository/google/com/android/tools/r8/8.5.35/r8-8.5.35.jar` |
| `dl/apksig.jar` | Aliyun Google mirror: `https://maven.aliyun.com/repository/google/com/android/tools/build/apksig/9.5.0/apksig-9.5.0.jar` |
| `dl/android-all.jar` | Maven Central: `https://repo1.maven.org/maven2/org/robolectric/android-all/14-robolectric-10818077/android-all-14-robolectric-10818077.jar` |

(`dl.google.com` and `maven.google.com` are unreachable from the machine this
was built on; the Aliyun mirrors and Adoptium/GitHub work.)

## Build

```bash
cd android
python build.py
```

The script runs the whole pipeline with no Gradle or Android SDK:

1. extracts the JDK and `aapt2.exe` (once, cached),
2. creates `release.keystore` if missing (keytool),
3. `aapt2 compile` + `aapt2 link` (against the Robolectric android-all jar
   as `android.jar`) — generates `R.java` and the unsigned APK,
4. `javac --release 8` → `jar` → D8 (`--min-api 24`) → `classes.dex`,
5. re-packages the zip with 4-byte alignment for stored entries and a
   deflated data asset,
6. signs with apksig (v1 + v2 + v3) and verifies the signature and badging.

Output: `build/EnglishLiterature_v1.0.0.apk` (signed release build,
`minSdk 24` = Android 7.0+, `targetSdk 34`).

To update the bundled data after future database installments:

```bash
cd ..                                   # repository root
python scripts/export_app_data.py       # rewrites the JSON asset
cd android && python build.py
```

## Install on a phone

Copy `build/EnglishLiterature_v1.0.0.apk` to the device and open it, or:

```bash
adb install build/EnglishLiterature_v1.0.0.apk
```

The APK is signed with the local `release.keystore` (alias `literature`,
password `english-literature-2026`). Keep that keystore file — reinstalls and
updates must be signed with the same key. If you later publish to a store,
generate a fresh private keystore and keep it secret.

## Layout

```
android/
|-- app/src/main/
|   |-- AndroidManifest.xml
|   |-- assets/data/english_literature.json   # exported from the master DB
|   |-- java/com/saeedlotfi/englishliterature/
|   |   |-- SplashActivity.java  MainActivity.java
|   |   |-- AuthorDetailActivity.java  WorkDetailActivity.java
|   |   |-- data/    (Author, Work, Library: load, index, search)
|   |   `-- ui/      (SearchAdapter, view helpers)
|   `-- res/         (themes incl. night + splash, icons, layouts)
|-- tools/           (SignApk.java, VerifyApk.java — apksig wrappers)
|-- build.py         (the whole build)
`-- release.keystore (generated on first build; do not lose)
```

## Screens

- **Splash** — burgundy, logo, "English Literature", gold divider,
  "Developed by Saeed Lotfi", tagline.
- **Home** — burgundy header, rounded search field, parchment list of
  author/work cards.
- **Detail** — burgundy hero header with genre/movement chips, parchment
  content cards with gold section headings.
