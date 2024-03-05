from src.Model.Student import Student
from src.Repository.StudentRepository import StudentRepository


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
        students = await Student.find_all(skip=skip, limit=page_size)
        return students

    @staticmethod
    async def get_student_courses(student_id: str):
        courses = StudentRepository().get_courses(student_id)

        for course in courses:
            course["_id"] = str(course["_id"])

        return courses

    @staticmethod
    async def get_student_books(student_id: str):
        books = StudentRepository().get_books(student_id)

        for book in books:
            book['_id'] = str(book['_id'])

        return books
