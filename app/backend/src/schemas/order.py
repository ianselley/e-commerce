from pydantic import BaseModel
from datetime import datetime


class OrderBase(BaseModel):
    address_id: int
    buyer_id: int
    seller_id: int
    product_id: int
    price: float
    quantity: int


class OrderCreate(OrderBase):
    pass


class OrderReturn(OrderBase):
    id: int
    date: datetime
    delivered: bool

    class Config:
        orm_mode = True


from src.schemas.product import ProductReturn
from src.schemas.user import BuyerReturn, SellerReturn
from src.schemas.address import AddressReturn


class Order(OrderReturn):
    address: AddressReturn
    buyer: BuyerReturn
    seller: SellerReturn
    product: ProductReturn