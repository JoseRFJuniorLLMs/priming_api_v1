from typing import Optional

from beanie import Document, PydanticObjectId


class TextPrime(Document):
    _id: Optional[PydanticObjectId] = None
    prime: str
    target: str
    text: str

    class Settings:
        name = "primeTargetTextCollection"

