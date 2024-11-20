from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin, UpdatedAtMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Numeric, Enum
from core.enums import OrderStatusEnum, OrderPaymentMethodEnum


class Order(BaseModel, IDMixin, CreatedAtMixin, UpdatedAtMixin):
    total_sum: Mapped[float] = mapped_column(
        Numeric(precision=7, scale=2), nullable=False
    )
    status: Mapped[OrderStatusEnum] = mapped_column(
        Enum(OrderStatusEnum), nullable=False
    )
    payment_method: Mapped[OrderPaymentMethodEnum] = mapped_column(
        Enum(OrderPaymentMethodEnum), nullable=False
    )
    check_serial: Mapped[str] = mapped_column(
        String(length=20), nullable=False, unique=True
    )

    def __str__(self) -> str:
        return f"Order by #{self.id}"
