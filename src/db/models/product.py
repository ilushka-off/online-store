from db.models import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Numeric, Boolean, Text
from db.models.category import Category
from db.models.order_product import OrderProduct


class Product(BaseModel, IDMixin, CreatedAtMixin):
    сategory_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("categories.id", ondelete="CASCADE"),
        nullable=False,
        unique=False,
    )
    number: Mapped[str] = mapped_column(String(length=50), nullable=False, unique=False)
    name: Mapped[str] = mapped_column(String(length=50), nullable=False, unique=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, unique=False)
    price: Mapped[float] = mapped_column(Numeric(7, 2), nullable=False, unique=False)
    amount: Mapped[int] = mapped_column(
        Integer, nullable=False, default=0, unique=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, unique=False, default=False
    )

    categories: Mapped[list["Category"]] = relationship(
        "Category",
        back_populates="categories",
        foreign_keys="Product.category_id",
        lazy="selectin",
    )

    order_products: Mapped[list["OrderProduct"]] = relationship(
        "OrderProduct",
        back_populates="order_product",
        foreign_keys="OrderProduct.product_id",
        cascade="all, delete-orphan",
    )

    def __str__(self) -> str:
        return f"Product {self.name} with id #{self.id}"
