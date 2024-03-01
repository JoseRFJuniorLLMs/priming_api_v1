from beanie import Document, PydanticObjectId
from typing import Optional, List

from pydantic import Field

from src.Model.Course import Course
from src.Model.Module import Module


class Classroom(Document):

    _id: Optional[PydanticObjectId] = None
    classroom_id: Optional[str] = Field(alias="_id")

    studentId: str
    course: Course
    module: List[Module]
    prime: List[str]
    target: List[str]
    phrases: List[str]
    audioUrls: List[str]
    imageUrls: List[str]
    videoUrls: List[str]
    text: str

    class Settings:
        name = "ClassroomCollection"
        arbitrary_types_allowed = True
        json_encoders = {
            PydanticObjectId: str
        }
        id_field = "books_id"