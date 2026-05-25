from app.models.todo_model import TodoModel
from app.database import SessionLocal

class TodoRepository:
  def create(self, name: str, task: str, user_id: int = None):
    db = SessionLocal()
    try:
      todo = TodoModel(name=name, task=task, user_id=user_id)
      db.add(todo)
      db.commit()
      db.refresh(todo)
      return todo
    finally:
      db.close()

  def get_all(self):
    db = SessionLocal()
    todos = db.query(TodoModel).all()
    db.close()
    return todos

  def get_by_id(self, todo_id: int):
    db = SessionLocal()
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    db.close()
    return todo

  def delete(self, todo_id: int):
    db = SessionLocal()
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()

    if not todo:
      db.close()
      return None

    db.delete(todo)
    db.commit()
    db.close()
    return todo

  def update(self, todo):
    db = SessionLocal()
    db.add(todo)
    db.commit()
    db.refresh(todo)
    db.close()
    return todo

  def update_by_id(self, todo_id: int, name: str = None, task: str = None):
    db = SessionLocal()
    try:
      todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
      if not todo:
        return None
      if name is not None:
        todo.name = name
      if task is not None:
        todo.task = task
      db.add(todo)
      db.commit()
      db.refresh(todo)
      return todo
    finally:
      db.close()

  def get_completed(self):
    db = SessionLocal()
    try:
      todos = db.query(TodoModel).filter(TodoModel.completed == True).all()
      return todos
    finally:
      db.close()

  def get_active(self):
    db= SessionLocal()
    try:
      todos = db.query(TodoModel).filter(TodoModel.completed == False).all()
      return todos
    finally: 
      db.close()