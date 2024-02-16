from typing import List, Optional
from beanie import Document



class ListWordTextPrime(Document):
    _id: Optional[int] = None
    list_word: List[str]
    text_prime: List[ObjectId] = []
    total: int

    class Settings:
        name = "primeTargetListWordTextCollecion"
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: dict
        }