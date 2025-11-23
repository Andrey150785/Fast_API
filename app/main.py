from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.routers import cart, categories, orders, products, users  # ← Новый импорт

# Создаём приложение FastAPI
app = FastAPI(
    title="FastAPI Интернет-магазин",
    version="0.1.0",
)

origins = [
    "http://localhost:3000",
    "https://example.com",
    "null"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем маршруты категорий и товаров
app.mount("/media", StaticFiles(directory="media"), name="media")

app.include_router(categories.router)
app.include_router(products.router)
app.include_router(users.router)
app.include_router(cart.router)
app.include_router(orders.router)  # ← Регистрация роутера заказов


# Корневой эндпоинт для проверки
@app.get("/")
async def root():
    """
    Корневой маршрут, подтверждающий, что API работает.
    """
    return {"message": "Добро пожаловать в API интернет-магазина!"}




