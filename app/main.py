from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.endpoints import book_router

app = FastAPI()
app.include_router(book_router)

