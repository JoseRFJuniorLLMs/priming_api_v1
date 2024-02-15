import datetime
from typing import Optional
from beanie import Document, ObjectIdField
from datetime import time  # Importe time do módulo datetime

class Lesson(Document):
    id: Optional[int] = None
    name: str
    prime: ObjectIdField
    youtubeUrl: ObjectIdField
    text: ObjectIdField
    pharse: ObjectIdField
    dictionary: ObjectIdField
    start: time  # Campo de início do tipo time
    end: time  # Campo de fim do tipo time
    status: str
    date: datetime
    duration_minutes: int