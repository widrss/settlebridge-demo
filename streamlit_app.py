"""SettleBridge Demo — Streamlit entry point."""

import streamlit as st

st.set_page_config(
    page_title="SettleBridge Demo",
    page_icon="🌉",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from app import demo_a, demo_b  # noqa: E402 — must come after set_page_config

# ---------------------------------------------------------------------------
# Top header
# ---------------------------------------------------------------------------

st.markdown(
    """
    <div style="text-align:center;padding:20px 0 8px 0;">
        <div style="font-size:0.8rem;font-weight:700;letter-spacing:0.18em;
                    text-transform:uppercase;color:#5555aa;margin-bottom:6px;">
            Live Demo
        </div>
        <h1 style="margin:0;font-size:2.2rem;color:#f8f8ff;">
            🌉 SettleBridge
        </h1>
        <p style="color:#8888aa;margin:8px 0 0 0;font-size:1rem;">
            Verified agent settlement — quality-gated payments for AI-to-AI transactions
        </p>
    </div>
    <hr style="border-color:#2d2d4e;margin:16px 0 0 0;">
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Tabs
# ---------------------------------------------------------------------------

tab_a, tab_b = st.tabs(["⚠  Without SettleBridge", "✓  With SettleBridge"])

with tab_a:
    demo_a.render()

with tab_b:
    demo_b.render()
