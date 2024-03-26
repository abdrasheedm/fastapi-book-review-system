from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .database import Base
from sqlalchemy.orm import relationship

class Book(Base):
    # Database model for books data
    __tablename__ = 'Books'

    # Book attributes
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    publication_year = Column(Integer)
    author_id = Column(Integer, ForeignKey("Authors.id"), nullable=True)

    # Relationship with Author and Review models
    author = relationship("Author", back_populates="books")
    review = relationship("Review", back_populates="books")

class Author(Base):
    # Database model for author data
    __tablename__ = 'Authors'

    # Author attributes
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date_of_birth = Column(DateTime)
    email = Column(String)
    nationality = Column(String)

    # Relationship with Book model
    books = relationship("Book", back_populates='author')

class Review(Base):
    # Database model for review data
    __tablename__ = 'Reviews'

    # Review attributes
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    review = Column(String)
    rating = Column(Integer)
    book_id = Column(Integer, ForeignKey("Books.id"), nullable=True)

    # Relationship with Book model
    books = relationship("Book", back_populates='review')

class User(Base):
    # Database model for user data
    __tablename__ = 'Users'

    # User attributes
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
