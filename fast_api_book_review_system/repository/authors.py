from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models



def get_all(db: Session):
    authors = db.query(models.Author).all()
    if not authors:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data in Author table")
    return authors


def view(id, db:Session):
    author = db.query(models.Author).filter(models.Author.id == id).first()
    if not author:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with id {id} not found")
    return author


def add(request, db:Session):
    new_teacher = models.Author(name=request.name, subject=request.subject)
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

def update(id, request, db:Session):
    author = db.query(models.Author).filter(models.Author.id == id)

    if not author.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with id {id} not found")

    author.update({"name": request.name, "subject" : request.subject})
    db.commit()
    return 'author updated'

def destroy(id:int, db : Session):
    author = db.query(models.Author).filter(models.Author.id == id)
    if not author.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Author with id {id} not found")
    author.delete(synchronize_session=False)
    db.commit()
    return 'Author deleted successfully'