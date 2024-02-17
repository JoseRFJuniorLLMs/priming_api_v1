from typing import Optional, List

from beanie import Document


class YoutubePrime(Document):
    _id: Optional[int] = None
<<<<<<< HEAD
    # prime: ObjectId = ObjectId()
=======
>>>>>>> origin/main
    prime: str
    target: str
    url: List[str]

    class Settings:
        name = "primeTargetYoutubeCollection"
