from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.backend.core.database import get_db
from app.backend.utils.redis_client import redis_client

router = APIRouter()

@router.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    result = db.execute("SELECT 1")
    return {"message": "Database connection successful", "result": result.scalar()}

@router.get("/test-redis")
def test_redis():
    redis_client.set("test_key", "test_value")
    value = redis_client.get("test_key")
    return {"message": "Redis connection successful", "value": value.decode()}