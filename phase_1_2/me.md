6. Latihan Mini Project (Sangat Disarankan)

Coba upgrade Todo API kamu:

Harus ada:
GET
get all
get by id
POST
add todo
PUT
update todo
DELETE
delete todo
Dan tambahkan:

✅ HTTPException
✅ status code
✅ response_model
✅ validation
✅ swagger metadata

contoh
===========
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(
    title="Todo API",
    version="1.0.0"
)

todos = []

class Todo(BaseModel):
    id: int
    title: str
    done: bool

@app.post(
    "/todos",
    status_code=status.HTTP_201_CREATED,
    response_model=Todo
)
def create_todo(todo: Todo):

    todos.append(todo)

    return todo

@app.get(
    "/todos/{todo_id}",
    response_model=Todo
)
def get_todo(todo_id: int):

    for todo in todos:
        if todo.id == todo_id:
            return todo

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )