from app.database.fake_db import users

def create_user(user_data: dict):
    users.append(user_data)
    return user_data

def find_user_by_email(email: str):
    for user in users:
        if user['email'] == email:
            return user
    return None
