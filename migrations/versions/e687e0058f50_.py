"""empty message

Revision ID: e687e0058f50
Revises: 64a749603fbc
Create Date: 2023-09-09 16:35:54.366552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e687e0058f50'
down_revision = '64a749603fbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ActiveLoan', schema=None) as batch_op:
        batch_op.add_column(sa.Column('paymentType', sa.Integer(), nullable=False))

    with op.batch_alter_table('LoanAdvertisement', schema=None) as batch_op:
        batch_op.add_column(sa.Column('paymentType', sa.Integer(), nullable=False))

    with op.batch_alter_table('LoanOffer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('paymentType', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('LoanOffer', schema=None) as batch_op:
        batch_op.drop_column('paymentType')

    with op.batch_alter_table('LoanAdvertisement', schema=None) as batch_op:
        batch_op.drop_column('paymentType')

    with op.batch_alter_table('ActiveLoan', schema=None) as batch_op:
        batch_op.drop_column('paymentType')

    # ### end Alembic commands ###
