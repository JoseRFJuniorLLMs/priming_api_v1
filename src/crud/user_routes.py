from fastapi import APIRouter, Body
from starlette import status

from src.model import StudentLogin, Student
from src.auth.jwt_handler import signJWT
from src.service import student_servicer as service

api = APIRouter()


@api.post('/login')
async def user_login(user: StudentLogin = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            'error': 'Invalid login details!'
        }


@api.post('/signup')
async def user_signup(user: Student = Body(default=None)):
    student = service.create_student(user)
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            'error': 'Invalid login details!'
        }


@api.patch('/', status_code=status.HTTP_204_NO_CONTENT)
async def update_student(user: Student = Body(...)):
    service.update_student(user)
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            'error': 'Invalid login details!'
        }


def check_user(data):
    user = service.get_student_by_email(data.email)
    if data.password == user['password']:
        return True
