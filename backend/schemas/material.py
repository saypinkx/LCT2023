from pydantic import BaseModel
from typing import Optional


class MaterialCreate(BaseModel):
    folder_id: int
    name: str
    link: str


class MaterialResponse(BaseModel):
    id: int
    folder_id: int
    name: str
    link: str


class MaterialUpdate(BaseModel):
    folder_id: Optional[int] = None
    name: Optional[str] = None
    link: Optional[str] = None

