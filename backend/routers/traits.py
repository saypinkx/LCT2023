from model.user_profile import UserProfile
from fastapi import APIRouter, Body, Path, HTTPException
from typing import Annotated
from model.trait import Trait

router = APIRouter(prefix='/api/traits')


@router.get('/')
def get_type_traits():
    traits_db = Trait.get_type_record()
    return traits_db



