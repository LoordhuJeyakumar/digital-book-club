# FastAPI Complete Learning Guide

A comprehensive guide to learning and teaching FastAPI - from basic concepts to advanced implementation, covering theory, REST API fundamentals, and practical examples.

---

## 📚 Table of Contents

### Part 1: Foundations

- What is FastAPI?
- Why FastAPI?
- How FastAPI Works
- Environment Setup

### Part 2: REST API Theory

- Understanding REST Architecture
- HTTP Methods & Status Codes
- API Design Principles

### Part 3: FastAPI Basics

- Your First API
- Path Parameters
- Query Parameters
- Request Body

### Part 4: Intermediate Concepts

- Data Validation with Pydantic
- Response Models
- Error Handling
- Dependencies

### Part 5: Advanced Topics

- Database Integration
- Authentication & Security
- Background Tasks
- WebSockets

### Part 6: Best Practices & Deployment

---

## Part 1: Foundations

### 🎯 What is FastAPI?

FastAPI is a **modern, fast (high-performance) web framework** for building APIs with Python 3.7+ based on standard Python type hints.

**Key Characteristics:**

- Built on top of Starlette (for web routing) and Pydantic (for data validation)
- Automatic interactive API documentation (Swagger UI and ReDoc)
- Based on OpenAPI and JSON Schema standards
- Asynchronous support out of the box

---

### 💡 Why FastAPI?

<aside>
⚡

**Performance**: One of the fastest Python frameworks available, on par with NodeJS and Go.

</aside>

**Advantages:**

1. **Fast to Code**: Increase development speed by 200-300%
2. **Fewer Bugs**: Reduce human-induced errors by about 40%
3. **Intuitive**: Great editor support with auto-completion everywhere
4. **Easy**: Designed to be easy to learn and use
5. **Short**: Minimize code duplication
6. **Robust**: Production-ready code with automatic interactive documentation
7. **Standards-based**: Based on OpenAPI and JSON Schema

**Comparison with Other Frameworks:**

| Feature | FastAPI | Flask | Django |
| --- | --- | --- | --- |
| Performance | Very High | Medium | Medium |
| Async Support | Native | Limited | Available |
| Auto Documentation | Yes | No | No |
| Type Validation | Automatic | Manual | Manual |
| Learning Curve | Easy | Easy | Moderate |

---

### ⚙️ How FastAPI Works

**Architecture Overview:**

1. **Type Hints**: Python type hints are used for data validation and serialization
2. **Pydantic Models**: Validate request/response data automatically
3. **Starlette**: Handles ASGI web routing and requests
4. **Uvicorn**: ASGI server that runs your application
5. **OpenAPI**: Generates automatic interactive documentation

**Request Flow:**

```
Client Request → Uvicorn (ASGI Server) → Starlette (Routing) 
→ FastAPI (Validation) → Your Code → Response
```

---

### 🛠️ Environment Setup

**Prerequisites:**

- Python 3.7 or higher
- pip (Python package manager)
- Code editor (VS Code, PyCharm, etc.)

**Installation Steps:**

```bash
# Create a virtual environment
python -m venv fastapi-env

# Activate virtual environment
# On Windows:
fastapi-env\Scripts\activate
# On macOS/Linux:
source fastapi-env/bin/activate

# Install FastAPI
pip install fastapi

# Install Uvicorn (ASGI server)
pip install "uvicorn[standard]"

# Optional: Install additional dependencies
pip install python-multipart  # For form data
pip install python-jose  # For JWT tokens
pip install passlib  # For password hashing
pip install sqlalchemy  # For database ORM
```

**Verify Installation:**

```bash
python -c "import fastapi; print(fastapi.__version__)"
```

**Managing Dependencies with requirements.txt:**

A `requirements.txt` file lists all Python packages your project needs. This makes it easy for others (or yourself on a different machine) to install all dependencies at once.

**Create requirements.txt:**

```bash
# After installing your packages, freeze them to a file
pip freeze > requirements.txt
```

**Example requirements.txt:**

```
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
python-multipart==0.0.6
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
sqlalchemy==2.0.23
alembic==1.12.1
```

**Install from requirements.txt:**

```bash
# Install all dependencies from the file
pip install -r requirements.txt
```

**Best Practices:**

