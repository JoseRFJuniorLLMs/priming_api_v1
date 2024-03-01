from typing import Optional

from beanie import Document, PydanticObjectId
from pydantic import Field


class TextPrime(Document):

    _id: Optional[PydanticObjectId] = None
    text_prime_id: Optional[str] = Field(alias="_id")

    prime: str
    target: str
    text: str

    class Settings:
        name = "primeTargetTextCollection"
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "text_prime_id"