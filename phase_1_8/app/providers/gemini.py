import asyncio
import queue
import threading
import google.generativeai as genai
from typing import AsyncGenerator
from app.core.config import settings
from app.providers.base import BaseProvider

class GeminiProvider(BaseProvider):
    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model = genai.GenerativeModel("gemini-3.5-flash")

    def chat(self, message: str) -> str:
        response = self.model.generate_content(message)
        return response.text

    async def stream(self, message: str) -> AsyncGenerator[str, None]:
        # pakai queue untuk bridge antara sync thread dan async generator
        q: queue.Queue = queue.Queue()
        DONE = object()  # sentinel value penanda selesai

        def run_sync():
            try:
                # configure ulang di thread ini karena config tidak terbawa antar thread
                genai.configure(api_key=settings.GEMINI_API_KEY)
                model = genai.GenerativeModel("gemini-3.5-flash")
                response = model.generate_content(message, stream=True)
                for chunk in response:
                    if chunk.text:
                        q.put(chunk.text)
            except Exception as e:
                q.put(e)
            finally:
                q.put(DONE)

        # jalankan sync code di thread terpisah
        thread = threading.Thread(target=run_sync)
        thread.start()

        # baca dari queue secara async
        while True:
            # tunggu item tersedia tanpa block event loop
            item = await asyncio.to_thread(q.get)
            if item is DONE:
                break
            if isinstance(item, Exception):
                raise item
            yield item
