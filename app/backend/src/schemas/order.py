from pydantic import BaseModel
from datetime import datetime


class OrderBase(BaseModel):
    buyerId: int
    productId: int
    quantity: int
    date: datetime


class OrderCreate(OrderBase):
    pass


class OrderReturn(OrderBase):
    id: int

    class Config:
        orm_mode = True


from src.schemas.product import ProductReturn
from src.schemas.user import BuyerReturn


class Order(OrderReturn):
    buyer: list[BuyerReturn]
    product: list[ProductReturn]