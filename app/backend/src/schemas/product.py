from typing import Optional
from pydantic import BaseModel
from datetime import datetime


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
    totalSold: int
    dayAdded: datetime
    sellerId: Optional[int] = None

    class Config:
        orm_mode = True


from src.schemas.user import BuyerReturn, SellerReturn
from src.schemas.order import OrderReturn


class Product(ProductReturn):
    seller: list[SellerReturn]
    buyers: list[BuyerReturn]
    orders: list[OrderReturn]
