from fastapi import FastAPI  # Import framwork itself
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime  # import the date and time module
import pytz  # this module handles the time zoning
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path='./.env')


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
@app.get("/myinfo")  # is a decorator that registers a GET request route. executes the function on link.  Define a GET endpoint at "/myinfo on the app"
def get_info():
    return {
        "email": os.getenv("EMAIL"),  
        "current_datetime": datetime.now(pytz.utc).isoformat(),  # Get current UTC time using pytz
        "github_url": os.getenv("GITHUB_REPO")  
    }
    return JSONResponse(content=data)
