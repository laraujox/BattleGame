"""create round and battle table

Revision ID: b14e7d72bdc7
Revises: 012a387816be
Create Date: 2024-06-10 19:53:01.752948

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b14e7d72bdc7"
down_revision = "012a387816be"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "battle",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("player1_id", sa.Integer(), nullable=False),
        sa.Column("player2_id", sa.Integer(), nullable=False),
        sa.Column("winner_id", sa.Integer(), nullable=True),
        sa.Column("gold_stolen", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["player1_id"],
            ["player.id"],
        ),
        sa.ForeignKeyConstraint(
            ["player2_id"],
            ["player.id"],
        ),
        sa.ForeignKeyConstraint(
            ["winner_id"],
            ["player.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "round",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("battle_id", sa.Integer(), nullable=False),
        sa.Column("log", sa.String(length=100), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["battle_id"],
            ["battle.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("round")
    op.drop_table("battle")
    # ### end Alembic commands ###
