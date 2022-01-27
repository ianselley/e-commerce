from sqlalchemy.orm import Session

from .. import models, schemas


def get_buyer(db: Session, buyer_id: int):
    return db.query(models.Buyer).filter(models.Buyer.id == buyer_id).first()


def get_buyer_by_email(db: Session, email: str):
    return db.query(models.Buyer).filter(models.Buyer.email == email).first()


def get_buyers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Buyer).offset(skip).limit(limit).all()


def create_buyer(db: Session, buyer: schemas.BuyerCreate):
    fake_hashed_password = buyer.password + "notreallyhashed"
    db_buyer = models.Buyer(email=buyer.email, hashed_password=fake_hashed_password)
    db.add(db_buyer)
    db.commit()
    db.refresh(db_buyer)
    return db_buyer


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_buyer_item(db: Session, item: schemas.ItemCreate, buyer_id: int):
    db_item = models.Item(**item.dict(), owner_id=buyer_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item