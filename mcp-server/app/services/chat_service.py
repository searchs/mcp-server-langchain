from app.services.redis_service import (
    get_user_context, get_chat_history, save_to_history
)
from app.llm.langchain_client import llm
from langchain.schema import SystemMessage, HumanMessage, AIMessage
import json

def build_prompt(context: dict):
    return [SystemMessage(content=f"""
You are an assistant for {context.get('name', 'a user')} who prefers answers that are {context.get('tone', 'clear')}.
They are currently working on: {', '.join(context.get('projects', [])) or 'various projects'}.
""".strip())]

async def handle_chat(user_id: str, message: str):
    context = get_user_context(user_id)
    messages = build_prompt(context)

    for msg in get_chat_history(user_id):
        if msg["role"] == "user":
            messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            messages.append(AIMessage(content=msg["content"]))

    messages.append(HumanMessage(content=message))
    response = llm(messages)

    save_to_history(user_id, "user", message)
    save_to_history(user_id, "assistant", response.content)
    return {"response": response.content}
