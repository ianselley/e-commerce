from sqlalchemy import Column, Float, ForeignKey, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship
import datetime

from src.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, default=1)
    price = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.datetime.now)
    delivered = Column(Boolean, default=False)
    address_id = Column(Integer, ForeignKey("addresses.id"))
    buyer_id = Column(Integer, ForeignKey("buyers.id"))
    seller_id = Column(Integer, ForeignKey("sellers.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    address = relationship("Address", back_populates="orders", uselist=False)
    buyer = relationship("Buyer", back_populates="orders")
    seller = relationship("Seller", back_populates="orders")
    product = relationship("Product", back_populates="orders", uselist=False)
