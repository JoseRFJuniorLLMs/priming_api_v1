from fastapi import APIRouter, Depends, HTTPException, status
from src.Model.Student import Student
from src.Service.StudentService import StudentService
from src.Service.LoginService import LoginService

app = APIRouter()


@app.post("/", response_model=Student, status_code=201)
async def create_student(student: Student, current_user: str = Depends(LoginService.get_current_user)):
    return await StudentService.create(student)


@app.get("/{username}", response_model=Student, status_code=200)
async def get_student_by_username(username: str, current_user: str = Depends(LoginService.get_current_user)):
    return await Student.find_one({"login": username})


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
