from pydantic import BaseModel
from datetime import datetime


class OrderBase(BaseModel):
    buyerId: int
    itemId: int
    quantity: int
    date: datetime


class OrderCreate(OrderBase):
    pass


class OrderReturn(OrderBase):
    id: int

    class Config:
        orm_mode = True


from src.schemas.item import ItemReturn
from src.schemas.user import BuyerReturn


class Order(OrderReturn):
    buyer: list[BuyerReturn]
    item: list[ItemReturn]