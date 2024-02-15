from beanie import Document
from typing import Optional, List

from Course import Course
from Module import Module
class Books(Document):
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