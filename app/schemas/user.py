from pydantic import BaseModel, EmailStr
from app.models.user import UserRole


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    """Schema for registering a new user"""
    password: str
    role: UserRole = UserRole.MEMBER


class UserLogin(BaseModel):
    """Schema for logging in (only needs email and password)"""
    email: EmailStr
    password: str


class User(UserBase):
    """Schema for reading user data (never show password!)"""
    id: int
    role: UserRole

    model_config = {
        "from_attributes": True
    }


class Token(BaseModel):
    """Schema for the JWT Access Token"""
    access_token: str
    token_type: str
