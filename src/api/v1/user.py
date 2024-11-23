from typing import Sequence
from fastapi import APIRouter, Depends, status
from services.user import UserService
from schemas.user import CreateUserSchema, GetUserSchema, UpdateUserSchema
from db.models.user import User
from db.filters.user import UserFilter
from fastapi_filter import FilterDepends

router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=GetUserSchema,
)
async def create_user(
    user_data: CreateUserSchema,
    user_service: UserService = Depends(),
) -> User:
    return await user_service.create_user(user_data=user_data)


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=list[GetUserSchema],
)
async def get_users_by_filters(
    user_filters: UserFilter = FilterDepends(UserFilter),
    user_service: UserService = Depends(),
) -> Sequence[User]:
    return await user_service.get_users_by_filters(user_filters=user_filters)


@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetUserSchema,
)
async def get_user_by_id(
    user_id: int,
    user_service: UserService = Depends(),
) -> User:
    return await user_service.get_user_by_id(user_id=user_id)


@router.patch(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetUserSchema,
)
async def update_user(
    user_id: int,
    user_data: UpdateUserSchema,
    user_service: UserService = Depends(),
) -> User:
    return await user_service.update_user(user_id=user_id, user_data=user_data)


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetUserSchema,
)
async def delete_user(
    user_id: int,
    user_service: UserService = Depends(),
) -> User:
    return await user_service.delete_user(user_id=user_id)
