"""empty message

Revision ID: 196a628b5682
Revises: 94a9a18e7f13
Create Date: 2024-09-20 12:49:05.092922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '196a628b5682'
down_revision = '94a9a18e7f13'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['name'])

    with op.batch_alter_table('vehicle', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['name'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicle', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
