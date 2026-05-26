from fastapi import FastAPI
from app.routers.todo_router import router as todo_router
from app.routers.auth_router import router as auth_router

from app.middleware.logger import LoggerMiddleware
from app.core.config import settings

app = FastAPI(
    title="FastAPI Clean Architecture",
    version="1.0.0"
)
app.add_middleware(LoggerMiddleware)

app.include_router(todo_router)
app.include_router(auth_router)

# uvicorn app.main:app --reload