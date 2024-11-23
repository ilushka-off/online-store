from typing import Sequence
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_session
from db.repositories.category import CategoryRepository
from schemas.category import CreateCategorySchema, UpdateCategorySchema
from core.exceptions import (
    category_not_found_exception,
    category_alredy_exists_exception,
)
from db.models.category import Category
from db.filters.category import CategoryFilter


class CategoryService:
    def __init__(
        self,
        category_repository: CategoryRepository = Depends(),
        session: AsyncSession = Depends(get_session),
    ) -> None:
        self._category_repository = category_repository
        self._session = session

    async def create_category(self, category_data: CreateCategorySchema) -> Category:
        is_such_category = await self._category_repository.get_category_by_title(
            title=category_data.title
        )

        if is_such_category:
            raise category_alredy_exists_exception
        category = await self._category_repository.create_category(
            category_data=category_data
        )
        await self._session.commit()

        return category

    async def get_categories_by_filters(
        self, category_filters: CategoryFilter
    ) -> Sequence[Category]:
        return await self._category_repository.get_category_by_filters(
            category_filters=category_filters
        )

    async def get_category_by_id(self, category_id: int) -> Category:
        category = await self._category_repository.get_category_by_id(
            category_id=category_id
        )

        if not category:
            raise category_not_found_exception

        return category

    async def update_category(
        self, category_id: int, category_data: UpdateCategorySchema
    ) -> Category:
        category = await self.get_category_by_id(category_id=category_id)

        if not category:
            raise category_not_found_exception

        await self._category_repository.update_category(
            instance=category, category_data=category_data
        )
        await self._session.commit()

        return category

    async def delete_category(self, category_id: int) -> Category:
        category = await self._category_repository.get_category_by_id(
            category_id=category_id
        )

        if not category:
            raise category_not_found_exception

        await self._category_repository.delete_category(category_id=category_id)

        await self._session.commit()

        return category
