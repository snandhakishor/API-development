"""adding new columns to the table

Revision ID: 7b250b803e25
Revises: a47ee45fc375
Create Date: 2026-03-11 02:16:08.712630

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b250b803e25'
down_revision: Union[str, Sequence[str], None] = 'a47ee45fc375'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(255), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
