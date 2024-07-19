from fastapi import HTTPException
from .model import LoginPayload, User


class UserAuthenticator:
    def __init__(self, user_db):
        self.user_db = user_db

    def authenticate(self, email: str, password: str):
        if email in self.user_db and self.user_db[email].get("password") == password:
            return self.user_db[email]

        raise HTTPException(status_code=401, detail="Invalid credentials")
