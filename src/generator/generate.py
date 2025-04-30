from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = init_chat_model("gemini-2.5-flash", model_provider="google_genai")