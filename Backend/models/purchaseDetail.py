import os
import sys

# Add the parent directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .base import Base  # Ensure base.py exists in models/
from .brand import Brand

class PurchaseDetail(Base):
    __tablename__ = "purchase_detail"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String)
    category_id = Column(Integer, ForeignKey("category.id"))
    brand_id = Column(Integer, ForeignKey("brand.id"))
    product_type_id = Column(Integer, ForeignKey("product_types.id"))
    unit_price = Column(Float)
    created_at = Column(DateTime, default=func.now())  
    updated_at = Column(DateTime, default=func.now())  

    # Relationships
    category = relationship("Category", back_populates="products")
    brand = relationship("Brand", back_populates="products")
    product_type = relationship("ProductType", back_populates="products")
    products = relationship("Product", back_populates="purchase_detail")