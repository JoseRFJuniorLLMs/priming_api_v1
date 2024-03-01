from beanie import PydanticObjectId

from src.Model.Course import Course


class CourseService:
    @staticmethod
    async def get_course_by_name(name: str):
        course = await Course.find_one({"name": name})
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

    @staticmethod
    async def get_all_courses():
        courses = await Course.find_all()
        return courses

    @staticmethod
    async def get_course(course_id: PydanticObjectId):
        course = await Course.get(course_id)
        return course

    @staticmethod
    async def update_course(db_course: Course, new_course_data: Course):
        for field, value in new_course_data.dict().items():
            setattr(db_course, field, value)
        await db_course.save()
        return db_course
