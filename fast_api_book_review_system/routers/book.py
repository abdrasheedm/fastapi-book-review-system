from fastapi import APIRouter, Depends, status
from .. import schemas, oauth2, database
from sqlalchemy.orm import Session
from ..repository import books
from typing import Optional
from datetime import date

# Creating a router for handling book-related endpoints
router = APIRouter(
    tags=['Books'],  # Tags for OpenAPI documentation
    prefix='/book'  # Prefix for all routes defined in this router
)
get_db = database.get_db  # Dependency to get the database session

# Endpoint to view all books
@router.get('/s/', response_model=list[schemas.BookWithAuthor], status_code=status.HTTP_200_OK)
def view_all_books(db: Session = Depends(get_db), author_name: Optional[str] = None, publication_year: Optional[int] = None, current_user: schemas.User = Depends(oauth2.get_current_user)):
    return books.get_all(db, author_name, publication_year)

# Endpoint to view a specific book by ID
@router.get('/{id}', response_model=schemas.BookWithAuthor, status_code=status.HTTP_200_OK)
def view_book(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return books.view(id, db)

# Endpoint to add a new book
@router.post('/', status_code=status.HTTP_201_CREATED)
def add_book(request: schemas.Book, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return books.add(request, db)

# Endpoint to update an existing book by ID
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_book(id: int, request: schemas.Book, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return books.update(id, request, db)

# Endpoint to delete a book by ID
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return books.destroy(id, db)
