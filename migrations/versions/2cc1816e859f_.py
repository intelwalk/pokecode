"""empty message

Revision ID: 2cc1816e859f
Revises: 49c5939a59f1
Create Date: 2022-02-05 18:35:39.569806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cc1816e859f'
down_revision = '49c5939a59f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kanto', sa.Column('sprite', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('kanto', 'sprite')
    # ### end Alembic commands ###
