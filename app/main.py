from fastapi import FastAPI

from app.transport.handlers.authors import author_router
from app.transport.handlers.books import book_router
from app.transport.handlers.comments import comment_router
from app.transport.handlers.publishers import publisher_router
from app.transport.handlers.users import user_router

app = FastAPI()
app.include_router(book_router)
app.include_router(author_router)
app.include_router(publisher_router)
app.include_router(user_router)
app.include_router(comment_router)