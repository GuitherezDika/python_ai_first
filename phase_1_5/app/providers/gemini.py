import asyncio
import google.generativeai as genai
from typing import AsyncGenerator
from app.core.config import settings
from app.providers.base import BaseProvider

class GeminiProvider(BaseProvider):
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-2.5-flash-lite")

    def chat(self, message: str) -> str:
        response = self.model.generate_content(message)
        return response.text

    async def stream(self, message: str) -> AsyncGenerator[str, None]:
        # generate_content(stream=True) adalah blocking/sync
        # asyncio.to_thread = jalankan di thread terpisah supaya tidak block event loop
        response = await asyncio.to_thread(
            self.model.generate_content, message, stream=True
        )
        for chunk in response:
            if chunk.text:
                yield chunk.text
            # beri kesempatan event loop jalan sebentar
            await asyncio.sleep(0)
