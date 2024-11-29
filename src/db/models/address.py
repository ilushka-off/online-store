from db.models.base import BaseModel
from db.models.mixins import IDMixin
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from db.models.order_detail import OrderDetail


class Address(BaseModel, IDMixin):
    house: Mapped[str] = mapped_column(String(length=50), nullable=False)
    street: Mapped[str] = mapped_column(String(length=50), nullable=False)
    city: Mapped[str] = mapped_column(String(length=50), nullable=False)
    country: Mapped[str] = mapped_column(String(length=50), nullable=False)
    index: Mapped[str] = mapped_column(String(length=50), nullable=True)

    order_detail: Mapped["OrderDetail"] = relationship(
        "OrderDetail",
        back_populates="address",
        uselist=False,
    )

    def __str__(self) -> str:
        return f"Address #{self.id}"
