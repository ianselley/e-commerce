from pydantic import BaseModel


class BuyerBase(BaseModel):
    name: str
    email: str
    telefone: str
    main_address_id: int 


class BuyerCreate(BuyerBase):
    password: str


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
    password: str


class SellerReturn(SellerBase):
    id: int

    class Config:
        orm_mode = True


from src.schemas.address import AddressReturn
from src.schemas.item import ItemReturn
from src.schemas.order import OrderReturn


class Buyer(BuyerReturn):
    main_address: AddressReturn
    delivery_addresses: list[AddressReturn] = []
    shopping_cart: dict[ItemReturn, int] = {}
    orders: list[OrderReturn] = []


class Seller(SellerReturn):
    items: list[ItemReturn] = []