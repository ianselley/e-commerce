from typing import Optional
from pydantic import BaseModel


class AddressBase(BaseModel):
    name: Optional[str] = None # By default make the name the username
    street: str
    number: Optional[str] = None
    city: str
    flat: Optional[str] = None
    state: str
    zipCode: str
    country: str
    details: Optional[str] = None


class AddressCreate(AddressBase):
    pass


class AddressReturn(AddressBase):
    id: int
    buyerId: int
    # buyerAddressesId: int

    class Config:
        orm_mode = True


from src.schemas.user import BuyerReturn


class Address(AddressReturn):
    # buyerMain: Optional[BuyerReturn]
    buyer: BuyerReturn
