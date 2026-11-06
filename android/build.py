#!/usr/bin/env python3
"""Deterministic, SDK-free APK build for the English Literature app.

Toolchain (downloaded once into ~/.android-build/, see tools/fetch_toolchain.py):
  dl/jdk/          JRE + JDK class files (jdk4py PyPI wheel, or any JDK 17+)
  tools/aapt2      aapt2 (Linux/macOS binary or aapt2.exe on Windows)
  dl/r8.jar        D8 (com.android.tools.r8.D8)
  dl/apksig.jar    apksig (v1+v2+v3 signing)
  dl/tools.jar     OpenJDK 8 tools.jar supplying com.sun.tools.javac.Main when
                   the JDK ships no javac binary
  dl/android-all.jar   platform android.jar (API 34)
No Gradle, no Android SDK, no network access needed at build time.

Usage:
    python build.py                    # -> build/EnglishLiterature_v1.0.0.apk
    python build.py --skip-sign-check  # faster rebuilds
"""

import glob
import os
import shutil
import struct
import subprocess
import sys
import zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
TOOLCHAIN = os.environ.get(
    "ANDROID_BUILD_HOME",
    os.path.join(os.path.expanduser("~"), ".android-build"))
DL = os.path.join(TOOLCHAIN, "dl")
TOOLS = os.path.join(TOOLCHAIN, "tools")

APP = os.path.join(ROOT, "app", "src", "main")
RES = os.path.join(APP, "res")
ASSETS = os.path.join(APP, "assets")
MANIFEST = os.path.join(APP, "AndroidManifest.xml")
JAVA_SRC = os.path.join(APP, "java")

BUILD = os.path.join(ROOT, "build")
GEN = os.path.join(BUILD, "gen")
CLASSES = os.path.join(BUILD, "classes")
DEX = os.path.join(BUILD, "dex")

KEYSTORE = os.path.join(ROOT, "release.keystore")
KEY_ALIAS = "literature"
KEY_PASS = "english-literature-2026"

VERSION_NAME = "1.0.0"
OUT_APK = os.path.join(BUILD, "EnglishLiterature_v%s.apk" % VERSION_NAME)

ANDROID_JAR = os.path.join(DL, "android-all.jar")
R8_JAR = os.path.join(DL, "r8.jar")
APKSIG_JAR = os.path.join(DL, "apksig.jar")
TOOLS_JAR = os.path.join(DL, "tools.jar")
JDK_ZIP = os.path.join(DL, "jdk17.zip")

IS_WINDOWS = os.name == "nt"
EXE = ".exe" if IS_WINDOWS else ""


def run(cmd):
    print("+ " + " ".join('"%s"' % c if " " in c else c for c in cmd))
    subprocess.check_call(cmd)


def ensure_jdk():
    java = os.path.join(TOOLCHAIN, "jdk", "bin", "java" + EXE)
    if os.path.isfile(java):
        return os.path.join(TOOLCHAIN, "jdk")
    os.makedirs(TOOLCHAIN, exist_ok=True)
    print("Extracting JDK from %s ..." % JDK_ZIP)
    with zipfile.ZipFile(JDK_ZIP) as z:
        z.extractall(TOOLCHAIN)
    homes = glob.glob(os.path.join(TOOLCHAIN, "*", "bin", "java" + EXE))
    if not homes:
        sys.exit("error: no bin/java.exe found after extracting " + JDK_ZIP)
    jdk = os.path.dirname(os.path.dirname(homes[0]))
    if not os.path.isfile(os.path.join(TOOLCHAIN, "jdk", "bin", "java" + EXE)):
        try:
            os.replace(jdk, os.path.join(TOOLCHAIN, "jdk"))
        except OSError:
            pass  # already normalized
    return os.path.join(TOOLCHAIN, "jdk")


