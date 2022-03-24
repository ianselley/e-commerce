from sqlalchemy.orm import Session

from tests.utils.utils import random_email, random_lower_string
from src import schemas, crud


def test_create_seller(db: Session):
    name = random_lower_string()
    email = random_email()
    brand = random_lower_string()
    telephone = random_lower_string()
    password = random_lower_string()

    seller_in = schemas.user.SellerCreate(name=name, email=email, brand=brand, telephone=telephone, password=password)
    seller = crud.user.create_seller(db=db, seller=seller_in)

    assert seller.name == name
    assert seller.email == email
    assert seller.brand == brand
    assert seller.telephone == telephone
    assert hasattr(seller, "hashed_password")
    assert seller.hashed_password != password
    assert seller.hashed_password != ""