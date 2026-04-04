"""Static simulation data for the SettleBridge demo — no LLM calls, fully deterministic."""

from datetime import UTC, datetime

# ---------------------------------------------------------------------------
# Task specification
# ---------------------------------------------------------------------------

TASK_SPEC = {
    "title": "Market Research Summary: Emerging AI Agent Frameworks",
    "description": (
        "Produce a concise market research summary covering the top 5 emerging AI agent "
        "frameworks as of Q1 2026. The summary will be used by our product team to inform "
        "a roadmap decision and will be presented to stakeholders next week."
    ),
    "acceptance_criteria": [
        "Identifies and names at least 5 distinct AI agent frameworks released or updated in 2025–2026",
        "Includes a brief (2–3 sentence) description of each framework's primary use case",
        "Compares frameworks on at least two dimensions (e.g. latency, cost, ecosystem maturity)",
        "Cites at least one public source or benchmark for each framework",
    ],
    "budget": 120.00,
    "currency": "USD",
    "task_id": "TASK-7841",
    "buyer_agent": "BuyerAgent-Alpha",
}

# ---------------------------------------------------------------------------
# Deliverables
# ---------------------------------------------------------------------------

BAD_DELIVERABLE = {
    "text": (
        "AI agents are revolutionizing the tech industry with many exciting new frameworks "
        "being developed every day. The leading players include OpenAI, Google, and Microsoft, "
        "all of whom are investing heavily in this space. These frameworks are fast, scalable, "
        "and easy to use. Many Fortune 500 companies are already adopting AI agents to "
        "automate their workflows and reduce costs significantly. The future of AI agents "
        "looks bright and there are many opportunities for growth in this sector."
    ),
    "word_count": 72,
    "frameworks_named": 0,
    "sources_cited": 0,
}

GOOD_DELIVERABLE = {
    "text": (
        "**Top 5 AI Agent Frameworks — Q1 2026 Market Summary**\n\n"
        "**1. LangGraph (LangChain)** — Graph-based orchestration for stateful, multi-actor "
        "workflows. Best suited for complex pipelines requiring durable execution. Benchmarked "
        "at <200ms per node hop on standard tasks (LangChain blog, Jan 2026).\n\n"
        "**2. Google ADK (Agent Developer Kit)** — Google's first-party framework for building "
        "A2A-compatible agents with native Gemini integration. Targets enterprise deployments. "
        "Public release: Google I/O 2025 — production-ready as of Q4 2025.\n\n"
        "**3. CrewAI** — Role-based multi-agent coordination with a focus on ease of setup. "
        "Popular for SMB automation. Reports 3× faster time-to-prototype vs. AutoGen in "
        "independent testing (CrewAI benchmarks, Nov 2025).\n\n"
        "**4. AutoGen v2 (Microsoft)** — Conversation-driven agent framework optimised for "
        "code generation and reasoning chains. Strong Azure integration. Azure DevBlogs "
        "benchmark shows 94% task completion on HumanEval-Agents (Dec 2025).\n\n"
        "**5. Semantic Kernel Agents (Microsoft)** — Plugin-based, enterprise-grade agents "
        "with first-class .NET and Python support. Preferred for regulated industries. "
        "SOC 2 Type II certified as of Q3 2025 (Microsoft Learn docs).\n\n"
        "**Comparison:** LangGraph and AutoGen lead on ecosystem maturity; CrewAI leads on "
        "setup speed; ADK leads on A2A interoperability. Cost per 1k tasks: CrewAI ~$0.40, "
        "LangGraph ~$0.65, AutoGen ~$0.55 (community benchmarks, Feb 2026)."
    ),
    "word_count": 218,
    "frameworks_named": 5,
    "sources_cited": 5,
}

# ---------------------------------------------------------------------------
# Agent profiles
# ---------------------------------------------------------------------------

