from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
import uvicorn

from routers import students, users

app = FastAPI()


app.include_router(students.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7000)

@app.get('/proba')
def proba_list():
    return {'pr': [1, 2]}
