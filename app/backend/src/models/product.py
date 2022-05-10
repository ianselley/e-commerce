from sqlalchemy import Column, ForeignKey, Integer, Float, Text, JSON, DateTime, Boolean
from sqlalchemy.orm import relationship
import datetime

from src.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    specifications = Column(JSON)
    total_sold = Column(Integer, default=0)
    day_added = Column(DateTime, default=datetime.datetime.now)
    available = Column(Boolean, default=True)
    seller_id = Column(Integer, ForeignKey("sellers.id"), nullable=False)

    seller = relationship("Seller", back_populates="products")
    images = relationship("Image", back_populates="product")
    cart_products = relationship("CartProduct", back_populates="product")
