from sqlalchemy.orm import Session
import bcrypt

from src import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    password_bytes = user.password.encode()
    created_user = models.User(**user.dict(exclude={'password'}))
    created_user.hashedPassword = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
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


def get_user(db: Session, userId: str):
    return db.query(models.User).filter_by(id=userId).first()


def get_user_by_email(db: Session, user_email: str):
    return db.query(models.User).filter_by(email=user_email).first()


def get_seller(db: Session, sellerId: int):
    return db.query(models.Seller).filter_by(id=sellerId).first()


def get_buyer(db: Session, buyerId: int):
    return db.query(models.Buyer).filter_by(id=buyerId).first()


def get_buyer_by_user_id(db: Session, userId: int):
    return db.query(models.Buyer).filter_by(userId=userId).first()


def verify_password(user: models.User, password: str):
    password_bytes = password.encode()
    user_hashed_password_bytes = user.hashedPassword.encode()
    return bcrypt.checkpw(password_bytes, user_hashed_password_bytes)
    