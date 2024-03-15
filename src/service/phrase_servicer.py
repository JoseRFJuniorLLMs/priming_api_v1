import re
from typing import List

from bson import ObjectId

from src.model import Phrase
from src.repository.mongodb import MongoDB as db

COLLECTION = 'primeTargetPhraseCollection'


def create_phrase(phrase_data: Phrase):
    return db().save_document(collection=COLLECTION, document=phrase_data.mongo())


def update_phrase(phrase_data: Phrase):
    db().update_document(
        collection=COLLECTION,
        key={'_id': phrase_data.id},
        document=phrase_data.mongo()
    )


def delete_by_id(phrase_id):
    db().delete_by_key(
        collection=COLLECTION,
        key={'_id': ObjectId(phrase_id)}
    )


def get_phrase_list():
    phrase_list = db().get_by_filter(collection=COLLECTION, key={})
    return dict_to_phrase_model(phrase_list)


def get_phrase_by_id(phrase_id: str):
    phrase = db().get_by_key(
        collection=COLLECTION,
        key={'_id': ObjectId(phrase_id)}
    )
    return Phrase.from_mongo(phrase)


def get_phrases_by_prime(phrase_level: str):
    regex = re.compile(f".*{phrase_level}.*", re.IGNORECASE)
    result = db().get_by_filter(
        collection=COLLECTION,
        key={"prime": regex}
    )
    return dict_to_phrase_model(result)


def dict_to_phrase_model(phrase_list: List) -> List[Phrase]:
    phrases = []
    for phrase in phrase_list:
        phrases.append(Phrase.from_mongo(phrase))
    return phrases
