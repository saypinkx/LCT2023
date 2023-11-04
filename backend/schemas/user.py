from pydantic import BaseModel
from pydantic import Json

class UserCreate(BaseModel):
    username: str
    password: str
    email: str
    params: str
    role: str


class UserLogin(BaseModel):
    username: str
    password: str
