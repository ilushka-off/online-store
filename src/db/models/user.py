from datetime import date

from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date


class User(BaseModel, IDMixin, CreatedAtMixin):
    full_name: Mapped[str] = mapped_column(String(length=100), nullable=False)
    email: Mapped[str] = mapped_column(String(length=50), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(length=30), nullable=False)
    birthday: Mapped[date] = mapped_column(Date, nullable=False)

    def __str__(self) -> str:
        return f"User {self.full_name} with id #{self.id}"
