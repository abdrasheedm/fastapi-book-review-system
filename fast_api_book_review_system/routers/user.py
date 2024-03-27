from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, oauth2, database, models, JWT_Token
from sqlalchemy.orm import Session
from ..repository import users
from fastapi.security import OAuth2PasswordRequestForm

# Creating a router for handling authentication-related endpoints
router = APIRouter(
    tags=['Authentication']  # Tags for OpenAPI documentation
)
get_db = database.get_db  # Dependency to get the database session

# Endpoint for user registration
@router.post('/register', response_model=schemas.ShowUser, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return users.register(request, db)

# Endpoint for user login
@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return users.login(request, db)
