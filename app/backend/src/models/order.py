from sqlalchemy import Column, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship
import datetime

from src.database import Base
from .many_to_many import orders_to_items


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    date = Column(Date, default=datetime.datetime.now)
    quantity = Column(Integer, default=1)
    buyer_id = Column(Integer, ForeignKey("buyers.id"))

    buyer = relationship("Buyer", back_populates="orders")
    items = relationship("Item", secondary=orders_to_items, back_populates="orders")

