from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import uvicorn
from urllib.parse import urlparse

from routers import students, users
from model import user
from api.ini_api import IAPI

app = FastAPI()


app.include_router(students.router)
app.include_router(users.router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7000)

@app.get('/proba')
def proba_list():
    return {'pr': [1, 2]}

@app.middleware("http")
async def modify_headers(request, call_next):

    uf = urlparse(str(request.url)).path.split('/')[-1]
    if (uf == ''):
        uf = urlparse(str(request.url)).path.split('/')[-2]
    if uf in ('login', 'proba'):
        return await call_next(request)

    if "HTTP_AUTHORIZATION" not in request.headers:
        return JSONResponse(status_code=401, content={'message': 'No authorization'})

    re = request.headers['HTTP_AUTHORIZATION']
    rw = re.split(' ')
    if rw[0] != 'Bearer':
        return JSONResponse(status_code=401, content={'message': 'No authorization'})

    us = user.User.check_session(rw[1])
    if us == None:
        return JSONResponse(status_code=401, content={'message': 'No session'})
    IAPI.US = us

    response = await call_next(request)

    return response