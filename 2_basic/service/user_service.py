from repository.user_repository import UserRepository
from typing import List

class UserService:
  def __init__(self):
    self.repo = UserRepository()

  def create_user(self, name: str):
    return self.repo.create(name)

  def list_users(self):
    return self.repo.get_all()