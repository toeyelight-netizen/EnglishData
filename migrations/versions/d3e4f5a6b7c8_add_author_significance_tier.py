"""Add author significance_tier for the searchable significance classification.

Nullable VARCHAR(64) on ``authors``. Installments 1-7 predate the column and keep
NULL, which the data dictionary defines as "not yet graded"; the application
treats NULL separately from the graded tiers so that no earlier record is
silently re-classified.

Revision ID: d3e4f5a6b7c8
Revises: c2d3e4f5a6b7
"""

from alembic import op
import sqlalchemy as sa

revision: str = "d3e4f5a6b7c8"
down_revision: str = "c2d3e4f5a6b7"


def upgrade() -> None:
    op.add_column("authors", sa.Column("significance_tier", sa.String(length=64), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table("authors", schema=None) as batch_op:
        batch_op.drop_column("significance_tier")
