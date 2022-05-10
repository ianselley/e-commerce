from pydantic import BaseModel
from typing import Optional


class CartProductBase(BaseModel):
    quantity: int
    buyer_id: Optional[int]
    product_id: int


class CartProductCreate(CartProductBase):
    pass


class CartProductReturn(CartProductBase):
    id: int
    purchased: bool

    class Config:
        orm_mode = True


from src.schemas.user import BuyerReturn
from src.schemas.product import ProductReturn
from src.schemas.order import OrderReturn


class CartProduct(CartProductReturn):
    buyer: Optional[BuyerReturn]
    product: Optional[ProductReturn]
    order: Optional[OrderReturn]
