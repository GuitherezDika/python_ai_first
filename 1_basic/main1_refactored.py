# =====================
# DATA LAYER (STORAGE)
# =====================

class TodoRepository:
  def __init__(self):
    self.todos = []
    self._next_id=1

  def add(self, name, task):
    todo = {
      "id": self._next_id,
      'name': name,
      'task': task,
      'isDone': False
    }
    self.todos.append(todo)
    self._next_id += 1
    return todo

  def get_all(self):
    return self.todos

  def find_by_id(self, todo_id):
    for todo in self.todos:
      if todo['id'] == todo_id:
        return todo
    return None

  def delete(self, todo_id):
    for i, todo in enumerate(self.todos):
      if todo['id'] == todo_id:
        return self.todos.pop(i)
    return None

# =====================
# SERVICE LAYER
# =====================

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

    todo['isDone'] = True
    return todo

  def delete_todo(self, todo_id):
    deleted = self.repo.delete(todo_id)
    if not deleted: 
      raise ValueError("Todo not found")
    return deleted

# =====================
# CONTROLLER (SIMULASI API)
#======================
def print_todos(todos):
  print('\n === TODO LIST ===')
  for todo in todos:
    status = "✅" if todo["isDone"] else "❌"
    print(f"{todo['id']}. {todo['name']} - {todo['task']} [{status}]")
  print("=================\n")


