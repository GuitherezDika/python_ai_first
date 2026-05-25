from pydantic import BaseModel, ConfigDict
from typing import Optional

class TodoCreate(BaseModel):
  name: str
  task: str
  completed: bool = False
  user_id: Optional[int] = None

class TodoUpdateById(BaseModel):
  name: str
  task: str

class TodoResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)
  id: int
  name: str
  task: str
  completed: bool
  user_id: Optional[int] = None
