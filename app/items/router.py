from typing import List, Union

from fastapi import APIRouter, Body, Depends, Request
from fastui import FastUI

from app.const import Format
from app.items.schemas import ItemCreate
from app.items.service import ItemsService
from app.kit.router import respond_to
from app.models import Item

router = APIRouter(
    tags=["items"],
    prefix="/api/items",
)


@router.get(
    "/", response_model=Union[FastUI, List[Item]], response_model_exclude_none=True
)
async def list_items(
    request: Request,
    items_svc: ItemsService = Depends(ItemsService),
) -> Union[FastUI, List[Item]]:
    data = await items_svc.list_items()
    return await respond_to(
        request,
        {
            Format.json: (data),
            Format.html: (data, items_svc.render_ui_list),
        },
    )


@router.post("/", response_model=Union[FastUI, Item], response_model_exclude_none=True)
async def create_item(
    request: Request,
    item_create: ItemCreate = Body(
        ..., example=ItemCreate.Config.json_schema_extra["example"]
    ),
    items_svc: ItemsService = Depends(ItemsService),
) -> Union[FastUI, Item]:
    data = await items_svc.create_item(item_create=item_create)
    return data
