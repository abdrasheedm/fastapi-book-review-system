from pydantic import BaseModel
from datetime import date


class Author(BaseModel):
    name : str
    date_of_birth : date
    email : str
    nationality : str


    class Config:
        from_attributes = True


class Book(BaseModel):
    title : str
    publication_year : int
    author_id : int

    class Config:
        from_attributes = True



class BookWithAuthor(BaseModel):
    title : str
    publication_year : int
    author : Author

    class Config:
        from_attributes = True


class Review(BaseModel):
    title : str
    review : str
    rating : int
    book_id : int

    class Config:
        from_attributes = True

class ReviewWithBook(BaseModel):
    title : str
    review : str
    rating : int
    books : BookWithAuthor

    class Config:
        from_attributes = True



class User(BaseModel):

    name : str
    email : str
    password : str


class ShowUser(BaseModel):
    
    name : str
    email : str

    class Config:
        from_attributes = True


class Login(BaseModel):
    email : str
    password : str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None