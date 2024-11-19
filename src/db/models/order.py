from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin, UpdatedAtMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Numeric, Enum
from core.enums import OrderStatusEnum, OrderPaymentMethodEnum
from db.models.order_product import OrderProduct


class Order(BaseModel, IDMixin, CreatedAtMixin, UpdatedAtMixin):
    total_sum: Mapped[float] = mapped_column(
        Numeric(7, 2), nullable=False, unique=False
    )
    status: Mapped[OrderStatusEnum] = mapped_column(
        Enum(OrderStatusEnum), nullable=False, unique=False
    )
    payment_method: Mapped[OrderPaymentMethodEnum] = mapped_column(
        Enum(OrderPaymentMethodEnum), nullable=False, unique=False
    )
    check_serial: Mapped[str] = mapped_column(
        String(length=20), nullable=False, unique=True
    )

    order_products: Mapped[list["OrderProduct"]] = relationship(
        "OrderProduct",
        back_populates="order_product",
        foreign_keys="OrderProduct.order_id",
        cascade="all, delete-orphan",
    )

    def __str__(self) -> str:
        return f"Order by #{self.id}"
