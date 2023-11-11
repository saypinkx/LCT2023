from fastapi import APIRouter, Body, Path, HTTPException
from typing import Annotated
from schemas.material import MaterialCreate, MaterialResponse
from model.material import Material
from model.folder import Folder
from schemas.folder import FolderResponse
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from api.dblink import db_session
from model.user import User
from model.message import Message
from schemas.message import MessageCreate, MessageUpdate

router = APIRouter(prefix='/api/messages')


@router.post('/', status_code=201)
def create_message(message: Annotated[MessageCreate, Body()]):
    if not User.is_have(message.from_id):
        raise HTTPException(status_code=404, detail='User sender not found')
    if not User.is_have(message.to_id):
        raise HTTPException(status_code=404, detail='User recipient not found')
    if message.after_id:
        if not Message.is_have(message.after_id):
            raise HTTPException(status_code=404, detail='Message with after_id not found')
    message_db = Message(from_id=message.from_id, after_id=message.after_id, to_id=message.to_id, date=message.date,
                         topic=message.topic, body=message.body, is_completed=message.is_completed,
                         is_read=message.is_read)
    Message.add_record(message_db)
    return message


@router.put('/{message_id}')
def update_message(message_id: Annotated[int, Path()], new_message: Annotated[MessageUpdate, Body()]):
    message_db = Message.get_record(message_id)
    if not message_db:
        raise HTTPException(status_code=404, detail='Message with id not found')
    Message.update_record(message_db, new_message)
    return new_message


@router.delete('/{message_id}')
def delete_message(message_id: Annotated[int, Path()]):
    message_db = Message.get_record(message_id)
    if not message_db:
        raise HTTPException(status_code=404, detail='Message with id not found')
    Message.delete_record(message_db)
    return 'OK'


@router.get('/{message_id}')
def get_message(message_id: Annotated[int, Path()]):
    message_db = Message.get_record(message_id)
    if not message_db:
        raise HTTPException(status_code=404, detail='Message with id not found')
    return message_db

@router.get('/incoming/{user_id}')
def get_incoming_messages(user_id: Annotated[int, Path()]):
    if not User.is_have(user_id):
        raise HTTPException(status_code=404, detail='User with id not found')
    messages_db = Message.get_incoming_messages(user_id)
    return messages_db


@router.get('/sent/{user_id}')
def get_sent_messages(user_id: Annotated[int, Path()]):
    if not User.is_have(user_id):
        raise HTTPException(status_code=404, detail='User with id not found')
    messages_db = Message.get_sent_messages(user_id)
    return messages_db
@router.get('/{user1_id}/{user2_id}')
def get_dialog(user1_id: Annotated[int, Path()], user2_id: Annotated[int, Path()]):
    if not User.is_have(user1_id):
        raise HTTPException(status_code=404, detail='User with user1_id not found')
    if not User.is_have(user2_id):
        raise HTTPException(status_code=404, detail='User with user2_id not found')
    dialog_db = Message.get_dialog(user1_id, user2_id)
    return dialog_db



