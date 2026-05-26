# repository = akses data
from app.database.fake_db import todos
from app.models.todo_model import (TodoCreate)


def get_all_todos():
    return todos

def get_todo_by_id(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    return None

def search_todo(keyword: str):
    results = []
    for todo in todos:
        if keyword.lower() in todo['title'].lower():
            results.append(todo)
    return results

def create_todo(todo_data: dict):
    todos.append(todo_data)
    return todo_data

def delete_todo(todo):
    todos.remove(todo)

def update_todo(todo_id: int, update_todo: TodoCreate):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['title'] = update_todo.title
            todo['done'] = update_todo.done
            return todo
        return None