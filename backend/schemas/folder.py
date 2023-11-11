from pydantic import BaseModel
from typing import Optional

class FolderCreate(BaseModel):
    name: str
    descr: str
    parent_id: int


class FolderResponse(BaseModel):
    id: int
    name: str
    descr: str
    parent_id: int


class FolderUpdate(BaseModel):
    name: Optional[str] = None
    descr: Optional[str] = None
    parent_id: Optional[int] = None
