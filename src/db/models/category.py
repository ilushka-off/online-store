from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text
from db.models.product import Product


class Category(BaseModel, IDMixin, CreatedAtMixin):
    name: Mapped[str] = mapped_column(String(length=50), nullable=False, unique=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, unique=False)

    products: Mapped[list["Product"]] = relationship(
        back_populates="category",
        foreign_keys="Product.category_id",
        cascade="all, delete-orphan",
    )

    def __str__(self) -> str:
        return f"Category {self.name} with id #{self.id}"
