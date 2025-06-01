from fastapi import FastAPI
from app.api.routes import router as api_router
from app.auth.auth_router import router as auth_router

app = FastAPI()
app.include_router(api_router, prefix="/api")
app.include_router(auth_router, prefix="/auth")
