from typing import Optional

from beanie import Document, PydanticObjectId


class DictionaryPrime(Document):
    _id: Optional[PydanticObjectId] = None
    prime: str
    target: str
    text: str

    class Settings:
        name = "primeTargetDictionaryCollection"
