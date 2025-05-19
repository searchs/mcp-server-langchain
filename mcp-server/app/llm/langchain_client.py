from langchain.chat_models import ChatOpenAI
import os

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY", "MISSING_KEY")
)
