from typing import Optional, List

from beanie import Document


class PrhasePrime(Document):
    _id: Optional[int] = None
    prime: str
    target: str
    phrase: List[str]
    url: List[str]
    image: List[str]

    class Settings:
        name = "primeTargetPharseCollection"
