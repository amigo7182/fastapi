"""add last few colums to posts table

Revision ID: 34c5ffc8e84e
Revises: e19ac890a75f
Create Date: 2026-01-01 03:12:20.332558

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '34c5ffc8e84e'
down_revision: Union[str, Sequence[str], None] = 'e19ac890a75f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable = False, server_default = 'TRUE'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone = True), nullable = False, server_default = sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    """Downgrade schema."""
    pass
