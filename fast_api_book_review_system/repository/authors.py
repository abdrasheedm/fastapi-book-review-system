from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models

# Function to get all authors
def get_all(db: Session):
    authors = db.query(models.Author).all()
    if not authors:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data in Author table")
    return authors

# Function to view an author by ID
def view(id, db: Session):
    author = db.query(models.Author).filter(models.Author.id == id).first()
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with id {id} not found")
    return author

# Function to add a new author
def add(request, db: Session):
    new_author = models.Author(name=request.name, date_of_birth=request.date_of_birth, email=request.email, nationality=request.nationality)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

# Function to update an existing author by ID
def update(id, request, db: Session):
    author = db.query(models.Author).filter(models.Author.id == id)

    if not author.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with id {id} not found")

    author.update({"name": request.name, "date_of_birth": request.date_of_birth, "email": request.email, "nationality": request.nationality})
    db.commit()
    return 'author updated'

# Function to delete an author by ID
def destroy(id: int, db: Session):
    author = db.query(models.Author).filter(models.Author.id == id)
    if not author.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with id {id} not found")
    author.delete(synchronize_session=False)
    db.commit()
    return 'Author deleted successfully'
