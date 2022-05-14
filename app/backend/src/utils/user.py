import jwt
import re
import os


email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
telephone_regex = r"\b(\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$)|^$\b"

def email_is_valid(email):
    if re.fullmatch(email_regex, email):
        return True
    return False


def telephone_is_valid(telephone):
    if telephone == "" or re.fullmatch(telephone_regex, telephone):
        return True
    return False


def passwords_are_valid(password, password_confirmation):
    if password == password_confirmation and len(password) >= 8:
        return True
    return False


def encode(payload):
    payload_dict = payload.__dict__
    payload = {
        "sub": payload_dict.get("id"),
        "email": payload_dict.get("email"),
        "role": payload_dict.get("role"),
    }
    token = jwt.encode(
        payload=payload,
        key=os.getenv("ACCESS_TOKEN")
    )
    return token


def decode(token):
    try:
        payload = jwt.decode(
            jwt=token.credentials,
            key=os.getenv("ACCESS_TOKEN"),
            algorithms=["HS256"]
        )
        return payload
    except jwt.exceptions.InvalidSignatureError as e:
        return {"status": "error", "message": str(e)}