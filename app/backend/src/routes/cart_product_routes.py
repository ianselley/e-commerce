from fastapi import  Depends, APIRouter, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from src import schemas, crud, utils

router = APIRouter()
token_auth_schema = HTTPBearer()


@router.post("", response_model=schemas.CartProduct)
def add_to_cart(product_id: int, quantity: int, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    product = crud.product.get_product(db=db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    buyer = crud.user.get_buyer_by_user_id(db=db, user_id=user_id)
    if not buyer:
        raise HTTPException(status_code=400, detail="Buyer not found")
    cart_product = crud.cart_product.get_cart_product_by_product_id(db=db, product_id=product_id, buyer_id=buyer.id)
    if cart_product and cart_product.quantity + quantity > product.stock:
        raise HTTPException(status_code=400, detail=f'This product has only {product.stock} units in stock, and you already have {cart_product.quantity} in your cart')
    cart_product_schema = schemas.CartProductCreate(quantity=quantity, buyer_id=buyer.id, product_id=product.id)
    if not cart_product:
        new_cart_product = crud.cart_product.add_to_cart(db=db, cart_product=cart_product_schema)
    else:
        new_cart_product = crud.cart_product.change_quantity(db=db, cart_product_id=cart_product.id, quantity=quantity + cart_product.quantity)
    return new_cart_product


@router.put("", response_model=schemas.CartProduct)
def change_quantity(cart_product_id: int, quantity: int, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    cart_product = crud.cart_product.get_cart_product(db=db, cart_product_id=cart_product_id)
    if not cart_product:
        raise HTTPException(status_code=404, detail="Cart product not found")
    cart_product = crud.cart_product.change_quantity(db=db, cart_product_id=cart_product.id, quantity=quantity)
    return cart_product


@router.delete("", response_model=schemas.CartProduct)
def remove_from_cart(cart_product_id: int, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    cart_product = crud.cart_product.get_cart_product(db=db, cart_product_id=cart_product_id)
    if not cart_product:
        raise HTTPException(status_code=404, detail="Cart product not found")
    buyer = crud.user.get_buyer_by_user_id(db=db, user_id=user_id)
    if buyer.id != cart_product.buyer_id:
        raise HTTPException(status_code=400, detail="User not owner of cart product")
    cart_product_removed = crud.cart_product.remove_from_cart(db=db, cart_product_id=cart_product_id)
    return cart_product_removed
