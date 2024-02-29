from src.Model.Lesson import Lesson


class LessonService:

    @staticmethod
    def get_lessons():
        lessons = Lesson.find_all()
        return lessons
