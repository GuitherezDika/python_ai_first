from fastapi import FastAPI
from app.core.config import settings
from app.routers.chat_router import router as chat_router


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

app.include_router(chat_router)

# source venv/bin/activate
# python3 -m uvicorn app.main:app --reload