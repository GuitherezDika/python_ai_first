from repository.todo_repository import TodoRepository
from typing import Optional

class TodoService:
  def __init__(self, repo: TodoRepository):
    self.repo = repo

  def create_todo(self, name, task, user_id: Optional[int] = None):
    return self.repo.create(name, task, user_id)

  def list_todos(self):
    return self.repo.get_all()

  def complete_todo(self, todo_id):
    todo = self.repo.get_by_id(todo_id)
    if not todo:
      raise ValueError("Todo not found")

    todo.completed = True
    return self.repo.update(todo)

  def delete_todo(self, todo_id):
    return self.repo.delete(todo_id)

  def get_completed(self):
    return self.repo.get_completed()

  def get_active(self):
    return self.repo.get_active()

  def update_by_id(self, todo_id: int, name: str, task: str):
    return self.repo.update_by_id(todo_id, name, task)