from fastapi import APIRouter, Depends, status
from .. import schemas, oauth2, database
from sqlalchemy.orm import Session
from ..repository import authors

# Creating a router for handling author-related endpoints
router = APIRouter(
    tags=['Author'],  # Tags for OpenAPI documentation
    prefix='/author'  # Prefix for all routes defined in this router
)
get_db = database.get_db  # Dependency to get the database session

# Endpoint to view all authors
@router.get('/s/', response_model=list[schemas.Author], status_code=status.HTTP_200_OK)
def view_all_authors(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return authors.get_all(db)

# Endpoint to view a single author by ID
@router.get('/{id}', response_model=schemas.Author, status_code=status.HTTP_200_OK)
def view_author(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return authors.view(id, db)

# Endpoint to add a new author
@router.post('/', status_code=status.HTTP_201_CREATED)
def add_author(request: schemas.Author, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return authors.add(request, db)

# Endpoint to update an existing author by ID
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_author(id, request: schemas.Author, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return authors.update(id, request, db)

# Endpoint to delete an author by ID
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_author(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return authors.destroy(id, db)
