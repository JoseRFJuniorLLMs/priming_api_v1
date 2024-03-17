import re
from typing import List

from bson import ObjectId

from src.model import Tag
from src.repository.mongodb import MongoDB as db

COLLECTION = 'TagCollection'


def create_tag(tag_data: Tag):
    return db().save_document(collection=COLLECTION, document=tag_data.mongo())


def update_tag(tag_data: Tag):
    db().update_document(
        collection=COLLECTION,
        key={"_id": tag_data.id},
        document=tag_data.mongo()
    )


def delete_by_id(tag_id):
    db().delete_by_key(
        collection=COLLECTION,
        key={"_id": ObjectId(tag_id)}
    )


def get_tag_by_id(tag_id):
    tag = db().get_by_key(
        collection=COLLECTION,
        key={"_id": ObjectId(tag_id)}
    )
    return Tag.from_mongo(tag)


def get_tag_by_student(student_id):
    tags = db().get_by_filter(
        collection=COLLECTION,
        key={'student_id': ObjectId(student_id)}
    )
    return dict_to_tag_model(tags)


def dict_to_tag_model(tag_list: List) -> List[Tag]:
    tags = []
    for tag in tag_list:
        tags.append(Tag.from_mongo(tag))
    return tags
