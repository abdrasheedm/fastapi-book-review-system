from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models
from typing import Optional
from fastapi import BackgroundTasks

# Function to get all books, with optional filters for author name and publication year
def get_all(db: Session, author_name: Optional[str] = None, publication_year: Optional[int] = None):
    query = db.query(models.Book)

    if author_name:
        # Joining with Author table and filtering by author name
        query = query.join(models.Book.author).filter(models.Author.name == author_name)
    
    if publication_year:
        # Filtering by publication year
        query = query.filter(models.Book.publication_year == publication_year)
    
    books = query.all()
    
    if not books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data in Book table")
    return books

# Function to view a book by ID
def view(id, db: Session):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found")
    return book

# Function to add a new book
def add(request, db: Session):
    author = db.query(models.Author).filter(models.Author.id == request.author_id)
    if not author.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with id {request.author_id} not found")
    new_book = models.Book(title=request.title, publication_year=request.publication_year, author_id=request.author_id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# Function to update an existing book by ID
def update(id, request, db: Session):
    book = db.query(models.Book).filter(models.Book.id == id)

    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found")

    book.update({"title": request.title, "publication_year": request.publication_year, "author_id": request.author_id})
    db.commit()
    return 'book updated'

# Function to delete a book by ID
def destroy(id, db):
    book = db.query(models.Book).filter(models.Book.id == id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found")
    book.delete(synchronize_session=False)
    db.commit()
    return 'Book deleted successfully'
