from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text, Boolean


class Category(BaseModel, IDMixin, CreatedAtMixin):
    title: Mapped[str] = mapped_column(String(length=50), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    def __str__(self) -> str:
        return f"Category {self.title}"
