import jwt
import re
import os
import phonenumbers


email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

def email_is_valid(email):
    if re.fullmatch(email_regex, email):
        return True
    return False


def telephone_is_valid(telephone):
    if telephone == " " or telephone == "":
        return True
    number = phonenumbers.parse(telephone)
    if phonenumbers.is_valid_number(number):
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