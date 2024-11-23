from schemas.base import BaseOrmSchema, CreatedAtMixin


class BaseCategorySchema(BaseOrmSchema):
    title: str
    description: str
    is_active: bool


class GetCategorySchema(BaseCategorySchema, CreatedAtMixin):
    id: int


class CreateCategorySchema(BaseCategorySchema): ...


class UpdateCategorySchema(BaseOrmSchema):
    title: str | None = None
    description: str | None = None
    is_active: bool | None = None
