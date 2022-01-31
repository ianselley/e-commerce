import jwt
from src.database import SessionLocal

from core.config import AUTH0


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class MyError(Exception):
    def __init__(self, message):
        self.message = message


class VerifyToken():
    def __init__(self, token):
        self.token = token
        self.config = AUTH0
        jwks_url = f'https://{self.config["DOMAIN"]}/.well-known/jwks.json'
        self.jwks_client = jwt.PyJWKClient(jwks_url)


    def get_signing_key(self):
        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(
                self.token
            ).key
        except jwt.exceptions.PyJWKClientError as e:
            raise MyError(e)
        except jwt.exceptions.DecodeError as e:
            raise MyError(e)

        return signing_key


    def get_payload(self):
        try:
            payload = jwt.decode(
                self.token,
                self.signing_key,
                algorithms=self.config["ALGORITHMS"],
                audience=self.config["API_AUDIENCE"],
                issuer=self.config["ISSUER"],
            )
        except Exception as e:
            raise MyError(e)

        return payload


    def verify(self):
        try:
            self.signing_key = self.get_signing_key()
            payload = self.get_payload()
        except Exception as e:
            return {"status": "error", "message": str(e)}

        return payload
