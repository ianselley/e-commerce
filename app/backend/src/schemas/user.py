from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    email: str
    telephone: Optional[str]
    role: str


class UserCreate(UserBase):
    password: str
    repeat_password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserReturn(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    email: Optional[str]
    telephone: Optional[str]
    password: Optional[str]


class BuyerBase(BaseModel):
    name: str


class BuyerCreate(BuyerBase):
    pass


class BuyerReturn(BuyerBase):
    id: int
    user_id: int
    main_address_id: Optional[int]

    class Config:
        orm_mode = True


class BuyerUpdate(BaseModel):
    name: str

    
class SellerBase(BaseModel):
    brand: str


class SellerCreate(SellerBase):
    pass


class SellerReturn(SellerBase):
    id: int
    user_id: int
    total_sold: int
    total_made: float

    class Config:
        orm_mode = True

    
class SellerUpdate(BaseModel):
    brand: str


from src.schemas.address import AddressReturn
from src.schemas.product import ProductReturn
from src.schemas.order import Order
from src.schemas.cart_product import CartProduct


class Buyer(BuyerReturn):
    user: UserReturn
    orders: Optional[list[Order]]
    addresses: Optional[list[AddressReturn]]
    shopping_cart: Optional[list[CartProduct]]


class Seller(SellerReturn):
    user: UserReturn
    products: Optional[list[ProductReturn]]
    orders: Optional[list[Order]]


class User(UserReturn):
    access_token: Optional[str]
    buyer: Optional[Buyer]
    seller: Optional[Seller]
