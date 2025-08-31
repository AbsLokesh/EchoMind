from fastapi import APIRouter, Request, HTTPException, Depends
from pydantic import BaseModel
from ..security import input_guard, check_app_secret
from ..providers.gemini import gemini_chat
from ..providers.ollama import ollama_chat

router = APIRouter()

class ChatIn(BaseModel):
    message: str
    provider: str | None = "gemini"
    system_prompt: str | None = "You are a concise, helpful assistant."

@router.post("/chat")
async def chat_endpoint(request: Request, payload: ChatIn):
    ok, why = check_app_secret(request.headers.get("X-APP-KEY"))
    if not ok:
        raise HTTPException(status_code=401, detail=why)
    blocked, reason = input_guard(payload.message)
    if blocked:
        return {"reply": f"Blocked: {reason}"}
    provider = (payload.provider or "gemini").lower()
    if provider == "gemini":
        res = await gemini_chat(payload.message, payload.system_prompt)
    elif provider == "ollama":
        res = await ollama_chat(payload.message, payload.system_prompt or "You are helpful.")
    else:
        raise HTTPException(status_code=400, detail="Unknown provider")
    return {"reply": res, "provider": provider}
