from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from sqlalchemy import select, update

from app.auth import get_current_seller
from app.models.products import Product as ProductModel
from app.models.categories import Category as CategoryModel
from app.models.reviews import Review
from app.schemas import Product as ProductSchema, ProductCreate, ReviewSchema
from app.models.users import User as UserModel
from app.db_depends import get_db, get_async_db

# Создаём маршрутизатор для товаров
router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],
)


@router.get("/", response_model=list[ReviewSchema])
async def get_all_products(db: AsyncSession = Depends(get_async_db)):
    """
    Возвращает список всех активных товаров.
    """
    result = await db.scalars(select(Review).where(Review.is_active == True))
    return result.all()