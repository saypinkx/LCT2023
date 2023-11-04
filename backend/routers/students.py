from fastapi import HTTPException
from pydantic import BaseModel
from fastapi import APIRouter

from api.dblink import Mydb

router = APIRouter()

students = [
    {'name': 'Student 1', 'age': 20},
    {'name': 'Student 2', 'age': 18},
    {'name': 'Student 3', 'age': 16}
]

class Student(BaseModel):
    name: str
    age: int


def student_check(student_id):
    if not students[student_id]:
        raise HTTPException(status_code=404, detail='Student Not Found')


@router.get('/students')
def user_list():
    return {'students': students}


@router.get('/students/{student_id}')
def user_detail(student_id: int):
    student_check(student_id)
    return {'student': students[student_id]}


@router.post('/students')
def user_add(student: Student):
    students.append(student)
    return {'student': students[-1]}


@router.put('/students/{student_id}')
def user_update(student: Student, student_id: int):
    student_check(student_id)
    students[student_id].update(student)

    return {'student': students[student_id]}


@router.delete('/students/{student_id}')
def user_delete(student_id: int):
    student_check(student_id)
    del students[student_id]

    return {'students': students}