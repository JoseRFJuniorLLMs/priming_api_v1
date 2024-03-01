from beanie import Document, PydanticObjectId
from typing import Optional, List

from src.Model.Course import Course
from src.Model.Module import Module


class Classroom(Document):
    _id: Optional[PydanticObjectId] = None
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

