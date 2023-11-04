from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

from routers import students, users

app = FastAPI()

app.include_router(students.router)
app.include_router(users.router)


@app.get('/proba')
def proba_list():
    return {'pr': [1, 2]}
