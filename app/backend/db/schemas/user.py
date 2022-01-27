from pydantic import BaseModel

from db.schemas.address import AddressReturn
from db.schemas.item import ItemReturn
from db.schemas.order import OrderReturn


class BuyerBase(BaseModel):
    name: str
    email: str
    telefone: str
    main_address_id: int 


class BuyerCreate(BuyerBase):
    hashed_password: str


class BuyerReturn(BuyerBase):
    id: int

    class Config:
        orm_mode = True

    
class SellerBase(BaseModel):
    name: str
    email: str
    brand: str
    telefone: str


class SellerCreate(SellerBase):
    hashed_password: str


class SellerReturn(SellerBase):
    id: int

    class Config:
        orm_mode = True

class Buyer(BuyerReturn):
    main_address: AddressReturn
    delivery_addresses: list[AddressReturn] = []
    shopping_cart: list[ItemReturn] = []
    orders: list[OrderReturn] = []

class Seller(SellerReturn):
    items: list[ItemReturn] = []