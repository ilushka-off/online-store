from enum import Enum


class ExtendedEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


class OrderStatusEnum(ExtendedEnum):
    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"
    TRANSIT = "TRANSIT"
    DELIVERED = "DELIVERED"
    CANCELED = "CANCELED"


class OrderPaymentMethodEnum(ExtendedEnum):
    UPON_RECEIPT = "UPON_RECEIPT"
    AFTER_FITTING = "AFTER_FITTING"
    IN_ADVANCE = "IN_ADVANCE"
    INSTALLMENTS = "INSTALLMENTS"
    UPON_DELIVERY = "UPON_DELIVERY"
    AFTER_VERIFICATION = "AFTER_VERIFICATION"
