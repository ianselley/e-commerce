from sqlalchemy import Column, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from src.database import Base


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True)
    filename = Column(Text)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)

    product = relationship("Product", back_populates="images")
