from model.user_profile import UserProfile
from fastapi import APIRouter, Body, Path, HTTPException, Query
from typing import Annotated
from model.up_trait import up_trait
from api.dblink import db_session
from model.trait import Trait

router = APIRouter(prefix='/api/profiles')


@router.get('/{user_id}')
def get_profile(user_id: Annotated[int, Path()]):
    profile_db = UserProfile.get_record_uid(user_id)
    if not profile_db:
        raise HTTPException(detail='Profile with user_id not found', status_code=404)
    return profile_db


@router.get('/')
def get_all_profiles():
    db_profiles = UserProfile.get_all_profiles_join_jobtitles()
    return db_profiles


@router.get('/{profile_id}/traits')
def get_traits(profile_id: Annotated[int, Path()]):
    user_profile_db = UserProfile.get_record_join_traits(profile_id)
    if not user_profile_db:
        raise HTTPException(detail='Profile with profile_id not found', status_code=404)
    traits_db = user_profile_db.traits
    return traits_db


@router.post('/{profile_id}/traits')
def add_trait(profile_id: Annotated[int, Path()], traits_id: Annotated[list[int], Body(title='traits_id')]):
    user_profile = UserProfile.get_record_upid(profile_id)
    if not user_profile:
        raise HTTPException(detail='Profile with profile id not found', status_code=404)
    for trait_id in traits_id:
        if not Trait.is_have(trait_id):
            raise HTTPException(detail='Trait with id not found', status_code=404)
    UserProfile.add_traits(user_profile, traits_id)
    return traits_id


@router.get('/position/{jt_id}')
def get_position(jt_id: Annotated[int, Path()]):
    records = UserProfile.get_static(jt_id)
    return records


@router.get('/likeness/{profile_id}')
def get_rating(profile_id: Annotated[int, Path()], jt_id: Annotated[int, Query()]):
    if not UserProfile.is_have(profile_id):
        raise HTTPException(detail='Profile with id not found', status_code=404)
    summa = UserProfile.get_rating(profile_id, jt_id)
    return summa


@router.get('/is_ideal/{profile_id}')
def get_is_ideal(profile_id: Annotated[int, Path()], jt_id: Annotated[int, Query()]):
    if not UserProfile.is_have(profile_id):
        raise HTTPException(status_code=404, detail='Profile with id not found')
    res = UserProfile.get_is_ideal(profile_id, jt_id)
    return res


@router.get('/plan/{profile_id}/{jt_id}')
def get_plan(profile_id: Annotated[int, Path()], jt_id: Annotated[int, Path()], limit: Annotated[int, Query()]):
    if not UserProfile.is_have(profile_id):
        raise HTTPException(status_code=404, detail='Profile with id not found')
    res = UserProfile.get_plan(profile_id, jt_id, limit)

    return res
