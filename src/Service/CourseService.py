from beanie import PydanticObjectId

from src.Model.Course import Course
from src.Repository.CourseRepository import CourseRepository


class CourseService:
    def __init__(self):
        self.repository = CourseRepository()

    async def get_course_by_name(self, name: str):
        course = await self.repository.get_course_by_name(name)
        return course

    @staticmethod
    async def create(course: Course):
        await course.insert()
        await course.save()
        return course

    @staticmethod
    async def get_courses_paginated(page: int, page_size: int):
        skip = page * page_size
        courses = await Course.find_all(skip=skip, limit=page_size)
        return courses

    async def get_all_courses(self):
        data = self.repository.get_all_courses()

        for item in data:
            item['_id'] = str(item['_id'])

        return data

    async def get_course(self, _id):
        course = self.repository.get_course_by_id(_id)
        course["_id"] = str(course["_id"])
        return course

    @staticmethod
    async def update_course(db_course: Course, new_course_data: Course):
        for field, value in new_course_data.dict().items():
            setattr(db_course, field, value)
        await db_course.save()
        return db_course
