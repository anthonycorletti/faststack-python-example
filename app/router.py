from fastapi import APIRouter

from app.items.router import router as items_router

router = APIRouter()

router.include_router(items_router)