- Always use a virtual environment before creating requirements.txt
- Update requirements.txt when you add new packages
- Consider using `pip freeze > requirements.txt` to capture exact versions
- For development dependencies, create a separate `requirements-dev.txt`

**Development vs Production:**

```bash
# requirements.txt (production)
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23

# requirements-dev.txt (development)
-r requirements.txt  # Include production requirements
pytest==7.4.3
pytest-cov==4.1.0
black==23.11.0
flake8==6.1.0
```

---

## Part 2: REST API Theory

### 🏗️ Understanding REST Architecture

**REST (Representational State Transfer)** is an architectural style for designing networked applications.

**Core Principles:**

1. **Client-Server Architecture**: Separation of concerns
2. **Stateless**: Each request contains all necessary information
3. **Cacheable**: Responses must define themselves as cacheable or not
4. **Uniform Interface**: Standardized way of communication
5. **Layered System**: Client cannot tell if connected directly to server
6. **Code on Demand** (optional): Servers can extend client functionality

**Resources:**

- Everything is a resource (users, products, orders)
- Resources are identified by URIs
- Resources are manipulated through representations (JSON, XML)

**Example Resource Structure:**

```
/users          → Collection of users
/users/{id}     → Specific user
/users/{id}/orders → User's orders
```

---

### 📡 HTTP Methods & Status Codes

**HTTP Methods (CRUD Operations):**

| Method | Purpose | CRUD | Idempotent |
| --- | --- | --- | --- |
| GET | Retrieve data | Read | Yes |
| POST | Create new resource | Create | No |
| PUT | Update/Replace resource | Update | Yes |
| PATCH | Partial update | Update | No |
| DELETE | Remove resource | Delete | Yes |

**Common HTTP Status Codes:**

**Success (2xx):**

- `200 OK`: Request succeeded
- `201 Created`: Resource created successfully
- `204 No Content`: Success but no content to return

**Client Errors (4xx):**

- `400 Bad Request`: Invalid request data
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: No permission
- `404 Not Found`: Resource doesn't exist
- `422 Unprocessable Entity`: Validation error

**Server Errors (5xx):**

- `500 Internal Server Error`: Server-side error
- `503 Service Unavailable`: Server temporarily unavailable

---

### 📐 API Design Principles

**1. Use Nouns, Not Verbs:**

```
✅ GET /users
❌ GET /getUsers

✅ POST /users
❌ POST /createUser
```

**2. Use Plural Nouns:**

```
✅ /users
❌ /user
```

**3. Use HTTP Methods Correctly:**

```
✅ DELETE /users/123
❌ POST /users/123/delete
```

**4. Use Query Parameters for Filtering:**

```
✅ GET /users?status=active&role=admin
❌ GET /users/active/admin
```

**5. Version Your API:**

```
/api/v1/users
/api/v2/users
```

**6. Use Proper Status Codes:**

- Return appropriate HTTP status codes
- Provide meaningful error messages

**7. Implement Pagination:**

```
GET /users?page=1&limit=20
```

---

## Part 3: FastAPI Basics

### 🎬 Your First API

