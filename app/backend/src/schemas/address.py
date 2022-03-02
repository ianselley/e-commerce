from typing import Optional
from pydantic import BaseModel


class AddressBase(BaseModel):
    name: Optional[str] = None # By default make the name the username
    street: str
    number: Optional[str] = None
    city: str
    flat: Optional[str] = None
    state: str
    zip_code: str
    country: str
    details: Optional[str] = None


class AddressCreate(AddressBase):
    pass


class AddressReturn(AddressBase):
    id: int
    buyer_id: int

    class Config:
        orm_mode = True


class Address(AddressReturn):
    pass