from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.params import Query
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from src.Model.Student import Student
from src.Repository.StudentRepository import StudentRepository
from src.Service.LoginService import LoginService
from src.Service.StudentService import StudentService

app = APIRouter()

origins = ["http://localhost:4200"];

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # If your API allows cookies
    allow_methods=["*"],  # Adjust for allowed methods (e.g., GET, POST, PUT, DELETE)
    allow_headers=["*"])  # Adjust for allowed headers (e.g., Content-Type, Authorization)

DEFAULT_PAGE = 0
DEFAULT_PAGE_SIZE = 10


# Dependency to ensure a valid token is provided
def get_current_user(token: str = Depends(LoginService().oauth2_scheme)):
    return LoginService().get_current_user(token)


@app.post("/", response_model=Student, status_code=201)
async def create_student(student: Student, current_user: str = Depends(get_current_user)):
    return await StudentService.create(student)


@app.get("/page", response_model=List[Student], status_code=200)
async def get_students_paginated(page: int = Query(DEFAULT_PAGE, ge=0),
                                 page_size: int = Query(DEFAULT_PAGE_SIZE, le=100),
                                 current_user: str = Depends(get_current_user)):
    students = await StudentService.get_students_paginated(page, page_size)
    return students


@app.get("/all", response_model=List[Student], status_code=200)
async def get_all_students_paginated(page: int = Query(DEFAULT_PAGE, ge=0),
                                     page_size: int = Query(DEFAULT_PAGE_SIZE, le=100),
                                     current_user: str = Depends(get_current_user)):
    # Calculate the offset based on the page and page size
    offset = page * page_size
    students = await StudentService.get_students_paginated(offset, page_size)
    return students


@app.get("/{username}", response_model=Student, status_code=200)
async def get_student_by_username(request: Request, current_user: str = Depends(get_current_user)):
    username = request.path_params["username"]
    student = StudentRepository().get_student_by_login(username)
    return student


@app.delete("/{username}", status_code=204)
async def delete_student(username: str, current_user: str = Depends(get_current_user)):
    student = await Student.find_one({"login": username})
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    await student.delete()
    return


@app.patch("/{username}", response_model=Student)
async def update_student(username: str, student: Student, current_user: str = Depends(get_current_user)):
    db_student = await Student.find_one({"login": username})
    if not db_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    updated_student = await Student.update(db_student, student)
    return updated_student


@app.get("/{student_id}/courses", status_code=200)
async def get_courses(student_id: str, current_user: str = Depends(get_current_user)):
    return await StudentService.get_student_courses(student_id)


@app.get("/{student_id}/books", status_code=200)
async def get_books(student_id: str, current_user: str = Depends(get_current_user)):
    return await StudentService.get_student_books(student_id)
