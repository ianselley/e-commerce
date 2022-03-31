from sqlalchemy.orm import Session

from src import models, schemas, crud


def update_main_address_id(db: Session, user_id: int, main_address_id: int):
    buyer_db = crud.user.get_buyer_by_user_id(db, user_id=user_id)
    buyer_db.main_address_id = main_address_id
    db.commit()
    db.refresh(buyer_db)
    return buyer_db


def create_address(db: Session, address: schemas.AddressCreate, user_id: int):
    buyer_db = crud.user.get_buyer_by_user_id(db, user_id=user_id)
    address = models.Address(**address.dict())
    address.buyer = buyer_db
    db.add(address)
    db.commit()
    db.refresh(address)
    if not buyer_db.main_address_id:
        update_main_address_id(db=db, user_id=user_id, main_address_id=address.id)
    return address


def get_address(db: Session, id: int):
    return db.query(models.Address).filter_by(id=id).first()