from sqlalchemy import Column, Integer, String, JSON
from .base import Base

class UserSettings(Base):
    __tablename__ = "user_settings"
    
    user_id = Column(Integer, primary_key=True)
    theme = Column(String, default="light")
    notifications = Column(JSON)
    language = Column(String, default="en") 