from src.Repository.Repository import connection
from bson import ObjectId


class CourseRepository:
    def __init__(self):
        self.db = connection()

    def get_course_by_id(self, course_id):
        course_id = ObjectId(course_id)

        query = {'_id': course_id}
        return self.db.CourseCollection.find_one(query)

    def get_courses_by_level(self, level: str):
        query = {'level': level}
        return list(self.db.CourseCollection.find(query))

    def get_all_courses(self):
        return list(self.db.CourseCollection.find())

    def get_course_by_name(self, name):
        query = {'name': name}
        return self.db.CourseCollection.find_one(query)

