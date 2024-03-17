import re
from typing import List

from bson import ObjectId

from src.model import Course
from src.repository.mongodb import MongoDB as db

COLLECTION = 'CourseCollection'


def create_course(course_data: Course):
    return db().save_document(collection=COLLECTION, document=course_data.mongo())


def update_course(course_data: Course):
    db().update_document(
        collection=COLLECTION,
        key={'_id': course_data.id},
        document=course_data.mongo()
    )


def delete_by_id(course_id):
    db().delete_by_key(
        collection=COLLECTION,
        key={'_id': ObjectId(course_id)}
    )


def get_course_list():
    course_list = db().get_by_filter(collection=COLLECTION, key={})
    return dict_to_course_model(course_list)


def get_course_by_id(course_id: str):
    course = db().get_by_key(
        collection=COLLECTION,
        key={'_id': ObjectId(course_id)}
    )
    return Course.from_mongo(course)


def get_courses_by_param(param_name: str, course_level: str):
    regex = re.compile(f".*{course_level}.*", re.IGNORECASE)
    result = db().get_by_filter(
        collection=COLLECTION,
        key={param_name: regex}
    )
    return dict_to_course_model(result)


def dict_to_course_model(course_list: List) -> List[Course]:
    courses = []
    for course in course_list:
        courses.append(Course.from_mongo(course))
    return courses
