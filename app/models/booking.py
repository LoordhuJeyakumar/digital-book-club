import enum
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum as SAEnum
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class BookingStatus(str, enum.Enum):
    """
    The states a booking can be in.
    """
    PENDING = "pending"       # Reserved but not yet picked up
    ACTIVE = "active"         # Currently borrowed
    COMPLETED = "completed"   # Returned to library
    CANCELLED = "cancelled"   # Reservation cancelled before pickup

class BookingModel(Base):
    """
    The 'Checkout Ledger' 📅
    Tracks who has borrowed what book, and for how long.
    """
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    book_id = Column(Integer, ForeignKey("books.id"), nullable=False)
    
    start_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    end_date = Column(DateTime, nullable=True) # Set when returned
    status = Column(SAEnum(BookingStatus), default=BookingStatus.ACTIVE, nullable=False)
    
    # Relationships
    user = relationship("UserModel")
    book = relationship("BookModel")
