from sqlalchemy.orm import Session
from fastapi import UploadFile
from pathlib import Path
import shutil

from src import models, crud, schemas


def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter_by(id=product_id).first()


def create_product(db: Session, product: schemas.ProductCreate, user_id: int):
    product_created = models.Product(**product.dict())
    seller = crud.user.get_seller_by_user_id(db=db, user_id=user_id)
    product_created.seller = seller
    db.add(product_created)
    db.commit()
    db.refresh(product_created)
    return product_created


def upload_image(image: UploadFile, destination: Path, list_of_image_paths: list):
    file = destination / image.filename
    if file.exists():
        return
    file.touch()
    try:
        with file.open("wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
    finally:
        image.file.close()
    list_of_image_paths.append(file)


def upload_images(db: Session, images: list[UploadFile], product_id: int):
    product = get_product(db=db, product_id=product_id)
    seller = crud.user.get_seller(db=db, seller_id=product.seller_id)
    cwd = Path.cwd()
    destination = cwd / "product_images" / f"{seller.id}_{seller.brand}" / f"{product.id}_{product.title}"
    if not destination.exists():
        destination.mkdir(parents=True)
    list_of_image_paths = []
    for image in images:
        upload_image(image=image, destination=destination, list_of_image_paths=list_of_image_paths)
    product.has_images = True
    db.commit()
    db.refresh(product)
    return list_of_image_paths
