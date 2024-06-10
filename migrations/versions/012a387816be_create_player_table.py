"""create player table

Revision ID: 012a387816be
Revises: 
Create Date: 2024-06-10 18:02:30.920137

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "012a387816be"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "player",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=20), nullable=False),
        sa.Column("gold", sa.Integer(), nullable=False),
        sa.Column("attack_value", sa.Integer(), nullable=False),
        sa.Column("hit_points", sa.Integer(), nullable=False),
        sa.Column("luck_value", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )


def downgrade():
    op.drop_table("player")
