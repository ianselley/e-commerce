from pydantic import BaseModel
import datetime


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


from src.schemas.item import ItemReturn
from src.schemas.user import BuyerReturn


class Order(OrderReturn):
    buyer: BuyerReturn
    item: ItemReturn