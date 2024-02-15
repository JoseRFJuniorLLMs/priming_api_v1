from typing import Optional

from beanie import Document


class Module(Document):
    id: Optional[int] = None
    prime: str
    target: str
    text: str
