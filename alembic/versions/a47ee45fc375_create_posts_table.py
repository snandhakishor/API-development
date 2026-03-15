"""create posts table

Revision ID: a47ee45fc375
Revises: 
Create Date: 2026-03-11 01:58:59.060922

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a47ee45fc375'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("posts",sa.Column('id', sa.Integer(), primary_key=True, nullable=False)
                           ,sa.Column('title', sa.String(255), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
    pass
