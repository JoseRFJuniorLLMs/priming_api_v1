from src.Repository.Repository import connection
from bson import ObjectId


class StudentRepository:
    def __init__(self):
        self.db = connection()

    def validate_login(self, username: str, password: str):
        query = {"email": username, "password": password}

        student = self.db.StudentCollection.find_one(query)
        return student

    def get_student_by_login(self, login: str) -> dict:
        query = {"login": login}

        student = self.db.StudentCollection.find_one(query)
        return student

    def get_courses(self, student_id: str):
        pipeline = [
            {'$match': {'_id': student_id}},
            {'$lookup': {
                'from': 'CourseCollection',
                'localField': 'courses',
                'foreignField': '_id',
                'as': 'course_details'
            }},
            {'$unwind': '$course_details'},
            {'$project': {
                '_id': '$course_details._id',
                'level': '$course_details.level',
                'name': '$course_details.name',
                'content': '$course_details.content',
                'objective': '$course_details.objective',
                'status': '$course_details.status'
            }}
        ]

        return list(self.db.StudentCollection.aggregate(pipeline))

    def get_books(self, student_id: str):
        pipeline = [
            {'$match': {'_id': student_id}},
            {'$lookup': {
                'from': 'BooksCollection',
                'localField': 'books',
                'foreignField': '_id',
                'as': 'books_details'
            }},
            {'$unwind': '$books_details'},
            {'$project': {
                '_id': '$books_details._id',
                'title': '$books_details.title',
                'author': '$books_details.author',
                'description': '$books_details.description'
            }}
        ]

        return list(self.db.StudentCollection.aggregate(pipeline))