def ensure_aapt2():
    exe = os.path.join(TOOLS, "aapt2" + EXE)
    if os.path.isfile(exe):
        if not IS_WINDOWS:
            os.chmod(exe, 0o755)
        return exe
    jar = os.path.join(DL, "aapt2.jar")
    if os.path.isfile(jar):
        os.makedirs(TOOLS, exist_ok=True)
        print("Extracting aapt2 from %s ..." % jar)
        with zipfile.ZipFile(jar) as z:
            member = "aapt2.exe" if IS_WINDOWS else "aapt2"
            with z.open(member) as src, open(exe, "wb") as dst:
                shutil.copyfileobj(src, dst)
        return exe
    sys.exit("error: no aapt2 binary at %s (run tools/fetch_toolchain.py)" % exe)


def javac_cmd(java, jdk):
    """Prefer a real javac binary; fall back to javac inside tools.jar."""
    exe = os.path.join(jdk, "bin", "javac" + EXE)
    if os.path.isfile(exe):
        return [exe]
    if os.path.isfile(TOOLS_JAR):
        return [java, "-cp", TOOLS_JAR, "com.sun.tools.javac.Main"]
    sys.exit("error: neither javac nor %s is available" % TOOLS_JAR)


def ensure_keystore(keytool):
    if os.path.isfile(KEYSTORE):
        return
    run([keytool, "-genkeypair", "-keystore", KEYSTORE, "-storetype", "PKCS12",
         "-storepass", KEY_PASS, "-keypass", KEY_PASS, "-alias", KEY_ALIAS,
         "-keyalg", "RSA", "-keysize", "2048", "-validity", "10950",
         "-dname", "CN=Saeed Lotfi, OU=English Literature, O=English Literature Database"])


def align_entry(zout, info):
    """Pad the entry's extra field so its data starts 4-byte aligned."""
    pos = zout.fp.tell()
    name_len = len(info.filename.encode("utf-8"))
    pad = (-(pos + 30 + name_len + 4)) % 4
    if pad:
        info.extra = struct.pack("<HH", 0xD935, pad) + b"\x00" * pad


def repack(in_path, out_path, extra_files):
    """Rebuild the APK zip: 4-byte-align stored entries, deflate assets,
    append the dex file."""
    with zipfile.ZipFile(in_path, "r") as zin:
        with zipfile.ZipFile(out_path, "w") as zout:
            for info in zin.infolist():
                data = zin.read(info.filename)
                new_info = zipfile.ZipInfo(info.filename, info.date_time)
                new_info.external_attr = info.external_attr
                if info.filename.startswith("assets/"):
                    new_info.compress_type = zipfile.ZIP_DEFLATED
                else:
                    new_info.compress_type = zipfile.ZIP_STORED
                    align_entry(zout, new_info)
                zout.writestr(new_info, data)
            for name, data in extra_files.items():
                info = zipfile.ZipInfo(name)
                info.compress_type = zipfile.ZIP_STORED
                info.external_attr = 0o100644 << 16
                align_entry(zout, info)
                zout.writestr(info, data)


def check_alignment(path):
    with zipfile.ZipFile(path) as z:
        for info in z.infolist():
            if info.compress_type == zipfile.ZIP_STORED:
                off = (info.header_offset + 30
                       + len(info.filename.encode("utf-8")) + len(info.extra))
                if info.filename in ("resources.arsc", "classes.dex") and off % 4 != 0:
                    sys.exit("error: %s not 4-byte aligned (%d)" % (info.filename, off))
    print("Alignment OK (resources.arsc, classes.dex 4-byte aligned).")


