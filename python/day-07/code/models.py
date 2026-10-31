from datetime import datetime, timezone
from uuid import uuid4

from pydantic import BaseModel, Field


class TaskInput(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(default="", max_length=500)


class TaskRecord(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    title: str
    description: str = ""
    completed: bool = False
    created_at: str = Field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
