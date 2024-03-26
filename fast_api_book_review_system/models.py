from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .database import Base
from sqlalchemy.orm import relationship


class Book(Base):
    # The database model for books data
    __tablename__ = 'Books'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    publication_year = Column(DateTime)
    author_id = Column(Integer, ForeignKey("Authors.id"), nullable=True)

    author = relationship("Author", back_populates="books")

class Author(Base):
    # The database model for Author data
    __tablename__ = 'Authors'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    date_of_birth = Column(DateTime)
    email = Column(String)
    nationality = Column(String)

    books = relationship("Book", back_populates='author')


class Review(Base):
    # The database model for Author data
    __tablename__ = 'Reviews'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    review = Column(String)
    rating = Column(Integer)

    books = relationship("Book", back_populates='review')