import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash-latest").strip()
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").strip()
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3").strip()

ALLOWED_ORIGINS = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "http://localhost:8000").split(",") if o.strip()]
RATE_LIMIT_RPM = int(os.getenv("RATE_LIMIT_RPM", "60"))
APP_SECRET = os.getenv("APP_SECRET", "").strip()
MAX_INPUT_CHARS = int(os.getenv("MAX_INPUT_CHARS", "4000"))
