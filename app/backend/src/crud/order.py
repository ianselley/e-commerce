from sqlalchemy.orm import Session

from src import models, crud


def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter_by(id=order_id).first()


def create_order(db: Session, address_id: int, cart_product_id: int, buyer_id: int):
    cart_product = crud.cart_product.get_cart_product(db=db, cart_product_id=cart_product_id)
    cart_product.purchased = True
    cart_product.buyer = None
    seller_id = cart_product.product.seller_id
    seller = crud.user.get_seller(db=db, seller_id=seller_id)
    seller.number_of_products_sold += cart_product.quantity
    order = models.Order(
        address_id=address_id,
        buyer_id=buyer_id,
        seller_id=seller_id,
        cart_product_id=cart_product_id,
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    db.refresh(cart_product)
    db.refresh(seller)
    return order


def create_orders(db: Session, address_id: int, buyer_id: int, cart_product_ids: list[int]):
    orders = []
    for cart_product_id in cart_product_ids:
        order = create_order(db=db, address_id=address_id, cart_product_id=cart_product_id, buyer_id=buyer_id)
        orders.append(order)
    return orders