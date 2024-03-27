from passlib.context import CryptContext

# Initialize a CryptContext object for password hashing
pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated='auto')

class Hash():
    # Class for password hashing and verification
    
    @staticmethod
    def bcrypt(password: str):
        # Hash a password using bcrypt
        return pwd_cxt.hash(password)
    
    @staticmethod
    def verify(hashed_password, plain_password):
        # Verify a plain password against a hashed password
        return pwd_cxt.verify(plain_password, hashed_password)
