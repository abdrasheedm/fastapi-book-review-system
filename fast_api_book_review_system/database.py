from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for SQLite
SQL_ALCHEMY_DATABASE_URL = 'sqlite:///./book.db'

# Create the database engine
engine = create_engine(SQL_ALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session local class
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Create a base class for declarative data models
Base = declarative_base()

# Function to get a database session
async def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
