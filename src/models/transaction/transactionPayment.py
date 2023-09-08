from sqlalchemy import Column, Integer, DateTime, Numeric, ForeignKey
from ..base import Base

class TransactionPayment(Base):
    __tablename__ = 'TransactionPayment'

    transactionPaymentID = Column(Integer, primary_key=True, autoincrement=True)
    transactionID = Column(Integer, ForeignKey('Transaction.transactionID'), nullable=False)
    amountPaid = Column(Numeric, nullable=False)
    datePaid = Column(DateTime(), nullable=False)
    paymentStatus = Column(Integer, ForeignKey('PaymentStatus.paymentStatusID'), nullable=False)