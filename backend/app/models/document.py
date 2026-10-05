"""Pydantic models for LegalEase document requests and responses."""
from typing import Optional
from pydantic import BaseModel, Field, field_validator

SUPPORTED_DOCUMENT_TYPES = [
    "Employment Contract",
    "NDA",
    "Freelance Work Contract",
    "Lease Agreement",
    "Offer Letter",
]


class DocumentRequest(BaseModel):
    """Incoming request to generate a legal document draft."""

    document_type: str = Field(..., description="Type of document to generate")
    parties: str = Field(..., description="Names/parties involved")
    terms: str = Field(..., description="Terms and conditions")
    effective_date: Optional[str] = Field(
        default=None, description="Effective date as DD-MM-YYYY or YYYY-MM-DD"
    )

    @field_validator("document_type")
    @classmethod
    def validate_document_type(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("document_type is required")
        if v.strip() not in SUPPORTED_DOCUMENT_TYPES:
            raise ValueError(
                f"Unsupported document_type. Must be one of: {', '.join(SUPPORTED_DOCUMENT_TYPES)}"
            )
        return v.strip()

    @field_validator("parties")
    @classmethod
    def validate_parties(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("parties is required")
        return v.strip()

    @field_validator("terms")
    @classmethod
    def validate_terms(cls, v: str) -> str:
        if not v or not v.strip():
            raise ValueError("terms is required")
        return v.strip()

    @field_validator("effective_date")
    @classmethod
    def validate_effective_date(cls, v: Optional[str]) -> Optional[str]:
        if v is None or (isinstance(v, str) and not v.strip()):
            return None
        from backend.app.utils.validators import parse_effective_date

        return parse_effective_date(v.strip())


class DocumentResponse(BaseModel):
    """Response containing the generated document draft."""

    success: bool = True
    document_type: str
    content: str
