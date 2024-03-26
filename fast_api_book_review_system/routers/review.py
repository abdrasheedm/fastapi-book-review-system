from fastapi import APIRouter, Depends, status
from .. import schemas, oauth2, database
from sqlalchemy.orm import Session
from ..repository import reviews
from typing import Optional

# Creating a router for handling review-related endpoints
router = APIRouter(
    tags=['Reviews'],  # Tags for OpenAPI documentation
    prefix='/review'  # Prefix for all routes defined in this router
)
get_db = database.get_db  # Dependency to get the database session

# Endpoint to view all reviews
@router.get('/s/', response_model=list[schemas.ReviewWithBook], status_code=status.HTTP_200_OK)
def view_all_reviews(db: Session = Depends(get_db), book_title: Optional[str] = None, current_user: schemas.User = Depends(oauth2.get_current_user)):
    return reviews.get_all(db, book_title)

# Endpoint to view a specific review by ID
@router.get('/{id}', response_model=schemas.ReviewWithBook, status_code=status.HTTP_200_OK)
def view_review(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return reviews.view(id, db)

# Endpoint to add a new review
@router.post('/', status_code=status.HTTP_201_CREATED)
def add_review(request: schemas.Review, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return reviews.add(request, db, current_user.email)

# Endpoint to update an existing review by ID
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_review(id: int, request: schemas.Review, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return reviews.update(id, request, db)

# Endpoint to delete a review by ID
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_review(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return reviews.destroy(id, db)
