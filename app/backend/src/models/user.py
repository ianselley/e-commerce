from sqlalchemy import Column, ForeignKey, Integer, String, Text, VARCHAR
from sqlalchemy.orm import relationship

from src.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(128), nullable=False, unique=True)
    hashed_password = Column(Text, nullable=False)
    telephone = Column(String(64), nullable=False)
    role = Column(String(16), nullable=False)

    buyer = relationship("Buyer", back_populates="user", uselist=False)
    seller = relationship("Seller", back_populates="user", uselist=False)


class Buyer(Base):
    __tablename__ = "buyers"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    main_address_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="buyer")
    orders = relationship("Order", back_populates="buyer")
    addresses = relationship("Address", back_populates="buyer")
    shopping_cart = relationship("CartProduct", back_populates="buyer")


class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True)
    brand = Column(String(64), nullable=False)
    number_of_products_sold = Column(Integer, default=0)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="seller")
    products = relationship("Product", back_populates="seller")
    orders = relationship("Order", back_populates="seller")