GOOD_AGENT_PROFILE = {
    "name": "ResearchAgent-7",
    "agent_id": "AGT-7R",
    "specialty": "Market Research & Competitive Analysis",
    "task_type_score": 4.7,
    "task_type_label": "Market Research",
    "total_tasks_completed": 312,
    "on_time_rate": "98%",
    "past_scores": [4.5, 4.8, 4.7, 4.9, 4.6, 4.7],
    "qualification": "PASS",
    "qualification_reason": "Consistent high-quality delivery across 312 market research tasks.",
    "registered_since": "2024-08-14",
}

BAD_AGENT_PROFILE = {
    "name": "ResearchAgent-23",
    "agent_id": "AGT-23R",
    "specialty": "Market Research & Competitive Analysis",
    "task_type_score": 1.9,
    "task_type_label": "Market Research",
    "total_tasks_completed": 47,
    "on_time_rate": "61%",
    "past_scores": [2.1, 1.8, 2.3, 1.5, 1.9, 1.7],
    "qualification": "FAIL",
    "qualification_reason": "Below-standard delivery on 6 of last 6 market research tasks. Score threshold: 3.0/5.",
    "registered_since": "2025-11-02",
}

# ---------------------------------------------------------------------------
# Scoring rubrics
# ---------------------------------------------------------------------------

SCORING_RESULT_PASS = [
    {"criterion": "Identifies at least 5 distinct AI agent frameworks", "result": "PASS", "note": "5 frameworks named with release dates"},
    {"criterion": "2–3 sentence description of each framework's use case", "result": "PASS", "note": "All 5 descriptions present and specific"},
    {"criterion": "Comparison on at least two dimensions", "result": "PASS", "note": "Compared on latency, cost, and ecosystem maturity"},
    {"criterion": "At least one source cited per framework", "result": "PASS", "note": "5 sources cited — blogs, benchmarks, and docs"},
]

SCORING_RESULT_FAIL = [
    {"criterion": "Identifies at least 5 distinct AI agent frameworks", "result": "FAIL", "note": "0 frameworks named — only company names mentioned"},
    {"criterion": "2–3 sentence description of each framework's use case", "result": "FAIL", "note": "No framework-specific descriptions found"},
    {"criterion": "Comparison on at least two dimensions", "result": "FAIL", "note": "No comparative data present"},
    {"criterion": "At least one source cited per framework", "result": "FAIL", "note": "Zero sources cited"},
]

# ---------------------------------------------------------------------------
# Audit log
# ---------------------------------------------------------------------------

def make_audit_log_entry(agent: dict, task: dict, score_results: list[dict]) -> str:
    ts = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    passed = sum(1 for r in score_results if r["result"] == "PASS")
    total = len(score_results)
    return (
        f"[{ts}] SETTLEMENT RECORD\n"
        f"  task_id        : {task['task_id']}\n"
        f"  buyer_agent    : {task['buyer_agent']}\n"
        f"  worker_agent   : {agent['name']} ({agent['agent_id']})\n"
        f"  outcome        : ACCEPTED\n"
        f"  criteria_score : {passed}/{total} criteria met\n"
        f"  payment        : ${task['budget']:.2f} {task['currency']} released\n"
        f"  agent_score    : {agent['task_type_score']}/5 (unchanged — within tolerance)\n"
        f"  verified_by    : SettleBridge Trust Layer v1.0\n"
        f"  immutable_hash : sb1q7xp4l3r8v2n9k5m0..."
    )


def make_rejection_log_entry(agent: dict, task: dict) -> str:
    ts = datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    new_score = round(agent["task_type_score"] - 0.2, 1)
    return (
        f"[{ts}] REJECTION RECORD\n"
        f"  task_id        : {task['task_id']}\n"
        f"  buyer_agent    : {task['buyer_agent']}\n"
        f"  worker_agent   : {agent['name']} ({agent['agent_id']})\n"
        f"  outcome        : REJECTED\n"
        f"  criteria_score : 0/4 criteria met\n"
        f"  payment        : ${task['budget']:.2f} {task['currency']} returned to buyer\n"
        f"  agent_score    : {agent['task_type_score']}/5 → {new_score}/5 (downgraded)\n"
        f"  verified_by    : SettleBridge Trust Layer v1.0\n"
        f"  immutable_hash : sb1q2xw3ec4rv5tb6yn..."
    )
