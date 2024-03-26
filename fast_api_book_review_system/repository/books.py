from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models



def get_all(db: Session):
    books = db.query(models.Book).all()
    if not books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data in Book table")
    return books


def view(id, db:Session):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found")
    return book


def add(request, db:Session):
    new_book = models.Book(title=request.title, publication_year=request.publication_year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def update(id, request, db:Session):
    book = db.query(models.Book).filter(models.Book.id == id)

    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found")

    book.update({"name": request.name, "department" : request.department})
    db.commit()
    return 'book updated'


def destroy(id, db):
    book = db.query(models.Book).filter(models.Book.id == id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found")
    book.delete(synchronize_session=False)
    db.commit()
    return 'Book deleted successfully'


def assign_teacher(id, request, db: Session):
    book = db.query(models.Book).filter(models.Book.id == id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found")
    author = db.query(models.Author).filter(models.Author.id == request.author_id)
    if not author.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with id {request.author_id} not found")
    book.update({"author_id": request.author_id})
    db.commit()
    return 'Author assigned'


def view_with_teacher(id, db):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {id} not found")
    if not book.author_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author not assigned for this Book")
    return book