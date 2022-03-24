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


@router.post("", response_model=schemas.Address)
def get_address(id: int, db: Session = Depends(utils.db.get_db)):
    address_db = crud.address.get_address(db=db, id=id)
    return address_db