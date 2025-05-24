from pydantic import BaseModel


class BookDTO(BaseModel):
    id: int
    author_name: str | None
    name: str
    publisher_name: str
    description: str | None
