python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn python-dotenv google-generativeai

===
envi

PLACEHOLDER___GEMINI_API_KEY=AQ.Ab8RN6I2qsxYITPx69ns9sjW4PRX4fim8xFzaUVQiHubyNo92g
PLACEHOLDER___APP_NAME=AI Gateway
PLACEHOLDER___OPENAI_API_KEY=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

=====
SSE (phase_1_5):
Client → POST /chat/stream → Server stream response → selesai

WebSocket (phase_1_6):
Client ←→ ws://localhost:8000/ws/chat  (connection tetap terbuka)
Client kirim pesan → Server balas streaming → Client kirim lagi → dst

=====
INSTALASI:
(venv) wcs@WCSs-MacBook-Pro phase_1_6 % pip install 'uvicorn[standard]'

Untuk test WebSocket, tidak bisa pakai curl biasa. Pakai wscat:
npm install -g wscat

terminal 1
uvicorn app.main:app --reload

terminal 2:
wscat -c ws://127.0.0.1:8000/ws/chat

postman
di kiri atas klik "NEW" -> WebSocket -> name websocket 
-> URL => ws://127.0.0.1:8000/ws/chat
-> connect
-> Message = "....." -> Send
-> [DONE]