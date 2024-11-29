from db.models.base import BaseModel
from db.models.mixins import IDMixin, CreatedAtMixin, UpdatedAtMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Numeric, Enum
from core.enums import OrderStatusEnum, OrderPaymentMethodEnum
from db.models.order_product import OrderProduct
from db.models.order_detail import OrderDetail


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

    order_products: Mapped[list["OrderProduct"]] = relationship(
        "OrderProduct", back_populates="order"
    )

    order_details: Mapped[list["OrderDetail"]] = relationship(
        "OrderDetail", back_populates="order", uselist=False
    )

    def __str__(self) -> str:
        return f"Order by #{self.id}"
