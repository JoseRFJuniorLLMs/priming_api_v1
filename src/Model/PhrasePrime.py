from typing import Optional, List
from bson import ObjectId
from beanie import Document, PydanticObjectId


class PhrasePrime(Document):
    _id: Optional[PydanticObjectId] = None
    prime: str
    target: str
    phrase: List[str]
    url: List[str]
    image: List[str]

    class Settings:
        name = "primeTargetPharseCollection"
