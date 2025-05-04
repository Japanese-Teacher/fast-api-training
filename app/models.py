from pydantic import BaseModel


class Book(BaseModel):
    id: int
    name: str