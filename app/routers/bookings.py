from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime

from ..database import get_db
from ..models.booking import BookingModel, BookingStatus
from ..models.book import BookModel
from ..schemas.booking import Booking, BookingCreate
from .deps import get_current_user
from ..models.user import UserModel

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings & Borrowing"]
)

@router.post("/", response_model=Booking, status_code=status.HTTP_201_CREATED)
def borrow_book(
    booking: BookingCreate, 
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    """
    Check out a book! 📅
    - Checks if the book exists.
    - Checks if the book is available.
    - Marks the book as unavailable and records the checkout time.
    """
    book = db.query(BookModel).filter(BookModel.id == booking.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
        
    if not book.is_available:
        raise HTTPException(status_code=400, detail="This book is currently checked out by someone else.")
    
    # 1. Create the booking record
    new_booking = BookingModel(
        user_id=current_user.id,
        book_id=book.id,
        status=BookingStatus.ACTIVE
    )
    db.add(new_booking)
    
    # 2. Take the book off the shelf
    book.is_available = False
    
    # Commit BOTH changes together (The Handshake 🤝)
    db.commit()
    db.refresh(new_booking)
    return new_booking

@router.post("/{booking_id}/return", response_model=Booking)
def return_book(
    booking_id: int, 
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    """
    Return a borrowed book. 📚
    - Verifies the user owns this active booking.
    - Marks the booking as COMPLETED.
    - Puts the book back on the shelf (is_available = True).
    """
    booking = db.query(BookingModel).filter(BookingModel.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
        
    if booking.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="You can only return books you checked out.")
        
    if booking.status != BookingStatus.ACTIVE:
        raise HTTPException(status_code=400, detail="This booking is not active (might be already returned).")

    # 1. Update the booking
    booking.status = BookingStatus.COMPLETED
    booking.end_date = datetime.utcnow()
    
    # 2. Put the book back on the shelf
    book = db.query(BookModel).filter(BookModel.id == booking.book_id).first()
    if book:
        book.is_available = True
        
    db.commit()
    db.refresh(booking)
    return booking

@router.get("/me", response_model=List[Booking])
def my_bookings(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    """See all the books you've checked out or returned."""
    return db.query(BookingModel).filter(BookingModel.user_id == current_user.id).all()
