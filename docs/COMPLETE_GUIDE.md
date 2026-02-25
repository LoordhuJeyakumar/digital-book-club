# 📚 Digital Book Club API: The Complete Guide

Welcome to the **Complete Guide** for the Digital Book Club API! This document is your master reference for everything we've built. It details the architecture, the database models, and every single endpoint available in the system.

---

## 🏗️ Architecture & Stack
This project is built using modern Python web development standards:
*   **Framework**: [FastAPI](https://fastapi.tiangolo.com/) (Fast, asynchronous, auto-documenting)
*   **Database**: MySQL (Robust, relational data storage)
*   **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) (Translates Python code to SQL queries)
*   **Data Validation**: [Pydantic v2](https://docs.pydantic.dev/latest/) (Ensures incoming data is perfectly formatted)
*   **Authentication**: JWT (JSON Web Tokens) & OAuth2 (Google)
*   **Security**: bcrypt (Password hashing), Role-Based Access Control (RBAC)

---

## 🗄️ Database Models (The Filing Cabinet)

We have four main tables in our database, fully linked via foreign keys.

### 1. `UserModel` (`users` table)
*   **`id`**: Primary Key (Integer)
*   **`email`**: Unique contact information (String)
*   **`hashed_password`**: Scrambled password (Nullable for Google users)
*   **`role`**: `ADMIN` or `MEMBER`
*   **`oauth_provider`**: "google", "github", or Null.
*   **`oauth_id`**: The unique ID string from the provider.

### 2. `BookModel` (`books` table)
*   **`id`**: Primary Key (Integer)
*   **`title`** & **`author`**: Strings
*   **`pages`**: Integer
*   **`is_available`**: Boolean (True if on the shelf, False if checked out)

### 3. `ReviewModel` (`reviews` table)
*   **`id`**: Primary Key (Integer)
*   **`rating`**: Float (1.0 to 5.0)
*   **`comment`**: Text review
*   **Relationships**: `user_id` (Who wrote it), `book_id` (Which book)

### 4. `BookingModel` (`bookings` table)
*   **`id`**: Primary Key (Integer)
*   **`start_date`** & **`end_date`**: Timestamps
*   **`status`**: PENDING, ACTIVE, COMPLETED, CANCELLED
*   **Relationships**: `user_id` (Who borrowed it), `book_id` (Which book)

---

## 🌐 API Endpoints Reference

### 🔐 Authentication (`/auth`)
*   `POST /auth/register`: Create a new account.
*   `POST /auth/login`: Standard username/password login. Returns a standard `Bearer` token.
*   `GET /auth/google/login`: Redirects the user to the Google Consent Screen.
*   `GET /auth/google/callback`: Re-entry point from Google. Creates/Merges the account and issues a standard `Bearer` token.

### 📚 Book Management (`/books`)
*   `GET /books/`: Get a list of all books. (Public)
*   `GET /books/{id}`: Get a single book. (Public)
*   `POST /books/`: Add a new book (**Admin Only**).
*   `PUT /books/{id}`: Edit a book (**Admin Only**).
*   `DELETE /books/{id}`: Remove a book (**Admin Only**).

### ✍️ Reviews & Engagement (`/reviews`)
*   `POST /reviews/`: Rate a book and leave a comment. (Requires Login)
*   `GET /reviews/book/{id}`: Read all reviews for a specific book. (Public)
*   `DELETE /reviews/{id}`: Delete a review (**Requires Login AND Ownership** - You can only delete your own!).
*   `POST /reviews/favorite/{id}`: Toggle a book in/out of your personal favorites list. (Requires Login)

### 📅 The Booking Ledger (`/bookings`)
*   `POST /bookings/`: Check out a book. Marks it as `is_available = False`. (Requires Login)
*   `POST /bookings/{id}/return`: Return a book. Marks it as `is_available = True`. (Requires Login)
*   `GET /bookings/me`: View your personal checkout history. (Requires Login)

---

## 🛡️ Security Features Explained

1.  **JWT (JSON Web Tokens)**: When a user logs in (via password or Google), we give them a signed string. They pass this string in the `Authorization: Bearer <TOKEN>` header for every future request. 
2.  **`get_current_user` Dependency**: This function runs *before* protected routes. It decrypts the JWT, ensures it's valid, looks up the user in the database, and injects that `User` object directly into the route function.
3.  **RoleChecker (RBAC)**: A custom class that acts as a bouncer. Used on the Book creation/deletion routes, it checks `user.role == "admin"`. If not, it throws a `403 Forbidden` error.
4.  **Ownership Logic**: Seen in the Review system. Before deleting a review, code explicitly checks `if review.user_id != active_user.id`.
5.  **CORS (Cross-Origin Resource Sharing)**: This is the "Security Guard" in `main.py` that allows your API to talk to frontends (like React or Vue) running on different URLs. Without this, the browser would block the connection for security reasons.

---

## 🚀 How to Run the Project

1.  **Activate the Virtual Environment**:
    ```bash
    source fastapi-env/bin/activate
    ```
2.  **Start MySQL**: Ensure your local XAMPP/MySQL server is running.
3.  **Start Uvicorn (The Server)**:
    ```bash
    python -m uvicorn app.main:app --reload
    ```
4.  **View Swagger UI**: Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive documentation and play with the API!
