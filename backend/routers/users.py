from fastapi import APIRouter, Body, Path, HTTPException, Depends
from typing import Annotated, Union
from schemas.user import UserCreate
from model.user import User
from sqlalchemy import select
from api.dblink import db_session

router = APIRouter(prefix='/api/v1/users')


@router.post('/create', status_code=201, response_model=UserCreate)
def user_create(user: Annotated[UserCreate, Body()], db=db_session()):
    user_db = User(username=user.username, password=user.password, email=user.email, params=user.params, role=user.role,
                   comp_id=user.comp_id)
    db.add(user_db)
    db.commit()
    return user_db


@router.get('/{user_id}', response_model=UserCreate)
def get_user(user_id: Annotated[int, Path()], db=db_session()):
    user_db = db.query(User).get(user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail='User with id not found')
    return user_db


@router.put('/{user_id}', response_model=UserCreate)
def update_user(user_id: Annotated[int, Path()], new_user: Annotated[UserCreate, Body()], db=db_session()):
    user_db: User = db.query(User).get(user_id)
    if not user_db:
        raise HTTPException(status_code=404, detail='User with id not found')
    new_user_dict = new_user.dict()
    for key in new_user_dict:
        if not new_user_dict[key]:
            new_user_dict[key] = user_db.__dict__[key]
    user_db.username, user_db.password, user_db.email, user_db.params, user_db.role, user_db.comp_id = new_user_dict[
        'username'], new_user_dict[
        'password'], new_user_dict['email'], new_user_dict['params'], new_user_dict['role'], new_user_dict['comp_id']
    db.add(user_db)
    db.commit()
    return user_db


@router.delete('/{user_id}', response_model=UserCreate)
def delete_user(user_id: Annotated[int, Path()], db=db_session()):
    user_db = db.query(User).get(user_id)
    if not user_db:
        raise HTTPException(detail='User with id not found', status_code=404)
    db.delete(user_db)
    db.commit()
    return user_db
