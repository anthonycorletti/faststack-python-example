from typing import List

from fastapi import Request
from fastapi.responses import HTMLResponse

from app.database import db
from app.items.schemas import ItemCreate
from app.kit.views import views
from app.models import Item


class ItemsService:
    async def list_items(self) -> List[Item]:
        return list(map(lambda val: Item(**val), db.values()))

    async def create_item(self, item_create: ItemCreate) -> Item:
        data = Item(**item_create.model_dump())
        if data.name in db:
            db[data.name]["count"] += 1
        else:
            db[data.name] = data.model_dump()
        return data

    async def list_items_html(self, request: Request, data: List[Item]) -> HTMLResponse:
        return views.TemplateResponse(
            name="items/list.html",
            context={"request": request, "data": data},
        )
