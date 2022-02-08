from fastapi import  Depends, APIRouter, HTTPException, Response, status
from sqlalchemy.orm import Session

from src import schemas, crud
from src.utils import utils

router = APIRouter()


@router.get("/buyer", response_model=schemas.Buyer)
def read_buyer(buyer_id: int, db: Session = Depends(utils.get_db)):
    buyer = crud.user.get_buyer(db=db, buyer_id=buyer_id)
    return buyer


@router.get("/seller", response_model=schemas.Seller)
def read_seller(seller_id: int, db: Session = Depends(utils.get_db)):
    seller = crud.user.get_seller(db=db, seller_id=seller_id)
    return seller


@router.post("/seller", response_model=schemas.Seller)
def create_seller(seller: schemas.SellerCreate, db: Session = Depends(utils.get_db)):
    db_seller = crud.user.get_seller_by_email(db=db, seller_email=seller.email)
    if db_seller:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.user.create_seller(db=db, seller=seller)
