from bson import ObjectId

from src.Model.Course import Course
from src.Repository.LessonRepository import LessonRepository


class LessonService:

    @staticmethod
    async def get_lessons_by_course(course_id):
        lessons = LessonRepository().get_lessons_by_course(course_id)
        return lessons

    @staticmethod
    async def get_lesson_by_id(lesson_id):
        lesson = LessonRepository().get_lesson_by_id(lesson_id)
        return lesson
