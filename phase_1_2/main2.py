from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "World FastAPI!"}

@app.get("/users")
def get_users():
    return ['Dika', 'Budi']

# === QUERY PARAM ===
@app.get("/todos")
def get_todos(limit: int = 10):
    return {"limit": limit}
# http://127.0.0.1:8000/todos?limit=6

# === MULTIPLE QUERY PARAM ===
@app.get("/search")
def search_todo(
    keyword: str,
    page: int = 1,
):
    return {
        "keyword": keyword,
        "page": page
    }
# http://127.0.0.1:8000/search?keyword=songs&page=2

# === POST & REQUEST BODY ===
@app.post("/todos")
def create_todo(todo: dict): # artinya raw = json
    print(todo)
    return {
        "message": "Todo created",
        "todo": todo
    }
# http://127.0.0.1:8000/todos
# body - raw - json
# {
#     "name": "dika",
#     "role": "engineer",
#     "age": 37
# }

# === PYDANTIC MODELS ===
# validasi, type checking, dokumentasi otomatis
from pydantic import BaseModel
todos = []
class Todo(BaseModel):
    title: str
    done: bool

@app.post("/todos-model")
def create_todo(todo: Todo):
    print(todo)
    return {
        "message": "Todo created",
        "todo": todo
    }

# === TODO API SEDERHANA ===
class TodoResponse(BaseModel):
    id: int
    title: str
    done: bool

@app.get(
    "/todo-list", 
    summary="Get all todos", 
    description="This endpoint returns a list of all todos"
)
def get_todo_list():
    return todos

@app.post(
    "/add-todo", 
    status_code=status.HTTP_201_CREATED, 
    response_model=TodoResponse
)
def add_todo(todo: Todo): # body - raw - json
    if todo.title == "":
        raise HTTPException(
            status_code=400, # BAD REQUEST
            detail="Title cannot be empty"
        )
    
    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title,
        "done": todo.done
    }
    todos.append(new_todo)
    return new_todo

# === PATH PARAMETER GET BY ID ===
@app.get(
    "/todos/{todo_id}", 
    response_model=TodoResponse
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

# === PATH PARAMETER DELETE BY ID ===
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo['id'] == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted", "todo": todo}
    return {"message": "Todo not found"}

# === PATH PARAMETER UPDATE BY ID ===
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['title'] = updated_todo.title
            todo['done'] = updated_todo.done
            return {"message": "Todo updated", "todo": todo}
    return {"message": "Todo not found"}

# === SEARCH BY TITLE ===
@app.get("/search-todo")
def search_todo(keyword: str):
    print(keyword)
    results = []
    for todo in todos:
        if keyword.lower() in todo['title'].lower():
            results.append(todo)
    return {"results": results}
# http://127.0.0.1:8000/search-todo?keyword=m
# http://127.0.0.1:8000/search-todo?keyword=mama

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

