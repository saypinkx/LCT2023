from pydantic import BaseModel


class MaterialCreate(BaseModel):
    folder_id: int
    name: str
    link: str

class MaterialResponse(BaseModel):
    id: int
    folder_id: int
    name: str
    link: str