from typing import List, Union

from fastapi import APIRouter, Body, Depends, Request
from fastapi.responses import HTMLResponse

from app.const import ResponseFormat
from app.items.schemas import ItemCreate
from app.items.service import ItemsService
from app.kit.router import respond_to
from app.models import Item

router = APIRouter(tags=["items"])


class Paths:
    list_items = "/items"
    create_item = "/items"


@router.get(
    Paths.list_items,
    response_model=List[Item],
)
async def list_items(
    request: Request,
    items_svc: ItemsService = Depends(ItemsService),
) -> Union[HTMLResponse, List[Item]]:
    data = await items_svc.list_items()
    return await respond_to(
        request,
        {
            ResponseFormat.json: {"data": data},
            ResponseFormat.html: {"data": data, "via": items_svc.list_items_html},
        },
    )


@router.post(
    Paths.create_item,
    response_model=Item,
)
async def create_item(
    request: Request,
    item_create: ItemCreate = Body(
        ...,
        example=ItemCreate.Config.json_schema_extra["example"],
    ),
    items_svc: ItemsService = Depends(ItemsService),
) -> Union[HTMLResponse, Item]:
    data = await items_svc.create_item(item_create=item_create)
    return data
