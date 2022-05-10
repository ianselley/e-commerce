from sqlalchemy import Column, ForeignKey, Integer, Boolean
from sqlalchemy.orm import relationship 

from src.database import Base


class CartProduct(Base):
    __tablename__ = "cart_products"

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
    purchased = Column(Boolean, default=False)
    buyer_id = Column(Integer, ForeignKey('buyers.id'))
    product_id = Column(Integer, ForeignKey('products.id'))

    buyer = relationship("Buyer", back_populates="shopping_cart", uselist=False)
    product = relationship("Product", back_populates="cart_products", uselist=False)
    order = relationship("Order", back_populates="cart_product", uselist=False)