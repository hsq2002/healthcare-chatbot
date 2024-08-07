# healthcare-chatbot

# Create virtual environment

1. cd to project directory
2. python -m venv .venv

# Start virtual environment

# WINDOWS

./.venv/Scripts/Activate.ps1

# MAC

source .venv/bin/activate

# Setting flask app

# Windows (CMD)

set FLASK_APP=openai_chatbot/chatbot.py

# Windows (Powershell)

$env:FLASK_APP = "openai_chatbot/chatbot.py"

# run app

- flask run
- python openai_chatbot/chatbot.py (NOTE: I recommend using this command to run server, use the top one of this doesn't work)
