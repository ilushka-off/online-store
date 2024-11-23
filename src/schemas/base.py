from datetime import datetime

from pydantic import ConfigDict, BaseModel, field_validator

from core.constants import moscow_timezone


class BaseOrmSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class CreatedAtMixin(BaseModel):
    created_at: datetime

    @field_validator("created_at")
    def created_at_to_moscow_tz(cls, v):
        return v.astimezone(moscow_timezone)


class UpdatedAtMixin(BaseModel):
    updated_at: datetime

    @field_validator("updated_at")
    def updated_at_to_moscow_tz(cls, v):
        return v.astimezone(moscow_timezone)
