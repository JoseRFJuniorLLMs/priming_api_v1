from typing import Optional

from beanie import Document, PydanticObjectId
from pydantic import Field


class Prime(Document):

    _id: Optional[PydanticObjectId] = None
    prime_id: Optional[str] = Field(alias="_id")

    prime: str
    target: str

    class Settings:
        name = "primeTargetCollection"
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "prime_id"