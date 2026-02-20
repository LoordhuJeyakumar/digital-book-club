import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# The "Filing Cabinet Location" (Connection URL)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

# Create the Engine (The person who opens the cabinet)
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create the SessionLocal (The notebook the librarian uses to take notes)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our Models (The template for every drawer)
Base = declarative_base()

# --- GET_DB DEPENDENCY ---
# This is our "Librarian's Session". 
# It opens the cabinet, lets us work, and CLOSES it when we are done.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
