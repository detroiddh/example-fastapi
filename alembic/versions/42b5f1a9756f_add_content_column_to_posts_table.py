"""add content column to posts table

Revision ID: 42b5f1a9756f
Revises: e509cf0e67ca
Create Date: 2025-08-01 21:30:51.967414

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42b5f1a9756f'
down_revision: Union[str, Sequence[str], None] = 'e509cf0e67ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
