import google.generativeai as genai
from app.core.config import settings
from app.providers.base import BaseProvider

class GeminiProvider(BaseProvider):
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-2.5-flash-lite")

    def chat(self, message: str) -> str:
        response = self.model.generate_content(message)
        return response.text