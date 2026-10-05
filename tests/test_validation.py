"""Validation and export tests."""
import io
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.services.document_export import export_txt, export_docx, export_pdf

client = TestClient(app)


def test_missing_document_type():
    r = client.post("/generate", json={"parties": "A", "terms": "T"})
    assert r.status_code == 422


def test_missing_parties():
    r = client.post("/generate", json={"document_type": "NDA", "terms": "T"})
    assert r.status_code == 422


def test_missing_terms():
    r = client.post("/generate", json={"document_type": "NDA", "parties": "A"})
    assert r.status_code == 422


def test_invalid_date():
    r = client.post("/generate", json={"document_type": "NDA", "parties": "A", "terms": "T", "effective_date": "bad"})
    assert r.status_code == 422


def test_txt_export():
    assert "hello".encode() in export_txt("hello \u20b9")


def test_docx_export():
    from docx import Document
    data = export_docx("Clause \u20b9 test")
    assert data[:2] == b"PK"
    doc = Document(io.BytesIO(data))
    assert "\u20b9" in "\n".join(p.text for p in doc.paragraphs)


def test_pdf_export():
    data = export_pdf("Hello \u20b9 world")
    assert data[:4] == b"%PDF"


def test_multipage_pdf():
    long_text = "\n".join(f"Clause {i} payment \u20b9{i}" for i in range(200))
    data = export_pdf(long_text)
    assert data[:4] == b"%PDF"
    assert len(data) > 5000
