from db.repositories.base import BaseDatabaseRepository
from schemas.user import CreateUserSchema, UpdateUserSchema
from db.models.user import User
from sqlalchemy import select, delete, and_
from db.filters.user import UserFilter

from collections.abc import Sequence


class UserRepository(BaseDatabaseRepository):
    async def create_user(self, user_data: CreateUserSchema) -> User:
        user = User(**user_data.model_dump(exclude_unset=True))
        self._session.add(user)
        await self._session.flush()

        return user

    async def get_users_by_filters(self, user_filters: UserFilter) -> Sequence[User]:
        query = user_filters.sort(user_filters.filter(select(User)))
        query_result = await self._session.execute(query)

        return query_result.scalars().all()

    async def get_user_by_email_and_full_name(
        self, email: str, full_name: str
    ) -> Sequence[User]:
        query = select(User).where(
            and_(User.email == email, User.full_name == full_name)
        )
        query_result = await self._session.execute(query)

        return query_result.scalars().all()

    async def get_user_by_id(self, user_id: int) -> User | None:
        return await self._session.get(User, user_id)

    async def update_user(self, instance: User, user_data: UpdateUserSchema) -> None:
        for key, value in user_data.model_dump(exclude_unset=True).items():
            setattr(instance, key, value)
        await self._session.flush()

    async def delete_user(self, user_id: int) -> None:
        query = delete(User).where(User.id == user_id)
        await self._session.execute(query)
