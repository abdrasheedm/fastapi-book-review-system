from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, JWT_Token
from ..hashing import Hash

# Function to register a new user
def register(request, db: Session):
    # Check if the email is already taken
    if db.query(models.User).filter(models.User.email == request.email).first():
        raise HTTPException(detail=f"Email {request.email} is already taken. Please try with another one.", status_code=status.HTTP_400_BAD_REQUEST)
    
    # Hash the password and create a new user
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Function to handle user login
def login(request, db: Session):
    # Find the user by email
    user = db.query(models.User).filter(models.User.email == request.username).first()

    # Check if the user exists
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
    
    # Verify the password
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect Password")
    
    # Generate JWT token for authentication
    access_token = JWT_Token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
