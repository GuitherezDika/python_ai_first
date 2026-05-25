virtual env
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn python-dotenv

mkdir app
mkdir app/routers
mkdir app/services
mkdir app/repositories
mkdir app/models
mkdir app/database
mkdir app/middleware
mkdir app/core

============
STEP 6 — Todo Service
app/services/todo_service.py

Business logic.

from app.repositories.todo_repository import (
    get_all_todos,
    get_todo_by_id,
    create_todo,
    delete_todo
)

def get_todos_service():
    return get_all_todos()

def get_todo_service(todo_id: int):
    return get_todo_by_id(todo_id)

def add_todo_service(title: str, done: bool):

    todo_data = {
        "id": len(get_all_todos()) + 1,
        "title": title,
        "done": done
    }

    return create_todo(todo_data)

def delete_todo_service(todo_id: int):

    todo = get_todo_by_id(todo_id)

    if not todo:
        return None

    delete_todo(todo)

    return True
STEP 7 — Todo Router
app/routers/todo_router.py
from fastapi import APIRouter, HTTPException, status

from app.models.todo_model import (
    TodoCreate,
    TodoResponse,
    ShortResponse
)

from app.services.todo_service import (
    get_todos_service,
    get_todo_service,
    add_todo_service,
    delete_todo_service
)

router = APIRouter(
    prefix="/todos",
    tags=["Todo"]
)

@router.get(
    "/",
    response_model=list[TodoResponse]
)
def get_todos():
    return get_todos_service()

@router.get(
    "/{todo_id}",
    response_model=TodoResponse
)
def get_todo(todo_id: int):

    todo = get_todo_service(todo_id)

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo

@router.post(
    "/",
    response_model=TodoResponse,
    status_code=status.HTTP_201_CREATED
)
def add_todo(todo: TodoCreate):

    return add_todo_service(
        title=todo.title,
        done=todo.done
    )

@router.delete(
    "/{todo_id}",
    response_model=ShortResponse
)
def delete_todo(todo_id: int):

    deleted = delete_todo_service(todo_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return {
        "message": "Todo deleted successfully"
    }
STEP 8 — Auth Model
app/models/auth_model.py
from pydantic import BaseModel, EmailStr, Field

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class AuthResponse(BaseModel):
    message: str
STEP 9 — Auth Repository
app/repositories/auth_repository.py
from app.database.fake_db import users

def create_user(user_data: dict):
    users.append(user_data)
    return user_data

def find_user_by_email(email: str):

    for user in users:
        if user["email"] == email:
            return user

    return None
STEP 10 — Auth Service
app/services/auth_service.py
from app.repositories.auth_repository import (
    create_user,
    find_user_by_email
)

def register_service(email: str, password: str):

    existing_user = find_user_by_email(email)

    if existing_user:
        return None

    user_data = {
        "id": 1,
        "email": email,
        "password": password
    }

    create_user(user_data)

    return user_data

def login_service(email: str, password: str):

    user = find_user_by_email(email)

    if not user:
        return None

    if user["password"] != password:
        return None

    return user
STEP 11 — Auth Router
app/routers/auth_router.py
from fastapi import APIRouter, HTTPException

from app.models.auth_model import (
    RegisterRequest,
    LoginRequest,
    AuthResponse
)

from app.services.auth_service import (
    register_service,
    login_service
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post(
    "/register",
    response_model=AuthResponse
)
def register(data: RegisterRequest):

    user = register_service(
        email=data.email,
        password=data.password
    )

    if not user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return {
        "message": "Register success"
    }

@router.post(
    "/login",
    response_model=AuthResponse
)
def login(data: LoginRequest):

    user = login_service(
        email=data.email,
        password=data.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    return {
        "message": "Login success"
    }
STEP 12 — Middleware Logger
app/middleware/logger.py
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

class LoggerMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        print(f"Request URL: {request.url}")

        response = await call_next(request)

        return response
STEP 13 — Config
.env
APP_NAME=FastAPI Clean Architecture
DEBUG=True
app/core/config.py
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME")
    DEBUG = os.getenv("DEBUG")

settings = Settings()
STEP 14 — main.py
app/main.py
from fastapi import FastAPI

from app.routers.todo_router import router as todo_router
from app.routers.auth_router import router as auth_router

from app.middleware.logger import LoggerMiddleware

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0"
)

app.add_middleware(LoggerMiddleware)

app.include_router(todo_router)
app.include_router(auth_router)
STEP 15 — RUN
uvicorn app.main:app --reload