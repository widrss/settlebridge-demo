"""Demo B — With SettleBridge.

State machine (b_step):
    0: idle
    1: task sent
    2: checking agent track record (spinner → pass/fail badge)
    3: payment held in escrow    [good path only — bad agent is blocked at step 2]
    4: deliverable received
    5: scoring against acceptance criteria
    6: outcome — pass (payment released + audit log) or fail (payment returned + score update)
    7: end card

For bad agent the sequence short-circuits at step 2 → jump to step 7 (blocked end card).
"""

import time
from datetime import UTC, datetime

import streamlit as st

from app.components import (
    inject_css,
    render_agent_profile,
    render_audit_log,
    render_cost_ticker,
    render_deliverable,
    render_end_card_good,
    render_end_card_rejected,
    render_payment_panel,
    render_scoring_panel,
    render_step_label,
    render_task_card,
)
from app.simulation import (
    BAD_AGENT_PROFILE,
    BAD_DELIVERABLE,
    GOOD_AGENT_PROFILE,
    GOOD_DELIVERABLE,
    SCORING_RESULT_FAIL,
    SCORING_RESULT_PASS,
    TASK_SPEC,
    make_audit_log_entry,
    make_rejection_log_entry,
)

STEP_DELAY = 2.5


def _init_state() -> None:
    defaults = {
        "b_step": 0,
        "b_running": False,
        "b_agent_choice": "Good Agent ✓",
        "b_timestamp": "",
        "b_audit_entry": "",
        "b_waste": 0.0,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def _agent_profile() -> dict:
    return (
        GOOD_AGENT_PROFILE
        if st.session_state["b_agent_choice"] == "Good Agent ✓"
        else BAD_AGENT_PROFILE
    )


def _is_good() -> bool:
    return st.session_state["b_agent_choice"] == "Good Agent ✓"


def render() -> None:
    inject_css()
    _init_state()

    step = st.session_state["b_step"]
    running = st.session_state["b_running"]
    good = _is_good()
    agent = _agent_profile()

    # ------------------------------------------------------------------ Header
    st.markdown(
        """
        <div style="margin-bottom:24px;">
            <h2 style="color:#4ade80;margin-bottom:4px;">✓ With SettleBridge</h2>
            <p style="color:#8888aa;font-size:0.9rem;margin:0;">
                The same task, now routed through the SettleBridge trust layer.
                Agent track record is verified before assignment. Payment is held in escrow.
                Delivery is scored against acceptance criteria before funds are released.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ------------------------------------------------------------------ Controls
    ctrl_col1, ctrl_col2, ctrl_col3, ctrl_col4 = st.columns([2, 2, 2, 4])

    with ctrl_col1:
        agent_disabled = running or step > 0
        choice = st.radio(
            "Select Agent",
            ["Good Agent ✓", "Bad Agent ✗"],
            index=0 if st.session_state["b_agent_choice"] == "Good Agent ✓" else 1,
            key="b_agent_radio",
            disabled=agent_disabled,
            horizontal=False,
            label_visibility="collapsed",
        )
        if not agent_disabled:
            st.session_state["b_agent_choice"] = choice
            good = choice == "Good Agent ✓"
            agent = _agent_profile()

    with ctrl_col2:
        play_disabled = running or step > 0
        if st.button("▶ Play Demo", disabled=play_disabled, use_container_width=True, key="b_play"):
            st.session_state["b_step"] = 1
            st.session_state["b_running"] = True
            st.rerun()

    with ctrl_col3:
        if st.button("↺ Reset", use_container_width=True, key="b_reset"):
            st.session_state["b_step"] = 0
            st.session_state["b_running"] = False
            st.session_state["b_waste"] = 0.0
            st.session_state["b_timestamp"] = ""
            st.session_state["b_audit_entry"] = ""
            st.rerun()

    # Agent label preview
    with ctrl_col4:
        if step == 0:
            label = agent["name"]
            score = agent["task_type_score"]
            color = "#4ade80" if good else "#ff6b6b"
            icon = "✓" if good else "✗"
            st.markdown(
                f"""
                <div style="padding:8px 16px;background:#1a1a2e;border-radius:8px;
                            border:1px solid #2d2d4e;font-size:0.85rem;color:#c0c0d8;">
                    Selected: <strong style="color:{color};">{icon} {label}</strong>
                    &nbsp;—&nbsp; Market Research Score:
                    <strong style="color:{color};">{score}/5</strong>
                </div>
                """,
                unsafe_allow_html=True,
            )

    if step == 0:
        st.markdown(
            "<p style='color:#5555aa;margin-top:20px;font-size:0.9rem;'>"
            "Choose an agent above, then press <strong>▶ Play Demo</strong>.</p>",
            unsafe_allow_html=True,
        )
        return

    st.markdown("<hr style='border-color:#2d2d4e;margin:16px 0;'>", unsafe_allow_html=True)

    # ------------------------------------------------------------------ Flow layout
    # Left column: task + agent profile + payment
    # Right column: deliverable + scoring + audit log
    col_left, col_right = st.columns([1, 1.4])

    with col_left:
        # Step 1 — Task
        render_step_label("Step 1 — Task Request")
        render_task_card(TASK_SPEC)

        # Step 2 — Agent track record
        if step >= 2:
            render_step_label("Step 2 — Agent Pre-Qualification")
            revealed = step >= 3 or (not good and step >= 2)
            render_agent_profile(agent, revealed=revealed)

        # Step 3 — Payment escrow (good path only, or skip on bad-blocked path)
        if good and step >= 3:
            render_step_label("Step 3 — Payment Held in Escrow")
            if step == 6:
                pay_status = "released"
            elif step == 7:
                pay_status = "released"
            else:
                pay_status = "held"
            render_payment_panel(
                TASK_SPEC,
                status=pay_status,
                timestamp=st.session_state["b_timestamp"] if step >= 6 else "",
            )

        # Bad agent fail path — show returned payment at step 7
        if not good and step >= 7:
            render_step_label("Step 3 — Payment (Never Released)")
            render_payment_panel(TASK_SPEC, status="returned")

    with col_right:
        # Step 4 — Deliverable (good path only — bad agent was blocked)
        if good and step >= 4:
            render_step_label("Step 4 — Deliverable Received")
            if step == 5:
                delivery_status = "pending"
            elif step >= 6:
                delivery_status = "pass"
            else:
                delivery_status = None
            render_deliverable(GOOD_DELIVERABLE, status=delivery_status)

        # Bad agent — deliverable shown for "bad agent delivered bad work" path
        if not good and step >= 4:
            render_step_label("Step 4 — Deliverable Received")
            delivery_status_bad = "pending" if step == 5 else "fail" if step >= 6 else None
            render_deliverable(BAD_DELIVERABLE, status=delivery_status_bad)

        # Step 5 — Scoring
        if step >= 5:
            render_step_label("Step 5 — Scoring Against Criteria")
            if step == 5:
                render_scoring_panel(in_progress=True)
            else:
                results = SCORING_RESULT_PASS if good else SCORING_RESULT_FAIL
                render_scoring_panel(results=results)

        # Step 6 — Audit log (good) or rejection log (bad)
        if step >= 6:
            if good:
                render_step_label("Step 6 — Audit Trail")
                render_audit_log(st.session_state["b_audit_entry"])
            else:
                render_step_label("Step 6 — Rejection & Score Update")
                render_audit_log(st.session_state["b_audit_entry"])

    # ------------------------------------------------------------------ Cost ticker
    render_cost_ticker(st.session_state["b_waste"], zero=(st.session_state["b_waste"] == 0.0))

    # ------------------------------------------------------------------ End card
    if step >= 7:
        if good:
            render_end_card_good()
        elif not good and step >= 7:
            # Distinguish: blocked at pre-qual vs failed delivery
            # In this demo bad agent always gets through (to show delivery rejection)
            render_end_card_rejected()

    # ------------------------------------------------------------------ Blocked path short card
    # (for bad agent shown at step 2 — shows qualification fail immediately, skips to step 7)
    # Actually we send bad agent through full path to show delivery rejection as more dramatic
    # Qualification FAIL is shown as a warning but task still assigned (demo choice)
    # This makes the payment-returned outcome more impactful than just "never assigned"

    # ------------------------------------------------------------------ Auto-advance
    if running:
        time.sleep(STEP_DELAY)
        next_step = step + 1

        # Generate audit entry when we hit outcome step
        if next_step == 6:
            ts = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S UTC")
            st.session_state["b_timestamp"] = ts
            if good:
                st.session_state["b_audit_entry"] = make_audit_log_entry(
                    agent, TASK_SPEC, SCORING_RESULT_PASS
                )
                st.session_state["b_waste"] = 0.0
            else:
                st.session_state["b_audit_entry"] = make_rejection_log_entry(agent, TASK_SPEC)
                st.session_state["b_waste"] = 0.0  # buyer gets money back

        if next_step > 7:
            st.session_state["b_running"] = False
        else:
            st.session_state["b_step"] = next_step

        st.rerun()
