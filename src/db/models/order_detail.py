from db.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, PrimaryKeyConstraint, UniqueConstraint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from db.models.address import Address
    from db.models.order import Order
    from db.models.user import User


class OrderDetail(BaseModel):
    address_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("addresses.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )
    order_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("orders.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        primary_key=True,
    )

    address: Mapped["Address"] = relationship("Address", back_populates="order_detail")
    user: Mapped["User"] = relationship("User", back_populates="order_detail")
    order: Mapped["Order"] = relationship("Order", back_populates="order_details")

    __table_args__ = (
        PrimaryKeyConstraint("order_id", "address_id", "user_id"),
        UniqueConstraint("address_id"),
        UniqueConstraint("user_id"),
    )

    def __str__(self) -> str:
        return f"OrderDetail of Order {self.order_id}, User {self.user_id} and Address {self.address_id}"
