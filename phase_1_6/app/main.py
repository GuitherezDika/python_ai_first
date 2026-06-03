from fastapi import FastAPI, WebSocket
from app.core.config import settings
from app.ws.chat_ws import chat_endpoint


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

@app.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await chat_endpoint(websocket)