
# Security Configuration
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
# Default algorithm is HS256
ALGORITHM = os.getenv("ALGORITHM", "HS256")
# Default access token expiration time is 30 minutes
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
