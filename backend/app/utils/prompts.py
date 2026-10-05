"""Prompt builder for LegalEase (Phase 5)."""
from typing import Optional

OUTLINES = {
    "Employment Contract": "Title, Parties, Position and Duties, Compensation, Working Hours, Leave, Confidentiality, Intellectual Property, Termination, Governing Law, Signatures",
    "NDA": "Title, Parties, Definition of Confidential Information, Obligations, Exclusions, Term, Return of Information, Governing Law, Signatures",
    "Freelance Work Contract": "Title, Parties, Scope of Work, Deliverables, Payment, Timeline, Intellectual Property, Confidentiality, Termination, Governing Law, Signatures",
    "Lease Agreement": "Title, Parties, Property, Term, Rent, Security Deposit, Maintenance, Utilities, Termination, Governing Law, Signatures",
    "Offer Letter": "Title, Parties, Role, Compensation, Start Date, Reporting, Acceptance, Signatures",
}

BASE_RULES = "Use only supplied facts. Use [___] for missing info. Use headings and numbered clauses. No invented names, addresses, dates or signatures. Draft only, no claim of legal validity."


def build_prompt(document_type: str, parties: str, terms: str, effective_date: Optional[str] = None) -> str:
    dt = (document_type or "").strip()
    outline = OUTLINES.get(dt, "Title, Parties, Terms, Signatures")
    date_line = effective_date.strip() if effective_date and effective_date.strip() else "[___]"
    return (
        f"Draft a {dt}.\n"
        f"DOCUMENT TYPE: {dt}\n"
        f"PARTIES: {parties.strip()}\n"
        f"TERMS AND CONDITIONS: {terms.strip()}\n"
        f"EFFECTIVE DATE: {date_line}\n"
        f"Structure: {outline}.\n"
        f"Rules: {BASE_RULES}"
    )
