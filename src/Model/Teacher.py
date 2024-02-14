from typing import Optional

from beanie import Document
from Course import Course


class Teacher(Document):
    id: Optional[int] = None
    name: str
    cpf: str
    course: Course
