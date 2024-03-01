from typing import Optional, List
from bson import ObjectId
from beanie import Document, PydanticObjectId
from pydantic import Field


class PhrasePrime(Document):

    _id: Optional[PydanticObjectId] = None
    phrase_id: Optional[str] = Field(alias="_id")

    prime: str
    target: str
    phrase: List[str]
    url: List[str]
    image: List[str]

    class Settings:
        name = "primeTargetPharseCollection"
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "module_id"