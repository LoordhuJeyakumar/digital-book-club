import enum
from sqlalchemy import Column, Integer, String, Enum as SAEnum
from ..database import Base


class UserRole(str, enum.Enum):
    """Roles define what a user is allowed to do (like job titles at the library)."""
    ADMIN = "admin"
    MEMBER = "member"


class UserModel(Base):
    """
    SQLAlchemy Model for the 'users' table.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(SAEnum(UserRole), default=UserRole.MEMBER, nullable=False)
