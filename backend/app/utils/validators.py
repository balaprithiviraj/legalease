"""Validation helpers for LegalEase."""
from datetime import datetime

ACCEPTED_DATE_FORMATS = ("%d-%m-%Y", "%Y-%m-%d")


def parse_effective_date(value: str) -> str:
    """Validate an effective date string and return it normalized.

    Accepts DD-MM-YYYY or YYYY-MM-DD. Returns the original
    stripped string when valid, otherwise raises ValueError.
    """
    text = (value or "").strip()
    if not text:
        raise ValueError("effective_date is invalid. Use DD-MM-YYYY or YYYY-MM-DD.")
    for fmt in ACCEPTED_DATE_FORMATS:
        try:
            datetime.strptime(text, fmt)
            return text
        except ValueError:
            continue
    raise ValueError("effective_date is invalid. Use DD-MM-YYYY or YYYY-MM-DD.")
