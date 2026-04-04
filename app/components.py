"""Shared UI components for the SettleBridge Streamlit demo."""

import streamlit as st

# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------

def inject_css() -> None:
    st.markdown(
        """
        <style>
        /* ---- General card ---- */
        .sb-card {
            background: #1a1a2e;
            border: 1px solid #2d2d4e;
            border-radius: 10px;
            padding: 20px 24px;
            margin-bottom: 12px;
        }
        .sb-card-title {
            font-size: 0.72rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #8888aa;
            margin-bottom: 8px;
        }
        .sb-card-body {
            font-size: 0.95rem;
            color: #d0d0e8;
            line-height: 1.6;
        }

        /* ---- Badges ---- */
        .badge {
            display: inline-block;
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
            margin-top: 6px;
        }
        .badge-red    { background: #3d1010; color: #ff6b6b; border: 1px solid #7a2020; }
        .badge-green  { background: #0d3320; color: #4ade80; border: 1px solid #1a6640; }
        .badge-orange { background: #3d2800; color: #fb923c; border: 1px solid #7a5000; }
        .badge-blue   { background: #0d1f3d; color: #60a5fa; border: 1px solid #1a3a7a; }
        .badge-gray   { background: #1e1e2e; color: #9ca3af; border: 1px solid #3a3a5e; }

        /* ---- Payment box ---- */
        .payment-box {
            background: #0d1117;
            border-radius: 8px;
            padding: 16px 20px;
            font-family: 'Courier New', monospace;
            font-size: 0.85rem;
            color: #c0c0d8;
            margin-top: 10px;
        }
        .payment-amount {
            font-size: 2rem;
            font-weight: 700;
            color: #f8f8ff;
            margin: 6px 0;
        }

        /* ---- Cost ticker ---- */
        .cost-ticker {
            background: #2d0a0a;
            border: 1px solid #7a1a1a;
            border-radius: 8px;
            padding: 14px 20px;
            text-align: center;
            margin-top: 8px;
        }
        .cost-ticker-label {
            font-size: 0.7rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #ff6b6b;
            margin-bottom: 4px;
        }
        .cost-ticker-value {
            font-size: 2rem;
            font-weight: 700;
            color: #ff4444;
            font-family: 'Courier New', monospace;
        }

        /* ---- Zero waste ticker ---- */
        .zero-ticker {
            background: #0a2d12;
            border: 1px solid #1a7a2a;
            border-radius: 8px;
            padding: 14px 20px;
            text-align: center;
            margin-top: 8px;
        }
        .zero-ticker-label {
            font-size: 0.7rem;
            font-weight: 700;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            color: #4ade80;
            margin-bottom: 4px;
        }
        .zero-ticker-value {
            font-size: 2rem;
            font-weight: 700;
            color: #22c55e;
            font-family: 'Courier New', monospace;
        }

        /* ---- End card ---- */
        .end-card {
            border-radius: 12px;
            padding: 28px 32px;
            margin-top: 20px;
            text-align: center;
        }
        .end-card-bad {
            background: #2d0a0a;
            border: 2px solid #7a1a1a;
        }
        .end-card-good {
            background: #0a2d12;
            border: 2px solid #1a7a2a;
        }
        .end-card-title {
            font-size: 1.1rem;
            font-weight: 700;
            color: #f8f8ff;
            margin-bottom: 12px;
        }
        .end-card-stat {
            font-size: 0.9rem;
            color: #b0b0c8;
            line-height: 2;
        }

        /* ---- Audit log ---- */
        .audit-log {
            background: #0a0a1a;
            border: 1px solid #1a4a3a;
            border-radius: 8px;
            padding: 16px 20px;
            font-family: 'Courier New', monospace;
            font-size: 0.78rem;
            color: #4ade80;
            white-space: pre;
            overflow-x: auto;
        }

        /* ---- Scoring table row ---- */
        .score-row {
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 7px 0;
            border-bottom: 1px solid #2d2d4e;
            font-size: 0.88rem;
            color: #c0c0d8;
        }
        .score-row:last-child { border-bottom: none; }
        .score-icon { font-size: 1rem; width: 20px; flex-shrink: 0; }
        .score-note { font-size: 0.78rem; color: #7878a0; margin-top: 2px; }

        /* ---- Agent profile ---- */
        .agent-row {
            display: flex;
            justify-content: space-between;
            padding: 5px 0;
            font-size: 0.88rem;
            color: #c0c0d8;
            border-bottom: 1px solid #2d2d4e;
        }
        .agent-row:last-child { border-bottom: none; }
        .agent-key { color: #8888aa; }

        /* ---- Escrow pill ---- */
        .escrow-pill {
            display: inline-block;
            padding: 5px 16px;
            border-radius: 20px;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }
        .escrow-held     { background: #3d2800; color: #fb923c; border: 1px solid #7a5000; }
        .escrow-released { background: #0d3320; color: #4ade80; border: 1px solid #1a6640; }
        .escrow-returned { background: #3d1010; color: #ff6b6b; border: 1px solid #7a2020; }

        /* ---- Step label ---- */
        .step-label {
            font-size: 0.68rem;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: #5555aa;
            margin-bottom: 4px;
        }

        /* Hide Streamlit default padding for cleaner look */
        .block-container { padding-top: 2rem !important; }
        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Task card
# ---------------------------------------------------------------------------

def render_task_card(task: dict, show_full: bool = True) -> None:
    criteria_html = "".join(
        f"<li style='margin-bottom:6px;'>{c}</li>"
        for c in task["acceptance_criteria"]
    )
    body = f"""
    <div class="sb-card">
        <div class="sb-card-title">📋 Task Request — {task['task_id']}</div>
        <div style="font-size:1.05rem;font-weight:600;color:#e0e0ff;margin-bottom:8px;">
            {task['title']}
        </div>
        <div class="sb-card-body">{task['description']}</div>
    """
    if show_full:
        body += f"""
        <div style="margin-top:14px;">
            <div class="sb-card-title" style="margin-bottom:6px;">Acceptance Criteria</div>
            <ul style="margin:0;padding-left:18px;color:#c0c0d8;font-size:0.88rem;line-height:1.8;">
                {criteria_html}
            </ul>
        </div>
        <div style="margin-top:14px;">
            <span class="badge badge-blue">Budget: ${task['budget']:.0f} {task['currency']}</span>
            &nbsp;
            <span class="badge badge-gray">Buyer: {task['buyer_agent']}</span>
        </div>
        """
    body += "</div>"
    st.markdown(body, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Deliverable panel
# ---------------------------------------------------------------------------

def render_deliverable(deliverable: dict, status: str | None = None) -> None:
    """status: None | 'pending' | 'pass' | 'fail'"""
    badge_html = ""
    if status == "fail":
        badge_html = '<br><span class="badge badge-red">✗ Does Not Meet Criteria</span>'
    elif status == "pass":
        badge_html = '<br><span class="badge badge-green">✓ Delivery Verified: Meets Criteria</span>'
    elif status == "pending":
        badge_html = '<br><span class="badge badge-orange">⏳ Scoring in Progress…</span>'

    # Convert markdown bold to HTML for display
    count = 0
    result = []
    i = 0
    raw = deliverable["text"]
    while i < len(raw):
        if raw[i:i+2] == "**":
            if count % 2 == 0:
                result.append("<strong>")
            else:
                result.append("</strong>")
            count += 1
            i += 2
        elif raw[i] == "\n":
            result.append("<br>")
            i += 1
        else:
            result.append(raw[i])
            i += 1
    text_html = "".join(result)

    st.markdown(
        f"""
        <div class="sb-card">
            <div class="sb-card-title">📄 Deliverable Received</div>
            <div class="sb-card-body" style="font-size:0.85rem;">{text_html}</div>
            {badge_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Payment panel
# ---------------------------------------------------------------------------

def render_payment_panel(task: dict, status: str, timestamp: str = "") -> None:
    """status: 'sent' | 'held' | 'released' | 'returned'"""
    if status == "sent":
        pill = '<span class="badge badge-red">⚠ No Quality Check</span>'
        status_label = "AUTO-SENT"
        color = "#ff6b6b"
    elif status == "held":
        pill = '<span class="escrow-pill escrow-held">⏳ Held — Pending Quality Check</span>'
        status_label = "IN ESCROW"
        color = "#fb923c"
    elif status == "released":
        pill = '<span class="escrow-pill escrow-released">✓ Released to Worker Agent</span>'
        status_label = "RELEASED"
        color = "#4ade80"
    elif status == "returned":
        pill = '<span class="escrow-pill escrow-returned">↩ Returned to Buyer</span>'
        status_label = "RETURNED"
        color = "#ff6b6b"
    else:
        pill = ""
        status_label = ""
        color = "#c0c0d8"

    ts_html = f'<div style="font-size:0.75rem;color:#666688;margin-top:4px;">{timestamp}</div>' if timestamp else ""

    st.markdown(
        f"""
        <div class="sb-card">
            <div class="sb-card-title">💳 Payment</div>
            <div class="payment-box">
                <div style="font-size:0.78rem;color:#888899;">Amount</div>
                <div class="payment-amount" style="color:{color};">${task['budget']:.2f}</div>
                <div style="font-size:0.78rem;color:#888899;">Status: <strong style="color:{color};">{status_label}</strong></div>
                {ts_html}
                <div style="margin-top:4px;font-size:0.72rem;color:#555577;">
                    Buyer: {task['buyer_agent']} &nbsp;|&nbsp; Task: {task['task_id']}
                </div>
            </div>
            <div style="margin-top:10px;">{pill}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Cost ticker
# ---------------------------------------------------------------------------

def render_cost_ticker(amount: float, zero: bool = False) -> None:
    if zero:
        st.markdown(
            f"""
            <div class="zero-ticker">
                <div class="zero-ticker-label">Wasted Spend</div>
                <div class="zero-ticker-value">${amount:.2f}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="cost-ticker">
                <div class="cost-ticker-label">💸 Wasted Spend — No Recourse</div>
                <div class="cost-ticker-value">${amount:.2f}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ---------------------------------------------------------------------------
# Agent profile card
# ---------------------------------------------------------------------------

def render_agent_profile(agent: dict, revealed: bool = True) -> None:
    if not revealed:
        st.markdown(
            """
            <div class="sb-card">
                <div class="sb-card-title">🔍 Checking Agent Track Record…</div>
                <div class="sb-card-body" style="color:#5555aa;">Querying SettleBridge registry…</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    qual = agent["qualification"]
    badge_cls = "badge-green" if qual == "PASS" else "badge-red"
    badge_icon = "✓" if qual == "PASS" else "✗"
    scores_html = " ".join(
        f'<span style="color:{"#4ade80" if s >= 3.0 else "#ff6b6b"};font-weight:600;">{s}</span>'
        for s in agent["past_scores"]
    )

    st.markdown(
        f"""
        <div class="sb-card">
            <div class="sb-card-title">🔍 Agent Track Record</div>
            <div class="agent-row">
                <span class="agent-key">Agent</span>
                <span>{agent['name']} &nbsp;<code style="font-size:0.75rem;color:#6666aa;">{agent['agent_id']}</code></span>
            </div>
            <div class="agent-row">
                <span class="agent-key">Specialty</span>
                <span>{agent['specialty']}</span>
            </div>
            <div class="agent-row">
                <span class="agent-key">{agent['task_type_label']} Score</span>
                <span style="font-weight:700;color:{"#4ade80" if agent['task_type_score'] >= 3.0 else "#ff6b6b"};">
                    {agent['task_type_score']}/5
                </span>
            </div>
            <div class="agent-row">
                <span class="agent-key">Tasks Completed</span>
                <span>{agent['total_tasks_completed']}</span>
            </div>
            <div class="agent-row">
                <span class="agent-key">On-Time Rate</span>
                <span>{agent['on_time_rate']}</span>
            </div>
            <div class="agent-row">
                <span class="agent-key">Last 6 Scores</span>
                <span>{scores_html}</span>
            </div>
            <div style="margin-top:12px;">
                <span class="badge {badge_cls}">{badge_icon} Qualification: {qual}</span>
            </div>
            <div style="font-size:0.78rem;color:#7878a0;margin-top:8px;">{agent['qualification_reason']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Scoring rubric panel
# ---------------------------------------------------------------------------

def render_scoring_panel(results: list[dict] | None = None, in_progress: bool = False) -> None:
    if in_progress or results is None:
        st.markdown(
            """
            <div class="sb-card">
                <div class="sb-card-title">⚖ Scoring Against Acceptance Criteria…</div>
                <div class="sb-card-body" style="color:#5555aa;">Evaluating deliverable…</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return

    rows_html = ""
    for r in results:
        icon = "✅" if r["result"] == "PASS" else "❌"
        color = "#4ade80" if r["result"] == "PASS" else "#ff6b6b"
        rows_html += f"""
        <div class="score-row">
            <span class="score-icon">{icon}</span>
            <div>
                <div style="color:{color};font-weight:600;">{r['criterion']}</div>
                <div class="score-note">{r['note']}</div>
            </div>
        </div>
        """

    passed = sum(1 for r in results if r["result"] == "PASS")
    total = len(results)
    overall_badge = (
        '<span class="badge badge-green">✓ Delivery Verified: Meets Criteria</span>'
        if passed == total
        else '<span class="badge badge-red">✗ Delivery Rejected: Below Standard</span>'
    )

    st.markdown(
        f"""
        <div class="sb-card">
            <div class="sb-card-title">⚖ Scoring Result — {passed}/{total} Criteria Met</div>
            {rows_html}
            <div style="margin-top:12px;">{overall_badge}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Audit log panel
# ---------------------------------------------------------------------------

def render_audit_log(entry: str) -> None:
    st.markdown(
        f"""
        <div class="sb-card">
            <div class="sb-card-title">📜 Audit Trail</div>
            <div class="audit-log">{entry}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# End cards
# ---------------------------------------------------------------------------

def render_end_card_bad() -> None:
    st.markdown(
        """
        <div class="end-card end-card-bad">
            <div class="end-card-title">⚠ Transaction Complete</div>
            <div class="end-card-stat">
                Task Completed &nbsp;•&nbsp; Payment Sent &nbsp;•&nbsp;
                Quality: <strong style="color:#ff6b6b;">Unknown</strong> &nbsp;•&nbsp;
                Recourse: <strong style="color:#ff6b6b;">None</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_end_card_good() -> None:
    st.markdown(
        """
        <div class="end-card end-card-good">
            <div class="end-card-title">✓ Verified Settlement Complete</div>
            <div class="end-card-stat">
                Task Completed &nbsp;•&nbsp;
                Quality: <strong style="color:#4ade80;">Verified</strong> &nbsp;•&nbsp;
                Payment: <strong style="color:#4ade80;">Fair</strong> &nbsp;•&nbsp;
                Audit Trail: <strong style="color:#4ade80;">Recorded</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_end_card_rejected() -> None:
    st.markdown(
        """
        <div class="end-card end-card-bad">
            <div class="end-card-title">✗ Delivery Rejected</div>
            <div class="end-card-stat">
                Task Rejected &nbsp;•&nbsp;
                Payment: <strong style="color:#4ade80;">Returned to Buyer</strong> &nbsp;•&nbsp;
                Agent Score: <strong style="color:#ff6b6b;">Updated Downward</strong> &nbsp;•&nbsp;
                Buyer: <strong style="color:#4ade80;">Protected</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_end_card_blocked() -> None:
    st.markdown(
        """
        <div class="end-card end-card-bad">
            <div class="end-card-title">🚫 Agent Blocked — Task Not Assigned</div>
            <div class="end-card-stat">
                Agent Failed Pre-Qualification &nbsp;•&nbsp;
                Task: <strong style="color:#fb923c;">Reassigned</strong> &nbsp;•&nbsp;
                Payment: <strong style="color:#4ade80;">Never At Risk</strong> &nbsp;•&nbsp;
                Buyer: <strong style="color:#4ade80;">Protected</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# Step indicator
# ---------------------------------------------------------------------------

def render_step_label(text: str) -> None:
    st.markdown(f'<div class="step-label">{text}</div>', unsafe_allow_html=True)
