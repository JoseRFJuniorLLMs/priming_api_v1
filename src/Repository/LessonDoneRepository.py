from src.Repository.Repository import connection
from bson import ObjectId


class LessonDoneRepository:
    @staticmethod
    def get_lesson_done_by_student(student_id):
        db = connection()

        student_id = ObjectId(student_id)

        pipeline = [
            {'$match': {'_id': student_id}},
            {'$lookup': {
                'from': 'StudentCollection',
                'localField': '_id',
                'foreignField': '_id',
                'as': 'student_details'
            }},
            {'$lookup': {
                'from': 'LessonDoneCollection',
                'localField': 'student_details.lessons_done',
                'foreignField': 'lesson',
                'as': 'lesson_done_details'
            }},
            {'$unwind': '$student_details'},  # Desdobrar a coleção StudentCollection
            {'$unwind': '$lesson_done_details'},
            {'$project': {
                '_id': 0,
                'student_id': '$student_details._id',
                'student_name': '$student_details.name',
                'lesson_done_details': {
                    'lesson_id': '$lesson_done_details.lesson',
                    'start_date': '$lesson_done_details.start',
                    'end_date': '$lesson_done_details.end',
                    'status_lesson': '$lesson_done_details.status_lesson'
                }
            }},
            {'$group': {
                '_id': {
                    'student_id': '$student_id',
                    'student_name': '$student_name',
                },
                'lesson_done_details': {'$push': '$lesson_done_details'},
            }}
        ]

        return list(db.StudentCollection.aggregate(pipeline))
