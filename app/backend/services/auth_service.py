from sqlalchemy.orm import Session
from ..models.user import User
from ..core.database import SessionLocal

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, email: str, password: str = None, is_oauth_user: bool = False):
    db_user = User(email=email, hashed_password=password, is_oauth_user=is_oauth_user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()