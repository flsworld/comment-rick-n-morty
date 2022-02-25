"""creating comment table
Revision ID: 79828ed16a2b
Revises: 43659a23ea92
Create Date: 2022-02-24 14:18:10.202568
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic
revision = "79828ed16a2b"
down_revision = "43659a23ea92"
branch_labels = None
depends_on = None


def alter_assoc_table() -> None:
    op.add_column("character_episode", sa.Column("comment_id", sa.Integer))


def create_user_table() -> None:
    op.create_table(
        "user",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False),
    )


def create_comment_table() -> None:
    op.create_table(
        "comment",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("text", sa.Text),
        sa.Column("user_id", sa.Integer),
    )


def upgrade() -> None:
    alter_assoc_table()
    create_user_table()
    create_comment_table()


def downgrade() -> None:
    op.drop_table("user")
    op.drop_table("comment")
    op.drop_column("character_episode", "comment_id")
