from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from .config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import HTTPException

# Password Hashing Context using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Verify password matches the hash
def verify_password(plain_password, hashed_password):
    """Check if a password matches the hash"""
    return pwd_context.verify(plain_password, hashed_password) # Returns True if the password matches the hash, False otherwise

# Hash a password for storage
"""
input : Test1234
output : $2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW
"""

def get_password_hash(password):
    """Hash a password for storage"""
    return pwd_context.hash(password) # Returns the hashed password

# Generate a JWT token
# data: dict - The data to encode in the JWT token
# expires_delta: Optional[timedelta] - The expiration time of the JWT token (default is 30 minutes)
# Returns the encoded JWT token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Generate a JWT token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Add the expiration time to the data to encode
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Decode a JWT token
# token: str - The JWT token to decode
# credentials_exception: HTTPException - The exception to raise if the token is invalid
# Returns the decoded JWT token
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        raise HTTPException(status_code=401, detail=str(e))