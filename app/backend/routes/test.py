from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services.auth_service import get_db
from app.backend.utils.redis_client import redis_client

router = APIRouter()

@router.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    result = db.execute("SELECT 1")
    return {"message": "Database connection successful", "result": result.scalar()}

@router.get("/test-redis")
def test_redis():
    try:
        # Set a key in Redis
        try:
            redis_client.set("test_key", "test_value")
            print("Key set successfully in Redis.")
        except Exception as e:
            print(f"Error setting key in Redis: {e}")
        
        # Get the key from Redis
        value = redis_client.get("test_key")
        
        if value is None:
            raise HTTPException(status_code=500, detail="Redis key not found")
        
        return {"message": "Redis connection successful", "value": value}  # No .decode() needed
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Redis error: {str(e)}")