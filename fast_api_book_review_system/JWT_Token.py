from datetime import datetime, timedelta
from jose import JWTError, jwt
from . import schemas 
import os

# Retrieving secret key, algorithm, and token expiration duration from environment variables
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")  # Access token expiration time in minutes

# Function to create an access token
def create_access_token(data: dict):
    # Prepare data to be encoded into the token
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # Set expiration time
    to_encode.update({"exp": expire})  # Update the data with expiration time
    # Encode data into a JWT token using the secret key and algorithm
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Function to verify the access token
def verify_token(token: str, credentials_exception):
    try:
        # Decode the token using the secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")  # Extract email from the token payload
        if email is None:
            # If email is not found in the token payload, raise credentials exception
            raise credentials_exception
        # Create token data object with extracted email
        token_data = schemas.TokenData(email=email)
    except JWTError:
        # If there's an error decoding the token, raise credentials exception
        raise credentials_exception
