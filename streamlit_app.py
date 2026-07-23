import streamlit as st

from graph import app

from ui.sidebar import render_sidebar
from ui.header import render_header
from ui.metrics import render_metrics
from ui.workflow import render_workflow

from ui.jobs import render_jobs

from ui.analysis import render_analysis

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="AI Job Copilot",
    page_icon="🤖",
    layout="wide",
)

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

    if goal.strip() == "":
        st.warning("Please enter a career goal.")
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

    with st.spinner("🤖 AI Agent is thinking..."):

        result = app.invoke(initial_state)

    st.success("✅ Agent Completed Successfully!")

    st.divider()

    # -------------------------------------------------
    # Metrics
    # -------------------------------------------------

    render_metrics(result)

    st.divider()

    # -------------------------------------------------
    # Workflow
    # -------------------------------------------------

    render_workflow(result.get("tasks", []))

    st.divider()

    # -------------------------------------------------
    # Tabs
    # -------------------------------------------------

    jobs_tab, analysis_tab, roadmap_tab, interview_tab = st.tabs(
        [
            "💼 Jobs",
            "📊 Skill Analysis",
            "🗺️ Roadmap",
            "🎤 Interview Prep",
        ]
    )

    # -------------------------------------------------
    # JOBS
    # -------------------------------------------------

    with jobs_tab:
        render_jobs(result)

    # -------------------------------------------------
    # ANALYSIS
    # -------------------------------------------------

    with analysis_tab:
        render_analysis(result)


    # -------------------------------------------------
    # ROADMAP
    # -------------------------------------------------

    with roadmap_tab:

        st.subheader("🗺️ Personalized Learning Roadmap")

        roadmap = result.get("learning_plan", "")

        if "Week" in roadmap:

            import re

            sections = re.split(r"(?=Week\s+\d+)", roadmap)

            for sec in sections:

                sec = sec.strip()

                if not sec:
                    continue

                heading = sec.split("\n")[0]

                with st.expander(f"📅 {heading}"):

                    st.markdown(sec)

        else:

            st.markdown(roadmap)

    # -------------------------------------------------
    # INTERVIEW
    # -------------------------------------------------

    with interview_tab:

        st.subheader("🎤 Interview Preparation")

        st.markdown(result.get("interview_questions", ""))

    st.divider()

    st.caption(
        "AI Job Copilot • LangGraph • Groq • Adzuna API • Streamlit"
    )