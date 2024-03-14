from fastapi import APIRouter, Body, Depends
from starlette import status

from src.auth.jwt_bearer import JWTBearer
from src.service import student_servicer as service


api = APIRouter(prefix='/student')


@api.get('/{name}', dependencies=[Depends(JWTBearer())])
async def get_student_by_name(name: str):
    student = service.get_student_by_name(name)
    return student


@api.get('/', dependencies=[Depends(JWTBearer())])
async def get_lessons():
    courses = service.get_student_list()
    return courses
