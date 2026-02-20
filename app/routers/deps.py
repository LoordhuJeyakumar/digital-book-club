from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from ..database import get_db
from ..core.security import ALGORITHM, SECRET_KEY
from ..models.user import UserModel, UserRole

# 🗺️ 1. The Entrance Sign (OAuth2)
# This tells the browser/Swagger UI: "To get into protected areas, 
# you MUST go to the '/auth/login' desk first and get an ID card."
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    🔍 2. The Identity Desk
    Workflow:
    - Input: The 'Wristband' (Token) from the user's header.
    - Logic: Use our 'Secret Decoder Ring' (SECRET_KEY) to read the token.
    - Logic: Check if that person exists in our File Cabinet (Database).
    - Output: The actual User object (who they are).
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials - please log in again.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        # Decrypt the wristband to read the person's email
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        # If the wristband is fake or expired, block them!
        raise credentials_exception
        
    # Look up that specific human in our database
    user = db.query(UserModel).filter(UserModel.email == email).first()
    if user is None:
        raise credentials_exception
        
    return user

class RoleChecker:
    """
    💂‍♂️ 3. The Security Guard
    Workflow:
    - Logic: This guard has a 'List of Allowed Jobs' in his hand.
    - Logic: He asks the Identity Desk who the user is.
    - Logic: If your 'Role' (Job Title) isn't on the list, he blocks you.
    """
    def __init__(self, allowed_roles: list[UserRole]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: UserModel = Depends(get_current_user)):
        # If your role isn't on my permitted list...
        if user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Sorry! You don't have the specific 'Library Keys' for this action."
            )
        return user
