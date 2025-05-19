from fastapi import FastAPI
from app.routes import chat

app = FastAPI(title="MCP Server", version="1.0.0", description="MCP Server with LangChain ")
app.include_router(chat.router)
