from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models
from typing import Optional
from .. import utils

# Function to get all reviews, with an optional filter for book title
def get_all(db: Session, book_title: Optional[str] = None):
    query = db.query(models.Review)

    if book_title:
        # Joining with Book table and filtering by book title
        query = query.join(models.Review.books).filter(models.Book.title == book_title)
    
    reviews = query.all()
    
    if not reviews:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data in Review table")
    return reviews

# Function to view a review by ID
def view(id, db: Session):
    review = db.query(models.Review).filter(models.Review.id == id).first()
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Review with id {id} not found")
    return review

# Function to add a new review
def add(request, db: Session, email:str):
    book = db.query(models.Book).filter(models.Book.id == request.book_id)
    if not book.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id {request.book_id} not found")
    new_review = models.Review(title=request.title, review=request.review, rating=request.rating, book_id=request.book_id)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    subject = "Review added"
    message = f"Hi {email}, You have added a new review for the book {book.title} as {request.review}"
    utils.sent_email(email, subject, message)
    return new_review

# Function to update an existing review by ID
def update(id, request, db: Session):
    review = db.query(models.Review).filter(models.Review.id == id)

    if not review.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Review with id {id} not found")

    review.update({"title": request.title, "review": request.review, "rating": request.rating, "book_id": request.book_id})
    db.commit()
    return 'review updated'

# Function to delete a review by ID
def destroy(id, db):
    review = db.query(models.Review).filter(models.Review.id == id)
    if not review.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Review with id {id} not found")
    review.delete(synchronize_session=False)
    db.commit()
    return 'Review deleted successfully'
