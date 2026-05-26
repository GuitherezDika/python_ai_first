from fastapi import FastAPI
from app.core.config import settings
from app.routers.chat_router import router as chat_router

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

app.include_router(chat_router)

# uvicorn app.main:app --reload
