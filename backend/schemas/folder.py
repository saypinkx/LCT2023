from pydantic import BaseModel


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
    name: str | None = None
    descr: str | None = None
    parent_id: int | None = None
