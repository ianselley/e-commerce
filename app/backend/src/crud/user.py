from sqlalchemy.orm import Session

from src import models, schemas


def create_seller(db: Session, seller: schemas.SellerCreate):
    seller = models.Seller(**seller.dict())
    db.add(seller)
    db.commit()
    db.refresh(seller)
    return seller


def create_buyer(db: Session, buyer: schemas.BuyerCreate):
    buyer = models.Buyer(**buyer.dict(exclude={"password"}))
    buyer.hashed_password = buyer.password + "fake hash"
    db.add(buyer)
    db.commit()
    db.refresh(buyer)
    return buyer


def get_seller(db: Session, seller_id: int):
    return db.query(models.Seller).filter_by(id=seller_id).first()


def get_buyer(db: Session, buyer_id: int):
    return db.query(models.Buyer).filter_by(id=buyer_id).first()


def get_seller_by_email(db: Session, seller_email: str):
    return db.query(models.Seller).filter_by(email=seller_email).first()