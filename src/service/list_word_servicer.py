import re
from typing import List

from bson import ObjectId

from src.model import ListWord
from src.repository.mongodb import MongoDB as db

COLLECTION = 'primeTargetListWordTextCollecion'


def create_word_list(list_word: ListWord):
    list_word.total = len(list_word.list_word)
    return db().save_document(collection=COLLECTION, document=list_word.mongo())


def update_list_word(list_word: ListWord):
    list_word.total = len(list_word.list_word)
    db().update_document(
        collection=COLLECTION,
        key={"_id": list_word.id},
        document=list_word.mongo()
    )


def delete_by_id(word_id: str):
    db().delete_by_key(
        collection=COLLECTION,
        key={'_id': ObjectId(word_id)}
    )


def get_list_word_by_id(word_id: str):
    list_word = db().get_by_key(
        collection=COLLECTION,
        key={'_id': ObjectId(word_id)}
    )
    return ListWord.from_mongo(list_word)


def get_list_word_by_text_prime(prime_id):
    list_word = db().get_by_filter(
        collection=COLLECTION,
        key={'text_prime': ObjectId(prime_id)}
    )
    return dict_to_list_word_model(list_word)


def dict_to_list_word_model(list_word_list: List) -> List[ListWord]:
    list_words = []
    for list_word in list_word_list:
        list_words.append(ListWord.from_mongo(list_word))
    return list_words
