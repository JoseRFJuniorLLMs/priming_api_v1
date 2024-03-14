from fastapi import APIRouter

from src.service import course_servicer as service

api = APIRouter(prefix='/course')


@api.get('/{level}')
async def get_student(level: str):
    student = service.get_courses_by_level(level)
    return student


@api.get('/')
async def get_courses():
    courses = service.get_course_list()
    return courses
