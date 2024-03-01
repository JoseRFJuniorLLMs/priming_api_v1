from typing import Optional

from beanie import Document, PydanticObjectId


class Prime(Document):
    _id: Optional[PydanticObjectId] = None
    prime: str
    target: str

    class Settings:
        name = "primeTargetCollection"
