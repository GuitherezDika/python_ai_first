from fastapi import APIRouter, HTTPException, status
from app.models.todo_model import (TodoCreate, TodoResponse, TodoUpdateResponse, ShortResponse)
from app.services.todo_service import (
    get_todos_service,
    get_todo_service,
    search_todo_service,
    add_todo_service,
    update_todo_service,
    delete_todo_service
)

router = APIRouter(
    prefix="/todos",
    tags=["Todo"]
)

@router.get("/", response_model=list[TodoResponse])
def get_todos():
    return get_todos_service()

@router.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    todo = get_todo_service(todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.get("/search-todo", response_model=list[TodoResponse])
def search_todo(keyword: str):
    todo_reponse = search_todo_service(keyword)
    if not todo_reponse:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo_reponse

@router.post("/add-todo", status_code=status.HTTP_201_CREATED, response_model=TodoResponse)
def add_todo(todo: TodoCreate):
    return add_todo_service(title= todo.title, done= todo.done)

@router.put("/update-todo", response_model=TodoUpdateResponse)
def update_todo(todo_id: int, todo: TodoCreate):
    updated = update_todo_service(todo_id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {
        "message": "Todo updated successfully",
        "todo": updated,
    }

@router.delete("/todos/{todo_id}", response_model=ShortResponse)
def delete_todo(todo_id: int):
    deleted = delete_todo_service(todo_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {
        "message": "Todo deleted successfully"
    }