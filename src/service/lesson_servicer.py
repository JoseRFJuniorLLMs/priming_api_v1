import re
from typing import List

from bson import ObjectId

from src.model import Lesson
from src.repository.mongodb import MongoDB as db

COLLECTION = 'LessonCollection'


def create_lesson(lesson_data: Lesson):
    return db().save_document(
        collection=COLLECTION,
        document=lesson_data.mongo()
    )


def update_lesson(lesson_data: Lesson):
    db().update_document(
        collection=COLLECTION,
        key={'_id': lesson_data.id},
        document=lesson_data.mongo()
    )


def delete_by_id(lesson_id):
    db().delete_by_key(
        collection=COLLECTION,
        key={'_id': ObjectId(lesson_id)}
    )


def get_lesson_list():
    lesson_list = db().get_by_filter(
        collection=COLLECTION,
        key={}
    )
    return dict_to_lesson_model(lesson_list)


def get_lesson_by_name(lesson_name):
    regex = re.compile(f'.*{lesson_name}.*', re.IGNORECASE)
    lessons = db().get_by_filter(
        collection=COLLECTION,
        key={'name': regex}
    )
    return dict_to_lesson_model(lessons)


def dict_to_lesson_model(lesson_list: List) -> List[Lesson]:
    lessons = []
    for lesson in lesson_list:
        lessons.append(Lesson.from_mongo(lesson))
    return lessons
