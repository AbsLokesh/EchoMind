# Gemini Chatbot — End-to-End Separated Project

This project is a fully separated, end-to-end chatbot using Gemini AI Studio (primary) and Ollama (optional local LLM).
It includes a FastAPI backend, modular providers, security helpers, and a Tailwind + Bootstrap UI.

Run locally:
```bash
unzip gemini-chatbot-endtoend.zip
cd gemini-chatbot-endtoend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# set GEMINI_API_KEY in .env, optionally run Ollama for local model
uvicorn app.main:app --reload --port 8000
```
