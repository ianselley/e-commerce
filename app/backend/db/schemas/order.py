from pydantic import BaseModel
import datetime

from db.schemas.item import ItemReturn, BuyerReturn


class OrderBase(BaseModel):
    buyer_id: int
    item_id: int
    quantity: int
    date: datetime.datetime


class OrderCreate(OrderBase):
    pass


class OrderReturn(OrderBase):
    id: int

    class Config:
        orm_mode = True


class Order(OrderReturn):
    buyer: BuyerReturn
    item: ItemReturn