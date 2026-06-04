from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.middleware.rate_limiter import rate_limit
import app.services.chat_service as chat_service

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
    dependencies=[Depends(rate_limit)]
)

class ChatRequest(BaseModel):
    message: str
    provider: str = "gemini"

class ChatResponse(BaseModel):
    message: str
    provider: str
    from_cache: bool


@router.post("/gemini", response_model=ChatResponse)
def chat_with_gemini(request: ChatRequest):
    try:
        result, from_cache = chat_service.chat(request.message, request.provider)
        return ChatResponse(
            message=result,
            provider=request.provider,
            from_cache=from_cache
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            # detail=f"Chat {request.provider} error: {str(e)}"
            detail=str(e)
        )
