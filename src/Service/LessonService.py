from src.Model.Course import Course
from src.Repository.LessonRepository import LessonRepository


class LessonService:

    @staticmethod
    async def get_lessons_by_course(course_id):
        lessons = LessonRepository().get_lessons_by_course(course_id)
        return lessons
