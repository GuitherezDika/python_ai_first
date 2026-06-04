from app.providers.base import BaseProvider
from app.providers.gemini import GeminiProvider
from app.cache.redis_cache import get_cache, set_cache
from typing import AsyncGenerator

def get_provider(provider: str) -> BaseProvider:
    if provider == 'gemini':
        return GeminiProvider()
    else:
        raise ValueError(f"Provider '{provider}' tidak di kenal")

def chat(message: str, provider: str) -> tupple[str, bool]:
    # cek cache dulu
    cached = get_cache(message)
    if cached:
        print(f"[CACHE HIT] {message[:30]}...")
        return cached, True
    
    #tidak ada cache, hit API
    print(f"[CACHE HIT] {message[:30]}...")
    p = get_provider(provider)
    response = p.chat(message)

    # simpan ke cache
    set_cache(message, response)
    return response, False

async def stream(message: str, provider: str) -> AsyncGenerator[str, None]:
    # streaming tidak di-cache karena response datang per chunk
    # cache hanya untuk endpoint non-streaming
    p = get_provider(provider)
    async for chunk in p.stream(message):
        yield chunk