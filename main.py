from fastapi import FastAPI  # Import framework itself
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime  # Import the date and time module
import pytz  # This module handles time zones
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path="./.env")

app = FastAPI(
    title="My API",
    description="This is a sample FastAPI application.",
    version="1.0.0",
    default_response_class=JSONResponse
)  # Create an instance of FastAPI

# ✅ Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],  # Allowed HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/myinfo")  # Define a GET endpoint at "/myinfo"
def get_info():
    # Get current UTC time using pytz
    current_time = datetime.now(pytz.utc).isoformat()

    # Ensure 'Z' instead of '+00:00'
    if current_time.endswith("+00:00"):
        current_time = current_time[:-6] + "Z"

    # Construct JSON response
    data = {
        "email": os.getenv("EMAIL"),
        "current_datetime": current_time,  # The dynamically generated UTC time with 'Z'
        "github_url": os.getenv("GITHUB_REPO")
    }

    return JSONResponse(content=data)  # Explicitly return JSONResponse
