from fastapi import APIRouter
from repository.user_repository import UserRepository
from schemas.user_schema import UserCreate, UserResponse
from service.user_service import UserService

router = APIRouter()

service = UserService()
# =========================
# CREATE
# =========================
@router.post("/users", response_model=UserResponse)
def create_user(payload: UserCreate):
    return service.create_user(payload.name)

# =========================   
# READ
# =========================
@router.get("/users", response_model=list[UserResponse])
def list_users():
    return service.list_users()