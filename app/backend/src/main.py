from fastapi import FastAPI
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
import os

from src.routes import user_routes, address_routes, product_routes, cart_product_routes
from src.database import engine, Base


Base.metadata.create_all(bind=engine)
token_auth_schema = HTTPBearer()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("BACKEND_CORS_ORIGINS"),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_routes.router, prefix="/user")
app.include_router(address_routes.router, prefix="/address")
app.include_router(product_routes.router, prefix="/product")
app.include_router(cart_product_routes.router, prefix="/cart-product")
