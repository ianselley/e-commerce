from fastapi import  Depends, APIRouter, HTTPException, File, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from pathlib import Path

from src import schemas, crud, utils


router = APIRouter()
token_auth_schema = HTTPBearer()

@router.get("", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(utils.db.get_db)):
    product = crud.product.get_product(db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/create-product", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    product_created = crud.product.create_product(db=db, product=product, user_id=user_id)
    return product_created


@router.post("/upload-images")
def upload_images(product_id: int = Form(...), images: list[UploadFile] = File(...), db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    product = crud.product.get_product(db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if (len_im := len(images)) > 10:
        raise HTTPException(status_code=400, detail=f"Too many images ({len_im}), you can only upload 10 images")
    if len(product.images) == 10:
        raise HTTPException(status_code=400, detail="Product already has 10 images, and can't have more")
    if (len_p_im := len(product.images)) + (len_im := len(images)) > 10:
        raise HTTPException(status_code=400, detail=f"Product can't have more than 10 images. Already has {len_p_im} and trying to add {len_im}")

    for image in images:
        if not image.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Invalid image type")

    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")

    user = crud.user.get_user(db=db, user_id=user_id)
    if not user.seller.id == product.seller_id:
        raise HTTPException(status_code=400, detail="You are not the owner of this product")
        
    list_of_images = crud.product.upload_images(db=db, images=images, product_id=product_id)
    return list_of_images


@router.get("/all", response_model=list[schemas.Product])
def get_all_products(substring: str = "", skip: int = 0, limit: int = 20, db: Session = Depends(utils.db.get_db)):
    products = crud.product.get_products(db=db, substring=substring, skip=skip, limit=limit)
    return products


@router.get("/{product_id}", response_model=schemas.Product)
def get_all_products(product_id: int, db: Session = Depends(utils.db.get_db)):
    product = crud.product.get_product(db=db, product_id=product_id)
    return product


@router.get("/images/{image_id}", response_class=FileResponse)
async def get_image(image_id: int):
    image_path = f"/app/product_images/{image_id}"
    if not Path(image_path).exists():
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(image_path, media_type="image/*")


@router.put("/update", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    product_updated = crud.product.update_product(db=db, product_id=product_id, product=product, user_id=user_id)
    return product_updated
    

@router.delete("/delete", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(utils.db.get_db), token: str = Depends(token_auth_schema)):
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    product = crud.product.get_product(db=db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    seller = crud.user.get_seller_by_user_id(db=db, user_id=user_id)
    if product.seller_id != seller.id:
        raise HTTPException(status_code=400, detail="You are not the seller of this product")
    product = crud.product.delete_product(db=db, product_id=product_id, user_id=user_id)
    return product