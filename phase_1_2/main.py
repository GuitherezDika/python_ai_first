from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, StrictBool

app = FastAPI(
    title="Todo API",
    description="Simple Todo API using FastAPI",
    version="1.0.0"
)

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

todos = []

# === TODO API SEDERHANA ===
# === GET ===
@app.get(
    "/todo-list", 
    summary="Get all todos", 
    description="This endpoint returns a list of all todos",
    response_model=list[TodoResponse],
    tags=["Todo"]
)
def get_todo_list():
    return todos

# === PATH PARAMETER GET BY ID ===
@app.get(
    "/todos/{todo_id}", 
    summary="Get Todo by ID",
    description="Todo detail data by ID",
    response_model=TodoResponse,
    tags=["Todo"]
)
def get_todo(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            return todo
    raise HTTPException(
        status_code=404, 
        detail="Todo not found"
    )
# http://127.0.0.1:8000/todos/3

# === SEARCH BY TITLE ===
@app.get(
    "/search-todo",
    summary="Search todo by keywords",
    description="Todos data will be retrieved by keywords",
    response_model=list[TodoResponse],
    tags=["Todo"]
)
def search_todo(keyword: str):
    # results = [ MODERN PYTHON
    #     todo
    #     for todo in todos
    #     if keyword.lower() in todo['title'].lower()
    # ]
    results = []
    for todo in todos:
        if keyword.lower() in todo['title'].lower():
            results.append(todo)
    return results
# http://127.0.0.1:8000/search-todo?keyword=m
# http://127.0.0.1:8000/search-todo?keyword=mama

# === POST ===
@app.post(
    "/add-todo", 
    summary="Add Todo",
    description="Add detail todo",
    status_code=status.HTTP_201_CREATED, 
    response_model=TodoResponse,
    tags=["Todo"]
)
def add_todo(todo: TodoCreate): # body - raw - json
    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title,
        "done": todo.done
    }
    todos.append(new_todo)
    return new_todo

# === PUT ===
# === PATH PARAMETER UPDATE BY ID ===
@app.put(
    "/todos/{todo_id}",
    summary="Update Todo by ID",
    description="Update detail todo by Id",
    response_model=TodoUpdateResponse,
    tags=["Todo"]
)
def update_todo(todo_id: int, updated_todo: TodoCreate):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['title'] = updated_todo.title
            todo['done'] = updated_todo.done
            return {"message": "Todo updated", "data": todo}
    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

# === DELETE ===
# === PATH PARAMETER DELETE BY ID ===
@app.delete(
    "/todos/{todo_id}",
    summary="Delete Todo Transaction",
    description="Delete Todo Transaction by Id",
    response_model=ShortResponse,
    tags=["Todo"]
)
def delete_todo(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )


# status status_code
# 200 = success
# 201 = created
# 400 = bad request
# 404 = not found
# 500 = internal server error

# 401 = unauthorized
# 403 = forbidden

# uvicorn main:app --reload
# http://127.0.0.1:8000/docs

# Sudah berhasil buat 1 Module = Module Todo
# next:
# tags=["Auth"]
# tags=["Users"]
# tags=["AI"]
# tags=["Admin"]
