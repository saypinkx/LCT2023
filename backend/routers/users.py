
from fastapi import APIRouter, Body, Path
from typing import Annotated
from schemas.user import UserCreate, UserLogin
from model.user import User

router = APIRouter(prefix='/api/users')

@router.post('/', status_code=201, response_model=UserCreate)
def user_create(user: Annotated[UserCreate, Body()]):
    user_db = User(username=user.username, password=user.password, email=user.email, params=user.params, role=user.role)
    User.addToBase(user_db)
    return user_db


# @router.get('/{user_id}', response_model=None)
# def get_user(user_id: Annotated[int, Path()], db: Session = Depends(get_db)):
#     user_db = db.query(User).get(user_id)
#     if not user_db:
#         raise HTTPException(status_code=401, detail='User with id not found')
#     return user_db


#============================================================================

# @router.post('/login')
# def login_user(user: Annotated[UserLogin, Body()]):
#
#     pass
# class UserLogin(ResFree):
#     def post(self):
#         jsonData = request.get_json()
#         loginResult, logRole = user.User().doLogin(jsonData)
#         if loginResult == 'invalid':
#             return make_response(jsonify({"error":"true", "message":"Wrong credentials"}), 401)
#         if loginResult == 'invalidFormat':
#             return make_response(jsonify({"error":"true", "message":"Invalid user name or password entry format"}), 401)
#
#         return make_response(jsonify(access_token=loginResult, user_role=logRole), 200)
#
#
# class UserLogout(Resource):
#     def get(self):
#         user.User().doUnLogin()
#         return make_response(jsonify({"message":"Successful"}), 202)
#
#
# class UserCurrent(Resource):
#     def get(self):
#         q = user.User().userCurrent()
#         return make_response(jsonify(q), 201)

#
# @router.put('/{user_id}', response_model=UserCreate)
# def update_user(user_id: Annotated[int, Path()], new_user: Annotated[UserCreate, Body()], db: Session = db_session()):
#     user_db: User = db.query(User).get(user_id)
#     if not user_db:
#         raise HTTPException(status_code=401, detail='User with id not found')
#     new_user_dict = new_user.dict()
#     for key in new_user_dict:
#         if not new_user_dict[key]:
#             new_user_dict[key] = user_db.__dict__[key]
#     user_db.username, user_db.password, user_db.email, user_db.params, user_db.role, user_db.comp_id = new_user_dict[
#         'username'], new_user_dict[
#         'password'], new_user_dict['email'], new_user_dict['params'], new_user_dict['role'], new_user_dict['comp_id']
#     db.add(user_db)
#     db.commit()
#     return user_db
#
#
# @router.delete('/{user_id}', response_model=UserCreate)
# def delete_user(user_id: Annotated[int, Path()], db: Session = db_session()):
#     user_db = db.query(User).get(user_id)
#     if not user_db:
#         raise HTTPException(detail='User with id not found', status_code=401)
#     db.delete(user_db)
#     db.commit()
#     return user_db

