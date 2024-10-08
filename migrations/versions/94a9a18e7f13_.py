"""empty message

Revision ID: 94a9a18e7f13
Revises: 0e68417db0a2
Create Date: 2024-09-20 12:47:20.615784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94a9a18e7f13'
down_revision = '0e68417db0a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.drop_constraint('planet_name_key', type_='unique')

    with op.batch_alter_table('vehicle', schema=None) as batch_op:
        batch_op.drop_constraint('vehicle_name_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('vehicle', schema=None) as batch_op:
        batch_op.create_unique_constraint('vehicle_name_key', ['name'])

    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.create_unique_constraint('planet_name_key', ['name'])

    # ### end Alembic commands ###
