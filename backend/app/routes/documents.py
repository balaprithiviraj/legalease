"""Document generation routes (Phase 6)."""
import logging
from fastapi import APIRouter, HTTPException

from backend.app.models.document import DocumentRequest, DocumentResponse
from backend.app.services import gemini_generator
from backend.app.utils.prompts import build_prompt

logger = logging.getLogger(__name__)

router = APIRouter(tags=["documents"])


@router.post("/generate", response_model=DocumentResponse)
def generate_document_endpoint(request: DocumentRequest) -> DocumentResponse:
    """Validate request, build prompt, call Gemini, return draft."""
    try:
        prompt = build_prompt(
            document_type=request.document_type,
            parties=request.parties,
            terms=request.terms,
            effective_date=request.effective_date,
        )
        content = gemini_generator.generate_document(prompt)
    except (RuntimeError, ValueError) as exc:
        logger.warning("Generation failed: %s", type(exc).__name__)
        raise HTTPException(status_code=502, detail=str(exc))
    except Exception:  # never expose stack traces or secrets
        logger.exception("Unexpected generation error")
        raise HTTPException(status_code=500, detail="Unexpected error generating document.")
    if not content or not content.strip():
        raise HTTPException(status_code=502, detail="Gemini returned an empty response.")
    return DocumentResponse(
        success=True,
        document_type=request.document_type,
        content=content.strip(),
    )
