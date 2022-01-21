from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, VARCHAR
from sqlalchemy.orm import relationship

from .database import Base


# class Product(Base):
#     __tablename__ = "products"

#     id = Column(Integer, primary_key=True, index=True)
#     path_to_images = Column(String(128), nullable=False)
#     name = Column(String(128), nullable=False)
#     description = Column(Text)
#     price = Column(Integer, nullable=False)
#     stock = Column(Integer, nullable=False)
#     is_available = Column(Boolean, nullable=False)

Text = Text(256)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(VARCHAR(256), unique=True)
    hashed_password = Column(Text)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")