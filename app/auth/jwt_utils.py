import jwt
from datetime import datetime, timedelta

SECRET = "supersecreto"
ALGORITHM = "HS256"
EXPIRATION_MINUTES = 30

def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=EXPIRATION_MINUTES)
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGORITHM])
    except jwt.PyJWTError:
        return None