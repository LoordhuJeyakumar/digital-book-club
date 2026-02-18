# 📖 THEORY_GUIDE: What is a REST API?

To understand APIs, let's imagine a **City Library**. 🏛️

---

### 1. Client vs. Server (The Visitor & The Librarian) 👤 vs. 🧙‍♂️
*   **The Client:** Imagine you are a visitor at the library. You want to borrow a book, but you aren't allowed to walk into the archives yourself. You must ask for help.
*   **The Server:** The **Librarian** is the Server. They sit behind a desk (the API) and have access to all the books (the Database). 
*   **The Interaction:** You (Client) send a **Request** to the Librarian (Server), and they send back a **Response** (either the book or an error message like "Sorry, we don't have that!").

### 2. JSON: The Language of the Web 📜
Since you and the Librarian might speak different languages, you use a **Standard Form** to communicate. 
*   **JSON** is like a neatly filled-out index card. It's easy for humans to read and easy for computers to process.
*   **Example of a "Book" in JSON:**
    ```json
    {
      "id": 101,
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "status": "Available"
    }
    ```

### 3. The 4 Main HTTP Methods (What can you ask the Librarian?) 🛠️
When you go to the Librarian's desk, you usually want to do one of four things:
1.  **GET:** "Can I **see** the list of all mystery books?" (Retrieving data).
2.  **POST:** "I have a **new** book to donate to the library." (Creating new data).
3.  **PUT:** "I noticed a typo in this book's title; can you **fix** it?" (Updating existing data).
4.  **DELETE:** "This book is too old/damaged; please **remove** it from the shelf." (Removing data).

### 4. Path vs. Query Parameters (Finding the Book) 🔍
*   **Path Parameters:** These are like the **Call Number** on a book's spine. They identify a *specific* item.
    *   *Example:* `/books/101` (Takes you directly to book #101).
*   **Query Parameters:** These are like **Search Filters**. They help you find a *subset* of items.
    *   *Example:* `/books?genre=mystery` (Asks the librarian to show only mystery books).

---

**Summary:** An API is just a set of rules that lets your application (The Visitor) talk to a database (The Library Shelves) safely and organized! 🌟
