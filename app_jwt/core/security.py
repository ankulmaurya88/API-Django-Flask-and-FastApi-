from datetime import datetime, timedelta
from jose import jwt, JWTError

SECRET_KEY = "993f213cd0e0142c49e41656502e02cc6340617425d9bb843f0caee1f0c715ba"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 15
REFRESH_TOKEN_EXPIRE_DAYS = 7

# ----- In-memory refresh token store (demo) -----
refresh_token_store = set()


def create_access_token(data: dict):
    payload = data.copy()
    payload.update({
        "type": "access",
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    })
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict):
    payload = data.copy()
    payload.update({
        "type": "refresh",
        "exp": datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    })
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    refresh_token_store.add(token)
    return token


def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None


def is_refresh_token_valid(token: str):
    return token in refresh_token_store
