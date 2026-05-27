from app.providers.base import BaseProvider
from app.providers.gemini import GeminiProvider 
from app.providers.openai import OpenAIProvider

def get_provider(provider: str) -> BaseProvider:
    if provider == "gemini":
        return GeminiProvider()
    elif provider == "openai":
        return OpenAIProvider()
    else :
        raise ValueError(f"Provider '{provider}' tidak dikenal")    

# fungsi utama
def chat(message: str, provider: str) -> str:
    p = get_provider(provider)
    return p.chat(message)
