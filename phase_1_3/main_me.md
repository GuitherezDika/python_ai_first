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

├── app/
│
│   ├── main.py
│
│   ├── routers/
│   │   ├── todo_router.py
│   │   └── auth_router.py
│
│   ├── services/
│   │   ├── todo_service.py
│   │   └── auth_service.py
│
│   ├── repositories/
│   │   ├── todo_repository.py
│   │   └── auth_repository.py
│
│   ├── models/
│   │   ├── todo_model.py
│   │   └── auth_model.py
│
│   ├── database/
│   │   └── fake_db.py
│
│   ├── middleware/
│   │   └── logger.py
│
│   └── core/
│       └── config.py
│
├── requirements.txt
└── .env