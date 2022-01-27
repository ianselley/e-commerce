from sqlalchemy import Column, ForeignKey, Integer, Date
from sqlalchemy.orm import relationship
import datetime

from db.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    date = Column(Date, default=datetime.datetime.now)
    quantity = Column(Integer, default=1)
    buyer_id = Column(Integer, ForeignKey("buyers.id"))
    item_id = Column(Integer, ForeignKey("items.id"))

    buyer = relationship("Buyer", back_populates="orders")
    item = relationship("Item", back_populates="orders")

