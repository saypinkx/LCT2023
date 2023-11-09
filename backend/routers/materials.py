from fastapi import APIRouter, Body, Path, HTTPException
from typing import Annotated
from schemas.material import MaterialCreate, MaterialResponse
from model.material import Material
from model.folder import Folder
from schemas.folder import FolderResponse
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from api.dblink import db_session

router = APIRouter(prefix='/api/materials')


@router.get('/{material_id}', response_model=MaterialResponse)
def get_material(material_id: Annotated[int, Path()]):
    material_db = Material.get_record(material_id)
    if not material_db:
        raise HTTPException(status_code=404, detail='material with id not found')
    return material_db


@router.post('/', response_model=MaterialCreate, status_code=201)
def create_material(material: Annotated[MaterialCreate, Body()]):
    folder = Folder.get_record(material.folder_id)
    if not folder:
        raise HTTPException(status_code=404, detail='folder with id not found')
    material_db = Material(name=material.name, folder=folder, link=material.link)
    Material.add_record(material_db)
    return material


@router.put('/{material_id}', response_model=MaterialCreate)
def update_material(material_id: Annotated[int, Path()], new_material: Annotated[MaterialCreate, Body()]):
    material_db = Material.get_record(material_id)
    if not material_db:
        raise HTTPException(status_code=404, detail='material with id not found')
    if new_material.folder_id != material_db.folder_id:
        folder_db = Folder.get_record(new_material.folder_id)
        if not folder_db:
            raise HTTPException(status_code=404, detail='folder with id not found')
        material_db.folder = folder_db
    Material.update_record(material_db, new_material)
    return new_material


@router.delete('/{material_id}')
def delete_material(material_id: Annotated[int, Path()]) -> str:
    material = Material.get_record(material_id)
    if not material:
        raise HTTPException(status_code=404, detail='material with id not found')
    Material.delete_record(material)
    return 'OK'


@router.get('/')
def get_all_materials():
    materials_db = Material.get_all_records()
    return materials_db


@router.get('/{material_id}/folder', response_model=FolderResponse)
def get_folder(material_id: Annotated[int, Path()]):
    material_db = Material.get_record_join_folder(material_id)
    if not material_db:
        raise HTTPException(status_code=404, detail='material with id not found')
    folder_db = material_db.folder
    return folder_db
