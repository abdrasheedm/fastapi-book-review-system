from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import JWT_Token 

# OAuth2 password bearer authentication scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Function to get the current user based on the provided token
def get_current_user(data: str = Depends(oauth2_scheme)):
    # Define exception for failed credential validation
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Call the verify_token function from JWT_Token module to verify the token and get user data
    return JWT_Token.verify_token(data, credentials_exception)
