from fastapi import  Depends, APIRouter, HTTPException, File, UploadFile, Form
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from src import schemas, crud, utils


router = APIRouter()
token_auth_schema = HTTPBearer()

@router.get("", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(utils.db.get_db)):
    product = crud.get_product(db, product_id=product_id)
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
    for image in images:
        if not image.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Invalid image type")
    token_data = utils.user.decode(token)
    user_id = token_data.get("sub")
    if not user_id:
        raise HTTPException(status_code=400, detail="Invalid token")
    list_of_image_paths = crud.product.upload_images(db=db, images=images, product_id=product_id)
    return list_of_image_paths