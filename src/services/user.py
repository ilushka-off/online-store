from typing import Sequence
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_session
from db.repositories.user import UserRepository
from schemas.user import CreateUserSchema, UpdateUserSchema
from core.exceptions import (
    user_not_found_exception,
    user_alredy_exists_exception,
)
from db.models.user import User
from db.filters.user import UserFilter


class UserService:
    def __init__(
        self,
        user_repository: UserRepository = Depends(),
        session: AsyncSession = Depends(get_session),
    ) -> None:
        self._user_repository = user_repository
        self._session = session

    async def create_user(self, user_data: CreateUserSchema) -> User:
        is_such_user = await self._user_repository.get_user_by_email_and_full_name(
            email=user_data.email, full_name=user_data.full_name
        )

        if is_such_user:
            raise user_alredy_exists_exception

        user = await self._user_repository.create_user(user_data=user_data)
        await self._session.commit()

        return user

    async def get_users_by_filters(self, user_filters: UserFilter) -> Sequence[User]:
        return await self._user_repository.get_users_by_filters(
            user_filters=user_filters
        )

    async def get_user_by_id(self, user_id: int) -> User:
        user = await self._user_repository.get_user_by_id(user_id=user_id)

        if not user:
            raise user_not_found_exception

        return user

    async def update_user(self, user_id: int, user_data: UpdateUserSchema) -> User:
        user = await self.get_user_by_id(user_id=user_id)

        if not user:
            raise user_not_found_exception

        await self._user_repository.update_user(instance=user, user_data=user_data)
        await self._session.commit()

        return user

    async def delete_user(self, user_id: int) -> User:
        user = await self._user_repository.get_user_by_id(user_id=user_id)

        if not user:
            raise user_not_found_exception

        await self._user_repository.delete_user(user_id=user_id)

        await self._session.commit()

        return user
