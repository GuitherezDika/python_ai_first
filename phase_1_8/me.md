global terminal: atau lokal terminal:
brew install redis
brew services start redis

ini akan install di root macbook

cek:
redis-cli ping
hasil = PONG
redis jalan
========

phase_1_8:
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn python-dotenv google-generativeai redis 'uvicorn[standard]'

source venv/bin/activate
uvicorn app.main:app --reload

swagger:
 http://127.0.0.1:8000/docs

coba di test 10x berturut2

 {
  "message": "test rate limit",
  "provider": "gemini"
}
