PHASE 1_4 — AI Gateway

Durasi: 2 minggu

Belajar
OpenAI SDK
Gemini SDK
provider abstraction
API key security

Project:

Multi AI Provider Gateway

========
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn python-dotenv openai google-generativeai

target:
phase_1_4/
├── .env                          ← API keys disimpan di sini
├── app/
│   ├── main.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   │   └── chat_model.py         ← request/response schema
│   ├── services/
│   │   ├── openai_service.py     ← logic call OpenAI
│   │   └── gemini_service.py     ← logic call Gemini
│   └── routers/
│       └── chat_router.py        ← endpoint /chat

=======

sisi front end:
Flutter/Client
    ↓
POST /chat  { provider: "openai", message: "Hello" }
    ↓
chat_router
    ↓
pilih service berdasarkan provider
    ↓
openai_service / gemini_service
    ↓
return response AI

======

1. API Key untuk Gemini gratis
https://aistudio.google.com/api-keys?project=gen-lang-client-0169963682
login google
name = fastapi-ai-gateway-dev
Generate API Key
Choose an important project: Default gemini project
Create Key

API Key details:
API Key = AIzaSyAxG4MomUvKjYhEG_5cIkYWuea1G7C0aes <---->
Name = fastapi-ai-gateway-dev
Project Name = projects/485494866617
Project Number = 485494866617

=====
file baru .env
GEMINI_API_KEY=AIzaSyAxG4MomUvKjYhEG_5cIkYWuea1G7C0aes

===
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn python-dotenv google-generativeai

mantab
===

create sutruktur project

phase_1_4/
├── .env                    ← sudah ada ✅
├── app/
│   ├── main.py
│   ├── core/
│   │   └── config.py
│   ├── models/
│   │   └── chat_model.py
│   ├── services/
│   │   └── gemini_service.py
│   └── routers/
│       └── chat_router.py


cek limit quota request AI
https://ai.dev/rate-limit 