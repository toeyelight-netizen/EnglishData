#!/usr/bin/env python3
"""Compile and run the tier-logic assertions on the desktop JVM.

The app classes are plain Java (no AndroidX), so the pure helpers in Library
can be exercised against the stubbed android-all.jar without an emulator.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUILD = Path.home() / ".android-build"
JAVA = BUILD / "jdk" / "bin" / "java"
ANDROID_JAR = BUILD / "dl" / "android-all.jar"
TOOLS_JAR = BUILD / "dl" / "tools.jar"

SRC = ROOT / "android" / "app" / "src" / "main" / "java"
APP = SRC / "com" / "saeedlotfi" / "englishliterature"
DATA = APP / "data"


def main():
    classes = Path(tempfile.mkdtemp(prefix="tier-test-"))
    try:
        cmd = [
            str(JAVA), "-cp", str(TOOLS_JAR), "com.sun.tools.javac.Main",
            "-encoding", "UTF-8", "-source", "8", "-target", "8",
            "-bootclasspath", str(ANDROID_JAR), "-d", str(classes),
            str(ROOT / "android" / "tools" / "TierLogicTest.java"),
            str(DATA / "Library.java"), str(DATA / "Author.java"),
            str(DATA / "Work.java"),
        ]
        subprocess.check_call(cmd)
        run = [str(JAVA), "-cp", os.pathsep.join([str(classes), str(ANDROID_JAR)]),
               "TierLogicTest"]
        subprocess.check_call(run)
    finally:
        shutil.rmtree(classes, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main())
