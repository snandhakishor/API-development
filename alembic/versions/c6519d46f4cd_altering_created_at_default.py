"""altering created_at default

Revision ID: c6519d46f4cd
Revises: 7657e29b0150
Create Date: 2026-03-17 01:16:42.758802

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6519d46f4cd'
down_revision: Union[str, Sequence[str], None] = '7657e29b0150'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('posts', 'created_at', existing_nullable=False ,existing_type= sa.DateTime(timezone=True),
                    server_default=sa.func.now())
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('posts', 'created_at', existing_nullable=False, existing_type=sa.DateTime(timezone=True),
                    server_default=None)
    pass
