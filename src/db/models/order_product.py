from db.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, PrimaryKeyConstraint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from db.models.order import Order
    from db.models.product import Product


class OrderProduct(BaseModel):
    order_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("orders.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )
    product_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("products.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )

    order: Mapped["Order"] = relationship("Order", back_populates="order_products")
    product: Mapped["Product"] = relationship(
        "Product", back_populates="order_products"
    )

    __table_args__ = (PrimaryKeyConstraint("order_id", "product_id"),)

    def __str__(self) -> str:
        return f"OrderProduct of Order {self.order_id} and Product {self.product_id}"
