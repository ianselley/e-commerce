from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from fastapi import UploadFile


class ProductBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    stock: int
    specifications: Optional[dict[str, str]] = None


class ProductCreate(ProductBase):
    pass


class ProductReturn(ProductBase):
    id: int
    total_sold: int
    has_images: bool
    day_added: datetime
    seller_id: Optional[int] = None

    class Config:
        orm_mode = True


from src.schemas.user import BuyerReturn, SellerReturn
from src.schemas.order import OrderReturn


class Product(ProductReturn):
    seller: SellerReturn
    buyers: list[BuyerReturn]
    orders: list[OrderReturn]
