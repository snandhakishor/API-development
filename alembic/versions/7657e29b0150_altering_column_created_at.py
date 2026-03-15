"""altering column created_at

Revision ID: 7657e29b0150
Revises: 992f2323ae29
Create Date: 2026-03-16 03:07:29.887088

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7657e29b0150'
down_revision: Union[str, Sequence[str], None] = '992f2323ae29'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('posts', 'created', nullable=False, existing_type= sa.DateTime(timezone=True),
                    server_default=sa.func.now(), new_column_name='created_at')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('posts','created', existing_type=sa.DateTime(timezone=True),
                    server_default=None, new_column_name='created')

    pass
