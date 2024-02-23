from typing import List

from fastui import components as c
from fastui.components import AnyComponent

from app.database import db
from app.items.schemas import ItemCreate
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

    async def render_ui_list(self, data: List[Item]) -> List[AnyComponent]:
        return [
            c.Page(
                components=[
                    c.Table(
                        data=data,
                        data_model=Item,
                        no_data_message="No items found.",
                    )
                ]
            ),
        ]
