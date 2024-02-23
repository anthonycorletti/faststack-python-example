from typing import Optional

from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "drink",
                "description": "tequila",
            }
        }
