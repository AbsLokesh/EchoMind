import httpx
from typing import Optional
from ..config import GEMINI_API_KEY, GEMINI_MODEL

BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"

async def gemini_chat(prompt: str, system_prompt: Optional[str] = None, model: Optional[str] = None) -> str:
    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY not set in env")
    model = model or GEMINI_MODEL
    url = f"{BASE_URL}/{model}:generateContent?key={GEMINI_API_KEY}"
    contents = []
    text = (system_prompt + "\n\n" if system_prompt else "") + prompt
    contents.append({"parts":[{"text": text}]})

    payload = {"contents": contents, "temperature": 0.2, "maxOutputTokens": 512}
    async with httpx.AsyncClient(timeout=60.0) as client:
        r = await client.post(url, json=payload)
        r.raise_for_status()
        data = r.json()
        candidates = data.get("candidates", [])
        if not candidates:
            return "No response from Gemini."
        parts = (candidates[0].get("content") or {}).get("parts") or []
        if not parts:
            return "No response."
        return parts[0].get("text", "").strip() or "No response."
