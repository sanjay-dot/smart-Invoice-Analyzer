from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from models.base import Base
from sqlalchemy.orm import relationship

class Brand(Base):
    __tablename__ = "brand"

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand_name = Column(String, unique=True)
    created_at = Column(DateTime, default=func.now())  
    updated_at = Column(DateTime, default=func.now())  


    # Relationship
    products = relationship("PurchaseDetail", back_populates="brand")
