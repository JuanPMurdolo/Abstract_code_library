from app.models.user_model import User
from typing import Dict

class AuthService:
    def __init__(self):
        self.users: Dict[str, User] = {}

    def register(self, username: str, password: str, role: str):
        if username in self.users:
            raise ValueError("Usuario ya existe")
        self.users[username] = User(username=username, password=password, role=role)

    def login(self, username: str, password: str) -> str | None:
        user = self.users.get(username)
        if user and user.password == password:
            return user.role
        return None