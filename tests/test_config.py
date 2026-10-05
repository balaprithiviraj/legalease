"""Configuration behavior tests (in-memory values only, never a real key)."""
import os
from unittest.mock import MagicMock, patch
from backend.app.services import gemini_generator as g


def test_missing_key_gives_clean_error(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    try:
        g.get_api_key()
        raise AssertionError("should have raised")
    except RuntimeError as exc:
        assert "GEMINI_API_KEY" in str(exc)


def test_present_key_is_accepted(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-key")
    assert g.get_api_key() == "test-key"


def test_generate_works_when_configured(monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-key")
    mock_client = MagicMock()
    mock_client.models.generate_content.return_value = MagicMock(text="draft")
    with patch("google.genai.Client", return_value=mock_client):
        assert g.generate_document("hello") == "draft"


def test_generate_fails_cleanly_when_missing(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    try:
        g.generate_document("hello")
        raise AssertionError("should have raised")
    except RuntimeError as exc:
        assert "GEMINI_API_KEY" in str(exc)
