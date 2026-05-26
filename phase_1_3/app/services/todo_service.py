from app.repositories.todo_repository import (get_all_todos, get_todo_by_id, search_todo, create_todo, update_todo, delete_todo)
from app.models.todo_model import (TodoCreate)
import app.database.fake_db as db

def get_todos_service():
    return get_all_todos()

def get_todo_service(todo_id: int):
    return get_todo_by_id(todo_id)

def search_todo_service(keyword: str):
    return search_todo(keyword)

def add_todo_service(title: str, done: bool):
    db.todo_id_counter += 1
    todo_data = {
        "id": db.todo_id_counter,
        "title": title,
        "done": done
    }
    return create_todo(todo_data)

def update_todo_service(todo_id: int, todo: TodoCreate):
    return update_todo(todo_id, todo)

def delete_todo_service(todo_id: int):
    todo = get_todo_by_id(todo_id)
    if not todo:
        return None
    delete_todo(todo)
    return True

