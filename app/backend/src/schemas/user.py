from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    email: str
    telephone: Optional[str] = None
    role: str
    buyer_id: Optional[int] = None
    seller_id: Optional[int] = None


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserReturn(UserBase):
    id: int

    class Config:
        orm_mode = True


class BuyerBase(BaseModel):
    name: str
    main_address_id: Optional[int] = None


class BuyerCreate(BuyerBase):
    pass


class BuyerReturn(BuyerBase):
    id: int

    class Config:
        orm_mode = True

    
class SellerBase(BaseModel):
    brand: str


class SellerCreate(SellerBase):
    pass


class SellerReturn(SellerBase):
    id: int

    class Config:
        orm_mode = True


from src.schemas.address import AddressReturn
from src.schemas.item import ItemReturn
from src.schemas.order import OrderReturn


class User(UserReturn):
    buyer: Optional[BuyerReturn] = None
    seller: Optional[SellerReturn] = None


class Buyer(BuyerReturn):
    main_address: Optional[AddressReturn] = None
    delivery_addresses: list[AddressReturn] = []
    shopping_cart: dict[ItemReturn, int] = {}
    orders: list[OrderReturn] = []


class Seller(SellerReturn):
    items: list[ItemReturn] = []