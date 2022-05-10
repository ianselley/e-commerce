from fastapi import  Depends, APIRouter, HTTPException 
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from src import schemas, crud, utils


router = APIRouter()
token_auth_schema = HTTPBearer()

@router.post("", response_model=schemas.User)
def signup_user(user: schemas.UserCreate, db: Session = Depends(utils.db.get_db)):
    valid_email = utils.user.email_is_valid(user.email)
    if not valid_email:
        raise HTTPException(status_code=400, detail="Email not valid")

    user_db = crud.user.get_user_by_email(db, user_email=user.email)
    if user_db:
        raise HTTPException(status_code=400, detail="Email already registered")

    user_created = crud.user.create_user(db=db, user=user)
    return user_created


@router.get("", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    token_user_id = token_data.get("sub")
    if not token_user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    if token_user_id != user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    user = crud.user.get_user(db=db, user_id=user_id)
    user.access_token = utils.user.encode(user)
    return user


@router.put("", response_model=schemas.User)
def edit_user(user: schemas.UserUpdate, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    user_db = crud.user.get_user(db, user_id=user_id)
    if not user_db:
        raise HTTPException(status_code=400, detail="User not found")
    updated_user = crud.user.update_user(db=db, user_id=user_id, user=user)
    updated_user.access_token = utils.user.encode(updated_user)
    return updated_user


@router.post("/login", response_model=schemas.User)
def login(user: schemas.UserLogin, db: Session = Depends(utils.db.get_db)):
    user_db = crud.user.get_user_by_email(db, user_email=user.email)
    if not user_db:
        raise HTTPException(status_code=400, detail="Email not registered")
    if not crud.user.verify_password(user_db, user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    user_db.access_token = utils.user.encode(user_db)
    return user_db


@router.post("/buyer", response_model=schemas.Buyer)
def signup_buyer(buyer: schemas.BuyerCreate, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")

    user_db = crud.user.get_user(db, user_id=user_id)
    if not user_db:
        raise HTTPException(status_code=400, detail="User does not exist")
    if user_db.buyer is not None:
        raise HTTPException(status_code=400, detail="User already registered as a buyer")

    buyer_created = crud.user.create_buyer(db=db, buyer=buyer, user=user_db)
    return buyer_created


@router.get("/buyer", response_model=schemas.Buyer)
def read_buyer(buyer_id: int, db: Session = Depends(utils.db.get_db)):
    buyer = crud.user.get_buyer(db=db, buyer_id=buyer_id)
    return buyer


@router.put("/buyer", response_model=schemas.Buyer)
def edit_buyer(buyer: schemas.BuyerUpdate, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")

    user_db = crud.user.get_user(db, user_id=user_id)
    if not user_db:
        raise HTTPException(status_code=400, detail="User does not exist")
    updated_buyer = crud.user.update_buyer(db=db, user_id=user_id, buyer=buyer)
    return updated_buyer


@router.post("/seller", response_model=schemas.Seller)
def signup_seller(seller: schemas.SellerCreate, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")

    user_db = crud.user.get_user(db, user_id=user_id)
    if not user_db:
        raise HTTPException(status_code=400, detail="User does not exist")
    if user_db.seller is not None:
        raise HTTPException(status_code=400, detail="User already registered as a seller")

    seller_created = crud.user.create_seller(db=db, seller=seller, user=user_db)
    return seller_created


@router.get("/seller", response_model=schemas.Seller)
def read_seller(seller_id: int, db: Session = Depends(utils.db.get_db)):
    seller = crud.user.get_seller(db=db, seller_id=seller_id)
    return seller


@router.put("/seller", response_model=schemas.Seller)
def edit_seller(seller: schemas.SellerUpdate, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")

    user_db = crud.user.get_user(db, user_id=user_id)
    if not user_db:
        raise HTTPException(status_code=400, detail="User does not exist")
    updated_seller = crud.user.update_seller(db=db, user_id=user_id, seller=seller)
    return updated_seller
