"""API client: Streamlit frontend talks only to FastAPI, never to Gemini directly."""
import os
import requests

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000").rstrip("/")


def generate_document(document_type: str, parties: str, terms: str, effective_date: str = "") -> str:
    """POST to FastAPI /generate and return the draft text."""
    payload = {
        "document_type": document_type,
        "parties": parties,
        "terms": terms,
    }
    if effective_date and effective_date.strip():
        payload["effective_date"] = effective_date.strip()
    try:
        resp = requests.post(f"{BACKEND_URL}/generate", json=payload, timeout=120)
    except Exception:
        raise RuntimeError("Backend unavailable. Start FastAPI with: uvicorn backend.app.main:app --reload")
    if resp.status_code == 200:
        data = resp.json()
        content = (data.get("content") or "").strip()
        if not content:
            raise RuntimeError("Backend returned an empty document.")
        return content
    try:
        detail = resp.json().get("detail", resp.text)
    except Exception:
        detail = resp.text
    raise RuntimeError(f"Generation failed: {detail}")
