import enum
from sqlalchemy import Column, Integer, String, Enum as SAEnum
from ..database import Base


class UserRole(str, enum.Enum):
    """
    Roles define what a user is allowed to do (like job titles at the library).
    - ADMIN: Can add/delete books and manage the club.
    - MEMBER: Can browse books and (soon) write reviews.
    """
    ADMIN = "admin"
    MEMBER = "member"


class UserModel(Base):
    """
    SQLAlchemy Model for the 'users' table.
    This defines exactly what a user's row looks like in our MySQL database.
    """
    __tablename__ = "users"

    # The unique library card number for the user
    id = Column(Integer, primary_key=True, index=True)
    
    # The person's registered email (must be unique)
    email = Column(String(100), unique=True, index=True, nullable=False)
    
    # The SCRAMBLED (hashed) version of their password - never plain text!
    hashed_password = Column(String(255), nullable=False)
    
    # Their job title in the club (defaults to Member)
    role = Column(SAEnum(UserRole), default=UserRole.MEMBER, nullable=False)
