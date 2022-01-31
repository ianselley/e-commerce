from typing import Optional
from pydantic import BaseModel


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


from src.schemas.user import BuyerReturn, SellerReturn
from src.schemas.order import OrderReturn


class Item(ItemReturn):
    seller: SellerReturn
    buyers: list[BuyerReturn] = []
    orders: list[OrderReturn] = []
