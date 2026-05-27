from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(min_length=1)
    provider: str = Field(default="gemini")

class ChatResponse(BaseModel):
    message: str
    provider: str
