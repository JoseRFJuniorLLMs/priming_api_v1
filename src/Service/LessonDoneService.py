from src.Repository.LessonDoneRepository import LessonDoneRepository


class LessonDoneService:
    @staticmethod
    def get_lesson_done_by_student(student_id):
        data = LessonDoneRepository().get_lesson_done_by_student(student_id)
        return data
