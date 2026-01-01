"""add foreign key to posts table

Revision ID: e19ac890a75f
Revises: 99da4c0498cc
Create Date: 2026-01-01 03:05:29.688320

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e19ac890a75f'
down_revision: Union[str, Sequence[str], None] = '99da4c0498cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key("posts_users_fk", source_table = 'posts', referent_table = 'users', local_cols = ['owner_id'], remote_cols = ['id'], ondelete = 'CASCADE')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("posts_users_fk", table_name = 'posts')
    op.drop_column('posts', 'owner_id')
    pass
