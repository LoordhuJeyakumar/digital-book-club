from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.user import UserModel, UserRole
from ..schemas.user import UserCreate, UserLogin, Token, User
from ..core.security import get_password_hash, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    The 'Sign Up' Counter 📝
    - Input: User sends an email and a password.
    - Logic: We check if the email is taken, scramble the password, and save to DB.
    - Output: We return the user info (minus the password!).
    """
    # Check if this person already has a library card
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Scramble the password so only the user knows the original
    hashed_pwd = get_password_hash(user.password)
    
    # Save the new user to the database
    new_user = UserModel(
        email=user.email, 
        hashed_password=hashed_pwd, 
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login", response_model=Token)
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    """
    The 'Identity Check' 🔑
    - Input: User sends login credentials.
    - Logic: Search for user, verify if password matches the scramble.
    - Output: Issue a Digital Wristband (JWT Access Token).
    """
    # Find the user by their email
    user = db.query(UserModel).filter(UserModel.email == user_credentials.email).first()
    
    # If user doesn't exist OR password is wrong, keep the door locked 🔒
    if not user or not verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create the Digital Wristband!
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
