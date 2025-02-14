from datetime import datetime, timedelta, timezone  # Import timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .config import settings
from app.backend.utils.redis_client import redis_client
from app.backend.models.user import User  # Import the User model 

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password, hashed_password):
    """Verify a plain password against a hashed password."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    """Hash a plain password."""
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    """Create a JWT token with an optional expiration time."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta  # Use timezone-aware datetime
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)  # Use timezone-aware datetime
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def decode_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        print(f"Decoded token payload: {payload}")  # Debug log
        return payload
    except JWTError:
        raise credentials_exception

def add_to_blacklist(token: str, expires_in: int):
    print(f"Adding token to Redis blacklist: {token}")  # Debug log
    try:
        redis_client.set(token, "blacklisted", ex=expires_in)
        print("Token successfully added to Redis blacklist.")
    except Exception as e:
        print(f"Error adding token to Redis blacklist: {e}")

def is_token_blacklisted(token: str) -> bool:
    print(f"Checking if token is blacklisted: {token}")  # Debug log
    try:
        exists = redis_client.exists(token) == 1
        print(f"Token '{token}' exists in Redis: {exists}")
        return exists
    except Exception as e:
        print(f"Error checking token in Redis: {e}")
        return False

def authenticate_user(db: Session, email: str, password: str) -> User:
    """Authenticate a user by email and password."""
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None  # User not found
    if not verify_password(password, user.hashed_password):
        return None  # Incorrect password
    return user

def create_reset_token(email: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=settings.RESET_TOKEN_EXPIRE_MINUTES)
    to_encode = {
        "exp": expire,
        "email": email,
        "type": "reset"
    }
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def verify_reset_token(token: str) -> str:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        if payload.get("type") != "reset":
            raise HTTPException(status_code=400, detail="Invalid token type")
        return payload.get("email")
    except JWTError:
        raise HTTPException(status_code=400, detail="Invalid or expired token")
