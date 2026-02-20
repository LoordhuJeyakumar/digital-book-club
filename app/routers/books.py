from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from ..schemas.book import Book, BookCreate, BookUpdate
from ..models.book import BookModel
from ..database import get_db
from ..models.user import UserRole, UserModel
from .deps import RoleChecker

# --- BOOKS ROUTER (MySQL Version) ---

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

# Admin utility
require_admin = RoleChecker([UserRole.ADMIN])

@router.get("/", response_model=List[Book])
def get_books(db: Session = Depends(get_db)):
    """Get all books from the MySQL database (The Digital Archives)"""
    return db.query(BookModel).all()

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Get a specific book by ID"""
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found"
        )
    return book

@router.post("/", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(
    book: BookCreate, 
    db: Session = Depends(get_db),
    admin: UserModel = Depends(require_admin)
):
    """Add a new book to the database (Admin Only)"""
    try:
        new_book = BookModel(**book.dict())
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error creating book: {str(e)}"
        )

@router.put("/{book_id}", response_model=Book)
def update_book(
    book_id: int, 
    updated_fields: BookUpdate, 
    db: Session = Depends(get_db),
    admin: UserModel = Depends(require_admin)
):
    """Update an existing book in the database (Admin Only)"""
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found"
        )
    
    update_data = updated_fields.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)
    
    db.commit()
    db.refresh(db_book)
    return db_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(
    book_id: int, 
    db: Session = Depends(get_db),
    admin: UserModel = Depends(require_admin)
):
    """Remove a book from the database (Admin Only)"""
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found"
        )
    
    db.delete(db_book)
    db.commit()
