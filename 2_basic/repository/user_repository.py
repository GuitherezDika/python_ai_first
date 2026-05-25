from app.models.user_model import UserModel
from app.database import SessionLocal

class UserRepository:
  def create(self, name: str):
    db = SessionLocal()
    try:
      user = UserModel(name=name)
      db.add(user)
      db.commit()
      db.refresh(user)
      return user
    finally:
      db.close()

  def get_all(self):
    db = SessionLocal()
    try:
      users = db.query(UserModel).all()
      return users
    finally: 
      db.close()