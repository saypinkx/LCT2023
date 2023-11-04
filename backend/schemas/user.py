from pydantic import BaseModel
from pydantic import Json

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    params: str
    role: str
    comp_id: int
    class Config:
        orm_mode = True


