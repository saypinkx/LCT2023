from fastapi import APIRouter, Body, Path, HTTPException
from typing import Annotated, Union
from schemas.user import UserCreate, UserLogin
from model.user import User
from sqlalchemy import select
from api.dblink import db_session

router = APIRouter(prefix='/api/users')


@router.post('/', status_code=201, response_model=UserCreate)
def user_create(user: Annotated[UserCreate, Body()]):
    user_db = User(username=user.username, password=user.password, email=user.email, params=user.params, role=user.role)
    User.add_record(user_db)
    return user_db


@router.get('/{user_id}', response_model=None)
def get_user(user_id: Annotated[int, Path()]):
    user_db = User.get_record(user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail='User with id not found')
    return user_db


@router.post('/login')
def login_user(c_user: Annotated[UserLogin, Body()]):
    loginResult, logRole = User.do_login(c_user.username, c_user.password)
    if loginResult == 'invalid':
        raise HTTPException(status_code=401, detail='Wrong credentials')
    return {"access_token": loginResult,
            "user_role": logRole}


@router.get('/logout')
def logout_user():
    User.un_login()
    return {"message": "Successful"}


@router.get('/current')
def current_user():
    q = User.current_user()
    return q


@router.put('/{user_id}', response_model=UserCreate)
def update_user(user_id: Annotated[int, Path()], new_user: Annotated[UserCreate, Body()]):
    user_db = User.get_record(user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail='User with id not found')
    User.update_record(user_db, new_user)
    return user_db


@router.delete('/{user_id}')
def delete_user(user_id: Annotated[int, Path()]) -> str:
    user_db = User.get_record(user_id)
    if not user_db:
        raise HTTPException(detail='User with id not found', status_code=404)
    User.delete_record(user_db)
    return 'OK'


@router.get('/')
def get_all_users():
    users_db = User.get_all_records()
    return users_db
