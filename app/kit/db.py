from datetime import datetime
from typing import Optional
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field


class TimestampsMixin(BaseModel):
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    deleted_at: Optional[datetime] = None


class UUIDMixin(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)


class RecordModel(TimestampsMixin, UUIDMixin):
    __abstract__ = True
