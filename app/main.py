from fastapi import FastAPI

from app.endpoints import book_router

app = FastAPI()
app.include_router(book_router)

