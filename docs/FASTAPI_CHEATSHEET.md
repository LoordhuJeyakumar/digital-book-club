# ⚡ FastAPI & SQLAlchemy Cheatsheet

A quick reference for our modular Digital Book Club! 🚀

---

### 🚦 Common HTTP Status Codes
| Code | Meaning | Plain English |
| :--- | :--- | :--- |
| **200** | **OK** | "Success!" ✅ |
| **201** | **Created** | "Success! Item added!" ✨ |
| **404** | **Not Found** | "We can't find that." 🕵️‍♂️ |
| **422** | **Validation Error** | "The data you sent is wrong." 🤨 |

---

### 🗄️ Database Operations (SQLAlchemy)
Use these inside your route functions to talk to MySQL:

```python
# 1. Get all items
items = db.query(BookModel).all()

# 2. Find one by ID
item = db.query(BookModel).filter(BookModel.id == 5).first()

# 3. Create a new item
new_item = BookModel(title="1984", author="Orwell")
db.add(new_item)
db.commit()      # Save to database
db.refresh(new_item) # Get the new ID from DB

# 4. Delete an item
db.delete(item)
db.commit()
```

---

### 💉 Dependency Injection
How to get the database session in your routes:

```python
from fastapi import Depends
from sqlalchemy.orm import Session
from ..db import get_db

@router.get("/books")
def my_route(db: Session = Depends(get_db)):
    # Now you can use 'db' here!
```

---

### 🚀 Running the App
Since we moved code to the `app/` folder, run from the root:

```bash
uvicorn app.main:app --reload
```

---

**Pro Tip:** Use `model_config = {"from_attributes": True}` in your Pydantic schemas so they can read data directly from SQLAlchemy models! 🧙‍♂️
