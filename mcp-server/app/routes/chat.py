from fastapi import APIRouter, Request
from app.services.chat_service import handle_chat

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_id = data.get("user_id")
    message = data.get("message")
    return await handle_chat(user_id, message)
