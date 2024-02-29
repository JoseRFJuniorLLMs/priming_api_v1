from src.Model.Course import Course


class LessonService:

    @staticmethod
    async def get_lessons(level: str):
        lessons = Course.find_one({'level': level})
        return await lessons
