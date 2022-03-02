from fastapi import  Depends, APIRouter, HTTPException, status 
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from src import schemas, crud
from src.utils import utils


router = APIRouter()
token_auth_scheme = HTTPBearer()

@router.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(utils.get_db)):
    if not utils.email_is_valid(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email not valid",
        )
    user_db = crud.user.get_user_by_email(db, user_email=user.email)
    if user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered",
        )
    user_created = crud.user.create_user(db=db, user=user)
    return user_created 


@router.post("/signup-seller")
def signup(seller: schemas.SellerCreate, db: Session = Depends(utils.get_db), token: str = Depends(token_auth_scheme)):
    token_data = utils.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token",
        )
    user_db = crud.user.get_user(db, user_id=user_id)
    seller_created = crud.user.create_seller(db=db, seller=seller, user=user_db)
    return seller_created 


@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(utils.get_db)):
    user_db = crud.user.get_user_by_email(db, user_email=user.email)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email not registered",
        )
    if not crud.user.verify_password(user_db, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password",
        )
    response = user_db.__dict__
    response["accessToken"] = utils.encode(user_db)
    if user_db.role == "seller" and user_db.seller is not None:
        response["seller"] = user_db.seller.__dict__
    elif user_db.role == "buyer" and user_db.buyer is not None:
        response["buyer"] = user_db.buyer.__dict__
    return response


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
