from fastapi import  Depends, APIRouter, HTTPException 
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from src import schemas, crud, utils


router = APIRouter()
token_auth_schema = HTTPBearer()

@router.post("/signup", response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(utils.db.get_db)):
    valid_email = utils.user.email_is_valid(user.email)
    if not valid_email:
        raise HTTPException(status_code=400, detail="Email not valid")

    user_db = crud.user.get_user_by_email(db, user_email=user.email)
    if user_db:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_created = crud.user.create_user(db=db, user=user)
    return user_created


@router.post("/signup-buyer", response_model=schemas.Buyer)
def signup_buyer(buyer: schemas.BuyerCreate, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    userId = token_data.get("sub")
    if not userId:
        raise HTTPException(status_code=400, detail="Invalid token")

    user_db = crud.user.get_user(db, userId=userId)
    if not user_db:
        raise HTTPException(status_code=400, detail="User does not exist")
    if user_db.buyer is not None:
        raise HTTPException(status_code=400, detail="User already registered as a buyer")

    buyer_created = crud.user.create_buyer(db=db, buyer=buyer, user=user_db)
    return buyer_created


@router.post("/signup-seller", response_model=schemas.Seller)
def signup_seller(seller: schemas.SellerCreate, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    userId = token_data.get("sub")
    if not userId:
        raise HTTPException(status_code=400, detail="Invalid token")

    user_db = crud.user.get_user(db, userId=userId)
    if not user_db:
        raise HTTPException(status_code=400, detail="User does not exist")
    if user_db.seller is not None:
        raise HTTPException(status_code=400, detail="User already registered as a seller")

    seller_created = crud.user.create_seller(db=db, seller=seller, user=user_db)
    return seller_created


@router.post("/login", response_model=schemas.User)
def login(user: schemas.UserLogin, db: Session = Depends(utils.db.get_db)):
    user_db = crud.user.get_user_by_email(db, user_email=user.email)
    if not user_db:
        raise HTTPException(status_code=400, detail="Email not registered")
    if not crud.user.verify_password(user_db, user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    user_db.accessToken = utils.user.encode(user_db)
    return user_db


@router.get("", response_model=schemas.User)
def read_user(userId: int, db: Session = Depends(utils.db.get_db)):
    user = crud.user.get_user(db=db, userId=userId)
    return user


@router.get("/buyer", response_model=schemas.Buyer)
def read_buyer(buyerId: int, db: Session = Depends(utils.db.get_db)):
    buyer = crud.user.get_buyer(db=db, buyerId=buyerId)
    return buyer


@router.get("/seller", response_model=schemas.Seller)
def read_seller(sellerId: int, db: Session = Depends(utils.db.get_db)):
    seller = crud.user.get_seller(db=db, sellerId=sellerId)
    return seller
