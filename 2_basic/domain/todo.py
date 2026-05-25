class Todo:
  def __init__(self, id, name, task, completed: bool = False):
    self.id = id
    self.name = name
    self.task = task
    self.completed = completed

  def mark_done(self):
    self.completed = True

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'task': self.task,
      'completed': self.completed
    }