from fastapi_filter.contrib.sqlalchemy import Filter
from pydantic import field_validator
from db.models.category import Category

from typing import Optional


class CategoryFilter(Filter):
    is_active: Optional[bool] = None
    title: Optional[str] = None
    title__ilike: Optional[str] = None
    description__ilike: Optional[str] = None

    order_by: list[str] | None = None

    @field_validator("order_by")
    def restrict_sortable_fields(cls, value):
        if value is None:
            return None

        allowed_field_names = ["title"]

        for field_name in value:
            field_name = field_name.replace("+", "").replace("-", "")
            if field_name not in allowed_field_names:
                raise ValueError(
                    f"You may only sort by: {', '.join(allowed_field_names)}"
                )

        return value

    class Constants(Filter.Constants):
        model = Category
