# pip3 install fastapi uvicorn
# pip3 install pydantic
# pip3 install sqlalchemy

from fastapi import FastAPI
from api.todo_router import router as todo_router
from api.user_router import router as user_router
from app.database import engine, Base
# register table here
from app.models import todo_model, user_model

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(todo_router)
app.include_router(user_router)

#run server =uvicorn main:app --reload