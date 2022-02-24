from fastapi import  Depends, APIRouter, HTTPException, Response, status
from sqlalchemy.orm import Session

from src import schemas, crud
from src.utils import utils

router = APIRouter()


@router.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(utils.get_db)):
    if crud.user.get_user_by_email(db, user_email=user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    return {"message": "Signup"}


@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(utils.get_db)):
    if not crud.user.get_user_by_email(db, user_email=user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email not registered",
        )
    return {"message": "Login"}


@router.post("", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(utils.get_db)):
    db_user = crud.user.get_user_by_email(db=db, user_email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.user.create_user(db=db, user=user)


@router.get("", response_model=schemas.User)
def read_buyer(user_id: int, db: Session = Depends(utils.get_db)):
    user = crud.user.get_user(db=db, user_id=user_id)
    return user


@router.get("/seller", response_model=schemas.Seller)
def read_seller(seller_id: int, db: Session = Depends(utils.get_db)):
    seller = crud.user.get_seller(db=db, seller_id=seller_id)
    return seller


@router.post("/buyer", response_model=schemas.Buyer)
def create_buyer(buyer: schemas.BuyerCreate, db: Session = Depends(utils.get_db)):
    db_buyer = crud.user.get_buyer_by_email(db=db, buyer_email=buyer.email)
    if db_buyer:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.user.create_buyer(db=db, buyer=buyer)


@router.post("/seller", response_model=schemas.Seller)
def create_seller(seller: schemas.SellerCreate, db: Session = Depends(utils.get_db)):
    db_seller = crud.user.get_seller_by_email(db=db, seller_email=seller.email)
    if db_seller:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.user.create_seller(db=db, seller=seller)
