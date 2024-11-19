from db.models.base import BaseModel
from db.models.mixins import IDMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class Address(BaseModel, IDMixin):
    flat: Mapped[str] = mapped_column(String(length=50), nullable=True)
    house: Mapped[str] = mapped_column(String(length=50), nullable=False)
    street: Mapped[str] = mapped_column(String(length=50), nullable=False)
    city: Mapped[str] = mapped_column(String(length=50), nullable=False)
    country: Mapped[str] = mapped_column(String(length=50), nullable=False)
    index: Mapped[str] = mapped_column(String(length=50), nullable=True)

    def __str__(self) -> str:
        return f"Address #{self.id}"
