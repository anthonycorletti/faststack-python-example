from typing import Optional

from app.kit.db import RecordModel


class Item(RecordModel):
    name: str
    count: int = 1
    description: Optional[str] = None
