from fastapi import APIRouter, HTTPException

from app.models.chat_model import ChatRequest, ChatResponse
from app.services.gemini_service import chat_gemini

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/gemini", response_model=ChatResponse)
def chat_with_gemini(request: ChatRequest):
    try:
        result = chat_gemini(request.message)
        return ChatResponse(
            message=result,
            provider="gemini"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Gemini error: {str(e)}"
        )
