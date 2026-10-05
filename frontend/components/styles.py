"""Premium glassmorphism theme for LegalEase.

Only visual styling lives here. No backend, validation,
generation, or export logic is changed by this file.
"""

import streamlit as st

# ---------------------------------------------------------------------------
# 1. Global glassmorphism CSS (injected once from app.py)
# ---------------------------------------------------------------------------

THEME_CSS = """
<style>
/* ============ Base typography & background ============ */
.stApp {
    font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background: linear-gradient(180deg, #070B14 0%, #0B1220 55%, #111827 100%);
    color: #E8EDF5;
}
/* Keep the default Streamlit containers transparent so our gradient shows */
[data-testid="stAppViewContainer"], [data-testid="stBottomBlockContainer"] {
    background: transparent;
}
[data-testid="stHeader"] {
    background: rgba(7, 11, 20, 0.55);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}
[data-testid="stToolbar"] { color: #9CA3AF; }
.main .block-container {
    max-width: 920px;
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    animation: leFadeUp 0.55s ease both;
}
.stApp p, .stApp li, .stApp label { color: #E8EDF5; }

/* ============ Ambient background orbs (very subtle, CSS only) ============ */
.le-ambient { position: fixed; inset: 0; z-index: 0; pointer-events: none; }
.le-orb { position: fixed; border-radius: 50%; filter: blur(90px); pointer-events: none; }
.le-orb-a {
    width: 540px; height: 540px; top: -170px; left: 8%;
    background: radial-gradient(circle, rgba(59,130,246,0.22), transparent 70%);
    animation: leDrift 18s ease-in-out infinite alternate;
}
.le-orb-b {
    width: 620px; height: 620px; bottom: -220px; right: 2%;
    background: radial-gradient(circle, rgba(139,92,246,0.20), transparent 70%);
    animation: leDrift 22s ease-in-out infinite alternate-reverse;
}
.le-orb-c {
    width: 320px; height: 320px; top: 42%; left: -120px;
    background: radial-gradient(circle, rgba(56,189,248,0.12), transparent 70%);
    animation: leDrift 26s ease-in-out infinite alternate;
}
@keyframes leDrift {
    from { transform: translate3d(0, 0, 0) scale(1); }
    to { transform: translate3d(40px, 30px, 0) scale(1.06); }
}
/* Keep content above the ambient layer */
.main .block-container, [data-testid="stSidebar"] { position: relative; z-index: 1; }

/* ============ Hero entrance animation ============ */
@keyframes leFadeUp {
    from { opacity: 0; transform: translateY(15px); }
    to { opacity: 1; transform: translateY(0); }
}
.le-hero { text-align: center; padding: 0.6rem 0 0.2rem; animation: leFadeUp 0.6s ease both; }
.le-badge {
    display: inline-flex; align-items: center; gap: 6px;
    font-size: 0.78rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase;
    color: #BFDBFE; background: rgba(96,165,250,0.10);
    border: 1px solid rgba(96,165,250,0.28); border-radius: 999px;
    padding: 6px 14px; margin-bottom: 14px;
}
.le-title {
    font-size: clamp(2.6rem, 6vw, 3.6rem); font-weight: 800; letter-spacing: -0.02em;
    margin: 0; line-height: 1.05;
    background: linear-gradient(92deg, #F9FAFB 20%, #93C5FD 55%, #C4B5FD 80%);
    -webkit-background-clip: text; background-clip: text; color: transparent;
}
.le-title .le-scale { font-weight: 300; }
.le-subtitle { font-size: 1.15rem; font-weight: 600; color: #F3F4F6; margin: 10px 0 6px; }
.le-desc { color: #9CA3AF; font-size: 0.98rem; max-width: 620px; margin: 0 auto; line-height: 1.6; }

/* ============ Workflow indicator (Describe → Generate → Edit → Export) ============ */
.le-workflow {
    display: flex; align-items: flex-start; justify-content: space-between;
    gap: 4px; margin: 22px auto 6px; max-width: 680px; padding: 14px 18px;
    background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.09);
    border-radius: 18px; backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    flex-wrap: nowrap;
}
.le-step { flex: 1; min-width: 0; text-align: center; }
.le-dot {
    width: 30px; height: 30px; border-radius: 50%; margin: 0 auto 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.75rem; font-weight: 700;
    background: rgba(255,255,255,0.07); color: #9CA3AF;
    border: 1px solid rgba(255,255,255,0.14);
}
.le-step small { display: block; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.06em; color: #9CA3AF; text-transform: uppercase; }
.le-step span.le-name { display: block; font-size: 0.86rem; font-weight: 600; color: #D1D5DB; margin-top: 2px; }
.le-line { flex: 0 0 34px; height: 2px; margin-top: 14px; border-radius: 2px; background: rgba(255,255,255,0.12); }
.le-step.is-active .le-dot {
    background: linear-gradient(135deg, #4F46E5, #7C3AED);
    color: #fff; border-color: transparent;
    box-shadow: 0 0 0 4px rgba(124,58,237,0.22), 0 4px 16px rgba(124,58,237,0.45);
}
.le-step.is-active small { color: #C4B5FD; }
.le-step.is-active span.le-name { color: #fff; }
.le-step.is-done .le-dot { background: rgba(52,211,153,0.16); color: #6EE7B7; border-color: rgba(52,211,153,0.4); }
.le-step.is-done small { color: #6EE7B7; }
.le-step.is-done ~ .le-line, .le-step.is-done + .le-line { background: rgba(52,211,153,0.35); }

/* ============ Glass cards (Streamlit bordered containers) ============ */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.10);
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    border-radius: 20px;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: rgba(255,255,255,0.18);
    box-shadow: 0 12px 40px rgba(0,0,0,0.35), 0 0 0 1px rgba(139,92,246,0.12);
}
div[data-testid="stVerticalBlockBorderWrapper"] > div {
    padding: 0.4rem 0.2rem;
}

/* ============ Section headings inside glass cards ============ */
.le-card-title { font-size: 1.25rem; font-weight: 700; color: #F9FAFB; margin: 0 0 2px; }
.le-card-sub { color: #9CA3AF; font-size: 0.9rem; margin: 0 0 4px; }
.le-section-gap { height: 18px; }

/* ============ Form labels, help text, captions ============ */
[data-testid="stWidgetLabel"] p {
    color: #F3F4F6 !important; font-weight: 600 !important; font-size: 0.92rem !important;
}
div[data-testid="stHelp"], [data-testid="stCaptionContainer"], .stCaption, small {
    color: #9CA3AF !important;
}

/* ============ Glass inputs ============ */
[data-testid="stTextInput"] input, [data-testid="stTextArea"] textarea {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 12px !important;
    color: #F9FAFB !important;
    caret-color: #A5B4FC;
    transition: border-color 0.18s ease, box-shadow 0.18s ease, background 0.18s ease;
}
[data-testid="stTextInput"] input::placeholder, [data-testid="stTextArea"] textarea::placeholder {
    color: #6B7280 !important; opacity: 1;
}
[data-testid="stTextInput"] input:focus, [data-testid="stTextArea"] textarea:focus {
    border-color: #6366F1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.25) !important;
    background: rgba(255,255,255,0.08) !important;
    outline: none !important;
}
/* Selectbox (BaseWeb) */
div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 12px !important;
    color: #F9FAFB !important;
    transition: border-color 0.18s ease, box-shadow 0.18s ease;
}
div[data-testid="stSelectbox"] div[data-baseweb="select"]:focus-within > div {
    border-color: #6366F1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.25) !important;
}
div[data-baseweb="select"] span, div[data-baseweb="select"] div { color: #F9FAFB !important; }
div[data-baseweb="menu"] { background: #111827 !important; border: 1px solid rgba(255,255,255,0.12); }
div[data-baseweb="menu"] li { color: #E5E7EB !important; }
div[data-baseweb="menu"] li:hover, div[data-baseweb="option"][aria-selected="true"] {
    background: rgba(99,102,241,0.22) !important;
}

/* ============ Primary CTA (Generate) + buttons ============ */
div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 55%, #2563EB 100%) !important;
    color: #fff !important; border: none !important; border-radius: 14px !important;
    font-weight: 700 !important; font-size: 1rem !important;
    padding: 0.72rem 1.2rem !important;
    box-shadow: 0 8px 24px rgba(99,102,241,0.38) !important;
    transition: transform 0.16s ease, box-shadow 0.16s ease, filter 0.16s ease !important;
}
div[data-testid="stFormSubmitButton"] > button:hover {
    transform: translateY(-2px) !important;
    filter: brightness(1.07) !important;
    box-shadow: 0 12px 32px rgba(124,58,237,0.5) !important;
}
div[data-testid="stFormSubmitButton"] > button:active { transform: translateY(0) !important; }
div[data-testid="stFormSubmitButton"] > button:focus-visible,
div[data-testid="stButton"] > button:focus-visible,
div[data-testid="stDownloadButton"] > button:focus-visible {
    outline: 2px solid #A5B4FC !important; outline-offset: 2px;
}
/* Secondary + sidebar buttons: subtle glass */
div[data-testid="stButton"] > button {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.14) !important;
    color: #E5E7EB !important; border-radius: 12px !important; font-weight: 600 !important;
    transition: transform 0.16s ease, box-shadow 0.16s ease, border-color 0.16s ease !important;
}
div[data-testid="stButton"] > button:hover {
    transform: translateY(-1px);
    border-color: rgba(165,180,252,0.5) !important;
    box-shadow: 0 6px 20px rgba(99,102,241,0.28) !important;
}
/* Download buttons: premium glass with accent glow */
div[data-testid="stDownloadButton"] > button {
    background: rgba(96,165,250,0.10) !important;
    border: 1px solid rgba(96,165,250,0.32) !important;
    color: #EFF6FF !important; border-radius: 12px !important; font-weight: 700 !important;
    letter-spacing: 0.02em;
    transition: transform 0.16s ease, box-shadow 0.16s ease, background 0.16s ease !important;
}
div[data-testid="stDownloadButton"] > button:hover {
    transform: translateY(-2px);
    background: rgba(96,165,250,0.18) !important;
    box-shadow: 0 8px 24px rgba(59,130,246,0.35) !important;
}

/* ============ Metrics (Words / Characters / Lines) ============ */
div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.09);
    border-radius: 14px; padding: 10px 12px;
    backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
}
div[data-testid="stMetric"] label { color: #9CA3AF !important; }
div[data-testid="stMetric"] div[data-testid="stMetricValue"] { color: #F9FAFB !important; }

/* ============ Document editor: premium workspace ============ */
.le-doc-shell [data-testid="stTextArea"] textarea {
    background: rgba(3, 7, 18, 0.62) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 14px !important;
    font-size: 0.95rem !important; line-height: 1.7 !important;
    padding: 20px !important;
    min-height: 380px;
}

/* ============ Status / spinner / alerts on dark background ============ */
div[data-testid="stStatusWidget"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 14px; backdrop-filter: blur(14px);
}
div[data-testid="stAlert"] {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 14px !important;
    color: #E5E7EB !important;
    backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px);
}
div[data-testid="stAlert"] p { color: #E5E7EB !important; }

/* ============ How-it-works cards (display-only HTML) ============ */
.le-hiw-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; margin-top: 6px; }
.le-hiw-card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.10);
    border-radius: 18px; padding: 18px 16px;
    backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
}
.le-hiw-card:hover {
    transform: translateY(-4px);
    border-color: rgba(165,180,252,0.45);
    box-shadow: 0 14px 36px rgba(0,0,0,0.35), 0 0 0 1px rgba(99,102,241,0.15);
}
.le-hiw-num {
    font-size: 0.75rem; font-weight: 800; letter-spacing: 0.1em;
    color: #A5B4FC; margin-bottom: 8px;
}
.le-hiw-title { font-size: 1rem; font-weight: 700; color: #F9FAFB; margin-bottom: 6px; }
.le-hiw-text { font-size: 0.86rem; color: #9CA3AF; line-height: 1.55; }

/* ============ Disclaimer card (display-only HTML) ============ */
.le-disclaimer {
    display: flex; gap: 12px; align-items: flex-start;
    background: rgba(251,191,36,0.07);
    border: 1px solid rgba(251,191,36,0.28);
    border-radius: 16px; padding: 16px 18px; margin-top: 8px;
    backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px);
}
.le-disclaimer .le-warn { font-size: 1.2rem; line-height: 1.3; }
.le-disclaimer strong { color: #FDE68A; }
.le-disclaimer p { color: #D1D5DB; font-size: 0.88rem; line-height: 1.6; margin: 2px 0 0; }
.le-foot { text-align: center; color: #6B7280; font-size: 0.82rem; margin-top: 14px; }

/* ============ Sidebar glass ============ */
[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.03);
    backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
    border-right: 1px solid rgba(255,255,255,0.08);
}
[data-testid="stSidebar"] .stApp p { color: #CBD5E1; }

/* ============ Dividers ============ */
hr { border-color: rgba(255,255,255,0.08) !important; }

/* ============ Responsive: stack gracefully on small screens ============ */
@media (max-width: 900px) {
    .le-hiw-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 640px) {
    .main .block-container { padding-left: 1rem; padding-right: 1rem; }
    .le-workflow { padding: 12px 10px; }
    .le-line { flex-basis: 12px; }
    .le-step span.le-name { font-size: 0.76rem; }
    .le-hiw-grid { grid-template-columns: 1fr; }
}

/* ============ Reduced motion: keep it calm for sensitive users ============ */
@media (prefers-reduced-motion: reduce) {
    .main .block-container, .le-hero, .le-orb { animation: none !important; }
    * { transition: none !important; }
}
</style>
"""


