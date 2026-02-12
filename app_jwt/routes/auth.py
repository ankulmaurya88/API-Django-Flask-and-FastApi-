from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from jose import jwt, JWTError
from core.security import (
    create_access_token,
    create_refresh_token,
    is_refresh_token_valid,
    SECRET_KEY,
    ALGORITHM
)

router = APIRouter(prefix="/auth", tags=["Auth"])


# ---------- Dummy users DB ----------
USERS_DB = {
    "admin@example.com": {
        "user_id": 1,
        "password": "admin123",
        "role": "admin"
    },
    "user@example.com": {
        "user_id": 2,
        "password": "user123",
        "role": "user"
    }
}

class LoginRequest(BaseModel):
    email: str
    password: str





@router.post("/login")
def login(data: LoginRequest):
    user = USERS_DB.get(data.email)

    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    payload = {
        "user_id": user["user_id"],
        "role": user["role"]
    }

    return {
        "access_token": create_access_token(payload),
        "refresh_token": create_refresh_token(payload)
    }


@router.post("/refresh")
def refresh(refresh_token: str):
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])

        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")

        if not is_refresh_token_valid(refresh_token):
            raise HTTPException(status_code=401, detail="Refresh token revoked")

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    new_access_token = create_access_token({
        "user_id": payload["user_id"],
        "role": payload["role"]
    })

    return {"access_token": new_access_token}
