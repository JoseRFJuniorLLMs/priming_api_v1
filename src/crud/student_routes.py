from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from src.auth.jwt_bearer import JWTBearer
from src.service import student_servicer as service


api = APIRouter(prefix='/student')


@api.get('/{id}')
async def get_student_by_id(id: str):
    try:
        student = service.get_student_by_id(id)
        return student
    except:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado!")


@api.get('/')
async def get_students(name: str | None = None, email: str | None = None):
    if email:
        return service.get_student_by_email(email)
    elif name:
        return service.get_student_by_name(name)
    return service.get_student_list()


@api.delete('/{student_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(student_id: str):
    service.delete_by_id(student_id)
