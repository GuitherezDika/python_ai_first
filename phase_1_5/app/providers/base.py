from abc import ABC, abstractmethod
from typing import AsyncGenerator

class BaseProvider(ABC):
    @abstractmethod
    def chat(self, message: str) -> str:
        pass
    
    @abstractmethod
    async def stream(self, message: str) -> AsyncGenerator[str, None]:
        """Kirim pesan, kembalikan response per chunk (kata/kalimat)"""
        pass
