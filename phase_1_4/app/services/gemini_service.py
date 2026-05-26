import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash-lite")

def chat_gemini(message: str) -> str:
    response = model.generate_content(message)
    return response.text