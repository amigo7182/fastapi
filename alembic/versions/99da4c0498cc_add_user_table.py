"""add user table

Revision ID: 99da4c0498cc
Revises: 8ac04039acf1
Create Date: 2025-12-31 22:36:26.813220

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '99da4c0498cc'
down_revision: Union[str, Sequence[str], None] = '8ac04039acf1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("users",
                    sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
                    sa.Column('email', sa.String(), nullable = False, unique = True),
                    sa.Column('password', sa.String(), nullable = False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone = True), server_default = sa.text('now()'), nullable = False)
                    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
