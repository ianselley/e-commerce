from sqlalchemy import Column, ForeignKey, Integer, String, Text, VARCHAR
from sqlalchemy.orm import relationship

from src.database import Base
from src.models.many_to_many import buyers_and_items
from src.models.address import Address


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(128), nullable=False, unique=True)
    hashedPassword = Column(Text, nullable=False)
    telephone = Column(String(64), nullable=False)
    role = Column(String(64), nullable=False)

    buyer = relationship("Buyer", back_populates="user", uselist=False)
    seller = relationship("Seller", back_populates="user", uselist=False)


class Buyer(Base):
    __tablename__ = "buyers"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    surname = Column(String(64))
    mainAddressId = Column(Integer)
    userId = Column(Integer, ForeignKey('users.id'))
    # addressId = Column(Integer, ForeignKey('addresses.id'))

    user = relationship("User", back_populates="buyer")
    orders = relationship("Order", back_populates="buyer")
    # mainAddress = relationship("Address", back_populates="buyerMain", uselist=False)
    addresses = relationship("Address", back_populates="buyer")
    shoppingCart = relationship("Item", secondary=buyers_and_items, back_populates="buyers")


class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True)
    brand = Column(String(64), nullable=False)
    numberOfItemsSold = Column(Integer, default=0)
    userId = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="seller")
    items = relationship("Item", back_populates="seller")
    # orders made to the seller?