**Create [`main.py`](http://main.py):**

```python
from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Define a route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Another endpoint
@app.get("/about")
def about():
    return {
        "app": "FastAPI Learning Guide",
        "version": "1.0.0",
        "description": "A comprehensive FastAPI tutorial"
    }
```

**Run the Application:**

```bash
uvicorn main:app --reload
```

**Access Your API:**

- API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Interactive docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Alternative docs: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

<aside>
💡

**The `--reload` flag** enables auto-reload during development. Remove it in production!

</aside>

---

### 🛣️ Path Parameters

Path parameters are variables in the URL path.

```python
from fastapi import FastAPI

app = FastAPI()

# Simple path parameter
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# Multiple path parameters
@app.get("/users/{user_id}/posts/{post_id}")
def get_user_post(user_id: int, post_id: int):
    return {
        "user_id": user_id,
        "post_id": post_id
    }

# Path parameter with string type
@app.get("/items/{item_name}")
def get_item(item_name: str):
    return {"item_name": item_name}

# Enum path parameters (predefined values)
from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model": "AlexNet", "message": "Deep Learning model"}
    if model_name == ModelName.lenet:
        return {"model": "LeNet", "message": "Classic CNN"}
    return {"model": model_name, "message": "ResNet architecture"}
```

**Type Validation:**

- FastAPI automatically validates types
- Returns `422` error if type doesn't match
- Converts string to specified type automatically

---

### 🔍 Query Parameters

Query parameters appear after `?` in the URL.

```python
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Basic query parameters
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit
    }

# Optional query parameters
@app.get("/users/")
def read_users(q: Optional[str] = None):
    if q:
        return {"q": q, "message": "Search query provided"}
    return {"message": "No search query"}

# Multiple optional parameters
@app.get("/products/")
def read_products(
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    in_stock: bool = True
):
    return {
        "category": category,
        "min_price": min_price,
        "max_price": max_price,
        "in_stock": in_stock
    }

# Required query parameter (no default value)
@app.get("/search/")
def search(query: str):
    return {"query": query}
```

**Usage Examples:**

```
GET /items/?skip=0&limit=20
GET /users/?q=john
GET /products/?category=electronics&min_price=100&in_stock=true
GET /search/?query=fastapi
```

---

### 📦 Request Body

Request body is used to send data to the API (typically with POST, PUT, PATCH).

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Define a Pydantic model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# POST endpoint with request body
@app.post("/items/")
def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

# Combining path, query, and body parameters
@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    item: Item,
    q: Optional[str] = None
):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

# Nested models
class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

class Order(BaseModel):
    item: Item
    user: User
    quantity: int

@app.post("/orders/")
def create_order(order: Order):
    return order
```

**Example Request:**

```json
POST /items/
{
    "name": "Laptop",
    "description": "Gaming laptop",
    "price": 1200.50,
    "tax": 120.05
}
```

---

### 📁 File Uploads

Handling file uploads in FastAPI.

```python
from fastapi import FastAPI, File, UploadFile, Form
from typing import List
import shutil
from pathlib import Path

app = FastAPI()

# Single file upload
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": file.size
    }

# Save uploaded file
@app.post("/upload-save/")
async def save_file(file: UploadFile = File(...)):
    upload_dir = Path("uploads")
    upload_dir.mkdir(exist_ok=True)
    
    file_path = upload_dir / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"filename": file.filename, "location": str(file_path)}

# Multiple file uploads
@app.post("/upload-multiple/")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    return {
        "filenames": [file.filename for file in files],
        "count": len(files)
    }

# File upload with form data
@app.post("/upload-with-data/")
async def upload_with_data(
    file: UploadFile = File(...),
    description: str = Form(...),
    category: str = Form(...)
):
    return {
        "filename": file.filename,
        "description": description,
        "category": category
    }

# Read file content
@app.post("/upload-read/")
async def read_file_content(file: UploadFile = File(...)):
    contents = await file.read()
    return {
        "filename": file.filename,
        "size": len(contents)
    }
```

**File Upload Tips:**

- Use `UploadFile` for better performance (uses spooled file)
- Validate file types and size
- Use async file operations for large files
- Store files outside your app directory
- Consider using cloud storage (S3, etc.) for production

---

### 🖼️ Static Files

Serving static files like images, CSS, JavaScript.

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Now files in 'static' folder are accessible at:
# http://localhost:8000/static/image.png
# http://localhost:8000/static/style.css
# http://localhost:8000/static/script.js
```

**Serving HTML Pages:**

```python
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "FastAPI App"}
    )
```

**Directory Structure:**

```
project/
├── app/
│   └── main.py
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── templates/
    └── index.html
```

---

## Part 4: Intermediate Concepts

### ✅ Data Validation with Pydantic

Pydantic provides powerful data validation.

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr, validator
from typing import List, Optional
from datetime import datetime

app = FastAPI()

# Advanced Pydantic model with validation
class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr  # Validates email format
    age: int = Field(..., ge=18, le=120)  # Greater than or equal to 18
    password: str = Field(..., min_length=8)
    created_at: datetime = Field(default_factory=datetime.now)
    tags: List[str] = []
    
    # Custom validator
    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v
    
    # Config for example data
    class Config:
        schema_extra = {
            "example": {
                "username": "johndoe",
                "email": "john@example.com",
                "age": 25,
                "password": "secretpass123",
                "tags": ["developer", "python"]
            }
        }

@app.post("/users/")
def create_user(user: User):
    return user

