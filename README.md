# Chatbot

Quick setup and run instructions for local development.

1. Create and activate a Python virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
python app.py
```

Notes:
- The project expects a `Vector_Database.xlsx` file in the project root for building the vector DB. If that file is not present, the app will start but the vector DB will not be populated.
- Some libraries used in the code (Ollama / LangChain integrations) may require additional setup or non-Python tooling; consult their docs if you plan to use those features.