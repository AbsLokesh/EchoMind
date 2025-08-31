import re
from typing import Tuple, Optional
from .config import APP_SECRET, MAX_INPUT_CHARS

BLOCKLIST = [
    r"(?i)please ignore previous instructions",
    r"(?i)act as .* system prompt",
    r"(?i)reveal.*api key",
    r"(?i)disable security",
]

def input_guard(text: str) -> Tuple[bool, str]:
    if not isinstance(text, str) or not text.strip():
        return True, "Empty or invalid message."
    if len(text) > MAX_INPUT_CHARS:
        return True, f"Message too long (>{MAX_INPUT_CHARS} chars)."
    for pat in BLOCKLIST:
        if re.search(pat, text):
            return True, "Blocked by safety rules."
    return False, ""

def check_app_secret(provided: Optional[str]) -> Tuple[bool, str]:
    if not APP_SECRET:
        return True, ""  # not enforced
    if not provided:
        return False, "Missing X-APP-KEY header."
    if provided != APP_SECRET:
        return False, "Invalid app key."
    return True, ""
