from fastapi import Depends, FastAPI, Form, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware

from app.routers import categories, products


# Создаём приложение FastAPI
app = FastAPI(
    title="FastAPI CRUD",
    version="0.1.0",
)

# Настраиваем CORS для взаимодействия с фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем маршруты категорий и товаров
app.include_router(categories.router)
app.include_router(products.router)


