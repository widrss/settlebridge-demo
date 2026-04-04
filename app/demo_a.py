"""Demo A — Without SettleBridge.

State machine (a_step):
    0: idle
    1: task sent to worker agent
    2: deliverable received (bad)
    3: payment auto-sent (no quality check)
    4: end card
"""

import time
from datetime import UTC, datetime

import streamlit as st

from app.components import (
    inject_css,
    render_cost_ticker,
    render_deliverable,
    render_end_card_bad,
    render_payment_panel,
    render_step_label,
    render_task_card,
)
from app.simulation import BAD_DELIVERABLE, TASK_SPEC

STEP_DELAY = 3.0  # seconds between auto-play transitions


def _init_state() -> None:
    if "a_step" not in st.session_state:
        st.session_state["a_step"] = 0
    if "a_running" not in st.session_state:
        st.session_state["a_running"] = False
    if "a_timestamp" not in st.session_state:
        st.session_state["a_timestamp"] = ""
    if "a_waste" not in st.session_state:
        st.session_state["a_waste"] = 0.0


def render() -> None:
    inject_css()
    _init_state()

    step = st.session_state["a_step"]
    running = st.session_state["a_running"]

    # ------------------------------------------------------------------ Header
    st.markdown(
        """
        <div style="margin-bottom:24px;">
            <h2 style="color:#ff6b6b;margin-bottom:4px;">⚠ Without SettleBridge</h2>
            <p style="color:#8888aa;font-size:0.9rem;margin:0;">
                A Buyer Agent commissions a market research task.
                The Worker Agent delivers a low-quality response.
                Payment is sent automatically — no verification, no recourse.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ------------------------------------------------------------------ Controls
    ctrl_col1, ctrl_col2, ctrl_col3 = st.columns([2, 2, 6])
    with ctrl_col1:
        play_disabled = running or step > 0
        if st.button("▶ Play Demo", disabled=play_disabled, use_container_width=True, key="a_play"):
            st.session_state["a_step"] = 1
            st.session_state["a_running"] = True
            st.rerun()
    with ctrl_col2:
        if st.button("↺ Reset", use_container_width=True, key="a_reset"):
            st.session_state["a_step"] = 0
            st.session_state["a_running"] = False
            st.session_state["a_waste"] = 0.0
            st.session_state["a_timestamp"] = ""
            st.rerun()

    if step == 0:
        st.markdown(
            "<p style='color:#5555aa;margin-top:20px;font-size:0.9rem;'>"
            "Press <strong>▶ Play Demo</strong> to begin the simulation.</p>",
            unsafe_allow_html=True,
        )
        return

    st.markdown("<hr style='border-color:#2d2d4e;margin:16px 0;'>", unsafe_allow_html=True)

    # ------------------------------------------------------------------ 3-column layout
    col_left, col_center, col_right = st.columns([1, 1.2, 1])

    # Left — always shown from step 1
    with col_left:
        render_step_label("Step 1 — Task Request Sent")
        render_task_card(TASK_SPEC)

    # Center — deliverable appears at step 2+
    with col_center:
        if step >= 2:
            render_step_label("Step 2 — Deliverable Received")
            render_deliverable(
                BAD_DELIVERABLE,
                status="fail" if step >= 3 else None,
            )
        else:
            st.markdown(
                """
                <div class="sb-card" style="min-height:160px;display:flex;align-items:center;justify-content:center;">
                    <div style="color:#3d3d6e;text-align:center;">
                        <div style="font-size:2rem;">📄</div>
                        <div style="font-size:0.8rem;margin-top:6px;">Awaiting deliverable…</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Right — payment appears at step 3+
    with col_right:
        if step >= 3:
            render_step_label("Step 3 — Payment Auto-Sent")
            render_payment_panel(
                TASK_SPEC,
                status="sent",
                timestamp=st.session_state["a_timestamp"],
            )
        else:
            st.markdown(
                """
                <div class="sb-card" style="min-height:100px;display:flex;align-items:center;justify-content:center;">
                    <div style="color:#3d3d6e;text-align:center;">
                        <div style="font-size:2rem;">💳</div>
                        <div style="font-size:0.8rem;margin-top:6px;">Payment pending…</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # ------------------------------------------------------------------ Cost ticker
    render_cost_ticker(st.session_state["a_waste"], zero=False)

    # ------------------------------------------------------------------ End card
    if step >= 4:
        render_end_card_bad()

    # ------------------------------------------------------------------ Auto-advance
    if running:
        time.sleep(STEP_DELAY)
        next_step = step + 1

        if next_step == 3:
            st.session_state["a_timestamp"] = datetime.now(UTC).strftime(
                "%Y-%m-%d %H:%M:%S UTC"
            )
            st.session_state["a_waste"] = TASK_SPEC["budget"]

        if next_step > 4:
            st.session_state["a_running"] = False
        else:
            st.session_state["a_step"] = next_step

        st.rerun()
