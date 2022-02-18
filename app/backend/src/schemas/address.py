from typing import Optional
from pydantic import BaseModel


class AddressBase(BaseModel):
    street: str
    name: Optional[str] = None
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