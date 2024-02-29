from src.Model.Student import Student


class StudentService:
    @staticmethod
    async def get_student_by_login(login: str):
        student = await Student.find_one({"login": login})
        return student

    @staticmethod
    async def get_student_by_email(email: str):
        student = await Student.find_one({"email": email})
        return student

    @staticmethod
    async def create(student: Student):
        await student.insert()
        await student.save()
        return student

    @staticmethod
    async def get_students_paginated(page: int, page_size: int):
        skip = page * page_size
        students = Student.find_all(skip=skip, limit=page_size)
        return students
