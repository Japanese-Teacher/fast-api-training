from datetime import datetime

from pydantic import BaseModel

class AuthorDTO(BaseModel):
    name: str
    nationality: str
    date_of_birth: datetime

class BookDTO(BaseModel):
    id: int
    authors: list[AuthorDTO]
    name: str
    publisher_name: str
    description: str | None
