Python Backend with Fast API

Description: This is a public API that returns the following information in JSON format:
1.Your registered email address (used to register on the HNG12 Slack workspace).
2.The current datetime as an ISO 8601 formatted timestamp.
3.The GitHub URL of the project's codebase.

How to Set-up
1. Make sure python is installed, otherwise install python3
2. Navigate to the project diretory 
3. setup a virtual environment (venv)
4. Use pip to install:  "pip install -r requirements.txt"
✅ FastAPI → Web framework
✅ Uvicorn → ASGI server to run the API
✅ pytz → Timezone support
5.start the server with  "uvicorn main:app --host 0.0.0.0 --port 8000 --reload"
6. Stop server with cltr+c
