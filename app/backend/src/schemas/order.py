from pydantic import BaseModel
from datetime import datetime


class OrderBase(BaseModel):
    address_id: int
    buyer_id: int
    seller_id: int
    cart_product_id: int


class OrderCreate(OrderBase):
    pass


class OrderReturn(OrderBase):
    id: int
    date: datetime
    delivered: bool

    class Config:
        orm_mode = True


from src.schemas.cart_product import CartProduct
from src.schemas.user import BuyerReturn, SellerReturn
from src.schemas.address import AddressReturn


class Order(OrderReturn):
    address: AddressReturn
    buyer: BuyerReturn
    seller: SellerReturn
    cart_product: CartProduct