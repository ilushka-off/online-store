from schemas.base import BaseOrmSchema


class BaseUserSchema(BaseOrmSchema):
    house: str
    street: str
    city: str
    country: str
    index: str


class GetUserSchema(BaseUserSchema):
    id: int


class CreateUserSchema(BaseUserSchema): ...


class UpdateUserSChema(BaseOrmSchema):
    house: str | None = None
    street: str | None = None
    city: str | None = None
    country: str | None = None
    index: str | None = None
