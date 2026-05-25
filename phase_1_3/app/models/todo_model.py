from pydantic import BaseModel, Field, StrictBool

class TodoCreate(BaseModel):
    title: str = Field(min_length=1)
    done: StrictBool

class TodoResponse(BaseModel):
    id: int
    title: str
    done: bool

class TodoUpdateResponse(BaseModel):
    message: str
    data: TodoResponse

class ShortResponse(BaseModel):
    message: str