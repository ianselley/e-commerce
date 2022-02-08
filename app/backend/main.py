from fastapi import Depends, FastAPI, HTTPException, Response, status
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from src.utils import utils

from core.config import BACKEND
from src.routes import user_routes
from src.database import engine, Base

Base.metadata.create_all(bind=engine)
token_auth_scheme = HTTPBearer()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=BACKEND["BACKEND_CORS_ORIGINS"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router, prefix="/user")


@app.get("/private")
def private_endpoint(response: Response, token: str = Depends(token_auth_scheme)):
    result = utils.VerifyToken(token.credentials).verify()

    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    return result

@app.get("/")
def root():
    return {"message": "Hello World"}

# @app.post("/buyers/", response_model=schema.Buyer)
# def create_buyer(buyer: schema.BuyerCreate, db: Session = Depends(get_db)):
#     db_buyer = crud.get_buyer_by_email(db, email=buyer.email)
#     if db_buyer:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_buyer(db=db, buyer=buyer)


# @app.get("/buyers/", response_model=list[schema.Buyer])
# def read_buyers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     buyers = crud.get_buyers(db, skip=skip, limit=limit)
#     return buyers


# @app.get("/buyers/{buyer_id}", response_model=schema.Buyer)
# def read_buyer(buyer_id: int, db: Session = Depends(get_db)):
#     db_buyer = crud.get_buyer(db, buyer_id=buyer_id)
#     if db_buyer is None:
#         raise HTTPException(status_code=404, detail="buyer not found")
#     return db_buyer


# @app.post("/buyers/{buyer_id}/items/", response_model=schema.Item)
# def create_item_for_buyer(
#     buyer_id: int, item: schema.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_buyer_item(db=db, item=item, buyer_id=buyer_id)


# @app.get("/items/", response_model=list[schema.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items