# List validation
class ItemBatch(BaseModel):
    items: List[str] = Field(..., min_items=1, max_items=10)

@app.post("/batch/")
def create_batch(batch: ItemBatch):
    return {"item_count": len(batch.items), "items": batch.items}
```

**Field Validators:**

- `min_length`, `max_length`: String length
- `ge`, `le`, `gt`, `lt`: Numeric comparisons
- `regex`: Pattern matching
- `min_items`, `max_items`: List length

---

### 📤 Response Models

Control what data is returned from your API.

```python
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from typing import Optional

app = FastAPI()

# Input model (with password)
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    full_name: Optional[str] = None

# Output model (without password)
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True
    
    class Config:
        orm_mode = True  # For database models

# Use response_model to specify output
@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):
    # Simulate user creation
    user_dict = user.dict()
    user_dict["id"] = 123  # Generated ID
    # Password is excluded from response automatically
    return user_dict

# Response with list
from typing import List

@app.get("/users/", response_model=List[UserResponse])
def get_users():
    return [
        {"id": 1, "username": "john", "email": "john@example.com"},
        {"id": 2, "username": "jane", "email": "jane@example.com"}
    ]

# Different status codes
from fastapi import status

@app.post(
    "/items/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def create_item(user: UserCreate):
    return user
```

---

### ⚠️ Error Handling

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Simulated database
fake_db = {
    1: {"id": 1, "name": "Item 1"},
    2: {"id": 2, "name": "Item 2"}
}

# Raise HTTP exceptions
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with id {item_id} not found"
        )
    return fake_db[item_id]

# Custom exception handler
from fastapi import Request
from fastapi.responses import JSONResponse

class CustomException(Exception):
    def __init__(self, name: str):
        self.name = name

@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something wrong."},
    )

@app.get("/custom/{name}")
def trigger_custom_error(name: str):
    if name == "error":
        raise CustomException(name=name)
    return {"message": "Success"}

# Validation error handling (automatic)
@app.post("/validate/")
def validate_data(age: int):
    if age < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Age must be positive"
        )
    return {"age": age}
```

---

### 🔗 Dependencies

Dependencies allow code reuse and inject common logic.

```python
from fastapi import FastAPI, Depends, HTTPException, status
from typing import Optional

app = FastAPI()

# Simple dependency
def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
def read_items(commons: dict = Depends(common_parameters)):
    return commons

@app.get("/users/")
def read_users(commons: dict = Depends(common_parameters)):
    return commons

# Class-based dependency
class Pagination:
    def __init__(self, page: int = 1, size: int = 10):
        self.page = page
        self.size = size
        self.skip = (page - 1) * size

@app.get("/products/")
def get_products(pagination: Pagination = Depends()):
    return {
        "page": pagination.page,
        "size": pagination.size,
        "skip": pagination.skip
    }

# Authentication dependency
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    # Verify token logic here
    if token != "valid-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token"
        )
    return {"user": "authenticated_user"}

@app.get("/protected/")
def protected_route(current_user: dict = Depends(verify_token)):
    return {"message": "Access granted", "user": current_user}

# Nested dependencies
def get_db():
    # Database connection logic
    return "db_connection"

def get_current_user(db = Depends(get_db), token: str = "default"):
    # Get user from database using token
    return {"username": "john", "db": db}

@app.get("/me/")
def read_current_user(current_user: dict = Depends(get_current_user)):
    return current_user
```

---

### 🔄 Middleware

Middleware allows you to run code before and after each request.

```python
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
import time

app = FastAPI()

# Custom middleware
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response

# Logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Response status: {response.status_code}")
    return response

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://example.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# GZip compression middleware
app.add_middleware(GZipMiddleware, minimum_size=1000)

# Trusted host middleware (security)
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["localhost", "*.example.com"]
)
```

**Custom Authentication Middleware:**

```python
from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Skip auth for public endpoints
        if request.url.path in ["/", "/docs", "/openapi.json"]:
            return await call_next(request)
        
        # Check for API key
        api_key = request.headers.get("X-API-Key")
        if not api_key or api_key != "your-secret-key":
            raise HTTPException(status_code=401, detail="Invalid API Key")
        
        response = await call_next(request)
        return response

app.add_middleware(AuthMiddleware)
```

---

## Part 5: Advanced Topics

### 🗄️ Database Integration

**Using SQLAlchemy with FastAPI:**

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List

# Database setup
DATABASE_URL = "sqlite:///./test.db"
# For PostgreSQL: "postgresql://user:password@localhost/dbname"
# For MySQL: "mysql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database model
class UserDB(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class UserCreate(BaseModel):
    email: str
    username: str
    full_name: str

class User(BaseModel):
    id: int
    email: str
    username: str
    full_name: str
    
    class Config:
        orm_mode = True

# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# CRUD operations
@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserDB(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(UserDB).offset(skip).limit(limit).all()
    return users

@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}
```

---

### 🗃️ Database Migrations with Alembic

Alembic manages database schema changes over time.

**Installation:**

```bash
pip install alembic
```

**Initialize Alembic:**

```bash
alembic init alembic
```

**Configure Alembic (`alembic/[env.py](http://env.py)`):**

```python
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Import your models
from app.models import Base
from app.config import settings

# Set target metadata
target_metadata = Base.metadata

config = context.config
config.set_main_option("sqlalchemy.url", settings.database_url)

# ... rest of env.py
```

**Create a Migration:**

```bash
# Auto-generate migration from model changes
alembic revision --autogenerate -m "Create users table"

# Or create empty migration
alembic revision -m "Add column to users"
```

**Example Migration File:**

```python
"""Create users table

Revision ID: 001
Revises: 
Create Date: 2024-01-01 10:00:00
"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('username', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)

def downgrade():
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
```

**Run Migrations:**

```bash
# Apply all pending migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1

# View migration history
alembic history

# View current version
alembic current
```

**Common Migration Operations:**

```python
# Add column
op.add_column('users', sa.Column('phone', sa.String(), nullable=True))

# Drop column
op.drop_column('users', 'phone')

# Rename column
op.alter_column('users', 'username', new_column_name='user_name')

# Create index
op.create_index('idx_email', 'users', ['email'])

# Add foreign key
op.create_foreign_key(
    'fk_user_posts',
    'posts', 'users',
    ['user_id'], ['id']
)
```

---

### 🔐 Authentication & Security

**JWT Authentication:**

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

app = FastAPI()

# Security configuration
SECRET_KEY = "your-secret-key-keep-it-secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Models
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

# Fake database
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "john@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

# Password utilities
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# Endpoints
@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
```

---

### ⏱️ Background Tasks

```python
from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()

# Background task function
def write_log(message: str):
    with open("log.txt", "a") as log:
        time.sleep(2)  # Simulate slow operation
        log.write(f"{message}\n")

def send_email(email: str, message: str):
    time.sleep(3)  # Simulate email sending
    print(f"Email sent to {email}: {message}")

# Use background task
@app.post("/send-notification/{email}")
async def send_notification(
    email: str,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(send_email, email, "Welcome to our service!")
    background_tasks.add_task(write_log, f"Notification sent to {email}")
    return {"message": "Notification sent in the background"}

# Multiple background tasks
@app.post("/register/{email}")
async def register_user(
    email: str,
    background_tasks: BackgroundTasks
):
    # Add multiple tasks
    background_tasks.add_task(write_log, f"New user registered: {email}")
    background_tasks.add_task(send_email, email, "Registration successful")
    background_tasks.add_task(write_log, "Background tasks completed")
    
    return {"message": "User registered successfully"}
```

---

### 🔌 WebSockets

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

# Connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            await manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat")

# Simple WebSocket example
@app.websocket("/ws")
async def websocket_simple(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
```

---

## Part 6: Best Practices & Deployment

### 📋 Project Structure

```
project/
│
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration
│   ├── dependencies.py      # Shared dependencies
│   │
│   ├── routers/            # API routes
│   │   ├── __init__.py
│   │   ├── users.py
│   │   ├── items.py
│   │   └── auth.py
│   │
│   ├── models/             # SQLAlchemy models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   │
│   ├── schemas/            # Pydantic schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   │
│   ├── crud/               # Database operations
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   │
│   └── utils/              # Utilities
│       ├── __init__.py
│       ├── security.py
│       └── email.py
│
├── tests/                  # Test files
│   ├── __init__.py
│   ├── test_main.py
│   └── test_users.py
│
├── alembic/               # Database migrations
├── .env                   # Environment variables
├── requirements.txt       # Dependencies
└── README.md
```

---

### ✨ Best Practices

**1. Use Environment Variables:**

```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    database_url: str
    secret_key: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```

**2. Use Routers for Organization:**

```python
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users():
    return []

# In main.py
app.include_router(router)
```

**3. Add API Versioning:**

```python
from fastapi import APIRouter

v1_router = APIRouter(prefix="/api/v1")
v2_router = APIRouter(prefix="/api/v2")

app.include_router(v1_router)
app.include_router(v2_router)
```

**4. Implement Proper Error Handling:**

```python
from fastapi import HTTPException, status

def get_user(user_id: int):
    user = db.get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user
```

**5. Use Dependency Injection:**

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/items/")
def read_items(db: Session = Depends(get_db)):
    return db.query(Item).all()
```

**6. Add CORS Middleware:**

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**7. Implement Rate Limiting:**

```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.get("/limited")
@limiter.limit("5/minute")
def limited_route(request: Request):
    return {"message": "This route is rate limited"}
```

**8. Implement Logging:**

```python
import logging
from logging.handlers import RotatingFileHandler
import sys

# Configure logging
logger = logging.getLogger("fastapi_app")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
console_handler.setFormatter(console_formatter)

# File handler with rotation
file_handler = RotatingFileHandler(
    'app.log',
    maxBytes=10485760,  # 10MB
    backupCount=5
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(console_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Usage in your app
@app.get("/items/{item_id}")
def get_item(item_id: int):
    logger.info(f"Fetching item with ID: {item_id}")
    try:
        item = fetch_item(item_id)
        logger.info(f"Successfully fetched item: {item_id}")
        return item
    except Exception as e:
        logger.error(f"Error fetching item {item_id}: {str(e)}")
        raise
```

**Structured Logging:**

```python
import logging
import json
from datetime import datetime

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
        }
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_data)

handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
```

**9. Input Validation & Sanitization:**

```python
from pydantic import BaseModel, validator, constr
import re

class UserInput(BaseModel):
    username: constr(min_length=3, max_length=20, regex=r'^[a-zA-Z0-9_]+$')
    email: str
    
    @validator('email')
    def validate_email(cls, v):
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', v):
            raise ValueError('Invalid email format')
        return v.lower()
```

**10. Use Configuration Management:**

```python
from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    admin_email: str
    database_url: str
    secret_key: str
    debug: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = False

@lru_cache()
def get_settings():
    return Settings()

# Usage
settings = get_settings()
```

---

### 🚀 Deployment

**Using Docker:**

```docker
# Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/mydb
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

**Production Server:**

```bash
# Install production server
pip install gunicorn

# Run with Gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

**Environment Variables (.env):**

```
DATABASE_URL=postgresql://user:password@localhost/dbname
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

### 🧪 Testing

```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_create_user():
    response = client.post(
        "/users/",
        json={
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpass123"
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "testuser"
    assert "password" not in data

def test_authentication():
    # Test login
    response = client.post(
        "/token",
        data={"username": "johndoe", "password": "secret"}
    )
    assert response.status_code == 200
    token = response.json()["access_token"]
    
    # Test protected route
    response = client.get(
        "/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
```

---

### 📚 Additional Resources

**Official Documentation:**

- FastAPI Docs: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- Pydantic Docs: [https://pydantic-docs.helpmanual.io](https://pydantic-docs.helpmanual.io)
- SQLAlchemy Docs: [https://docs.sqlalchemy.org](https://docs.sqlalchemy.org)

**Learning Resources:**

- FastAPI GitHub: [https://github.com/tiangolo/fastapi](https://github.com/tiangolo/fastapi)
- Awesome FastAPI: [https://github.com/mjhea0/awesome-fastapi](https://github.com/mjhea0/awesome-fastapi)
- FastAPI Tutorial: [https://fastapi.tiangolo.com/tutorial/](https://fastapi.tiangolo.com/tutorial/)

**Tools & Extensions:**

- FastAPI Users: Authentication library
- FastAPI Mail: Email sending
- FastAPI Cache: Caching support
- FastAPI Pagination: Pagination helpers

---

<aside>
🎉

**Congratulations!** You now have a comprehensive guide to FastAPI. Start with the basics, practice with examples, and gradually move to advanced topics. Happy coding!

</aside>