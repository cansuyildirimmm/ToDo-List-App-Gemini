"""phone number added

Revision ID: 60d0e72c81bb
Revises: 
Create Date: 2025-03-18 06:20:31.994261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60d0e72c81bb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String(),nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    pass
