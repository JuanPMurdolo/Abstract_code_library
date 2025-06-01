from typing import Literal
from fastapi import APIRouter, HTTPException
from .auth_service import AuthService
from app.auth.jwt_utils import create_token
from pydantic import BaseModel

router = APIRouter()
auth = AuthService()

class AuthRequest(BaseModel):
    username: str
    password: str
    role: Literal["admin", "user"] = "user"  # default es "user"

#Register and login with auth_service
@router.post("/register")
def register(request: AuthRequest):
    username = request.username
    password = request.password
    role = request.role
    if not username or not password:
        raise HTTPException(status_code=400, detail="Username y password son requeridos")
    try:
        auth.register(username, password, role)
        return {"message": "Usuario registrado"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
def login(request: AuthRequest):
    username = request.username
    password = request.password
    if not username or not password:
        raise HTTPException(status_code=400, detail="Username y password son requeridos")
    user = auth.login(username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    token = create_token(user.username, user.role)
    return {"token": token, "role": user.role}