from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from db.database import Base
from many_to_many import buyers_to_addresses


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True)
    street = Column(String(128), nullable=False)
    number = Column(String(64))
    city = Column(String(64), nullable=False)
    flat = Column(String(64))
    state = Column(Text, nullable=False)
    zip_code = Column(String(64), nullable=False)
    country = Column(String(64), nullable=False)
    details = Column(Text)

    buyers_main = relationship("Buyer", back_populates="main_address")
    buyers_deliveries = relationship("Buyer", secondary=buyers_to_addresses, back_populates="delivery_addresses")