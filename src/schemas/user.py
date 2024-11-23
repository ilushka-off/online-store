from datetime import date
from schemas.base import BaseOrmSchema, CreatedAtMixin


class BaseUserSchema(BaseOrmSchema):
    full_name: str
    email: str
    birthday: date
    phone: str


class GetUserSchema(BaseUserSchema, CreatedAtMixin):
    id: int


class CreateUserSchema(BaseUserSchema): ...


class UpdateUserSchema(BaseOrmSchema):
    full_name: str | None = None
    email: str | None = None
    birthday: date | None = None
    phone: str | None = None
