from beanie import Document
from typing import Optional, List

<<<<<<< HEAD
from src.Model.Course import Course
from src.Model.Module import Module
=======
from Course import Course
from Module import Module
>>>>>>> origin/main


class Classroom(Document):
    _id: Optional[int] = None
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

