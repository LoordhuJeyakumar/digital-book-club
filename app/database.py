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
