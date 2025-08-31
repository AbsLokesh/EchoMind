import httpx
from ..config import OLLAMA_BASE_URL, OLLAMA_MODEL

async def ollama_chat(prompt: str, system_prompt: str = "You are a helpful assistant.") -> str:
    url = f"{OLLAMA_BASE_URL}/api/chat"
    payload = {"model": OLLAMA_MODEL, "messages":[{"role":"system","content":system_prompt},{"role":"user","content":prompt}], "stream": False}
    async with httpx.AsyncClient(timeout=60.0) as client:
        r = await client.post(url, json=payload)
        r.raise_for_status()
        data = r.json()
        msg = data.get("message", {}).get("content")
        return msg or "No response."
