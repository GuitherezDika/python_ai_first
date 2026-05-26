from fastapi import FastAPI
from app.routers.todo_router import router as todo_router

app = FastAPI(
    title="FastAPI Clean Architecture",
    version="1.0.0"
)

app.include_router(todo_router)

# uvicorn app.main:app --reload