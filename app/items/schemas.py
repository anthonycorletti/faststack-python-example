from typing import Optional

from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    count: Optional[int] = 1
    description: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "tequila",
                "count": 1,
                "description": "casa dragones",
            }
        }


class ItemUpdate(ItemCreate):
    pass
