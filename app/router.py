from fastapi import APIRouter

from app.items.router import router as items_router

app_router = APIRouter()

app_router.include_router(items_router)
