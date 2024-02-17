from typing import Optional, List
from bson import ObjectId
from beanie import Document


class PhrasePrime(Document):
    _id: Optional[ObjectId] = None
    prime: str
    target: str
    phrase: List[str]
    url: List[str]
    image: List[str]

    class Settings:
        name = "primeTargetPharseCollection"
