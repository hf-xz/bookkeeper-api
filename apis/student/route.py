from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from .model import *
from .service import *

router = APIRouter()


@router.post('', response_description='Student data added into the database')
def add_student_data(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = add_student(student)
    return ResponseModel(new_student, 'Student added successfully.')


@router.get('', response_description='Students retrieved')
def get_students():
    students = retrieve_students()
    if students:
        return ResponseModel(students, 'Students data retrieved successfully')
    return ResponseModel(students, 'Empty list returned')


@router.get('/{id}', response_description='Student data retrieved')
def get_student_data(id):
    student = retrieve_student(id)
    if student:
        return ResponseModel(student, 'Student data retrieved successfully')
    return ErrorResponseModel('An error occurred.', 404, 'Student doesn\'t exist.')


@router.put('/{id}')
def update_student_data(id: str, req: UpdateStudentModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_student = update_student(id, req)
    if updated_student:
        return ResponseModel(
            'Student with ID: {} name update is successful'.format(id),
            'Student name updated successfully',
        )
    return ErrorResponseModel(
        'An error occurred',
        404,
        'There was an error updating the student data.',
    )


@router.delete('/{id}', response_description='Student data deleted from the database')
def delete_student_data(id: str):
    deleted_student = delete_student(id)
    if deleted_student:
        return ResponseModel(
            'Student with ID: {} removed'.format(id), 'Student deleted successfully'
        )
    return ErrorResponseModel(
        'An error occurred', 404, 'Student with id {0} doesn\'t exist'.format(id)
    )
