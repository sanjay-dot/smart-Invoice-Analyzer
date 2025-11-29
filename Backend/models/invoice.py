from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .base import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_date = Column(String)
    subtotal = Column(Float)
    discount = Column(Float)
    tax_rate = Column(Float)
    total_price = Column(Float)
    invoice_number = Column(String, unique=True)
    created_at = Column(DateTime, default=func.now())  # Timestamp when created
    updated_at = Column(DateTime, default=func.now())  # Timestamp when created


    # Relationship
    products = relationship("Product", back_populates="invoice")
