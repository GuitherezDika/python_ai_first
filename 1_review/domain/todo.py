class Todo:
  def __init__(self, id, name, task, is_done=False):
    self.id = id
    self.name = name
    self.task = task
    self.is_done = is_done

  def mark_done(self):
    self.is_done = True