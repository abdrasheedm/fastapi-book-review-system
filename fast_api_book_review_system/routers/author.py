from fastapi import APIRouter, Depends,status
from .. import schemas, oauth2, database
from sqlalchemy.orm import Session
from ..repository import authors

router = APIRouter(
    tags=['Author'],
    prefix= '/author'
)
get_db = database.get_db

# VIEW ALL AUTHORS
@router.get('s/', response_model=list[schemas.Author], status_code=status.HTTP_200_OK)
def view_all_authors(db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return authors.get_all(db)

# VIEW SINGLE AUTHOR
@router.get('/{id}', response_model=schemas.Author, status_code=status.HTTP_200_OK)
def view_author(id:int, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return authors.view(id, db)

# ADD NEW AUTHOR
@router.post('/', status_code=status.HTTP_201_CREATED)
def add_author(request: schemas.Author ,db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return authors.add(request, db)

# UPDATE A AUTHOR
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_author(id, request: schemas.Author, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return authors.update(id, request, db)

# DELETE A AUTHOR
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_author(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return authors.destroy(id, db)