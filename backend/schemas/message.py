from pydantic import BaseModel
from datetime import datetime


class MessageCreate(BaseModel):
    from_id: int
    to_id: int
    after_id: None | int = None
    topic: str
    date: datetime = datetime.utcnow()
    body: str
    is_completed: int = 0
    is_read: int = 0


class MessageUpdate(BaseModel):
    topic: str | None = None
    body: str | None = None
    is_completed: int = 0
    is_read: int = 0
