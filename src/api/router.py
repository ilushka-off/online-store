from fastapi import APIRouter

from api.v1.user import router as user_router
from api.v1.category import router as category_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(user_router)
v1_router.include_router(category_router)

api_router = APIRouter(prefix="/api")
api_router.include_router(v1_router)
