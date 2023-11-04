from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

from routers import students

app = FastAPI()

app.include_router(students.router)

@app.get('/proba')
def proba_list():
    return { 'pr': [1,2]}

