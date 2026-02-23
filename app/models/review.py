from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class ReviewModel(Base):
    """
    The 'Critic's Ledger' ✍️
    Stores ratings and comments left by members for specific books.
    """
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Float, nullable=False) # 1.0 to 5.0
    comment = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships (The 'Direct Line' to who wrote it and what book it's for)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)

    # These allow us to do review.user and review.book in Python
    user = relationship("UserModel")
    book = relationship("BookModel")

class FavoriteModel(Base):
    """
    The 'Personal Bookshelf' ❤️
    A simple list of books that a user has 'Favorited'.
    """
    __tablename__ = "favorites"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"), primary_key=True)

    user = relationship("UserModel")
    book = relationship("BookModel")
