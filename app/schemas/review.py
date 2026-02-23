from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class ReviewBase(BaseModel):
    """The core info for a review."""
    rating: float = Field(..., ge=1.0, le=5.0, description="Rating from 1 to 5")
    comment: Optional[str] = Field(None, max_length=500)

class ReviewCreate(ReviewBase):
    """The 'Review Form' - what the user fills out."""
    book_id: int

class Review(ReviewBase):
    """The 'Review Display' - what we show back to the user."""
    id: int
    user_id: int
    book_id: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }

class FavoriteBase(BaseModel):
    """The core info for a favorite."""
    book_id: int

class Favorite(FavoriteBase):
    """The favorite status display."""
    user_id: int

    model_config = {
        "from_attributes": True
    }
