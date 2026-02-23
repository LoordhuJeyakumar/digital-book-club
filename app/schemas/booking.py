from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from ..models.booking import BookingStatus

class BookingBase(BaseModel):
    """The core booking request details."""
    book_id: int

class BookingCreate(BookingBase):
    """The form to check out a book."""
    pass

class Booking(BookingBase):
    """The checkout receipt / active booking record."""
    id: int
    user_id: int
    start_date: datetime
    end_date: Optional[datetime] = None
    status: BookingStatus

    model_config = {
        "from_attributes": True
    }
