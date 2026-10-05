"""Document generation endpoint tests (mocked Gemini)."""
from unittest.mock import patch
from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)
PAYLOAD = {
    "document_type": "Employment Contract",
    "parties": "ABC Technologies and John Doe",
    "terms": "John will work as Software Developer. Salary Rs.50000 per month.",
    "effective_date": "01-01-2027",
}


def test_valid_request():
    with patch("backend.app.routes.documents.gemini_generator.generate_document", return_value="DRAFT"):
        r = client.post("/generate", json=PAYLOAD)
    assert r.status_code == 200
    assert r.json()["content"] == "DRAFT"
    assert r.json()["success"] is True


def test_gemini_failure():
    with patch("backend.app.routes.documents.gemini_generator.generate_document", side_effect=RuntimeError("Gemini request failed")):
        r = client.post("/generate", json=PAYLOAD)
    assert r.status_code == 502


def test_empty_gemini_response():
    with patch("backend.app.routes.documents.gemini_generator.generate_document", side_effect=RuntimeError("Gemini returned an empty response.")):
        r = client.post("/generate", json=PAYLOAD)
    assert r.status_code == 502
