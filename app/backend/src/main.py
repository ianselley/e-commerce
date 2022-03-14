from fastapi import Depends, FastAPI, Response, status
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
import os

from src import utils
from src.routes import user_routes, address_routes
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


@app.get("/private")
def private_endpoint(response: Response, token: str = Depends(token_auth_schema)):
    result = utils.user.decode(token)

    if result.get("status"):
        response.status_code = status.HTTP_400_BAD_REQUEST
        return result

    return result