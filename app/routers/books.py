from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from ..schemas.book import Book, BookCreate, BookUpdate
from ..models.book import BookModel
from ..db import get_db

# --- BOOKS ROUTER (MySQL Version) ---

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

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
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Add a new book to the database"""
    new_book = BookModel(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, updated_fields: BookUpdate, db: Session = Depends(get_db)):
    """Update an existing book in the database"""
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found"
        )
    
    # Update only the fields that were provided
    update_data = updated_fields.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)
    
    db.commit()
    db.refresh(db_book)
    return db_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Remove a book from the database"""
    db_book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not db_book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {book_id} not found"
        )
    
    db.delete(db_book)
    db.commit()
    return
