from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from src.schemas.image import Image


class ProductBase(BaseModel):
    title: str
    description: Optional[str]
    price: float
    stock: int


class ProductCreate(ProductBase):
    pass


class ProductReturn(ProductBase):
    id: int
    items_sold: int
    money_made: float
    images: list[Image]
    day_added: datetime
    available: bool
    seller_id: Optional[int]

    class Config:
        orm_mode = True


class ProductUpdate(ProductBase):
    id: int


from src.schemas.user import SellerReturn
from src.schemas.order import OrderReturn
from src.schemas.cart_product import CartProductReturn


class Product(ProductReturn):
    seller: SellerReturn
    cart_products: Optional[list[CartProductReturn]]
    orders: Optional[list[OrderReturn]]
