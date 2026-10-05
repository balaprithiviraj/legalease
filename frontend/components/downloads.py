"""Download buttons using edited session text for every export."""
import streamlit as st

from backend.app.services.document_export import (
    export_docx,
    export_pdf,
    export_txt,
    safe_filename,
)


def render_downloads() -> None:
    text = st.session_state.get("document_text", "")
    if not text:
        return
    doc_type = st.session_state.get("document_type", "document")
    st.markdown(
        '<p class="le-card-title">Export Your Document</p>'
        '<p class="le-card-sub">Download your edited final version.</p>',
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        col1, col2, col3 = st.columns(3)
        try:
            with col1:
                st.download_button(
                    "↓ TXT",
                    data=export_txt(text),
                    file_name=safe_filename(doc_type, "txt"),
                    mime="text/plain",
                    use_container_width=True,
                    help="Plain text file",
                )
            with col2:
                st.download_button(
                    "↓ DOCX",
                    data=export_docx(text),
                    file_name=safe_filename(doc_type, "docx"),
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True,
                    help="Word document",
                )
            with col3:
                st.download_button(
                    "↓ PDF",
                    data=export_pdf(text),
                    file_name=safe_filename(doc_type, "pdf"),
                    mime="application/pdf",
                    use_container_width=True,
                    help="PDF document",
                )
        except Exception as exc:
            st.error(f"Export failed: {exc}")
