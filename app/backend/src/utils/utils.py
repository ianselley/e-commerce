import jwt
from src.database import SessionLocal

import os


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class VerifyToken():
    def __init__(self, token):
        self.token = token
        jwks_url = f'https://{os.getenv("AUTH0_DOMAIN")}/.well-known/jwks.json'
        self.jwks_client = jwt.PyJWKClient(jwks_url)


    def get_signing_key(self):
        signing_key = self.jwks_client.get_signing_key_from_jwt(self.token).key

        return signing_key


    def get_payload(self):
        payload = jwt.decode(
            self.token,
            self.signing_key,
            algorithms=os.getenv("AUTH0_ALGORITHMS"),
            audience=os.getenv("AUTH0_AUDIENCE"),
            issuer=os.getenv("AUTH0_ISSUER"),
        )

        return payload


    def verify(self):
        try:
            self.signing_key = self.get_signing_key()
            payload = self.get_payload()
        except Exception as e:
            return {"status": "error", "message": str(e)}

        return payload
