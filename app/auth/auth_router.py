from typing import Literal
from fastapi import APIRouter, HTTPException
from auth.auth_service import AuthService
from auth.jwt_utils import create_token
from pydantic import BaseModel

router = APIRouter()
auth = AuthService()

class AuthRequest(BaseModel):
    username: str
    password: str
    role: Literal["admin", "user"] = "user"  # default es "user"

@router.post("/register")
def register(payload: AuthRequest):
    try:
        auth.register(payload.username, payload.password, payload.role)
        return {"message": "Usuario registrado"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(payload: AuthRequest):
    role = auth.login(payload.username, payload.password)
    if role:
        token = create_token({"sub": payload.username, "role": role})
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Credenciales inválidas")
