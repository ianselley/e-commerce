from fastapi import  Depends, APIRouter, HTTPException 
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from src import schemas, crud, utils


router = APIRouter()
token_auth_schema = HTTPBearer()

@router.post("/register", response_model=schemas.Address)
def registerAddress(address: schemas.AddressCreate, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    address_created = crud.address.create_address(db=db, address=address, user_id=user_id)
    return address_created


@router.get("", response_model=schemas.Address)
def get_address(address_id: int, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    address_db = crud.address.get_address(db=db, address_id=address_id)
    if not address_db:
        raise HTTPException(status_code=404, detail="Address not found")
    buyer_db = crud.user.get_buyer_by_user_id(db=db, user_id=user_id)
    if not buyer_db.id == address_db.buyer_id:
        raise HTTPException(status_code=400, detail="You are not the owner of this address")
    return address_db


@router.put("/change-main_address_id", response_model=schemas.Buyer)
def change_main_address_id(address_id: int, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    address_db = crud.address.get_address(db=db, address_id=address_id)
    if not address_db:
        raise HTTPException(status_code=404, detail="Address not found")
    buyer_db = crud.user.get_buyer_by_user_id(db=db, user_id=user_id)
    if not buyer_db.id == address_db.buyer_id:
        raise HTTPException(status_code=400, detail="You are not the owner of this address")
    updated_buyer = crud.address.update_main_address_id(db=db, user_id=user_id, main_address_id=address_id)
    return updated_buyer
    

@router.delete("/delete", response_model=schemas.Address)
def delete_address(address_id: int, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    address_db = crud.address.get_address(db=db, address_id=address_id)
    if not address_db:
        raise HTTPException(status_code=404, detail="Address not found")
    buyer_db = crud.user.get_buyer_by_user_id(db=db, user_id=user_id)
    if not buyer_db.id == address_db.buyer_id:
        raise HTTPException(status_code=400, detail="You are not the owner of this address")
    address_deleted = crud.address.delete_address(db=db, address_id=address_id)
    return address_deleted