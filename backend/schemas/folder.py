from pydantic import BaseModel


class FolderCreate:
    name: str
    descr: str
    parent_id: int

    class Config:
        orm_mode = True
