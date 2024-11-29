from datetime import date

from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Date
from db.models.order_detail import OrderDetail


class User(BaseModel, IDMixin, CreatedAtMixin):
    full_name: Mapped[str] = mapped_column(String(length=100), nullable=False)
    email: Mapped[str] = mapped_column(String(length=50), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(length=30), nullable=False)
    birthday: Mapped[date] = mapped_column(Date, nullable=False)

    order_detail: Mapped["OrderDetail"] = relationship(
        "OrderDetail", back_populates="user", uselist=False
    )

    def __str__(self) -> str:
        return f"User {self.full_name} with id #{self.id}"
