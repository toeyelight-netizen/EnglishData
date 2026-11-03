"""Initialize the SQLite database: schema, foreign keys, and FTS5 indexes.

The canonical creation path is ``alembic upgrade head`` (see migrations/).
This script is a self-contained convenience that produces the same schema via
``Base.metadata.create_all`` plus the FTS5 virtual tables and triggers. It is
idempotent: existing tables are left untouched.

Usage:
    python scripts/initialize_database.py
"""

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from models import Base, DATABASE_DIR, DATABASE_PATH, engine  # noqa: E402

FTS_STATEMENTS = [
    """CREATE VIRTUAL TABLE IF NOT EXISTS works_fts USING fts5(
        title, description, plot_or_argument, principal_characters,
        content='works', content_rowid='work_id')""",
    """CREATE TRIGGER IF NOT EXISTS works_ai AFTER INSERT ON works BEGIN
        INSERT INTO works_fts(rowid, title, description, plot_or_argument, principal_characters)
        VALUES (new.work_id, new.title, new.description, new.plot_or_argument, new.principal_characters);
    END""",
    """CREATE TRIGGER IF NOT EXISTS works_ad AFTER DELETE ON works BEGIN
        INSERT INTO works_fts(works_fts, rowid, title, description, plot_or_argument, principal_characters)
        VALUES ('delete', old.work_id, old.title, old.description, old.plot_or_argument, old.principal_characters);
    END""",
    """CREATE TRIGGER IF NOT EXISTS works_au AFTER UPDATE ON works BEGIN
        INSERT INTO works_fts(works_fts, rowid, title, description, plot_or_argument, principal_characters)
        VALUES ('delete', old.work_id, old.title, old.description, old.plot_or_argument, old.principal_characters);
        INSERT INTO works_fts(rowid, title, description, plot_or_argument, principal_characters)
        VALUES (new.work_id, new.title, new.description, new.plot_or_argument, new.principal_characters);
    END""",
    """CREATE VIRTUAL TABLE IF NOT EXISTS authors_fts USING fts5(
        full_name, biography, literary_profile, historical_significance,
        content='authors', content_rowid='author_id')""",
    """CREATE TRIGGER IF NOT EXISTS authors_ai AFTER INSERT ON authors BEGIN
        INSERT INTO authors_fts(rowid, full_name, biography, literary_profile, historical_significance)
        VALUES (new.author_id, new.full_name, new.biography, new.literary_profile, new.historical_significance);
    END""",
    """CREATE TRIGGER IF NOT EXISTS authors_ad AFTER DELETE ON authors BEGIN
        INSERT INTO authors_fts(authors_fts, rowid, full_name, biography, literary_profile, historical_significance)
        VALUES ('delete', old.author_id, old.full_name, old.biography, old.literary_profile, old.historical_significance);
    END""",
    """CREATE TRIGGER IF NOT EXISTS authors_au AFTER UPDATE ON authors BEGIN
        INSERT INTO authors_fts(authors_fts, rowid, full_name, biography, literary_profile, historical_significance)
        VALUES ('delete', old.author_id, old.full_name, old.biography, old.literary_profile, old.historical_significance);
        INSERT INTO authors_fts(rowid, full_name, biography, literary_profile, historical_significance)
        VALUES (new.author_id, new.full_name, new.biography, new.literary_profile, new.historical_significance);
    END""",
]


def main() -> None:
    DATABASE_DIR.mkdir(parents=True, exist_ok=True)
    Base.metadata.create_all(engine)

    with engine.connect() as connection:
        try:
            has_fts5 = connection.exec_driver_sql(
                "SELECT 1 FROM pragma_compile_options "
                "WHERE compile_options LIKE '%fts5%'"
            ).fetchone() is not None
        except Exception:
            has_fts5 = False
        if has_fts5:
            for statement in FTS_STATEMENTS:
                connection.exec_driver_sql(statement)
            connection.commit()
            print("FTS5 full-text indexes created (works_fts, authors_fts).")
        else:
            print("Warning: FTS5 not available in this SQLite build; "
                  "full-text search disabled.")

    print(f"Database initialized at {DATABASE_PATH}")


if __name__ == "__main__":
    main()
