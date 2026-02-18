# ⚡ FastAPI Cheatsheet

A quick reference for building our Digital Book Club! 🚀

---

### 🚦 Common HTTP Status Codes
Think of these as **Status Reports** from the Librarian:

| Code | Meaning | Plain English |
| :--- | :--- | :--- |
| **200** | **OK** | "Here is the book you asked for!" ✅ |
| **201** | **Created** | "Success! I've added the new book to the shelf!" ✨ |
| **400** | **Bad Request** | "Your request is confusing; please check the form again." 🤨 |
| **401** | **Unauthorized** | "You need a library card (login) to do this!" 🔑 |
| **404** | **Not Found** | "We checked everywhere, but that book doesn't exist." 🕵️‍♂️ |
| **500** | **Internal Server Error** | "Oops! The librarian tripped. Something went wrong on our end." 🔥 |

---

### 💻 FastAPI "Decorator" Syntax
Decorators tell FastAPI which **URL** and which **Action** should trigger your code.

```python
from fastapi import FastAPI

app = FastAPI()

# 1. GET: Read data
@app.get("/books")
def get_all_books():
    return {"message": "Listing all books"}

# 2. POST: Create data
@app.post("/books")
def add_book():
    return {"message": "Book added!"}

# 3. GET with ID (Path Parameter)
@app.get("/books/{book_id}")
def get_one_book(book_id: int):
    return {"book_id": book_id}
```

---

### 🚀 Starting Your Server
To bring your API to life, use the **Uvicorn** command in your terminal:

```bash
# Basic command
uvicorn main:app --reload
```
*   `main`: The name of your Python file (`main.py`).
*   `app`: The name of the FastAPI object inside that file.
*   `--reload`: **MAGIC!** The server will automatically restart every time you save your code. 🧙‍♂️

---

**Tip:** Once your server is running, visit `http://127.0.0.1:8000/docs` to see your interactive documentation! 📄✨
