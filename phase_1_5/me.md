cd phase_1_5
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn python-dotenv google-generativeai openai


# app/providers/base.py
from abc import ABC, abstractmethod
from typing import AsyncGenerator

class BaseProvider(ABC):
    @abstractmethod
    def chat(self, message: str) -> str:
        pass

    @abstractmethod
    async def stream(self, message: str) -> AsyncGenerator[str, None]:
        pass



=====
# app/ws/chat_ws.py
from fastapi import WebSocket, WebSocketDisconnect
import app.services.gemini_service as chat_service

async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()  # terima koneksi
    
    try:
        while True:
            # tunggu pesan dari client
            message = await websocket.receive_text()
            
            # stream response ke client per chunk
            async for chunk in chat_service.stream(message, "gemini"):
                await websocket.send_text(chunk)
            
            # kirim tanda selesai
            await websocket.send_text("[DONE]")

    except WebSocketDisconnect:
        print("Client disconnected")

====
# app/main.py
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
