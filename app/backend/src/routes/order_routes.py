from fastapi import  Depends, APIRouter, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from src import schemas, crud, utils

router = APIRouter()
token_auth_schema = HTTPBearer()

@router.post("", response_model=list[schemas.Order])
def create_order(address_id: int, cart_product_ids: str, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    buyer = crud.user.get_buyer_by_user_id(db=db, user_id=user_id)
    if not buyer:
        raise HTTPException(status_code=400, detail="Buyer not found")
    cart_product_ids = cart_product_ids.split(",")
    for cart_product_id in cart_product_ids:
        cart_product = crud.cart_product.get_cart_product(db=db, cart_product_id=cart_product_id)
        if not cart_product:
            raise HTTPException(status_code=400, detail="Cart product not found")
        if cart_product.buyer_id != buyer.id:
            raise HTTPException(status_code=400, detail="You can't buy this product, it's not in your cart")
    created_orders = crud.order.create_orders(db=db, address_id=address_id, buyer_id=buyer.id, cart_product_ids=cart_product_ids)
    return created_orders


@router.put("")
def product_delivered(order_id: int, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    buyer = crud.user.get_buyer_by_user_id(db=db, user_id=user_id)
    if not buyer:
        raise HTTPException(status_code=400, detail="Buyer not found")
    order = crud.order.get_order(db=db, order_id=order_id)
    if not order:
        raise HTTPException(status_code=400, detail="Order not found")
    if order.buyer_id != buyer.id:
        raise HTTPException(status_code=400, detail="You can't update this order, it's not yours")
    updated_order = crud.order.product_delivered(db=db, order_id=order_id)
    return updated_order
