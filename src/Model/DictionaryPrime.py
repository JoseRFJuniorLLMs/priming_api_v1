from typing import Optional

from beanie import Document, PydanticObjectId
from pydantic import Field


class DictionaryPrime(Document):

    _id: Optional[PydanticObjectId] = None
    dictionary_id: Optional[str] = Field(alias="_id")

    prime: str
    target: str
    text: str

    class Settings:
        name = "primeTargetDictionaryCollection"
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "dictionary_id"