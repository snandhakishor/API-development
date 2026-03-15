"""add foreign keys to post table

Revision ID: 875249730b16
Revises: 580322aa32ca
Create Date: 2026-03-13 02:29:42.420217

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '875249730b16'
down_revision: Union[str, Sequence[str], None] = '580322aa32ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    
    op.add_column('posts',sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table='posts',referent_table='users',
                        local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE',onupdate='CASCADE')
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('post_user_fk', table_name='posts', type_= 'foreignkey')
    op.drop_column('posts','owner_id')
    pass
