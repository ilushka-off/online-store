from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import field_validator
from db.models.user import User

from typing import Optional


class UserFilter(Filter):
    phone: Optional[str] = None
    phone__ilike: Optional[str] = None
    email: Optional[str] = None
    email__ilike: Optional[str] = None

    order_by: list[str] | None = None

    @field_validator("order_by")
    def restrict_sortable_fields(cls, value):
        if value is None:
            return None

        allowed_field_names = ["full_name", "created_at"]

        for field_name in value:
            field_name = field_name.replace("+", "").replace("-", "")
            if field_name not in allowed_field_names:
                raise ValueError(
                    f"You may only sort by: {', '.join(allowed_field_names)}"
                )

        return value

    class Constants(Filter.Constants):
        model = User
