from typing import List

from app.database import db
from app.items.schemas import ItemCreate
from app.kit.html import Element, Tag
from app.models import Item
from app.pages.items import ListItemsPage


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

    async def list_items_page(self, data: List[Item]) -> ListItemsPage:
        list_items_page = ListItemsPage()
        if len(data) == 0:
            list_items_page.doc.body.append(
                Element(
                    tag=Tag.p,
                    children=[
                        "There are no items.",
                    ],
                )
            )
        else:
            list_items_page.doc.body.append(
                Element(
                    tag=Tag.ul,
                    children=[
                        Element(
                            tag=Tag.li,
                            children=[
                                f"{item.name} - {item.count}"
                                f"{f' - {item.description}' or ''}",
                            ],
                        )
                        for item in data
                    ],
                )
            )
        return list_items_page
