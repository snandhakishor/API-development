"""add users table

Revision ID: 580322aa32ca
Revises: 7b250b803e25
Create Date: 2026-03-11 02:24:22.006288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '580322aa32ca'
down_revision: Union[str, Sequence[str], None] = '7b250b803e25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('users', sa.Column('id',sa.Integer(), primary_key=True, nullable=False),
                        sa.Column('email', sa.String(255), nullable=False),
                        sa.Column('password', sa.String(255), nullable=False),
                        sa.Column('created_at', sa.DateTime(timezone=True), default=sa.func.now()))
    print("this file runs")
    pass



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
