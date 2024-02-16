from typing import Optional

from beanie import Document


class DictionaryPrime(Document):
    _id: Optional[int] = None
    #prime: ObjectId = ObjectId()
    prime: str
    target: str
    text: str

    class Settings:
        name = "primeTargetDictionaryCollection"
