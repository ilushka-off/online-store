from db.repositories.base import BaseDatabaseRepository
from schemas.category import CreateCategorySchema, UpdateCategorySchema
from db.models.category import Category
from sqlalchemy import select, delete
from db.filters.category import CategoryFilter

from collections.abc import Sequence


class CategoryRepository(BaseDatabaseRepository):
    async def create_category(self, category_data: CreateCategorySchema) -> Category:
        category = Category(**category_data.model_dump())
        self._session.add(category)
        await self._session.flush()

        return category

    async def get_category_by_filters(
        self, category_filters: CategoryFilter
    ) -> Sequence[Category]:
        query = category_filters.sort(category_filters.filter(select(Category)))
        query_result = await self._session.execute(query)
        return query_result.scalars().all()

    async def get_category_by_title(self, title: str) -> Sequence[Category]:
        query = select(Category).where(Category.title == title)
        query_result = await self._session.execute(query)

        return query_result.scalars().all()

    async def get_category_by_id(self, category_id: int) -> Category | None:
        return await self._session.get(Category, category_id)

    async def update_category(
        self, instance: Category, category_data: UpdateCategorySchema
    ) -> None:
        for key, value in category_data.model_dump(exclude_unset=True).items():
            setattr(instance, key, value)
        await self._session.flush()

    async def delete_category(self, category_id: int) -> None:
        query = delete(Category).where(Category.id == category_id)
        await self._session.execute(query)
