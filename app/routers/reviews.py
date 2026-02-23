from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models.review import ReviewModel, FavoriteModel
from ..models.book import BookModel
from ..schemas.review import Review, ReviewCreate, Favorite
from .deps import get_current_user
from ..models.user import UserModel

router = APIRouter(
    prefix="/reviews",
    tags=["Reviews & Favorites"]
)

@router.post("/", response_model=Review, status_code=status.HTTP_201_CREATED)
def post_review(
    review: ReviewCreate, 
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    """
    Share your thoughts! ✍️
    Only registered members can leave a review.
    """
    # 1. Does the book even exist?
    book = db.query(BookModel).filter(BookModel.id == review.book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    # 2. Create the review
    new_review = ReviewModel(
        **review.dict(),
        user_id=current_user.id
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review

@router.get("/book/{book_id}", response_model=List[Review])
def get_book_reviews(book_id: int, db: Session = Depends(get_db)):
    """Get all reviews for a specific book."""
    return db.query(ReviewModel).filter(ReviewModel.book_id == book_id).all()

@router.delete("/{review_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_review(
    review_id: int, 
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    """
    Remove a review. 🗑️
    Rules: You can ONLY delete your own reviews.
    """
    review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    
    # Ownership Check! 💂‍♂️
    if review.user_id != current_user.id:
        raise HTTPException(
            status_code=403, 
            detail="You are not allowed to delete someone else's review!"
        )
    
    db.delete(review)
    db.commit()
    return

@router.post("/favorite/{book_id}", response_model=Favorite)
def toggle_favorite(
    book_id: int, 
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    """ ❤️ Add or Remove a book from your favorites. """
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    existing_fav = db.query(FavoriteModel).filter(
        FavoriteModel.user_id == current_user.id,
        FavoriteModel.book_id == book_id
    ).first()

    if existing_fav:
        db.delete(existing_fav)
        db.commit()
        raise HTTPException(status_code=200, detail="Removed from favorites")
    
    new_fav = FavoriteModel(user_id=current_user.id, book_id=book_id)
    db.add(new_fav)
    db.commit()
    db.refresh(new_fav)
    return new_fav
