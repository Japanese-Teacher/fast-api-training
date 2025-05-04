from pydantic import BaseModel


class BookDTO(BaseModel):
    id: int
    name: str