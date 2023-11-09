from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import JSONResponse
import uvicorn
from urllib.parse import urlparse


from routers import students, users, materials, folders, messages
from model import user
from api.ini_api import IAPI

from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(users.router)
app.include_router(folders.router)
app.include_router(materials.router)
app.include_router(messages.router)


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

    if uf not in ('login', 'proba'):

        if "Authorization" not in request.headers:
            return JSONResponse(status_code=401, content={'message': 'No authorization'})
        re = request.headers['Authorization']
        rw = re.split(' ')
        if rw[0] != 'Bearer':
            return JSONResponse(status_code=401, content={'message': 'No authorization'})

        us = user.User.check_session(rw[1])
        if us is None:
            return JSONResponse(status_code=401, content={'message': 'No session'})
        IAPI.US = us

    response = await call_next(request)
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE,OPTIONS'
    # response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8180", "http://185.221.152.242:8180"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)