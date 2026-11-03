#!/usr/bin/env python3
"""Deterministic, SDK-free APK build for the English Literature app.

Toolchain (downloaded once into ~/.android-build/): JDK 17, aapt2, D8 (r8),
apksig, and a Robolectric android-all jar standing in for android.jar.
No Gradle, no Android SDK, no network access needed at build time.

Usage:
    python build.py          # builds build/EnglishLiterature_v1.0.0.apk
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

AAPT2_JAR = os.path.join(DL, "aapt2.jar")
ANDROID_JAR = os.path.join(DL, "android-all.jar")
R8_JAR = os.path.join(DL, "r8.jar")
APKSIG_JAR = os.path.join(DL, "apksig.jar")
JDK_ZIP = os.path.join(DL, "jdk17.zip")


def run(cmd):
    print("+ " + " ".join('"%s"' % c if " " in c else c for c in cmd))
    subprocess.check_call(cmd)


def ensure_jdk():
    java = os.path.join(TOOLCHAIN, "jdk", "bin", "java.exe")
    if os.path.isfile(java):
        return os.path.join(TOOLCHAIN, "jdk")
    os.makedirs(TOOLCHAIN, exist_ok=True)
    print("Extracting JDK from %s ..." % JDK_ZIP)
    with zipfile.ZipFile(JDK_ZIP) as z:
        z.extractall(TOOLCHAIN)
    homes = glob.glob(os.path.join(TOOLCHAIN, "*", "bin", "java.exe"))
    if not homes:
        sys.exit("error: no bin/java.exe found after extracting " + JDK_ZIP)
    jdk = os.path.dirname(os.path.dirname(homes[0]))
    if not os.path.isfile(os.path.join(TOOLCHAIN, "jdk", "bin", "java.exe")):
        try:
            os.replace(jdk, os.path.join(TOOLCHAIN, "jdk"))
        except OSError:
            pass  # already normalized
    jdk = os.path.join(TOOLCHAIN, "jdk")
    return jdk


def ensure_aapt2():
    exe = os.path.join(TOOLS, "aapt2.exe")
    if os.path.isfile(exe):
        return exe
    os.makedirs(TOOLS, exist_ok=True)
    print("Extracting aapt2.exe from %s ..." % AAPT2_JAR)
    with zipfile.ZipFile(AAPT2_JAR) as z:
        with z.open("aapt2.exe") as src, open(exe, "wb") as dst:
            shutil.copyfileobj(src, dst)
    return exe


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
    for needed in (AAPT2_JAR, ANDROID_JAR, R8_JAR, APKSIG_JAR, JDK_ZIP):
        if not os.path.isfile(needed):
            sys.exit("error: missing toolchain file %s" % needed)

    jdk = ensure_jdk()
    java = os.path.join(jdk, "bin", "java.exe")
    javac = os.path.join(jdk, "bin", "javac.exe")
    jar = os.path.join(jdk, "bin", "jar.exe")
    keytool = os.path.join(jdk, "bin", "keytool.exe")
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
    run([javac, "-encoding", "UTF-8", "--release", "8",
         "-cp", ANDROID_JAR, "-d", CLASSES, "@" + sources_file])

    # 3. Dex with D8.
    classes_jar = os.path.join(BUILD, "classes.jar")
    run([jar, "cf", classes_jar, "-C", CLASSES, "."])
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

    # 5. Sign (v1 + v2 + v3) with apksig.
    signer_classes = os.path.join(BUILD, "signer")
    os.makedirs(signer_classes)
    run([javac, "-encoding", "UTF-8", "--release", "8", "-cp", APKSIG_JAR,
         "-d", signer_classes, os.path.join(ROOT, "tools", "SignApk.java")])
    run([java, "-cp", APKSIG_JAR + os.pathsep + signer_classes, "SignApk",
         aligned, OUT_APK, KEYSTORE, KEY_ALIAS, KEY_PASS])

    # 6. Verify signature and APK metadata.
    run([javac, "-encoding", "UTF-8", "--release", "8", "-cp", APKSIG_JAR,
         "-d", signer_classes, os.path.join(ROOT, "tools", "VerifyApk.java")])
    run([java, "-cp", APKSIG_JAR + os.pathsep + signer_classes,
         "VerifyApk", OUT_APK])

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
