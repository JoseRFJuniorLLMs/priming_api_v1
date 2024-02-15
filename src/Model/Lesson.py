from typing import Optional
from beanie import Document

from src.Model.Course import Course


class Lesson(Document):
    id: Optional[int] = None
    name: str
    youtubeUrl: str
    course: Course
    time: str
