
from fastapi import APIRouter, Body, Path, HTTPException
from typing import Annotated
from schemas.user import UserCreate, UserLogin
from model.user import User

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
        raise HTTPException(status_code=403, detail='User with id not found')
    return user_db



@router.post('/login')
def login_user(user: Annotated[UserLogin, Body()]):
    pass


class UserLogin(ResFree):
    def post(self):
        jsonData = request.get_json()
        loginResult, logRole = user.User().doLogin(jsonData)
        if loginResult == 'invalid':
            return make_response(jsonify({"error": "true", "message": "Wrong credentials"}), 401)
        if loginResult == 'invalidFormat':
            return make_response(jsonify({"error": "true", "message": "Invalid user name or password entry format"}),
                                 401)

        return make_response(jsonify(access_token=loginResult, user_role=logRole), 200)


class UserLogout(Resource):
    def get(self):
        user.User().doUnLogin()
        return make_response(jsonify({"message": "Successful"}), 202)


class UserCurrent(Resource):
    def get(self):
        q = user.User().userCurrent()
        return make_response(jsonify(q), 201)


@router.put('/{user_id}', response_model=UserCreate)
def update_user(user_id: Annotated[int, Path()], new_user: Annotated[UserCreate, Body()]):
    user_db = User.get_record(user_id)
    if not user_db:
        raise HTTPException(status_code=403, detail='User with id not found')
    User.update_record(user_db, new_user)
    return user_db


@router.delete('/{user_id}')
def delete_user(user_id: Annotated[int, Path()]) -> str:
    user_db = User.get_record(user_id)
    if not user_db:
        raise HTTPException(detail='User with id not found', status_code=403)
    User.delete_record(user_db)
    return 'OK'

