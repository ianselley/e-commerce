from sqlalchemy.orm import Session

from src import models, crud, schemas


def get_cart_product(db: Session, cart_product_id: int):
    return db.query(models.CartProduct).filter_by(id=cart_product_id).first()


def add_to_cart(db: Session, cart_product: schemas.CartProductCreate):
    cart_product_created = models.CartProduct(**cart_product.dict())
    db.add(cart_product_created)
    db.commit()
    db.refresh(cart_product_created)
    return cart_product_created


def remove_from_cart(db: Session, cart_product_id: int):
    cart_product = get_cart_product(db=db, cart_product_id=cart_product_id)
    product_id = cart_product.product_id
    crud.product.get_product(db=db, product_id=product_id)
    db.delete(cart_product)
    db.commit()
    return cart_product