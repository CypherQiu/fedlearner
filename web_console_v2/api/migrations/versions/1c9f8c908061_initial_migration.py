"""Initial migration.

Revision ID: 1c9f8c908061
Revises: 
Create Date: 2020-11-25 16:57:46.699205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c9f8c908061'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects_v2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('config', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_projects_v2_name'), 'projects_v2', ['name'], unique=False)
    op.create_table('users_v2',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_v2_username'), 'users_v2', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_v2_username'), table_name='users_v2')
    op.drop_table('users_v2')
    op.drop_index(op.f('ix_projects_v2_name'), table_name='projects_v2')
    op.drop_table('projects_v2')
    # ### end Alembic commands ###