def main():
    skip_sign_check = "--skip-sign-check" in sys.argv
    for needed in (ANDROID_JAR, R8_JAR, APKSIG_JAR):
        if not os.path.isfile(needed):
            sys.exit("error: missing toolchain file %s (run tools/fetch_toolchain.py)" % needed)

    jdk = ensure_jdk()
    java = os.path.join(jdk, "bin", "java" + EXE)
    javac = javac_cmd(java, jdk)
    keytool = os.path.join(jdk, "bin", "keytool" + EXE)
    aapt2 = ensure_aapt2()

    if os.path.isdir(BUILD):
        shutil.rmtree(BUILD)
    os.makedirs(GEN)
    os.makedirs(CLASSES)

    ensure_keystore(keytool)

    # 1. Compile and link resources.
    res_zip = os.path.join(BUILD, "compiled_res.zip")
    run([aapt2, "compile", "--dir", RES, "-o", res_zip])
    unsigned = os.path.join(BUILD, "unsigned.apk")
    run([aapt2, "link", "-o", unsigned, "-I", ANDROID_JAR,
         "--manifest", MANIFEST, "--java", GEN, "-A", ASSETS,
         "--min-sdk-version", "24", "--target-sdk-version", "34",
         res_zip])

    # 2. Compile Java sources (app + generated R.java) against android.jar.
    sources = []
    for base in (JAVA_SRC, GEN):
        for root, _, files in os.walk(base):
            for f in files:
                if f.endswith(".java"):
                    sources.append(os.path.join(root, f))
    sources_file = os.path.join(BUILD, "sources.txt")
    with open(sources_file, "w", encoding="utf-8") as f:
        for s in sorted(sources):
            f.write(s + "\n")
    javac_extra = ["-source", "8", "-target", "8", "-bootclasspath", ANDROID_JAR] \
        if len(javac) > 1 else ["--release", "8", "-cp", ANDROID_JAR]
    run(javac + ["-encoding", "UTF-8"] + javac_extra + ["-d", CLASSES, "@" + sources_file])

    # 3. Dex with D8.
    classes_jar = os.path.join(BUILD, "classes.jar")
    with zipfile.ZipFile(classes_jar, "w", zipfile.ZIP_DEFLATED) as jar_zip:
        for root, _, files in os.walk(CLASSES):
            for f in files:
                full = os.path.join(root, f)
                jar_zip.write(full, os.path.relpath(full, CLASSES))
    os.makedirs(DEX)
    run([java, "-cp", R8_JAR, "com.android.tools.r8.D8",
         "--release", "--min-api", "24", "--lib", ANDROID_JAR,
         "--output", DEX, classes_jar])
    dex_path = os.path.join(DEX, "classes.dex")
    with open(dex_path, "rb") as f:
        dex_bytes = f.read()

    # 4. Package: align stored entries, deflate assets, add classes.dex.
    aligned = os.path.join(BUILD, "aligned.unsigned.apk")
    repack(unsigned, aligned, {"classes.dex": dex_bytes})
    check_alignment(aligned)

    # 5. Sign (v1 + v2 + v3) with apksig's own CLI.
    run([java, "-jar", APKSIG_JAR, "sign",
         "--ks", KEYSTORE, "--ks-key-alias", KEY_ALIAS,
         "--ks-pass", "pass:" + KEY_PASS, "--key-pass", "pass:" + KEY_PASS,
         "--min-sdk-version", "24", "--v1-signing-enabled", "true",
         "--v2-signing-enabled", "true", "--v3-signing-enabled", "true",
         "--out", OUT_APK, aligned])

    # 6. Verify signature and APK metadata.
    if not skip_sign_check:
        run([java, "-jar", APKSIG_JAR, "verify", "--min-sdk-version", "24", OUT_APK])

    badging = subprocess.run(
        [aapt2, "dump", "badging", OUT_APK],
        capture_output=True, text=True, encoding="utf-8", errors="replace")
    if badging.returncode != 0:
        sys.exit("error: aapt2 dump badging failed:\n" + badging.stderr)
    for line in badging.stdout.splitlines():
        if line.startswith(("package:", "sdkVersion", "targetSdkVersion",
                            "application-label", "launchable-activity")):
            print(line)
    if "com.saeedlotfi.englishliterature" not in badging.stdout \
            or "launchable-activity" not in badging.stdout:
        sys.exit("error: badging output missing package or launcher activity")

    size = os.path.getsize(OUT_APK)
    print("\nBUILD OK: %s (%.1f MB)" % (OUT_APK, size / (1024.0 * 1024.0)))


if __name__ == "__main__":
    main()
