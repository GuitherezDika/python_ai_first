from repository.todo_repository import TodoRepository

class TodoService:
  def __init__(self, repo: TodoRepository):
    self.repo = repo

  def create_todo(self, name, task):
    return self.repo.add(name, task)

  def list_todos(self):
    return self.repo.get_all()

  def complete_todo(self, todo_id):
    todo = self.repo.find_by_id(todo_id)
    if not todo:
      raise ValueError("Todo not found")

    todo.mark_done()
    return todo

  def delete_todo(self, todo_id):
    deleted = self.repo.delete(todo_id)
    if not deleted:
      raise ValueError("Todo not found")
    return deleted