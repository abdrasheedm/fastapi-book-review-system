from fastapi import APIRouter, Depends, status
from .. import schemas, oauth2, database
from sqlalchemy.orm import Session
from ..repository import books

router = APIRouter(
    tags=['Books'],
    prefix= '/book'
)
get_db = database.get_db


# BOOKS CRUD

#VIEW ALL BOOKS
@router.get('s/', response_model=list[schemas.Book], status_code=status.HTTP_200_OK)
def view_all_books(db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return books.get_all(db)


#VIEW SPECIFIC BOOK
@router.get('/{id}', response_model=schemas.Book, status_code=status.HTTP_200_OK)
def view_student(id:int, db:Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return books.view(id, db)


# ADD NEW BOOK
@router.post('/', status_code=status.HTTP_201_CREATED)
def add_book(request: schemas.Book ,db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return books.add(request, db)


# UPDATE BOOK
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_book(id:int, request: schemas.Book, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return books.update(id,request,db)


# DELETE BOOK
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id:int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return books.destroy(id, db)








# Assign Book To a Particular Teacher
@router.put('/assign-teacher/{id}', status_code=status.HTTP_202_ACCEPTED)
def assign_teacher(id:int , request:schemas.AddTeacher, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return books.assign_teacher(id, request, db)



#view Book with assigned Teacher
@router.get('/assigned-teacher/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ViewStudentWithTeacher)
def view_student_with_teacher(id:int , db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return books.view_with_teacher(id, db)

