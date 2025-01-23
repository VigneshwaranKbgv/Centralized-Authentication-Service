from ..utils.redis_client import redis_client

def store_session(user_id: str, session_data: dict, expires_in: int):
    print(f"Storing session for user: {user_id}, data: {session_data}")  # Debug log
    try:
        redis_client.hset(f"session:{user_id}", mapping=session_data)
        redis_client.expire(f"session:{user_id}", expires_in)
        print("Session stored successfully in Redis.")
    except Exception as e:
        print(f"Error storing session in Redis: {e}")

def get_session(user_id: str) -> dict:
    """Retrieve user session data from Redis."""
    print(f"Retrieving session for user: {user_id}")  # Debug log
    return redis_client.hgetall(f"session:{user_id}")