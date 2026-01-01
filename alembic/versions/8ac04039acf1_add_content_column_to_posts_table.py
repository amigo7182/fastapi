"""add content column to posts table

Revision ID: 8ac04039acf1
Revises: face7f71508d
Create Date: 2025-12-31 22:23:56.998279

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ac04039acf1'
down_revision: Union[str, Sequence[str], None] = 'face7f71508d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
