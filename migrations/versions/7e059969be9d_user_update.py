"""'user_update'

Revision ID: 7e059969be9d
Revises: a88870997ff2
Create Date: 2019-01-30 15:13:01.618089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e059969be9d'
down_revision = 'a88870997ff2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('bio', sa.String(length=128), nullable=True))
    op.add_column('user', sa.Column('first_name', sa.String(length=128), nullable=True))
    op.add_column('user', sa.Column('last_name', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'bio')
    # ### end Alembic commands ###