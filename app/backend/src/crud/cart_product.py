from sqlalchemy.orm import Session

from src import models, crud, schemas


def get_cart_product(db: Session, cart_product_id: int):
    return db.query(models.CartProduct).filter_by(id=cart_product_id).first()


def get_cart_product_by_product_id(db: Session, product_id: int, buyer_id: int):
    return db.query(models.CartProduct).filter_by(product_id=product_id, buyer_id=buyer_id).first()


def add_to_cart(db: Session, cart_product: schemas.CartProductCreate):
    cart_product_created = models.CartProduct(**cart_product.dict())
    db.add(cart_product_created)
    db.commit()
    db.refresh(cart_product_created)
    return cart_product_created


def change_quantity(db: Session, cart_product_id: int, quantity: int):
    cart_product = get_cart_product(db=db, cart_product_id=cart_product_id)
    cart_product.quantity = quantity
    db.commit()
    db.refresh(cart_product)
    return cart_product


def remove_from_cart(db: Session, cart_product_id: int):
    cart_product = get_cart_product(db=db, cart_product_id=cart_product_id)
    product_id = cart_product.product_id
    product = crud.product.get_product(db=db, product_id=product_id) # Needed
    db.delete(cart_product)
    db.commit()
    return cart_product