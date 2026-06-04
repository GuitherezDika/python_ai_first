# app/main.py
from fastapi import FastAPI, WebSocket
from app.core.config import settings
from app.ws.chat_ws import chat_endpoint
from app.routers.chat_router import router as chat_router

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

# WebSocket endpoint
@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await chat_endpoint(websocket)

# HTTP endpoint (dengan cache)
app.include_router(chat_router)
