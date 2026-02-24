from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
import httpx
import os

from ..database import get_db
from ..models.user import UserModel, UserRole
from ..schemas.user import UserCreate, UserLogin, Token, User
from ..core.security import get_password_hash, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

# --- Social Login Config ---
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "your-google-client-id")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "your-google-client-secret")
GOOGLE_REDIRECT_URI = "http://127.0.0.1:8000/auth/google/callback"

@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    The 'Sign Up' Counter 📝
    - Input: User sends an email and a password.
    - Logic: We check if the email is taken, scramble the password, and save to DB.
    - Output: We return the user info (minus the password!).
    """
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Password can be None for OAuth, but required for manual registration
    if not user.password:
        raise HTTPException(status_code=400, detail="Password is required for manual registration")

    hashed_pwd = get_password_hash(user.password)
    
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
    user = db.query(UserModel).filter(UserModel.email == user_credentials.email).first()
    
    if not user or not user.hashed_password or not verify_password(user_credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

# --- OAUTH: THE GLOBAL PASSPORT ---

@router.get("/google/login")
def google_login():
    """
    Step 1: The Redirect ✈️
    Send the user to Google's official login page.
    """
    return RedirectResponse(
        url=f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id={GOOGLE_CLIENT_ID}&redirect_uri={GOOGLE_REDIRECT_URI}&scope=openid%20email%20profile&prompt=select_account"
    )

@router.get("/google/callback", response_model=Token)
async def google_callback(code: str, db: Session = Depends(get_db)):
    """
    Step 2: The Callback & Token Exchange 🤝
    Google sends the user back here with a secret 'code'.
    We trade that code for their actual email and create our own JWT token.
    """
    async with httpx.AsyncClient() as client:
        # A. Trade the code for a Google Access Token
        token_response = await client.post(
            "https://oauth2.googleapis.com/token",
            data={
                "client_id": GOOGLE_CLIENT_ID,
                "client_secret": GOOGLE_CLIENT_SECRET,
                "code": code,
                "grant_type": "authorization_code",
                "redirect_uri": GOOGLE_REDIRECT_URI,
            },
        )
        if token_response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to authenticate with Google")
            
        access_token = token_response.json().get("access_token")

        # B. Use the Google Access Token to get the user's details
        user_info_response = await client.get(
            "https://www.googleapis.com/oauth2/v2/userinfo",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        user_info = user_info_response.json()

    user_email = user_info.get("email")
    google_id = user_info.get("id")

    # C. The Integration: Check if they exist in our Database
    user = db.query(UserModel).filter(UserModel.email == user_email).first()
    
    if not user:
        # If new, create an account WITHOUT a password!
        user = UserModel(
            email=user_email,
            role=UserRole.MEMBER,
            oauth_provider="google",
            oauth_id=google_id
        )
        db.add(user)
        db.commit()
        db.refresh(user)
    else:
        # If they exist but haven't linked Google yet, link it now.
        if not user.oauth_provider:
             user.oauth_provider = "google"
             user.oauth_id = google_id
             db.commit()

    # D. Issue OUR "Digital Wristband" (JWT)
    # They are now fully authenticated in our system!
    our_jwt_token = create_access_token(data={"sub": user.email})
    return {"access_token": our_jwt_token, "token_type": "bearer"}
