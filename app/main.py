from fastapi import FastAPI

from app.transport.handlers.authors import author_router
from app.transport.handlers.books import book_router

app = FastAPI()
app.include_router(book_router)
app.include_router(author_router)