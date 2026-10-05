"""LegalEase Streamlit frontend — premium glassmorphism UI.

Functionality is unchanged: Streamlit -> FastAPI -> Gemini -> draft,
then preview/edit -> TXT/DOCX/PDF export. This file only improves
visual design; all controls stay Streamlit-native.
"""
import streamlit as st

from frontend.components.downloads import render_downloads
from frontend.components.form import render_form
from frontend.components.preview import render_preview
from frontend.components.styles import (
    disclaimer_html,
    hero_html,
    how_it_works_html,
    inject_theme,
    workflow_html,
)
from frontend.utils.api_client import BACKEND_URL, generate_document

# ---------------------------------------------------------------------------
# Page config + theme (visual only)
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_theme()

# ---------------------------------------------------------------------------
# Session state (unchanged behavior)
# ---------------------------------------------------------------------------

if "document_text" not in st.session_state:
    st.session_state["document_text"] = ""
if "document_type" not in st.session_state:
    st.session_state["document_type"] = "document"

has_doc = bool(st.session_state.get("document_text"))

# ---------------------------------------------------------------------------
# Sidebar: progress + backend check (same logic, glass styling via CSS)
# ---------------------------------------------------------------------------

with st.sidebar:
    st.header("Your progress")
    steps = [
        ("Enter details", True),
        ("Generate draft", has_doc),
        ("Preview and edit", has_doc),
        ("Download TXT / DOCX / PDF", has_doc),
    ]
    for label, done in steps:
        st.write(("✓ " if done else "○ ") + label)
    st.divider()
    if st.button("Test backend connection", use_container_width=True):
        import requests

        with st.spinner("Checking..."):
            try:
                resp = requests.get(f"{BACKEND_URL}/health", timeout=5)
                if resp.json().get("status") == "ok":
                    st.success("Backend is online.")
                else:
                    st.error("Backend gave an unexpected response.")
            except Exception:
                st.error("Backend offline. Start it: uvicorn backend.app.main:app --reload")

# ---------------------------------------------------------------------------
# Hero + workflow indicator (display only)
# ---------------------------------------------------------------------------

st.markdown(hero_html(), unsafe_allow_html=True)

# Visual stage only — never drives logic.
# 0 Describe → 1 Generate → 2 Edit → 3 Export
stage = 3 if has_doc else 0
st.markdown(workflow_html(stage), unsafe_allow_html=True)
st.markdown('<div class="le-section-gap"></div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Main workflow: form → generate → preview → export (logic unchanged)
# ---------------------------------------------------------------------------

inputs = render_form()

if inputs:
    with st.status("✦ Building your document...", expanded=True) as status:
        st.write("Analyzing your requirements")
        st.write("Structuring the agreement")
        st.write("Generating your legal draft")
        try:
            st.session_state["document_text"] = generate_document(**inputs)
            st.session_state["document_type"] = inputs["document_type"]
            status.update(label="Draft ready!", state="complete", expanded=False)
            st.success("Document generated. Preview and edit below.")
        except RuntimeError as exc:
            status.update(label="Generation failed", state="error")
            st.error(str(exc))

if not st.session_state.get("document_text"):
    st.markdown('<div class="le-section-gap"></div>', unsafe_allow_html=True)
    st.markdown(
        '<p class="le-card-title">How it works</p>'
        '<p class="le-card-sub">From idea to signed-ready draft in four steps.</p>',
        unsafe_allow_html=True,
    )
    st.markdown(how_it_works_html(), unsafe_allow_html=True)

st.markdown('<div class="le-section-gap"></div>', unsafe_allow_html=True)
render_preview()
st.markdown('<div class="le-section-gap"></div>', unsafe_allow_html=True)
render_downloads()

# ---------------------------------------------------------------------------
# Disclaimer + footer (wording preserved, glass card styling)
# ---------------------------------------------------------------------------

st.markdown('<div class="le-section-gap"></div>', unsafe_allow_html=True)
st.markdown(disclaimer_html(), unsafe_allow_html=True)
st.markdown(
    '<div class="le-foot">LegalEase is an AI-assisted drafting tool, not a law firm.</div>',
    unsafe_allow_html=True,
)
