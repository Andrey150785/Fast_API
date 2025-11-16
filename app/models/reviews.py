from datetime import datetime

from sqlalchemy import Boolean, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
from app.models import User, Product


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(ForeignKey("users.id"), nullable=False)
    product_id = mapped_column(ForeignKey("products.id"), nullable=False)
    comment: Mapped[str | None] = mapped_column(String(500), nullable=True)
    comment_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    grade: Mapped[int] = mapped_column(Integer, ge=1, le=5, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    user = relationship("User", back_populates="reviews")
    product = relationship("Product", back_populates="reviews")

    def __repr__(self):
        return f"Review(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, comment={self.comment}, comment_date={self.comment_date}, grade={self.grade}, is_active={self.is_active})"

    def __str__(self):
        return f"Review(id={self.id}, user_id={self.user_id}, product_id={self.product_id}, comment={self.comment}, comment_date={self.comment_date}, grade={self.grade}, is_active={self.is_active})"
