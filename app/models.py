from pydantic import BaseModel


class Book(BaseModel):
    id: int
    name: str


# books_db = [
#     Book(id=1, title="Sample Book", author="Sample Author")
# ]