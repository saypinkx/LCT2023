from fastapi import APIRouter, Body, Path, HTTPException
from typing import Annotated
from schemas.folder import FolderCreate
from model.folder import Folder

router = APIRouter(prefix='/api/folders')


# @router.get('/{folder_id}', response_model=FolderCreate)
# def get_folder(folder_id: Annotated[int, Path()]):
#     folder_db = Folder.get_record(folder_id)
#     if not folder_db:
#         raise HTTPException(status_code=404, detail='folder with id not found')
#     return folder_db


@router.delete('/{folder_id}')
def delete_folder(folder_id: Annotated[int, Path()]) -> str:
    folder_db = Folder.get_record(folder_id)
    if not folder_db:
        raise HTTPException(status_code=404, detail='folder with id not found')
    return 'OK'


@router.post('/', response_model=FolderCreate)
def create_folder(folder: Annotated[FolderCreate, Body()]):
    parent = Folder.get_record(folder.parent_id)
    if not parent:
        raise HTTPException(status_code=404, detail='paren with id not found')
    folder_db = Folder(name=folder.name, descr=folder.descr, parent=parent)
    Folder.add_record(folder_db)
    return folder_db


@router.put('/{folder_id}', response_model=FolderCreate)
def update_folder(folder_id: Annotated[int, Path()], new_folder=Annotated[FolderCreate, Body()]):
    folder_db = Folder.get_record(folder_id)
    if not folder_db:
        raise HTTPException(status_code=404, detail='folder with id not found')
    new_folder.parent = Folder.get_record(new_folder.parent_id)
    if not new_folder.parent:
        raise HTTPException(status_code=404, detail='parent with  id not found')
    Folder.update_record(folder_db, new_folder)
    return new_folder


