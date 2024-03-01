from typing import List, Optional
from beanie import Document, PydanticObjectId
from bson import ObjectId
from pydantic import Field


class ListWordTextPrime(Document):

    _id: Optional[PydanticObjectId] = None
    list_word_text_prime_id: Optional[str] = Field(alias="_id")

    list_word: List[str]
    text_prime: [ObjectId]
    total: int

    class Settings:
        name = "primeTargetListWordTextCollection"
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "list_word_text_prime_id"