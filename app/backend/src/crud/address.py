from sqlalchemy.orm import Session

from src import models, schemas, crud


def update_mainAddressId(db: Session, userId: int, mainAddressId: int):
    buyer_db = crud.user.get_buyer_by_user_id(db, userId=userId)
    buyer_db.mainAddressId = mainAddressId
    db.commit()
    return buyer_db

def create_address(db: Session, address: schemas.AddressCreate, userId: int):
    buyer_db = crud.user.get_buyer_by_user_id(db, userId=userId)
    address = models.Address(**address.dict())
    address.buyer = buyer_db
    db.add(address)
    db.commit()
    db.refresh(address)
    if not buyer_db.mainAddressId:
        update_mainAddressId(db=db, userId=userId, mainAddressId=address.id)
    return address


def get_address(db: Session, id: int):
    return db.query(models.Address).filter_by(id=id).first()