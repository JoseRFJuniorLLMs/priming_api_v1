from fastapi import APIRouter, Depends, HTTPException, status
from starlette.requests import Request
from starlette.responses import RedirectResponse

from src.Model.Student import Student
from src.Service.StudentService import StudentService
from src.Service.LoginService import LoginService

app = APIRouter()


# Dependency to ensure a valid token is provided
def get_current_user(token: str = Depends(LoginService().oauth2_scheme)):
    return LoginService().get_current_user(token)


@app.post("/", response_model=Student, status_code=201)
async def create_student(student: Student, current_user: str = Depends(get_current_user)):
    return await StudentService.create(student)


@app.get("/{username}", response_model=Student, status_code=200)
@LoginService.validate_login_or_google
async def get_student_by_username(request: Request):
    username = request.path_params["username"]
    print(username)
    return await Student.find_one({"login": username})


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
