"""Gemini generation service. Uses official google-genai SDK."""
import os
from pathlib import Path
from dotenv import load_dotenv

# Resolve the project-root .env explicitly so the backend finds it
# regardless of the shell working directory uvicorn was started from:
# backend/app/services/gemini_generator.py -> parents[3] == LegalEase/
PROJECT_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(PROJECT_ROOT / ".env")

DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")


def get_api_key() -> str:
    key = (os.getenv("GEMINI_API_KEY") or "").strip()
    if not key:
        raise RuntimeError("GEMINI_API_KEY is not set. Add it to your .env file.")
    return key


def generate_document(prompt: str) -> str:
    """Generate document text from a prompt string."""
    if not prompt or not prompt.strip():
        raise ValueError("Prompt must not be empty.")
    api_key = get_api_key()
    try:
        from google import genai

        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=DEFAULT_MODEL, contents=prompt.strip()
        )
    except RuntimeError:
        raise
    except Exception as exc:
        raise RuntimeError(f"Gemini request failed: {exc}") from exc
    text = (getattr(response, "text", "") or "").strip()
    if not text:
        raise RuntimeError("Gemini returned an empty response.")
    return text
