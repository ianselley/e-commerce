from sqlalchemy import Column, ForeignKey, Integer, Float, Text, JSON
from sqlalchemy.orm import relationship

from db.database import Base
from many_to_many import buyers_to_items


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    specifications = Column(JSON)
    total_sold = Column(Integer, default=0)
    day_added = Column()
    seller_id = Column(Integer, ForeignKey("sellers.id"), nullable=False)

    seller = relationship("Seller", back_populates="items")
    buyers = relationship("Buyer", secondary=buyers_to_items, back_populates="shopping_cart")
    order = relationship("Order", back_populates="item")
