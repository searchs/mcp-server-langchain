import redis
import json
from app.config import settings

r = redis.Redis(host=settings.redis_host, port=settings.redis_port, db=0, decode_responses=True)

def get_user_context(user_id: str):
    context = r.get(f"user_context:{user_id}")
    return json.loads(context) if context else {}

def get_chat_history(user_id: str):
    return [json.loads(x) for x in r.lrange(f"chat_history:{user_id}", -10, -1)]

def save_to_history(user_id: str, role: str, content: str):
    r.rpush(f"chat_history:{user_id}", json.dumps({"role": role, "content": content}))
    r.ltrim(f"chat_history:{user_id}", -10, -1)
