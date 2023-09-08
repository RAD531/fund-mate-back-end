from sqlalchemy import Column, Integer, String, ForeignKey
from ..base import Base

class Contract(Base):
    __tablename__ = 'Contract'

    contractID = Column(Integer, primary_key=True, autoincrement=True)
    transactionID = Column(Integer, ForeignKey('Transaction.transactionID'), nullable=False)
    contractDocumentLink = Column(String, nullable=False)
    contractFileName = Column(String(50), nullable=False)