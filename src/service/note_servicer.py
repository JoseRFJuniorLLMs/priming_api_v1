import re
from typing import List

from bson import ObjectId

from src.model import Note
from src.repository.mongodb import MongoDB as db

COLLECTION = 'NoteCollection'


def create_note(note_data: Note):
    note_data.student_id = ObjectId(note_data.student_id)
    return db().save_document(collection=COLLECTION, document=note_data.mongo())


def update_note(note_data: Note):
    db().update_document(
        collection=COLLECTION,
        key={"_id": note_data.id},
        document=note_data.mongo()
    )


def delete_by_id(note_id):
    db().delete_by_key(
        collection=COLLECTION,
        key={'_id': ObjectId(note_id)}
    )


def get_notes_by_student(student_id):
    notes = db().get_by_filter(
        collection=COLLECTION,
        key={'student_id': ObjectId(student_id)}
    )
    return dict_to_note_model(notes)


# ! Todo: Fazer no formato de foreach para pegar uma das tags de uma nota
# def get_notes_by_tag(tag_id):
#     notes = db().get_by_key(
#         collection=COLLECTION,
#         key={'student_id': ObjectId(tag_id)}
#     )
#     return Note.from_mongo(notes)

def get_note_by_title(note_title):
    regex = re.compile(f'.*{note_title}.*', re.IGNORECASE)
    notes = db().get_by_filter(
        collection=COLLECTION,
        key={'title': regex}
    )
    return dict_to_note_model(notes)


def dict_to_note_model(note_list: List) -> List[Note]:
    notes = []
    for note in note_list:
        notes.append(Note.from_mongo(note))
    return notes
