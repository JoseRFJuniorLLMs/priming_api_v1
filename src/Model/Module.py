from typing import Optional

from beanie import Document, PydanticObjectId
from pydantic import Field


class Module(Document):

    _id: Optional[PydanticObjectId] = None
    module_id: Optional[str] = Field(alias="_id")

    prime: str
    target: str
    text: str

    class Settings:
        name = "ModuleCollection"
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "module_id"