# Automated Helpdesk Ticket Analytics & Knowledge Base Generator

A lightweight internal web tool and script designed for IT support interns to ingest helpdesk support tickets, categorize recurring issues, and automatically draft structured troubleshooting knowledge base articles.

## Virtual Environment (.venv) Setup Instructions

Always run Python projects within an isolated virtual environment.

### On Unix / macOS (Terminal):
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### On Windows (PowerShell):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Running the Application
After activating your virtual environment and installing dependencies:
```bash
streamlit run app.py
```
