from fastapi import APIRouter, Body, HTTPException
from starlette import status

from src.model import StudentLogin, Student
from src.auth.jwt_handler import signJWT
from src.service import student_servicer as service

api = APIRouter()


@api.post('/login')
async def user_login(user: StudentLogin = Body(default=None)):
    user_data = service.get_student_by_email(user.email)[0]
    if user_data and user.password == user_data.password:
        return signJWT(user.email)
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid login details")


@api.post('/signup')
async def user_signup(user: Student = Body(default=None)):
    student = service.create_student(user)
    return signJWT(user.email)


@api.patch('/student', status_code=status.HTTP_204_NO_CONTENT)
async def update_student(user: Student = Body(...)):
    service.update_student(user)
    return signJWT(user.email)

