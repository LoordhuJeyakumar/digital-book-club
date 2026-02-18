import uvicorn
from app.main import app

# --- ENTRY POINT WRAPPER ---
# This file allows you to still run the app using 'python main.py' 
# or 'uvicorn main:app', but it points to our new modular 'app' folder.

if __name__ == "__main__":
    # We run the application from the 'app' module
    uvicorn.run(app, host="127.0.0.1", port=3333, reload=True)