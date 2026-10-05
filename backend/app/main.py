"""FastAPI entry point for LegalEase."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.routes import documents

app = FastAPI(
    title="LegalEase",
    description="AI-Powered Legal Document Generator",
)

# Local development CORS (Streamlit runs on 8501 by default).
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",
        "http://127.0.0.1:8501",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(documents.router)


@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok"}
