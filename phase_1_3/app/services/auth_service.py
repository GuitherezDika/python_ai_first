from app.repositories.auth_repository import (
    create_user,
    find_user_by_email
)

def register_service(email: str, password: str):
    existing_user = find_user_by_email(email)
    if existing_user:
        return None

    user_data = {
        "id": 1,
        "email": email,
        "password": password
    }

    create_user(user_data)  
    return user_data

def login_service(email: str, password: str):
    user = find_user_by_email(email)
    if not user:
        return None
    
    if user['password'] != password:
        return None
        
