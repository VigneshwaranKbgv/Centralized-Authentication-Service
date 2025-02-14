import json

class SessionManager:
    def __init__(self, redis_client):
        self.redis = redis_client
    
    async def create_session(self, user_id: str, data: dict):
        session_id = generate_session_id()
        await self.redis.setex(f"session:{session_id}", 3600, json.dumps(data))
        return session_id 