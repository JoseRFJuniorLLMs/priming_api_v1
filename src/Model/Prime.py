from typing import Optional

from beanie import Document


class Prime(Document):
    _id: Optional[int] = None
    prime: str
    target: str


    class Settings:
        name = "primeTargetCollection"

