from typing import Optional
from pydantic import BaseModel


class AddressBase(BaseModel):
    name: Optional[str]
    street: str
    number: Optional[str] 
    city: str
    flat: Optional[str]
    state: str
    zip_code: str
    country: str
    details: Optional[str]


class AddressCreate(AddressBase):
    pass


class AddressReturn(AddressBase):
    id: int
    buyer_id: int

    class Config:
        orm_mode = True


from src.schemas.user import BuyerReturn


class Address(AddressReturn):
    buyer: BuyerReturn
