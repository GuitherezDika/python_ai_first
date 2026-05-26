from fastapi import APIRouter, HTTPException

from app.services.auth_service import (
    register_service,
    login_service,
)

from app.models.auth_model import (AuthResponse, LoginRequest, RegisterRequest)

router = APIRouter(
    prefix='/auth',
    tags=['Auth']
)

@router.post('/register', response_model=AuthResponse)
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
    return {"message": "Register success"}

@router.post("/login", response_model=AuthResponse)
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
    
    return {"message": "Login success"}