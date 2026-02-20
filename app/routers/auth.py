from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..db import get_db
from ..models.user import UserModel, UserRole
from ..schemas.user import UserCreate, UserLogin, Token, User
from ..core.security import get_password_hash, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user (Sign Up)
    1. Check if email already exists
    2. Hash the password
    3. Save to database
    """
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    if user.role not in [UserRole.ADMIN, UserRole.MEMBER]:
        raise HTTPException(status_code=400, detail="Invalid role")

    if user.role == UserRole.ADMIN:
        raise HTTPException(status_code=400, detail="Admin registration is not allowed")

    role = UserRole.MEMBER
    if user.role == UserRole.ADMIN:
        role = UserRole.ADMIN

    if user.role == UserRole.MEMBER:
        role = UserRole.MEMBER

    
    
    hashed_pwd = get_password_hash(user.password)
    new_user = UserModel(email=user.email, hashed_password=hashed_pwd, role=role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login", response_model=Token)
def login(user_credentials: UserLogin, db: Session = Depends(get_db)):
    """
    Login to get an Access Token (Sign In)
    1. Find user by email
    2. Check if password matches hash
    3. Issue JWT token
    """
    user = db.query(UserModel).filter(UserModel.email == user_credentials.email).first()
    
    if not user or not verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
