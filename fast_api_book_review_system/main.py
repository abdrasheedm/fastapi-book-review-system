from fastapi import FastAPI
from . import models
from .database import engine
from .routers import author, book, user, distance


app = FastAPI()

models.Base.metadata.create_all(engine)



# HELLO WORLD
@app.get('/', tags=['Hello world'])
def index():
    return "hello world"


# OTHER ROUTERS
app.include_router(author.router)
app.include_router(book.router)
app.include_router(user.router)
app.include_router(distance.router)

