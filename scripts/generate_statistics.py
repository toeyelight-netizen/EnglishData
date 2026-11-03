"""Generate database statistics and write them to documentation/statistics.md.

Usage:
    python scripts/generate_statistics.py
"""

import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from sqlalchemy import text  # noqa: E402

from models import get_session  # noqa: E402


def scalar(session, query, **params):
    return session.execute(text(query), params).scalar()


def main() -> int:
    session = get_session()
    stats = {}
    try:
        stats["authors"] = scalar(session, "SELECT COUNT(*) FROM authors")
        stats["works"] = scalar(session, "SELECT COUNT(*) FROM works")
        stats["anonymous_works"] = scalar(
            session, "SELECT COUNT(*) FROM works WHERE authorship_status = 'anonymous'")
        stats["periods"] = scalar(session, "SELECT COUNT(*) FROM periods")
        stats["movements"] = scalar(session, "SELECT COUNT(*) FROM movements")
        stats["genres"] = scalar(session, "SELECT COUNT(*) FROM genres")
        stats["themes"] = scalar(session, "SELECT COUNT(*) FROM themes")
        stats["sources"] = scalar(session, "SELECT COUNT(*) FROM sources")
        stats["work_editions"] = scalar(session, "SELECT COUNT(*) FROM work_editions")
        stats["author_influence_links"] = scalar(session, "SELECT COUNT(*) FROM author_influences")

        per_genre = defaultdict(int)
        for genre, count in session.execute(text(
            "SELECT g.name, COUNT(wg.work_id) FROM genres g "
            "LEFT JOIN work_genres wg ON wg.genre_id = g.genre_id GROUP BY g.name"
        )):
            per_genre[genre] = count

        per_theme = defaultdict(int)
        for theme, count in session.execute(text(
            "SELECT t.name, COUNT(wt.work_id) FROM themes t "
            "LEFT JOIN work_themes wt ON wt.theme_id = t.theme_id GROUP BY t.name"
        )):
            per_theme[theme] = count

        per_period = session.execute(text(
            "SELECT p.name, COUNT(wp.work_id) FROM periods p "
            "LEFT JOIN work_periods wp ON wp.period_id = p.period_id GROUP BY p.name"
        )).fetchall()

        per_movement = session.execute(text(
            "SELECT m.name, COUNT(wm.work_id) FROM movements m "
            "LEFT JOIN work_movements wm ON wm.movement_id = m.movement_id GROUP BY m.name"
        )).fetchall()
    finally:
        session.close()

    lines = [
        "# Database Statistics",
        "",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Totals",
        "",
        "| Entity | Count |",
        "|---|---|",
        f"| Authors | {stats['authors']} |",
        f"| Works | {stats['works']} |",
        f"| Anonymous works | {stats['anonymous_works']} |",
        f"| Periods | {stats['periods']} |",
        f"| Movements | {stats['movements']} |",
        f"| Genres | {stats['genres']} |",
        f"| Themes | {stats['themes']} |",
        f"| Sources | {stats['sources']} |",
        f"| Editions recorded | {stats['work_editions']} |",
        f"| Author influence links | {stats['author_influence_links']} |",
        "",
        "## Works per period",
        "",
        "| Period | Works |",
        "|---|---|",
    ]
    for name, count in per_period:
        lines.append(f"| {name} | {count} |")
    lines += ["", "## Works per movement", "", "| Movement | Works |", "|---|---|"]
    for name, count in per_movement:
        lines.append(f"| {name} | {count} |")
    lines += ["", "## Works per genre", "", "| Genre | Works |", "|---|---|"]
    for name, count in sorted(per_genre.items(), key=lambda x: -x[1]):
        lines.append(f"| {name} | {count} |")
    lines += ["", "## Works per theme", "", "| Theme | Works |", "|---|---|"]
    for name, count in sorted(per_theme.items(), key=lambda x: -x[1]):
        lines.append(f"| {name} | {count} |")

    path = PROJECT_ROOT / "documentation" / "statistics.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Statistics written to {path}")
    print(f"  authors={stats['authors']}, works={stats['works']}, "
          f"anonymous={stats['anonymous_works']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
