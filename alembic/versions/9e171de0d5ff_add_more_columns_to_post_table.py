"""add more columns to post table

Revision ID: 9e171de0d5ff
Revises: 875249730b16
Create Date: 2026-03-13 03:35:20.998116

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e171de0d5ff'
down_revision: Union[str, Sequence[str], None] = '875249730b16'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('published',sa.Boolean() ,server_default='1', nullable=False))
    op.add_column('posts', sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()))
    
                  
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','published')
    op.drop_column('posts', 'created_at')
    pass
