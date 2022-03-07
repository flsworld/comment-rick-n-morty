"""create main tables
Revision ID: 43659a23ea92
Revises:
Create Date: 2022-02-18 13:24:38.668314
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic
revision = "43659a23ea92"
down_revision = None
branch_labels = None
depends_on = None


def create_character_table() -> None:
    op.create_table(
        "character",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("status", sa.Text, nullable=False),
        sa.Column("species", sa.Text, nullable=False),
        sa.Column("type", sa.Text, nullable=False),
        sa.Column("gender", sa.Text, nullable=False),
    )


def create_episode_table() -> None:
    op.create_table(
        "episode",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False),
        sa.Column("air_date", sa.Date, nullable=False),
        sa.Column("segment", sa.Text, nullable=False),
    )


def create_association_table() -> None:
    op.create_table(
        "character_episode",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("character_id", sa.Integer),
        sa.Column("episode_id", sa.Integer),
    )
    op.create_unique_constraint(
        "_character_episode_uc", "character_episode", ["character_id", "episode_id"]
    )


def upgrade() -> None:
    create_character_table()
    create_episode_table()
    create_association_table()


def downgrade() -> None:
    op.drop_table("character")
    op.drop_table("episode")
    op.drop_table("character_episode")
