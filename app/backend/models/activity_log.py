from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class ActivityLog(Base):
    __tablename__ = "activity_logs"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    action = Column(String)
    ip_address = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow) 