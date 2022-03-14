from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from src.database import Base


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    street = Column(String(128), nullable=False)
    number = Column(String(64))
    city = Column(String(64), nullable=False)
    flat = Column(String(64))
    state = Column(Text, nullable=False)
    zipCode = Column(String(64), nullable=False)
    country = Column(String(64), nullable=False)
    details = Column(Text)
    buyerId = Column(Integer, ForeignKey("buyers.id"))

    buyer = relationship("Buyer", back_populates="addresses")
    # buyerMain = relationship("Buyer", back_populates="mainAddress", foreign_keys=[buyerId])
