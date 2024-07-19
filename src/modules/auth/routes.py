from fastapi import HTTPException, routing, APIRouter, Query, Depends
from pathlib import Path

from utils.file_helper import FileHelper
from .service import UserAuthenticator
from .model import LoginPayload, User

router = APIRouter(prefix="/auth", tags=["Authentication"])

mock_users = {
    "test@example.com": {
        "username": "test_user",
        "email": "test@example.com",
        "password": "12345678",
    }
}

authenticator = UserAuthenticator(mock_users)


@router.post("/login", summary="Login accound")
async def login(payload: LoginPayload, user=Depends(authenticator.authenticate)):
    return {"user": user}
