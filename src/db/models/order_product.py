from db.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer
from db.models.product import Product
from db.models.order import Order


class OrderProduct(BaseModel):
    order_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(Order.id, ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )
    product_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey(Product.id, ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )

    def __str__(self) -> str:
        return f"OrderProduct of Order {self.order_id} and Product {self.product_id}"
