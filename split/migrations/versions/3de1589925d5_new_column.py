"""new column

Revision ID: 3de1589925d5
Revises: 66cf38190652
Create Date: 2020-09-23 08:02:52.073728

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3de1589925d5'
down_revision = '66cf38190652'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('petname', sa.String(length=20), server_default='true', nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('petname')

    # ### end Alembic commands ###
