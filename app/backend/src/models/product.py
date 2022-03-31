from sqlalchemy import Column, ForeignKey, Integer, Float, Text, JSON, DateTime
from sqlalchemy.orm import relationship
import datetime

from src.database import Base
from .many_to_many import buyers_and_products, orders_and_products


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
    seller_id = Column(Integer, ForeignKey("sellers.id"), nullable=False)

    seller = relationship("Seller", back_populates="products")
    images = relationship("Image", back_populates="product", cascade="all, delete")
    buyers = relationship("Buyer", secondary=buyers_and_products, back_populates="shopping_cart")
    orders = relationship("Order", secondary=orders_and_products, back_populates="products")
