"""Add visibility field to Post model

Revision ID: f67096c3cf6a
Revises: 45401c352fed
Create Date: 2025-04-11 20:25:46.209465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f67096c3cf6a'
down_revision = '45401c352fed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('visibility', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('visibility')

    # ### end Alembic commands ###
