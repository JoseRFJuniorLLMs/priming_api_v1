from typing import Optional

from beanie import Document, PydanticObjectId


class Module(Document):
    _id: Optional[PydanticObjectId] = None
    prime: str
    target: str
    text: str
