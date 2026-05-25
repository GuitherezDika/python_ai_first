# repository = akses data
from app.database.fake_db import todos

det get_all_todos():
    return todos

def get_todo_by_id(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    return None

def create_todo(todo_data: dict):
    todos.append(todo_data)
    return todo_data

def delete_todo(todo):
    todos.remove(todo)