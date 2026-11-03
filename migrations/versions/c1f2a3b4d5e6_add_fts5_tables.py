"""Add FTS5 full-text search tables for works and authors.

Creates two external-content FTS5 tables (``works_fts``, ``authors_fts``) with
insert/update/delete triggers so the indexes stay in sync with the base tables.
If FTS5 is unavailable in the SQLite build, the migration is skipped gracefully.
"""

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "c1f2a3b4d5e6"
down_revision: str = "ccac64cc3f25"

FTS_STATEMENTS = [
    """CREATE VIRTUAL TABLE IF NOT EXISTS works_fts USING fts5(
        title,
        description,
        plot_or_argument,
        principal_characters,
        content='works',
        content_rowid='work_id'
    )""",
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
        full_name,
        biography,
        literary_profile,
        historical_significance,
        content='authors',
        content_rowid='author_id'
    )""",
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

DROP_STATEMENTS = [
    "DROP TRIGGER IF EXISTS works_ai",
    "DROP TRIGGER IF EXISTS works_ad",
    "DROP TRIGGER IF EXISTS works_au",
    "DROP TRIGGER IF EXISTS authors_ai",
    "DROP TRIGGER IF EXISTS authors_ad",
    "DROP TRIGGER IF EXISTS authors_au",
    "DROP TABLE IF EXISTS works_fts",
    "DROP TABLE IF EXISTS authors_fts",
]


def _fts5_available() -> bool:
    connection = op.get_bind()
    row = connection.exec_driver_sql(
        "SELECT 1 FROM pragma_compile_options WHERE compile_options LIKE '%fts5%'"
    ).fetchone()
    return row is not None


def upgrade() -> None:
    if not _fts5_available():
        return
    for statement in FTS_STATEMENTS:
        op.execute(statement)


def downgrade() -> None:
    if not _fts5_available():
        return
    for statement in DROP_STATEMENTS:
        op.execute(statement)
