from sqlalchemy import Column, ForeignKey, Integer, String, Text, VARCHAR
from sqlalchemy.orm import relationship

from src.database import Base
from .many_to_many import buyers_and_items


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(128), nullable=False, unique=True)
    hashed_password = Column(Text, nullable=False)
    telephone = Column(String(64), nullable=False)
    role = Column(String(64), nullable=False)
    buyer_id = Column(Integer, ForeignKey('buyers.id'))
    seller_id = Column(Integer, ForeignKey('sellers.id'))

    buyer = relationship("Buyer", back_populates="user")
    seller = relationship("Seller", back_populates="user")


class Buyer(Base):
    __tablename__ = "buyers"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    surname = Column(String(64))
    main_address_id = Column(Integer, ForeignKey("addresses.id"))

    user = relationship("User", back_populates="buyer")
    orders = relationship("Order", back_populates="buyer")
    main_address = relationship("Address", back_populates="buyer")
    delivery_addresses = relationship("Address", overlaps="buyer,main_address", back_populates="buyer_addresses")
    shopping_cart = relationship("Item", secondary=buyers_and_items, back_populates="buyers")


class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True)
    brand = Column(String(64), nullable=False)
    number_of_items_sold = Column(Integer, default=0)

    user = relationship("User", back_populates="seller")
    items = relationship("Item", back_populates="seller")
    # orders made to the seller?