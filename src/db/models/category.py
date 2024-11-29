from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, Boolean
from db.models.product import Product


class Category(BaseModel, IDMixin, CreatedAtMixin):
    title: Mapped[str] = mapped_column(String(length=50), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

    products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="category",
        foreign_keys="Product.category_id",
        cascade="all, delete-orphan",
    )

    def __str__(self) -> str:
        return f"Category {self.title}"
