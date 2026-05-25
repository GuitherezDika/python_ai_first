from domain.todo import Todo

class TodoRepository:
  def __init__(self):
    self.todos = []
    self._next_id = 1

  def add(self, name, task):
    todo = Todo(self._next_id, name, task)
    self.todos.append(todo)
    self._next_id += 1
    return todo

  def get_all(self):
    return self.todos

  def find_by_id(self, todo_id):
    for todo in self.todos:
      if todo.id == todo_id:
        return todo
    return None

  def delete(self, todo_id):
    for i,todo in enumerate(self.todos):
      if todo.id == todo_id:
        return self.todos.pop(i)
    return None