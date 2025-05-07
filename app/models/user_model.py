from pydantic import BaseModel
from typing import Literal

class User(BaseModel):
    username: str
    password: str  # para demo, en real usar hash
    role: Literal["admin", "user"]