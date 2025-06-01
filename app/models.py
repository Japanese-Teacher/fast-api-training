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


class NewPublisherDTO(BaseModel):
    name: str


class UserDTO(BaseModel):
    id: int
    first_name: str
    second_name: str
    age: int
    login: str
    password_hash: str


class NewUserDTO(BaseModel):
    id: int
    new_first_name: str
    new_second_name: str
    new_age: int
    new_login: str
    new_password_hash: str
