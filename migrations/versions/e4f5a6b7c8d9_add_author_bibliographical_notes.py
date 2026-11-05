"""Add authors.bibliographical_notes for installment-8 documented-only works.

Nullable TEXT. Used to record writings that are documented but that cannot
honestly be given a full work record (lost or fragmentary titles, works known
only from a periodical reference), so the bibliography is complete without
inventing records.

Revision ID: e4f5a6b7c8d9
Revises: d3e4f5a6b7c8
"""

from alembic import op
import sqlalchemy as sa

revision: str = "e4f5a6b7c8d9"
down_revision: str = "d3e4f5a6b7c8"


def upgrade() -> None:
    op.add_column("authors", sa.Column("bibliographical_notes", sa.Text(), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table("authors", schema=None) as batch_op:
        batch_op.drop_column("bibliographical_notes")
