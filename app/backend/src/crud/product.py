from sqlalchemy.orm import Session
from sqlalchemy import or_
from fastapi import UploadFile
from pathlib import Path
import shutil

from src import models, crud, schemas


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter_by(id=product_id).first()


def create_product(db: Session, product: schemas.ProductCreate, user_id: int):
    product_created = models.Product(**product.dict())
    product_created.available = False
    seller = crud.user.get_seller_by_user_id(db=db, user_id=user_id)
    product_created.seller = seller
    db.add(product_created)
    db.commit()
    db.refresh(product_created)
    return product_created


def update_product(db: Session, product: schemas.ProductUpdate):
    product_db = get_product(db=db, product_id=product.id)
    for attribute, value in vars(product).items():
        setattr(product_db, attribute, value)
    db.commit()
    db.refresh(product_db)
    return product_db


def upload_image(image: UploadFile, name: int):
    file = Path("/app/product_images") / str(name)
    if file.exists():
        return
    file.touch()
    try:
        with file.open("wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
    finally:
        image.file.close()


def upload_images(db: Session, images: list[UploadFile], product_id: int):
    product = get_product(db=db, product_id=product_id)
    for image in images:
        for product_image in product.images:
            if product_image.filename == image.filename:
                break
        else:
            models.Image(filename=image.filename, product=product)
            db.commit()
            db.refresh(product)
            upload_image(image=image, name=product.images[-1].id)
    return product.images


def change_product_availability(db: Session, product_id: int):
    product = get_product(db=db, product_id=product_id)
    product.available = not product.available
    db.commit()
    db.refresh(product)
    return product


def get_products_by_string(db: Session, substring: str = ""):
    query = db.query(models.Product).order_by(models.Product.id.desc())
    criterion = or_(
        models.Product.title.contains(substring),
        models.Product.description.contains(substring),
        models.Seller.brand.contains(substring),
    )
    return query.join(models.Seller).filter(models.Product.available).filter(criterion)


def get_products(db: Session, substring: str = "", skip: int = 0, limit: int = 20):
    products_query = get_products_by_string(db=db, substring=substring)
    return products_query.offset(skip).limit(limit).all()


def get_total_products(db: Session, substring: str = ""):
    products_query = get_products_by_string(db=db, substring=substring)
    return products_query.count()


def get_image(db: Session, image_id: int):
    return db.query(models.Image).filter_by(id=image_id).first()


def delete_image_file(image_id: int):
    Path(f"/app/product_images/{image_id}").unlink()


def delete_product(db: Session, product_id: int):
    product = get_product(db=db, product_id=product_id)
    for image in product.images:
        delete_image_file(image_id=image.id)
    db.delete(product)
    db.commit()
    return product


def delete_image(db: Session, image_id: int):
    delete_image_file(image_id=image_id)
    image = get_image(db=db, image_id=image_id)
    db.delete(image)
    db.commit()
    return image


def delete_images(db: Session, image_ids: list[int]):
    for image_id in image_ids:
        delete_image(db=db, image_id=image_id)
    return image_ids