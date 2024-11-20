from db.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer, PrimaryKeyConstraint


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

    __table_args__ = (PrimaryKeyConstraint("order_id", "product_id"),)

    def __str__(self) -> str:
        return f"OrderProduct of Order {self.order_id} and Product {self.product_id}"
