from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from beanie import PydanticObjectId
from src.Model.Course import Course
from src.Service.LoginService import LoginService
from src.Service.CourseService import CourseService


app = APIRouter()


def get_current_user(token: str = Depends(LoginService().oauth2_scheme)):
    return LoginService().get_current_user(token)


@app.post("/", response_model=Course, status_code=201)
async def create_course(course: Course, current_user: str = Depends(get_current_user)):
    return await CourseService.create(course)


@app.get("/", response_model=List[Course], status_code=200)
async def get_all_courses(current_user: str = Depends(LoginService.get_current_user)):
    return await CourseService.get_all_courses()


@app.get("/{course_id}", response_model=Course, status_code=200)
async def get_course(course_id: PydanticObjectId, current_user: str = Depends(get_current_user)):
    course = await CourseService.get_course(course_id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    return course


@app.delete("/{course_id}", status_code=204)
async def delete_course(course_id: PydanticObjectId, current_user: str = Depends(get_current_user)):
    course = await CourseService.get_course(course_id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    await course.delete()
    return


@app.patch("/{course_id}", response_model=Course)
async def update_course(course_id: PydanticObjectId, course: Course, current_user: str = Depends(get_current_user)):
    db_course = await CourseService.get_course(course_id)
    if not db_course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
    updated_course = await CourseService.update_course(db_course, course)
    return updated_course
