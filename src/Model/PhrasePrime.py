from typing import Optional, List
from bson import ObjectId
from beanie import Document


class PrhasePrime(Document):
    _id: Optional[int] = None
    # prime: ObjectId = ObjectId()
    prime: ObjectId = ObjectId()
    target: str
    phrase: List[str]
    url: List[str]
    image: List[str]

    class Settings:
        name = "primeTargetPharseCollection"
