from typing import Optional
from pydantic import BaseModel
from datetime import datetime

from src.schemas.image import Image


class ProductBase(BaseModel):
    title: str
    description: Optional[str]
    price: float
    stock: int
    specifications: dict[str, str]


class ProductCreate(ProductBase):
    pass


class ProductReturn(ProductBase):
    id: int
    total_sold: int
    images: list[Image]
    day_added: datetime
    seller_id: Optional[int]

    class Config:
        orm_mode = True


from src.schemas.user import SellerReturn
from src.schemas.order import OrderReturn


class Product(ProductReturn):
    seller: SellerReturn
    orders: list[OrderReturn]
