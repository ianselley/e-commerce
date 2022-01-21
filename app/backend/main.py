from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.db.database import session
# from src.db.models import Product
from src.db.models import User, Item
from core import config

from typing import Optional

from sqlalchemy.orm import Session

from src.db import models, crud, schemas
from src.db.database import Session, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=config.BACKEND_CORS_ORIGINS,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.get("/")
# def read_root():

#     return {"New Hello": "New World!!"}


# @app.get("/items")
# def read_item(q: str = None):
#     if q is not None:
#         product = Product(name=q)
#         print(product)
#         session.add(product)
#         session.commit()
#         products = session.query(Product).all()
#         return {"products": [item.name for item in products]}
#     return {"q": q}


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items