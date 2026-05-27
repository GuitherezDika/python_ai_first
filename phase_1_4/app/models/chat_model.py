from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(min_length=1)
    provider: str = Field(default="gemini")  # default gemini kalau tidak diisi

class ChatResponse(BaseModel):
    message: str
    provider: str
    # provider bisa dinamis OpenAI, Gemini, Llama
