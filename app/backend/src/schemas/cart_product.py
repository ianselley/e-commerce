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

    class Config:
        orm_mode = True


from src.schemas.user import BuyerReturn
from src.schemas.product import ProductReturn


class CartProduct(CartProductReturn):
    buyer: Optional[BuyerReturn]
    product: Optional[ProductReturn]
