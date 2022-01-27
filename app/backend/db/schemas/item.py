from typing import Optional
from pydantic import BaseModel

from db.schemas.user import BuyerReturn, SellerReturn
from db.schemas.item import ItemReturn
from db.schemas.order import OrderReturn


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float
    specifications: Optional[dict[str, str]] = None
    stock: int
    seller_id: int


class ItemCreate(ItemBase):
    pass


class ItemReturn(ItemBase):
    id: int

    class Config:
        orm_mode = True

class Item(ItemReturn):
    seller: SellerReturn
    buyers: list[BuyerReturn] = []
    orders: list[OrderReturn] = []
