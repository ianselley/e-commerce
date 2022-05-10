from sqlalchemy import Column, ForeignKey, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship
import datetime

from src.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.datetime.now)
    delivered = Column(Boolean, default=False)
    address_id = Column(Integer, ForeignKey("addresses.id"))
    buyer_id = Column(Integer, ForeignKey("buyers.id"))
    seller_id = Column(Integer, ForeignKey("sellers.id"))
    cart_product_id = Column(Integer, ForeignKey("cart_products.id"))

    address = relationship("Address", back_populates="orders", uselist=False)
    buyer = relationship("Buyer", back_populates="orders")
    seller = relationship("Seller", back_populates="orders")
    cart_product = relationship("CartProduct", back_populates="order", uselist=False)
