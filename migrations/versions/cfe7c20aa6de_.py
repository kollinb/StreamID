"""empty message

Revision ID: cfe7c20aa6de
Revises: 
Create Date: 2019-05-04 15:14:57.290333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfe7c20aa6de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clip',
    sa.Column('id', sa.String(length=70), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=True),
    sa.Column('broadcaster_name', sa.String(length=70), nullable=True),
    sa.Column('thumb_url', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clip')
    # ### end Alembic commands ###