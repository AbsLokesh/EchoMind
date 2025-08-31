from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from loguru import logger
from .config import ALLOWED_ORIGINS, RATE_LIMIT_RPM
from .routes import chat as chat_router

app = FastAPI(title="Gemini Chatbot - End to End")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

limiter = Limiter(key_func=get_remote_address, default_limits=[f"{RATE_LIMIT_RPM}/minute"])
app.state.limiter = limiter

@app.exception_handler(RateLimitExceeded)
def ratelimit_handler(request, exc):
    return JSONResponse({"error":"rate_limited"}, status_code=429)

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/", response_class=HTMLResponse)
def home():
    with open("public/index.html", "r", encoding="utf-8") as f:
        return f.read()

# Include router
app.include_router(chat_router.router)
