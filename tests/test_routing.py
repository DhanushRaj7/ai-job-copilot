"""Offline unit tests for the agent's routing logic.

These tests never call the LLM or the network — they exercise the pure
state-transition functions that decide which node runs next. A dummy
GROQ_API_KEY is set so importing the graph module (which constructs the
LLM client at import time) succeeds without real credentials.
"""

import os

os.environ.setdefault("GROQ_API_KEY", "test-not-used")

from graph import app, route_decision, task_route_decision, task_router_node  # noqa: E402


def _state(**overrides):
    base = {
        "user_goal": "",
        "jobs_found": "",
        "skill_gap_analysis": "",
        "learning_plan": "",
        "interview_questions": "",
        "next_step": "",
        "tasks": [],
        "task_index": 0,
    }
    base.update(overrides)
    return base


def test_task_router_ends_when_all_tasks_done():
    state = _state(tasks=["search"], task_index=1)
    assert task_router_node(state)["next_step"] == "end"


def test_task_router_returns_current_task_in_order():
    tasks = ["search", "analysis", "roadmap"]
    assert task_router_node(_state(tasks=tasks, task_index=0))["next_step"] == "search"
    assert task_router_node(_state(tasks=tasks, task_index=1))["next_step"] == "analysis"
    assert task_router_node(_state(tasks=tasks, task_index=2))["next_step"] == "roadmap"


def test_task_route_decision_reads_next_step():
    assert task_route_decision(_state(next_step="interview")) == "interview"


def test_route_decision_reads_next_step():
    assert route_decision(_state(next_step="analysis")) == "analysis"


def test_graph_compiles():
    assert app is not None
