import re
from typing import List

from bson import ObjectId

from src.model import Student
from src.repository.mongodb import MongoDB as db

COLLECTION = 'StudentCollection'


def create_student(student_data: Student):
    return db().save_document(collection=COLLECTION, document=student_data.mongo())


def update_student(student_data: Student):
    db().update_document(
        collection=COLLECTION,
        key={"_id": student_data.id},
        document=student_data.mongo()
    )


def delete_by_id(student_id):
    db().delete_by_key(
        collection=COLLECTION,
        key={'_id': ObjectId(student_id)}
    )


def get_student_list():
    student_list = db().get_by_filter(collection=COLLECTION, key={})
    return dict_to_student_model(student_list)


def get_student_by_id(student_id):
    result = db().get_by_key(
        collection=COLLECTION,
        key={'_id': student_id}
    )
    return Student.from_mongo(result)


def get_student_by_name(student_name: str):
    regex = re.compile(f".*{student_name}.*", re.IGNORECASE)
    result = db().get_by_filter(
        collection=COLLECTION,
        key={'name': regex}
    )
    return dict_to_student_model(result)


def get_student_by_email(student_email: str):
    regex = re.compile(f".*{student_email}.*", re.IGNORECASE)
    result = db().get_by_filter(
        collection=COLLECTION,
        key={'email': regex}
    )
    return dict_to_student_model(result)


def dict_to_student_model(student_list: List) -> List[Student]:
    students = []
    for student in student_list:
        students.append(Student.from_mongo(student))
    return students
