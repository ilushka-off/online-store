from db.models import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey, Numeric, Boolean, Text


class Product(BaseModel, IDMixin, CreatedAtMixin):
    сategory_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=False,
    )
    number: Mapped[str] = mapped_column(String(length=50), nullable=False)
    name: Mapped[str] = mapped_column(String(length=50), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    price: Mapped[float] = mapped_column(Numeric(7, 2), nullable=False)
    amount: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0, unique=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, unique=False, default=False
    )

    def __str__(self) -> str:
        return f"Product {self.name}"
