"""Add work detail columns for Anglo-Latin and expanded work records.

Adds ten nullable columns to ``works``: composition_date_circa, summary,
significance, provenance_and_manuscripts, editions, modern_translations,
related_works, manuscript_locations, canonical_status, research_notes.
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "c2d3e4f5a6b7"
down_revision: str = "c1f2a3b4d5e6"

NEW_COLUMNS = [
    ("composition_date_circa", sa.Boolean()),
    ("summary", sa.Text()),
    ("significance", sa.Text()),
    ("provenance_and_manuscripts", sa.Text()),
    ("editions", sa.Text()),
    ("modern_translations", sa.Text()),
    ("related_works", sa.Text()),
    ("manuscript_locations", sa.Text()),
    ("canonical_status", sa.String(length=32)),
    ("research_notes", sa.Text()),
]


def upgrade() -> None:
    for name, column_type in NEW_COLUMNS:
        op.add_column("works", sa.Column(name, column_type, nullable=True))


def downgrade() -> None:
    with op.batch_alter_table("works", schema=None) as batch_op:
        for name, _ in NEW_COLUMNS:
            batch_op.drop_column(name)
