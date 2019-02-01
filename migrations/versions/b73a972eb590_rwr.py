"""rwr

Revision ID: b73a972eb590
Revises: 
Create Date: 2019-02-01 12:33:04.511400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b73a972eb590'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('first_name', sa.String(length=128), nullable=True),
    sa.Column('last_name', sa.String(length=128), nullable=True),
    sa.Column('bio', sa.String(length=128), nullable=True),
    sa.Column('spol', sa.String(length=10), nullable=True),
    sa.Column('user_picture', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('trip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=120), nullable=True),
    sa.Column('about', sa.String(length=1000), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('min_people', sa.String(length=120), nullable=True),
    sa.Column('max_people', sa.String(length=120), nullable=True),
    sa.Column('total_cost', sa.Integer(), nullable=True),
    sa.Column('transport', sa.String(length=120), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.Column('trip_rating', sa.Integer(), nullable=True),
    sa.Column('trip_picture', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_trip_about'), 'trip', ['about'], unique=False)
    op.create_index(op.f('ix_trip_date'), 'trip', ['date'], unique=False)
    op.create_index(op.f('ix_trip_location'), 'trip', ['location'], unique=False)
    op.create_index(op.f('ix_trip_max_people'), 'trip', ['max_people'], unique=False)
    op.create_index(op.f('ix_trip_min_people'), 'trip', ['min_people'], unique=False)
    op.create_index(op.f('ix_trip_total_cost'), 'trip', ['total_cost'], unique=False)
    op.create_index(op.f('ix_trip_transport'), 'trip', ['transport'], unique=False)
    op.create_table('user_rating',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_rating', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.Column('coments', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_coments'), 'comments', ['coments'], unique=False)
    op.create_table('join_trip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('join_trip')
    op.drop_index(op.f('ix_comments_coments'), table_name='comments')
    op.drop_table('comments')
    op.drop_table('user_rating')
    op.drop_index(op.f('ix_trip_transport'), table_name='trip')
    op.drop_index(op.f('ix_trip_total_cost'), table_name='trip')
    op.drop_index(op.f('ix_trip_min_people'), table_name='trip')
    op.drop_index(op.f('ix_trip_max_people'), table_name='trip')
    op.drop_index(op.f('ix_trip_location'), table_name='trip')
    op.drop_index(op.f('ix_trip_date'), table_name='trip')
    op.drop_index(op.f('ix_trip_about'), table_name='trip')
    op.drop_table('trip')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
