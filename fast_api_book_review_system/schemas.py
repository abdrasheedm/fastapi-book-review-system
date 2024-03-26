from pydantic import BaseModel

class Author(BaseModel):
    name : str
    date_of_birth : str
    email : str
    nationality : str


    class Config:
        orm_mode = True


class Book(BaseModel):
    title : str
    publication_year : str

    class Config:
        orm_mode = True



class AddAuthor(BaseModel):
    author_id : int



# class ViewStudentWithTeacher(BaseModel):
#     name : str
#     department : str
#     teacher : Teacher

#     class Config:
#         orm_mode = True



# class User(BaseModel):

#     name : str
#     email : str
#     password : str


# class ShowUser(BaseModel):
    
#     name : str
#     email : str

#     class Config:
#         orm_mode = True


# class Login(BaseModel):
#     email : str
#     password : str


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     username: str | None = None


# class Distance(BaseModel):
#     lat1 : int
#     lat2 : int
#     lon1 : int
#     lon2 : int