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

class NewBookDTO(BaseModel):
    id: int
    new_authors: list[AuthorDTO]
    new_name: str
    new_publisher_name: str
    new_description: str | None

class NewAuthorDTO(BaseModel):
    new_name: str
    new_nationality: str
    new_date_of_birth: datetime

class PublisherDTO(BaseModel):
    name: str