Mini Clean Architecture FastAPI

dengan:
Todo Module
+
Auth Module

============
Itu akan jadi foundation kuat sebelum:

PostgreSQL
SQLAlchemy
Redis
Docker
CI/CD
AI Gateway
Production Backend

=======
fastapi_clean/

phase_1_3/
├── .env
├── app/
│   ├── main.py           ← entry point
│   ├── core/config.py    ← baca .env
│   ├── middleware/logger.py
│   ├── database/fake_db.py
│   ├── models/
│   │   ├── todo_model.py
│   │   └── auth_model.py
│   ├── repositories/
│   │   ├── todo_repository.py
│   │   └── auth_repository.py
│   ├── services/
│   │   ├── todo_service.py
│   │   └── auth_service.py
│   └── routers/
│       ├── todo_router.py
│       └── auth_router.py
└── venv/

uvicorn app.main:app --reload
