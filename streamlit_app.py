import streamlit as st

from graph import app

from ui.sidebar import render_sidebar
from ui.header import render_header
from ui.metrics import render_metrics
from ui.workflow import render_workflow
from ui.jobs import render_jobs
from ui.analysis import render_analysis
from ui.roadmap import render_roadmap
from ui.interview import render_interview
from ui.styles import load_css


# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="AI Job Copilot",
    page_icon="🤖",
    layout="wide",
)

load_css()


# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------

render_sidebar()


# -----------------------------------------------------
# Header
# -----------------------------------------------------

goal, run = render_header()


# -----------------------------------------------------
# Run Agent
# -----------------------------------------------------

if run:

    if not goal.strip():
        st.warning("⚠️ Please enter a career goal.")
        st.stop()

    initial_state = {
        "user_goal": goal,
        "jobs_found": "",
        "skill_gap_analysis": "",
        "learning_plan": "",
        "interview_questions": "",
        "next_step": "",
        "tasks": [],
        "task_index": 0,
    }

    # ---------------------------------------------
    # Run LangGraph Agent
    # ---------------------------------------------

    with st.spinner("🤖 AI Agent is analyzing your career goal..."):
        result = app.invoke(initial_state)

    st.success("✅ Analysis completed successfully!")

    st.divider()

    # ---------------------------------------------
    # Dashboard
    # ---------------------------------------------

    render_metrics(result)

    st.divider()

    # ---------------------------------------------
    # Workflow
    # ---------------------------------------------

    render_workflow(result)

    st.divider()

    # ---------------------------------------------
    # Result Tabs
    # ---------------------------------------------

    jobs_tab, analysis_tab, roadmap_tab, interview_tab = st.tabs(
        [
            "💼 Jobs",
            "📊 Skill Analysis",
            "🗺️ Roadmap",
            "🎤 Interview Prep",
        ]
    )

    # ---------------------------------------------
    # Jobs
    # ---------------------------------------------

    with jobs_tab:
        render_jobs(result)

    # ---------------------------------------------
    # Skill Analysis
    # ---------------------------------------------

    with analysis_tab:
        render_analysis(result)

    # ---------------------------------------------
    # Learning Roadmap
    # ---------------------------------------------

    with roadmap_tab:
        render_roadmap(result)

    # ---------------------------------------------
    # Interview Preparation
    # ---------------------------------------------

    with interview_tab:
        render_interview(result)