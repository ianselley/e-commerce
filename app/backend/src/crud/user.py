from sqlalchemy.orm import Session
import bcrypt

from src import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    password_bytes = user.password.encode()
    created_user = models.User(**user.dict(exclude={'password'}))
    created_user.hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    db.add(created_user)
    db.commit()
    db.refresh(created_user)
    return created_user


def create_buyer(db: Session, buyer: schemas.BuyerCreate, user: models.User):
    buyer = models.Buyer(**buyer.dict())
    buyer.user = user
    db.add(buyer)
    db.commit()
    db.refresh(buyer)
    return buyer


def create_seller(db: Session, seller: schemas.SellerCreate, user: models.User):
    seller = models.Seller(**seller.dict())
    seller.user = user
    db.add(seller)
    db.commit()
    db.refresh(seller)
    return seller


def get_user(db: Session, user_id: str):
    return db.query(models.User).filter_by(id=user_id).first()


def get_user_by_email(db: Session, user_email: str):
    return db.query(models.User).filter_by(email=user_email).first()


def get_buyer(db: Session, buyer_id: int):
    return db.query(models.Buyer).filter_by(id=buyer_id).first()


def get_buyer_by_user_id(db: Session, user_id: int):
    return db.query(models.Buyer).filter_by(user_id=user_id).first()


def get_seller(db: Session, seller_id: int):
    return db.query(models.Seller).filter_by(id=seller_id).first()


def get_seller_by_user_id(db: Session, user_id: int):
    return db.query(models.Seller).filter_by(user_id=user_id).first()


def verify_password(user: models.User, password: str):
    password_bytes = password.encode()
    user_hashed_password_bytes = user.hashed_password.encode()
    return bcrypt.checkpw(password_bytes, user_hashed_password_bytes)
    