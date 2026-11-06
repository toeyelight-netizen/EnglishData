"""Run the installment-10 verification chain, in parallel, with one exit status.

The chain used to be nine commands issued one at a time. Nothing in it depends
on anything else except the order of the first three (build, then rebuild the
database, because the importer reads the JSON), so the rest runs concurrently.

    python3 scripts/i10_gates.py            # check, build, rebuild db, then all gates
    python3 scripts/i10_gates.py --fast     # skip the slowest (tests, app export)
    python3 scripts/i10_gates.py --no-db    # content gates only, database untouched

Each gate prints one line; a failure prints the gate's own output. Exit status is
0 only when every gate passed.

The gates, and what each one is for:

    strict        the content modules pass scripts/strict_checks.py
    build         the JSON is written (author and work files, relationships)
    import        the database is rebuilt from the JSON and a fresh migration
    installment   check_installment.py 08, 09 and 10: no author is defined twice
    duplicates    check_duplicates.py: no row exists that no installment defines
    validation    validate_database.py --installment 10: no integrity issues
    audit         the audit report, coverage matrix and search tests regenerate
    export        the Android asset is regenerated and matches the database
    tests         the unittest suite passes
    statistics    documentation/statistics.md is regenerated from the database
"""

import argparse
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = sys.executable


def run(cmd, cwd=ROOT):
    t0 = time.time()
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    return p.returncode, p.stdout + p.stderr, time.time() - t0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true", help="skip the unittest suite")
    ap.add_argument("--no-db", action="store_true", help="content gates only")
    ap.add_argument("--installment", default="10")
    args = ap.parse_args()
    n = args.installment
    failures = []
    t0 = time.time()

    def gate(name, cmd, ok_codes=(0,)):
        rc, out, dt = run(cmd)
        ok = rc in ok_codes
        print("%-12s %-5s %5.1fs" % (name, "PASS" if ok else "FAIL", dt))
        if not ok:
            failures.append((name, out))
        return out

    # 1. content: one pass of the real strict checker over every wave file
    gate("preflight", [PY, "scripts/i10_preflight.py", "--all"])
    if failures:
        return finish(failures, t0)

    # 2. build the JSON
    gate("build", [PY, "scripts/build_installment.py", n])
    if failures:
        return finish(failures, t0)

    if not args.no_db:
        # 3. rebuild the database from scratch, then import
        db = os.path.join(ROOT, "database", "English_Literature_Master.db")
        if os.path.exists(db):
            os.remove(db)
        os.makedirs(os.path.dirname(db), exist_ok=True)
        rc, out, _ = run([PY, "-m", "alembic", "upgrade", "head"])
        if rc:
            failures.append(("migrate", out))
            return finish(failures, t0)
        gate("import", [PY, "scripts/import_data.py"])

        # 4. the gates, in parallel; the export must come before the audit,
        #    which compares the asset against the database
        from concurrent.futures import ThreadPoolExecutor
        gate("export", [PY, "scripts/export_app_data.py"])
        jobs = [("installment", [PY, "scripts/check_installment.py", k]) for k in ("08", "09", n)]
        jobs += [
            ("duplicates", [PY, "scripts/check_duplicates.py"]),
            ("validation", [PY, "scripts/validate_database.py", "--installment", n]),
            ("audit", [PY, "scripts/audit_installment_10.py"]),
            ("statistics", [PY, "scripts/generate_statistics.py"]),
        ]
        if not args.fast:
            jobs.append(("tests", [PY, "-m", "unittest", "discover", "-s", "tests", "-q"]))
        with ThreadPoolExecutor(max_workers=6) as pool:
            futures = [(name, pool.submit(run, cmd)) for name, cmd in jobs]
            for name, fut in futures:
                rc, out, dt = fut.result()
                ok = rc == 0
                print("%-12s %-5s %5.1fs" % (name, "PASS" if ok else "FAIL", dt))
                if not ok:
                    failures.append((name, out))

    return finish(failures, t0)


def finish(failures, t0):
    print("\n%s in %.1fs" % ("ALL GATES PASSED" if not failures else
                            "%d GATE(S) FAILED" % len(failures), time.time() - t0))
    for name, out in failures:
        print("\n===== %s =====\n%s" % (name, out[-4000:]))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
