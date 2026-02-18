from .database import SessionLocal

# --- GET_DB DEPENDENCY ---
# This is our "Librarian's Session". 
# It opens the cabinet, lets us work, and CLOSES it when we are done.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
