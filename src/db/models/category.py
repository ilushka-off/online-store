from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text


class Category(BaseModel, IDMixin, CreatedAtMixin):
    name: Mapped[str] = mapped_column(String(length=50), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)

    def __str__(self) -> str:
        return f"Category {self.name}"
