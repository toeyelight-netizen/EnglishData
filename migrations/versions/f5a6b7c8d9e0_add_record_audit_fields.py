"""Add per-record audit fields used from installment 10 onwards.

works.thematic_analysis   TEXT        the principal themes, explained (not keywords)
works.critical_context    TEXT        critical interpretations, controversies, reception
works.verification_status VARCHAR(32) verified | partially verified | unverified
authors.bibliography_status   VARCHAR(32) complete | substantially complete | incomplete
authors.verification_status   VARCHAR(32) verified | partially verified | unverified

All nullable, so installments 1-9 are untouched (NULL = not assessed).

Revision ID: f5a6b7c8d9e0
Revises: e4f5a6b7c8d9
"""

from alembic import op
import sqlalchemy as sa

revision: str = "f5a6b7c8d9e0"
down_revision: str = "e4f5a6b7c8d9"


def upgrade() -> None:
    op.add_column("works", sa.Column("thematic_analysis", sa.Text(), nullable=True))
    op.add_column("works", sa.Column("critical_context", sa.Text(), nullable=True))
    op.add_column("works", sa.Column("verification_status", sa.String(length=32), nullable=True))
    op.add_column("authors", sa.Column("bibliography_status", sa.String(length=32), nullable=True))
    op.add_column("authors", sa.Column("verification_status", sa.String(length=32), nullable=True))


def downgrade() -> None:
    with op.batch_alter_table("works", schema=None) as batch_op:
        batch_op.drop_column("verification_status")
        batch_op.drop_column("critical_context")
        batch_op.drop_column("thematic_analysis")
    with op.batch_alter_table("authors", schema=None) as batch_op:
        batch_op.drop_column("verification_status")
        batch_op.drop_column("bibliography_status")
