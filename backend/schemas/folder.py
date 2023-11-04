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
