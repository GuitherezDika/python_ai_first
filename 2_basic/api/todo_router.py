# pip3 install fastapi uvicorn
# pip3 install pydantic
from fastapi import APIRouter, HTTPException
from repository.todo_repository import TodoRepository
from service.todo_service import TodoService
from schemas.todo_schema import TodoCreate, TodoResponse, TodoUpdateById

router = APIRouter()

repo = TodoRepository()
service = TodoService(repo)


# =========================
# CREATE
# =========================
@router.post("/todos", response_model = TodoResponse)
def create_todo(payload: TodoCreate):
    todo = service.create_todo(payload.name, payload.task, payload.user_id)
    return todo


# =========================
# READ
# =========================
@router.get("/todos", response_model=list[TodoResponse])
def get_todos():
    todos = service.list_todos()
    return todos

# =========================
# UPDATE (mark done)
# =========================
@router.put("/todos/{todo_id}", response_model=TodoResponse)
def complete_todo(todo_id: int):
    try:
        todo = service.complete_todo(todo_id)
        return todo
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# =========================
# DELETE
# =========================
@router.delete("/todos/{todo_id}", response_model=TodoResponse)
def delete_todo(todo_id: int):
    try:
        todo = service.delete_todo(todo_id)
        return todo
    except:
        raise HTTPException(status_code=404, detail=str(e))

#run server =uvicorn main:router --reload

# =========================
# COMPLeted
# =========================
@router.get("/todos/completed", response_model=list[TodoResponse])
def list_completed_todos():
    """
    Return only todos with completed == True
    """
    todos = service.get_completed()
    return todos

# =========================
# is Active
# =========================
@router.get("/todos/active", response_model=list[TodoResponse])
def list_active_todos():
    """
    Return only todos with completed = = False
    """
    todos = service.get_active()
    return todos

# =========================
# update by id
# =========================
@router.put("/todos/{todo_id}/edit", response_model=TodoResponse)
def edit_todo(id: int, payload: TodoUpdateById):
    """
    Update name and task by id
    """
    try:
        todo = service.update_by_id(id, payload.name, payload.task)
        return todo
    except ValueError as e:
        raise HTTPException(status_code=404, detail="Todo not found!")
