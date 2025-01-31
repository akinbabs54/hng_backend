from fastapi import FastAPI  # Import framwork itself
from datetime import datetime  # import the date and time module
import pytz  # this module handles the time zoning
from dotenv import load_dotenv

app = FastAPI(
    title="My API",
    description="This is a sample FastAPI application.",
    version="1.0.0"
)  # Create an instance of FastAPI

@app.get("/myinfo")  # is a decorator that registers a GET request route. executes the function on link.  Define a GET endpoint at "/myinfo on the app"
def get_info():
    return {
        "email": ("EMAIL"),  
        "current_time": datetime.now(pytz.utc).isoformat(),  # Get current UTC time using pytz
        "github_repo": ("GITHUB_REPO")  
    }

