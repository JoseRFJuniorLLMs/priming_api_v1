
from fastapi import APIRouter, Depends, HTTPException, status

from fastapi import APIRouter, Depends

from src.Model.Student import Student
from src.Service.StudentService import StudentService
from src.Service.LoginService import LoginService

app = APIRouter()


@app.post("/", response_model=Student, status_code=201)
async def create_student(student: Student, current_user: str = Depends(LoginService.get_current_user)):
    return await StudentService.create(student)



@app.get("/page", response_model=List[Student], status_code=200)
async def get_students_paginated(page: int = Query(DEFAULT_PAGE, ge=0),
                                 page_size: int = Query(DEFAULT_PAGE_SIZE, le=100),
                                 current_user: str = Depends(get_current_user)):
    students = await StudentService.get_students_paginated(page, page_size)
    return students

  
@app.get("/{username}", response_model=Student, status_code=200)
async def get_student_by_username(username: str, current_user: str = Depends(LoginService.get_current_user)):
    return await Student.find_one({"login": username})


@app.get("/v2/{username}", response_model=Student, status_code=200)
async def get_student_by_username_no_auth(request: Request):
    username = request.path_params["username"]
    student = StudentRepository().get_student_by_login(username)
    return student


@app.delete("/{username}", status_code=204)

async def delete_student(username: str, current_user: str = Depends(LoginService.get_current_user)):
    student = await Student.find_one({"login": username})
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    if student.login != current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You don't have permission to delete this student")

    await student.delete()
    return


@app.patch("/{username}", response_model=Student)
async def update_student(username: str, student: Student, current_user: str = Depends(LoginService.get_current_user)):
    db_student = await Student.find_one({"login": username})
    if not db_student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    if db_student.login != current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You don't have permission to update this student")

    updated_student = await StudentService.update(db_student, student)
    return updated_student

async def delete_student(username: str):
    # ! todo
    pass


@app.patch("/{username}", response_model=Student)
async def update_student(username: str, student:Student):
    # ! TODO
    pass

  
@app.get("/v2/{student_id}/courses", status_code=200)
async def get_courses_no_auth(student_id: str):
    return await StudentService.get_student_courses(student_id)


@app.get("/{student_id}/books", status_code=200)
async def get_books(student_id: str, current_user: str = Depends(get_current_user)):
    return await StudentService.get_student_books(student_id)
