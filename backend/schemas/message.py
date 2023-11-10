from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MessageCreate(BaseModel):
    from_id: int
    to_id: int
    after_id: Optional[int] = None
    topic: str
    date: datetime = datetime.utcnow()
    body: str
    is_completed: int = 0
    is_read: int = 0


class MessageUpdate(BaseModel):
    topic: Optional[str] = None
    body: Optional[str] = None
    is_completed: int = 0
    is_read: int = 0
