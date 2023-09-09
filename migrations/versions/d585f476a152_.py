"""empty message

Revision ID: d585f476a152
Revises: e687e0058f50
Create Date: 2023-09-09 16:46:52.943371

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd585f476a152'
down_revision = 'e687e0058f50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('PaymentType',
    sa.Column('paymentTypeID', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('paymentType', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('paymentTypeID')
    )
    with op.batch_alter_table('ActiveLoan', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'PaymentType', ['paymentType'], ['paymentTypeID'])

    with op.batch_alter_table('LoanAdvertisement', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'PaymentType', ['paymentType'], ['paymentTypeID'])

    with op.batch_alter_table('LoanOffer', schema=None) as batch_op:
        batch_op.drop_column('paymentType')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('LoanOffer', schema=None) as batch_op:
        batch_op.add_column(sa.Column('paymentType', sa.INTEGER(), autoincrement=False, nullable=False))

    with op.batch_alter_table('LoanAdvertisement', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    with op.batch_alter_table('ActiveLoan', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    op.drop_table('PaymentType')
    # ### end Alembic commands ###
