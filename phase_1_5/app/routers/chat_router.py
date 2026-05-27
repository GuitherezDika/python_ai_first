from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from app.models.chat_model import ChatRequest, ChatResponse
import app.services.chat_service as chat_service

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

@router.post("/gemini", response_model=ChatResponse)
def chat_with_gemini(request: ChatRequest):
    try:
        result = chat_service.chat(request.message, request.provider)
        return ChatResponse(
            message=result,
            provider=request.provider
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Chat {request.provider} error: {str(e)}"
        )

@router.post("/stream")
async def chat_stream(request: ChatRequest):
    async def generate():
        async for chunk in chat_service.stream(request.message, request.provider):
            yield f"data: {chunk}\n\n"  # format SSE standar

    return StreamingResponse(
        generate(),
        media_type="text/event-stream"
    )
