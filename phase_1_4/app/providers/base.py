from abc import ABC, abstractmethod

class BaseProvider(ABC):
    # aturan untuk semua provider
    @abstractmethod  # method yang wajib ada di tiap provider
    def chat(self, message: str) -> str:
        pass  # isinya kosong, karena tiap provider punya implementasi masing2
