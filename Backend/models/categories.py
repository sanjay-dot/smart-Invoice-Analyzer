from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from models.base import Base

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String, unique=True)
    created_at = Column(DateTime, default=func.now())  
    updated_at = Column(DateTime, default=func.now())  


    # Relationship
    products = relationship("PurchaseDetail", back_populates="category")
    product_types = relationship("ProductType", back_populates="category")
    
