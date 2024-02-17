from typing import Optional

from beanie import Document


class Prime(Document):
    _id: Optional[int] = None
    prime: str
    target: str
<<<<<<< HEAD

    class Settings:
        name = "primeTargetCollection"
=======
>>>>>>> origin/main
