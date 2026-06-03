from fastapi import WebSocket, WebSocketDisconnect
import app.services.gemini_service as chat_service

async def chat_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            message = await websocket.receive_text()

            #stream response ke client per chunk
            async for chunk in chat_service.stream(message, "gemini"):
                await websocket.send_text(chunk)

            #kirim tanda selesai
            await websocket.send_text("[DONE]")

    except WebSocketDisconnect:
        print("Client disconnected")