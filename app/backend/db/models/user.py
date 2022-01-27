from sqlalchemy import Column, ForeignKey, Integer, String, Text, VARCHAR
from sqlalchemy.orm import relationship

from db.database import Base
from many_to_many import buyers_to_items, buyers_to_addresses


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    email = Column(VARCHAR(128), unique=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    telefone = Column(String(64), nullable=False)


class Buyer(User):
    __tablename__ = "buyers"

    id = Column(None, ForeignKey('users.id'), primary_key=True)
    main_address_id = Column(Integer, ForeignKey("addresses.id"), nullable=False)

    items_bought = relationship("Item", secondary=buyers_to_items, back_populates="buyers")
    main_address = relationship("Address", back_populates="buyers_main")
    delivery_addresses = relationship("Address", secondary=buyers_to_addresses, back_populates="buyers_deliveries")
    shopping_cart = relationship("Item", secondary=buyers_to_items, back_populates="buyers")
    order = relationship("Order", back_populates="buyer")


class Seller(User):
    __tablename__ = "sellers"

    id = Column(None, ForeignKey('users.id'), primary_key=True)
    brand = Column(String(64), nullable=False)
    items_sold = Column(Integer, default=0)

    items = relationship("Item", back_populates="seller")