from fastapi import HTTPException
from redis import Redis
import time

class RateLimiter:
    def __init__(self, redis_client: Redis):
        self.redis = redis_client
        
    async def check_rate(self, user_id: str, limit: int, window: int):
        current = time.time()
        key = f"rate:{user_id}"
        
        if await self.redis.get(key) > limit:
            raise HTTPException(status_code=429, detail="Too many requests") 