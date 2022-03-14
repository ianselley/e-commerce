from sqlalchemy import Column, ForeignKey, Integer, Float, Text, JSON, DateTime
from sqlalchemy.orm import relationship
import datetime

from src.database import Base
from .many_to_many import buyers_and_items, orders_and_items


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    specifications = Column(JSON)
    totalSold = Column(Integer, default=0)
    dayAdded = Column(DateTime, default=datetime.datetime.now)
    sellerId = Column(Integer, ForeignKey("sellers.id"), nullable=False)

    seller = relationship("Seller", back_populates="items")
    buyers = relationship("Buyer", secondary=buyers_and_items, back_populates="shoppingCart")
    orders = relationship("Order", secondary=orders_and_items, back_populates="items")
