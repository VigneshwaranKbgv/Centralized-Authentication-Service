from fastapi import HTTPException, status
from ..utils.redis_client import redis_client

def rate_limit(user_id: str, limit: int = 10, window: int = 60):
    """Rate limit requests for a user."""
    key = f"rate_limit:{user_id}"
    print(f"Rate limiting user: {user_id}")  # Debug log
    current = redis_client.incr(key)
    if current == 1:
        redis_client.expire(key, window)
    if current > limit:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail="Rate limit exceeded",
        )