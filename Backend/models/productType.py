from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models.base import Base

class ProductType(Base):
    __tablename__ = "product_types"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_type = Column(String, unique=True)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)

    created_at = Column(DateTime, default=func.now())  
    updated_at = Column(DateTime, default=func.now())  


    # Relationship
    category = relationship("Category", back_populates="product_types")
    products = relationship("PurchaseDetail", back_populates="product_type")
