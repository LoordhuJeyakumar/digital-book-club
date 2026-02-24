# 📚 Digital Book Club API

Welcome to the Digital Book Club API! This project is a comprehensive, production-ready backend built with **FastAPI**. It is designed as a learning resource and a fully functional API, covering everything from basic CRUD operations to advanced Hybrid Authentication.

## ✨ Features

- **Robust Architecture**: Modular folder structure (`routers/`, `models/`, `schemas/`) for scalable development.
- **Relational Database**: Fully integrated MySQL database using **SQLAlchemy** ORM.
- **Pydantic Validation**: Strict data validation ensuring clean inputs and outputs.
- **Hybrid Authentication**: Support for both traditional Email/Password login (hashed via `bcrypt`) AND **Google OAuth2** Social Login.
- **Role-Based Access Control (RBAC)**: Distinct permissions for `Admin` vs `Member` users.
- **The Booking System**: Complex state management to "checkout" and "return" books.
- **Social Engagement**: Endpoints to leave ratings, write reviews, and favorite books, complete with Ownership Protection (users can only edit their own content).

## 📖 Documentation

This project contains extensive "Teacher Mode" documentation designed to help you understand *why* we built it this way.

*   👉 **[The Complete API Reference Guide](docs/COMPLETE_GUIDE.md)**: Start here! This details every endpoint, the database schema, and the security flow.
*   👉 **[The Learning Curriculum](docs/CURRICULUM.md)**: An 8-day suggested learning path.
*   👉 **[Technical Deep Dive](docs/TECH_DEEP_DIVE.md)**: An explanation of the architecture, workflow, and deprecated syntax choices.
*   👉 **[Google OAuth Setup Guard](docs/OAUTH_SETUP.md)**: A step-by-step guide to generating your Social Login credentials.
*   👉 **[Free Deployment Guide](docs/DEPLOYMENT.md)**: Learn how to launch your API and Database to the internet for free using Render.com!
*   👉 **[FastAPI Cheatsheet](docs/FASTAPI_CHEATSHEET.md)**: Quick reference for decorators and status codes.


## 🚀 Getting Started

1.  **Clone the repository** and navigate to the project folder.
2.  **Set up your virtual environment**:
    ```bash
    python3 -m venv fastapi-env
    source fastapi-env/bin/activate
    ```
3.  **Install requirements**:
    *(Ensure you have installed `fastapi`, `uvicorn`, `sqlalchemy`, `pymysql`, `passlib[bcrypt]`, `python-jose[cryptography]`, `httpx`, and `authlib`)*
4.  **Configure Environment Variables**: Create a `.env` file in the root directory (see `.env` for the required keys, including your `DATABASE_URL` and `GOOGLE_CLIENT_ID`).
5.  **Run the Server**:
    ```bash
    python -m uvicorn app.main:app --reload
    ```
6.  **Explore the API**: Open your browser and navigate to the auto-generated Swagger UI at `http://127.0.0.1:8000/docs`.

---
*Built with ❤️ for learners everywhere.*
