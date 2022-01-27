from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.backend.db.crud import crud
from app.backend.db.models import models
from core import config

from app.backend.db.schemas import schema
from db.database import Session, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.post("/buyers/", response_model=schema.Buyer)
def create_buyer(buyer: schema.BuyerCreate, db: Session = Depends(get_db)):
    db_buyer = crud.get_buyer_by_email(db, email=buyer.email)
    if db_buyer:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_buyer(db=db, buyer=buyer)


@app.get("/buyers/", response_model=list[schema.Buyer])
def read_buyers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    buyers = crud.get_buyers(db, skip=skip, limit=limit)
    return buyers


@app.get("/buyers/{buyer_id}", response_model=schema.Buyer)
def read_buyer(buyer_id: int, db: Session = Depends(get_db)):
    db_buyer = crud.get_buyer(db, buyer_id=buyer_id)
    if db_buyer is None:
        raise HTTPException(status_code=404, detail="buyer not found")
    return db_buyer


@app.post("/buyers/{buyer_id}/items/", response_model=schema.Item)
def create_item_for_buyer(
    buyer_id: int, item: schema.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_buyer_item(db=db, item=item, buyer_id=buyer_id)


@app.get("/items/", response_model=list[schema.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items