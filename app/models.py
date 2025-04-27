from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str


books_db = [
    Book(id=1, title="Sample Book", author="Sample Author")
]