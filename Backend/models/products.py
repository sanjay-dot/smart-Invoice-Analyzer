from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from models.base import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    product_id = Column(Integer, ForeignKey("purchase_detail.id"))
    quantity = Column(Float)
    unit_price = Column(Float)
    created_at = Column(DateTime, default=func.now())  
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now()) 



    # Relationships
    invoice = relationship("Invoice", back_populates="products")
    purchase_detail = relationship("PurchaseDetail", back_populates="products")
