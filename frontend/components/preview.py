"""Preview + editing area. Edited text is the canonical final document."""
import streamlit as st


def render_preview() -> None:
    if "document_text" not in st.session_state or not st.session_state["document_text"]:
        return
    st.markdown(
        '<p class="le-card-title">✦ Generated Document</p>'
        '<p class="le-card-sub">Review and edit your AI-generated draft before exporting.</p>',
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        text = st.session_state["document_text"]
        stat1, stat2, stat3 = st.columns(3)
        stat1.metric("Words", f"{len(text.split()):,}")
        stat2.metric("Characters", f"{len(text):,}")
        stat3.metric("Lines", f"{len(text.splitlines()):,}")
        # Wrapper class gives the editor its premium document-workspace look.
        st.markdown('<div class="le-doc-shell">', unsafe_allow_html=True)
        st.session_state["document_text"] = st.text_area(
            "Document preview (editable)",
            value=text,
            height=400,
            help="Edit the draft here — your edits are used for all downloads.",
        )
        st.markdown("</div>", unsafe_allow_html=True)
