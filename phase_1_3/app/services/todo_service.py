from app.repositories.todo_repository import get_all_todos, get_todo_by_id, create_todo, delete_todo

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

