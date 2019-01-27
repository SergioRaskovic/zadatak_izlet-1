"""jabuka

Revision ID: b0028c33fd25
Revises: 828be6a4d36a
Create Date: 2019-01-26 21:08:56.452442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0028c33fd25'
down_revision = '828be6a4d36a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=120), nullable=True),
    sa.Column('about', sa.String(length=1000), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('min_people', sa.String(length=120), nullable=True),
    sa.Column('max_people', sa.String(length=120), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.Column('trip_rating', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_trip_about'), 'trip', ['about'], unique=False)
    op.create_index(op.f('ix_trip_cost'), 'trip', ['cost'], unique=False)
    op.create_index(op.f('ix_trip_date'), 'trip', ['date'], unique=False)
    op.create_index(op.f('ix_trip_location'), 'trip', ['location'], unique=False)
    op.create_index(op.f('ix_trip_max_people'), 'trip', ['max_people'], unique=False)
    op.create_index(op.f('ix_trip_min_people'), 'trip', ['min_people'], unique=False)
    op.create_table('user_rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_rating', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_rating')
    op.drop_index(op.f('ix_trip_min_people'), table_name='trip')
    op.drop_index(op.f('ix_trip_max_people'), table_name='trip')
    op.drop_index(op.f('ix_trip_location'), table_name='trip')
    op.drop_index(op.f('ix_trip_date'), table_name='trip')
    op.drop_index(op.f('ix_trip_cost'), table_name='trip')
    op.drop_index(op.f('ix_trip_about'), table_name='trip')
    op.drop_table('trip')
    # ### end Alembic commands ###