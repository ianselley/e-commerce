from sqlalchemy import Column, ForeignKey, Integer, String, Text, VARCHAR
from sqlalchemy.orm import relationship

from src.database import Base
from .many_to_many import buyers_to_items, buyers_to_addresses


class Buyer(Base):
    __tablename__ = "buyers"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    email = Column(VARCHAR(128), unique=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    telefone = Column(String(64), nullable=False)
    main_address_id = Column(Integer, ForeignKey("addresses.id"), nullable=False)

    main_address = relationship("Address", back_populates="buyers_main")
    delivery_addresses = relationship("Address", secondary=buyers_to_addresses, back_populates="buyers_deliveries")
    shopping_cart = relationship("Item", secondary=buyers_to_items, back_populates="buyers")
    orders = relationship("Order", back_populates="buyer")


class Seller(Base):
    __tablename__ = "sellers"

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    email = Column(VARCHAR(128), unique=True, nullable=False)
    hashed_password = Column(Text, nullable=False)
    telefone = Column(String(64), nullable=False)
    brand = Column(String(64), nullable=False)
    items_sold = Column(Integer, default=0)

    items = relationship("Item", back_populates="seller")