from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    email: str
    telephone: Optional[str] = None
    role: str


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
    surname: str


class BuyerCreate(BuyerBase):
    pass


class BuyerReturn(BuyerBase):
    id: int
    userId: int
    mainAddressId: Optional[int]

    class Config:
        orm_mode = True

    
class SellerBase(BaseModel):
    brand: str


class SellerCreate(SellerBase):
    pass


class SellerReturn(SellerBase):
    id: int
    userId: int

    class Config:
        orm_mode = True


from src.schemas.address import AddressReturn
from src.schemas.product import ProductReturn
from src.schemas.order import OrderReturn


class Buyer(BuyerReturn):
    user: UserReturn
    # mainAddress: Optional[AddressReturn]
    addresses: Optional[list[AddressReturn]]
    shoppingCart: Optional[dict[ProductReturn, int]]
    orders: Optional[list[OrderReturn]]


class Seller(SellerReturn):
    user: UserReturn
    products: Optional[list[ProductReturn]]


class User(UserReturn):
    accessToken: Optional[str]
    buyer: Optional[Buyer]
    seller: Optional[Seller]
