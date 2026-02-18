# 🛠️ PRACTICE_EXERCISES: Day-by-Day Coding Tasks

These exercises are designed to be built **incrementally**. Each day adds one layer of complexity to our Book Club.

---

### 🗓️ Day 1: Hello Book Club!
**Goal:** Get the server running and see a response.
1.  **Task 1:** Create a file named `main.py`.
2.  **Task 2:** Write a basic FastAPI app with a root `@app.get("/")` that returns `{"message": "Welcome to the Digital Book Club!"}`.
3.  **Task 3:** Start the server using `uvicorn main:app --reload` and visit `http://127.0.0.1:8000` in your browser.

### 🗓️ Day 2: The Book Model
**Goal:** Define what a "Book" is in our system.
1.  **Task 1:** Create a list named `books_db` (a simple Python list for now).
2.  **Task 2:** Create a class (Model) for a Book with attributes: `id`, `title`, `author`, and `pages`.
3.  **Task 3:** Create a GET endpoint `/books` that returns your `books_db` list.

### 🗓️ Day 3: Librarian Actions (CRUD)
**Goal:** Add and delete books from our list.
1.  **Task 1:** Create a POST endpoint `/books` that takes a new book and appends it to `books_db`.
2.  **Task 2:** Create a DELETE endpoint `/books/{book_id}` that finds a book by its ID and removes it.
3.  **Task 3:** Use the `/docs` page (Swagger) to test adding a book and then deleting it.

### 🗓️ Day 4: The VIP Section (Auth)
**Goal:** Protect our "Delete" action so only authorized users can do it.
1.  **Task 1:** Create a simple "Login" route that returns a fake token.
2.  **Task 2:** Modify the DELETE endpoint to check if a token is provided in the header.
3.  **Task 3:** Try to delete a book *without* a token and see if you get a `401 Unauthorized` error.

### 🗓️ Day 5: Making it Real
**Goal:** Connect to MySQL and polish.
1.  **Task 1:** Replace the `books_db` list with actual database calls using SQLAlchemy.
2.  **Task 2:** Add a "Query Parameter" to the `/books` endpoint so you can search by author (e.g., `/books?author=Tolkien`).
3.  **Task 3:** Refactor your code: move the models to `models.py` and the routes to `routes.py`.

---

**Teacher Tip:** Encourage students to **"Save and Refresh"** after every single step. Small wins build big confidence! 🏆
