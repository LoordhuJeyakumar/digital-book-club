from fastapi import FastAPI
from .routers import books, auth, reviews
from .database import engine, Base
from .models import book, user, review  # Ensure models are imported for create_all

# Create the tables (The "Librarian" building the shelves)
# In professional apps, we use 'Alembic' for this, but for now, this is perfect!
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Digital Book Club API (Modular)",
    description="A professional, modular API base for the Book Club.",
    version="3.0.0"
)

# Connect our Routers (The sections of the library)
app.include_router(auth.router)
app.include_router(books.router)
app.include_router(reviews.router)

@app.get("/", tags=["General"])
def read_root():
    """Welcome message for the API"""
    return {
        "message": "Welcome to the Digital Book Club API (Modular Version)! 📚",
        "instructions": "Go to /docs to see the interactive documentation."
    }

if __name__ == "__main__":
    import uvicorn
    # Note: When running from this file, we use "app.main:app" 
    # so that imports within the app/ folder resolve correctly.
    uvicorn.run("app.main:app", host="127.0.0.1", port=3333, reload=True)
