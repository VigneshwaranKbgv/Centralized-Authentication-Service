from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import httpx
from fastapi.responses import JSONResponse, RedirectResponse
from ..core.security import create_access_token, get_password_hash, verify_password
from ..models.user import User
from ..core.config import settings
from ..services.auth_service import get_db, get_user_by_email, create_user
from datetime import timedelta
from ..schemas.user import UserCreate

router = APIRouter()

# Endpoint for Google OAuth2 login
@router.get("/auth/google")
def login_google():
    google_auth_url = (
        f"https://accounts.google.com/o/oauth2/auth?"
        f"response_type=code&"
        f"client_id={settings.GOOGLE_CLIENT_ID}&"
        f"redirect_uri={settings.GOOGLE_REDIRECT_URI}&"
        f"scope=openid%20profile%20email&"
        f"access_type=offline"
    )
    # Directly redirect the user to the Google OAuth2 URL
    return RedirectResponse(url=google_auth_url)

# Endpoint for Google OAuth2 callback
@router.get("/auth/google/callback")
def callback(code: str, db: Session = Depends(get_db)):
    # Exchange the code for a token
    token_url = "https://oauth2.googleapis.com/token"
    data = {
        "code": code,
        "client_id": settings.GOOGLE_CLIENT_ID,
        "client_secret": settings.GOOGLE_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = httpx.post(token_url, data=data, headers=headers)
    token_data = response.json()

    if "error" in token_data:
        raise HTTPException(status_code=400, detail=token_data["error"])

    # Get user info using the access token
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    headers = {"Authorization": f"Bearer {token_data['access_token']}"}
    userinfo_response = httpx.get(userinfo_url, headers=headers)
    userinfo = userinfo_response.json()

    # Check if the user exists, if not, create a new user
    db_user = get_user_by_email(db, userinfo["email"])
    if not db_user:
        db_user = create_user(db, userinfo["email"], None, is_oauth_user=True)

    # Generate a JWT token for the user
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": db_user.email}, expires_delta=access_token_expires)

    # Return the token and email in the response
    frontend_url = f"http://localhost:3000/login-success?token={access_token}&email={db_user.email}"
    return RedirectResponse(url=frontend_url)

# Endpoint for user registration
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if the user already exists
    db_user = get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password and create the user
    hashed_password = get_password_hash(user.password)
    db_user = create_user(db, email=user.email, password=hashed_password)

    return {"message": "User registered successfully"}

# Endpoint for user login (token generation)
@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Check if the user exists
    db_user = get_user_by_email(db, form_data.username)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    # Verify the password
    if not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )

    # Generate a JWT token
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": db_user.email}, expires_delta=access_token_expires)

    return {"access_token": access_token, "token_type": "bearer", "email": db_user.email}