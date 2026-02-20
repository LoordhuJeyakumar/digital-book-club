# 📚 Digital Book Club API: 5-Day Curriculum

Welcome to the **Digital Book Club API** project! 🚀 Over the next 5 days, we'll build a professional backend from scratch. 

### 🗓️ Day 1: The Basics (Hello World & Setup)
*   **The Big Picture:** Understanding Client-Server architecture.
*   **The Toolbox:** Installing Python, FastAPI, and Uvicorn.
*   **First Steps:** Creating your first API endpoint.
*   **Activity:** Run "Hello Book Club!" on your browser.

### 🗓️ Day 2: In-Memory CRUD (The Digital Librarian's List)
*   **Modeling:** Using **Pydantic** to define what a **Book** looks like.
*   **The 4 Actions:** Implementing **C**reate, **R**ead, **U**pdate, and **D**elete using a simple Python list.
*   **Validation:** Ensuring we don't allow "broken" data into our list.

### 🗓️ Day 3: Models & The Database (The Library's Filing Cabinet)
*   **Persistence:** Understanding why we need a real database.
*   **MySQL:** Connecting our app to a real MySQL database.
*   **SQLAlchemy:** Refactoring our in-memory code to store data permanently.

### 🗓️ Day 4: Security & Authentication (The VIP Membership)
*   **Signing Up:** Creating user accounts.
*   **JWT (JSON Web Tokens):** Issuing "digital ID cards" for users.
*   **OAuh2:** Handling secure logins.
*   **RBAC:** Deciding who can delete a book (Admin) vs. just reading it (User).
*   **Activity:** Lock down your API so only club members can enter!

### 🗓️ Day 5: The Reviewer's Bench (Engagement)
*   **Reviews & Ratings:** Allowing members to share their thoughts.
*   **Favorites:** Bookmarking books for later.
*   **Ownership:** Ensuring only you can edit your own reviews.

### 🗓️ Day 6: The Booking Ledger (Business Logic)
*   **Availability:** Tracking which books are on the shelf and which are borrowed.
*   **Reservations:** Creating a system to "Book" a book for a specific time.
*   **Relationships:** Linking Users to Books via a third "Booking" table.

### 🗓️ Day 7: The Global Passport (Social Login)
*   **OAuth2:** "Login with Google/GitHub".
*   **Hybrid Auth:** Supporting both local passwords and social logins.
*   **External APIs:** Talking to Google's servers to verify identities.

### 🗓️ Day 8: Deployment & Documentation (Show the World)
*   **Swagger UI:** FastAPI's built-in interactive documentation.
*   **Final Audit:** Cleaning up code and final end-to-end testing.
*   **Showcase:** Share your professional, multi-feature API! 🌟
