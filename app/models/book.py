from sqlalchemy import Column, Integer, String, Boolean
from ..database import Base

class BookModel(Base):
    """
    SQLAlchemy Model for the 'books' table.
    This is what the database table looks like.
    """
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    pages = Column(Integer)
    is_read = Column(Boolean, default=False)
    
    # 📚 New: Is the book currently on the shelf?
    is_available = Column(Boolean, default=True, nullable=False)