def inject_theme() -> None:
    """Inject the global glassmorphism CSS. Call once at the top of app.py."""
    st.markdown(THEME_CSS, unsafe_allow_html=True)
    st.markdown(
        '<div class="le-ambient" aria-hidden="true">'
        '<span class="le-orb le-orb-a"></span>'
        '<span class="le-orb le-orb-b"></span>'
        '<span class="le-orb le-orb-c"></span>'
        "</div>",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# 2. Small display-only HTML helpers (no controls, no logic)
# ---------------------------------------------------------------------------


def hero_html() -> str:
    """Premium hero section (text/CSS only, no image assets)."""
    return """
    <div class="le-hero">
        <div class="le-badge">⚖&nbsp; Legal AI Workspace</div>
        <h1 class="le-title">LegalEase</h1>
        <div class="le-subtitle">AI-Powered Legal Document Generator</div>
        <p class="le-desc">Create professional legal document drafts with AI.
        Describe your requirements, generate a draft, edit it,
        and export it in your preferred format.</p>
    </div>
    """


def workflow_html(stage: int) -> str:
    """Render the 4-step indicator.

    stage: 0 = Describe, 1 = Generate, 2 = Edit/Review, 3 = Export.
    Steps before `stage` are marked done, the current one active.
    Purely visual — it never changes app behavior.
    """
    steps = [("01", "Describe"), ("02", "Generate"), ("03", "Edit"), ("04", "Export")]
    parts = ['<div class="le-workflow" role="list" aria-label="Workflow progress">']
    for i, (num, name) in enumerate(steps):
        if i < stage:
            cls = "is-done"
            dot = "✓"
        elif i == stage:
            cls = "is-active"
            dot = num
        else:
            cls = ""
            dot = num
        parts.append(
            f'<div class="le-step {cls}" role="listitem">'
            f'<div class="le-dot">{dot}</div>'
            f"<small>{num}</small>"
            f'<span class="le-name">{name}</span>'
            "</div>"
        )
        if i < len(steps) - 1:
            parts.append('<div class="le-line"></div>')
    parts.append("</div>")
    return "".join(parts)


def how_it_works_html() -> str:
    """Four elegant display-only cards (hover micro-interaction via CSS)."""
    cards = [
        ("01", "Describe", "Pick a document type, then enter the parties, terms, and effective date."),
        ("02", "Generate", "Gemini creates your draft from your requirements."),
        ("03", "Review", "Read the preview and edit anything you like."),
        ("04", "Export", "Download your final version as TXT, DOCX, or PDF."),
    ]
    parts = ['<div class="le-hiw-grid">']
    for num, title, text in cards:
        parts.append(
            f'<div class="le-hiw-card"><div class="le-hiw-num">{num}</div>'
            f'<div class="le-hiw-title">{title}</div>'
            f'<div class="le-hiw-text">{text}</div></div>'
        )
    parts.append("</div>")
    return "".join(parts)


def disclaimer_html() -> str:
    """Legal disclaimer card. Wording preserved — styling only."""
    return """
    <div class="le-disclaimer" role="note" aria-label="AI and legal disclaimer">
        <div class="le-warn">⚠</div>
        <div>
            <strong>AI &amp; Legal Disclaimer</strong>
            <p>LegalEase uses artificial intelligence to assist with legal document drafting.
            Generated documents are drafts and may not be suitable for every situation or
            jurisdiction. Review the document carefully and consult a qualified legal
            professional before signing or using it.</p>
            <p>LegalEase is an AI-assisted drafting tool, not a law firm.</p>
        </div>
    </div>
    """
