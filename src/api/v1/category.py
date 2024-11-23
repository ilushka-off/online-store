from typing import Sequence
from fastapi import APIRouter, Depends, status
from services.category import CategoryService
from schemas.category import (
    CreateCategorySchema,
    GetCategorySchema,
    UpdateCategorySchema,
)
from db.models.category import Category
from db.filters.category import CategoryFilter
from fastapi_filter import FilterDepends

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    response_model=GetCategorySchema,
)
async def create_category(
    category_data: CreateCategorySchema,
    category_service: CategoryService = Depends(),
) -> Category:
    return await category_service.create_category(category_data=category_data)


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=list[GetCategorySchema],
)
async def get_categories(
    category_filters: CategoryFilter = FilterDepends(CategoryFilter),
    category_service: CategoryService = Depends(),
) -> Sequence[Category]:
    return await category_service.get_categories_by_filters(
        category_filters=category_filters
    )


@router.get(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetCategorySchema,
)
async def get_category_by_id(
    category_id: int,
    category_service: CategoryService = Depends(),
) -> Category:
    return await category_service.get_category_by_id(category_id=category_id)


@router.patch(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetCategorySchema,
)
async def update_category(
    category_id: int,
    category_data: UpdateCategorySchema,
    category_service: CategoryService = Depends(),
) -> Category:
    return await category_service.update_category(
        category_id=category_id, category_data=category_data
    )


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=GetCategorySchema,
)
async def delete_category(
    category_id: int,
    category_service: CategoryService = Depends(),
) -> Category:
    return await category_service.delete_category(category_id=category_id)
