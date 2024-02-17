from typing import Optional

from beanie import Document


class TextPrime(Document):
    _id: Optional[int] = None
    prime: str
    target: str
    text: str
<<<<<<< HEAD

    class Settings:
        name = "primeTargetTextCollection"

=======
>>>>>>> origin/main
