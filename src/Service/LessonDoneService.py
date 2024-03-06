from src.Repository.LessonDoneRepository import LessonDoneRepository


class LessonDoneService:
    @staticmethod
    async def get_lesson_done_by_student(student_id):
        data = LessonDoneRepository().get_lesson_done_by_student(student_id)
        return data
