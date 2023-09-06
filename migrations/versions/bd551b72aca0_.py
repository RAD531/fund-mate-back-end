"""empty message

Revision ID: bd551b72aca0
Revises: 4279546d0280
Create Date: 2023-09-05 18:55:00.871565

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bd551b72aca0'
down_revision = '4279546d0280'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('BankDetails', schema=None) as batch_op:
        batch_op.alter_column('bankIssueDate',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=False)
        batch_op.alter_column('bankExpiryDate',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('BankDetails', schema=None) as batch_op:
        batch_op.alter_column('bankExpiryDate',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
        batch_op.alter_column('bankIssueDate',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)

    # ### end Alembic commands ###