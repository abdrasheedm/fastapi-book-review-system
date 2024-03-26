from fastapi import FastAPI
from . import models
from .database import engine
from .routers import author, book, user, review

# Create a FastAPI instance
app = FastAPI()

# Create database tables if they don't exist
models.Base.metadata.create_all(engine)

# Define a simple route to return "hello world"
@app.get('/', tags=['Hello world'])
def index():
    return "hello world"

# Include routers for different endpoints
app.include_router(author.router)
app.include_router(book.router)
app.include_router(user.router)
app.include_router(review.router)
