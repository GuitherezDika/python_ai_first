from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(min_length=1)

class ChatResponse(BaseModel):
    messageL: str
    provider: str
    # provider bisa dinamis OpenAI, Gemini, Llama
