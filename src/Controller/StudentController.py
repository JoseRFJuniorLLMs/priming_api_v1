from fastapi import APIRouter, Depends
from Model.Student import Student
from Service.StudentService import StudentService
from Service.LoginService import LoginService

app = APIRouter()


@app.post("/", response_model=Student, status_code=201)
async def create_student(student: Student, current_user: str = Depends(LoginService.get_current_user)):
    return await StudentService.create(student)


@app.get("/{username}", response_model=Student, status_code=200)
async def get_student_by_username(username: str, current_user: str = Depends(LoginService.get_current_user)):
    return await Student.find_one({"login": username})


@app.delete("/{username}", status_code=204)
async def delete_student(username: str):
    # ! todo
    pass


@app.patch("/{username}", response_model=Student)
async def update_student(username: str, student:Student):
    # ! TODO
    pass
