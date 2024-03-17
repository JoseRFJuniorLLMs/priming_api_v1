from fastapi import APIRouter, Depends
from starlette import status

from src.auth.jwt_bearer import JWTBearer
from src.service import student_servicer as service


api = APIRouter(prefix='/student')


@api.get('/{id}', dependencies=[Depends(JWTBearer())])
async def get_student_by_id(id: str):
    student = service.get_student_by_id(id)
    return student


@api.get('/', dependencies=[Depends(JWTBearer())])
async def get_students(name: str | None = None, email: str | None = None):
    if email:
        return service.get_student_by_email(email)
    elif name:
        return service.get_student_by_name(name)
    return service.get_student_list()


@api.delete('/{student_id}', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
async def delete_student(student_id: str):
    service.delete_by_id(student_id)
