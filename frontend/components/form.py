"""Input form for LegalEase (glass card, same logic as before)."""
import streamlit as st

DOCUMENT_TYPES = [
    "Employment Contract",
    "NDA",
    "Freelance Work Contract",
    "Lease Agreement",
    "Offer Letter",
]


def render_form() -> dict | None:
    """Render the Document Details form; return validated inputs or None."""
    st.markdown(
        '<p class="le-card-title">Document Details</p>'
        '<p class="le-card-sub">Tell LegalEase what you need to draft.</p>',
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        with st.form("doc_form"):
            doc_type = st.selectbox(
                "Document Type",
                DOCUMENT_TYPES,
                help="Choose one of the five supported documents.",
            )
            parties = st.text_input(
                "Parties",
                placeholder="e.g. ABC Technologies and John Doe",
                help="Who is involved in this agreement?",
            )
            terms = st.text_area(
                "Terms & Conditions",
                placeholder="e.g. Role, salary, duration, confidentiality, responsibilities...",
                height=160,
                help=(
                    "Describe the important terms, responsibilities, payment, "
                    "duration, confidentiality, and other requirements."
                ),
            )
            effective_date = st.text_input(
                "Effective Date",
                placeholder="DD-MM-YYYY or YYYY-MM-DD",
                help="Optional — leave blank to use a placeholder.",
            )
            submitted = st.form_submit_button(
                "✦ Generate Legal Document",
                use_container_width=True,
            )
    if submitted:
        if not parties.strip():
            st.error("Please enter the parties.")
            return None
        if not terms.strip():
            st.error("Please enter terms and conditions.")
            return None
        return {
            "document_type": doc_type,
            "parties": parties.strip(),
            "terms": terms.strip(),
            "effective_date": effective_date.strip(),
        }
    return None
