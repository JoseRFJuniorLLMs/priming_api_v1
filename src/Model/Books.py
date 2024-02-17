from typing import List, Optional
from beanie import Document
from bson import ObjectId

from src.Model.Course import Course
from src.Model.Module import Module


class Books(Document):
    _id: Optional[ObjectId] = None
    title: str
    author: str
    isbn: str
    publisher: str
    publication_year: str
    genre: str
    pages: str
    language: str
    description: str
    price: str
    availability: str
    url: str

    class Settings:
        name = "BooksCollection"
