from app.providers.base import BaseProvider
from app.providers.gemini import GeminiProvider
from typing import AsyncGenerator


def get_provider(provider: str) -> BaseProvider:
    if provider == "gemini":
        return GeminiProvider()
    else:
        raise ValueError(f"Provider '{provider}' tidak dikenal")    

# fungsi utama
def chat(message: str, provider: str) -> str:
    p = get_provider(provider)
    return p.chat(message)

async def stream(message: str, provider: str) -> AsyncGenerator[str, None]:
    p = get_provider(provider)
    async for chunk in p.stream(message):
        yield chunk