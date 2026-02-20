from pydantic import BaseModel, EmailStr
from app.models.user import UserRole


class UserBase(BaseModel):
    """The shared blueprint for user data (the basics)"""
    email: EmailStr


class UserCreate(UserBase):
    """
    The 'Sign Up' form.
    Input: What the user sends when creating an account.
    """
    password: str
    role: UserRole = UserRole.MEMBER


class UserLogin(BaseModel):
    """
    The 'Log In' form.
    Input: Only needs email and password to prove who they are.
    """
    email: EmailStr
    password: str


class User(UserBase):
    """
    The 'Membership Display'.
    Output: This is what we send BACK to the user.
    Logic: We show the ID and Role, but NEVER the password.
    """
    id: int
    role: UserRole

    model_config = {
        "from_attributes": True
    }


class Token(BaseModel):
    """
    The 'Digital Wristband'.
    Output: The JWT token sent after a successful login.
    """
    access_token: str
    token_type: str
