import streamlit as st

from graph import app

from ui.sidebar import render_sidebar
from ui.header import render_header
from ui.metrics import render_metrics
from ui.workflow import render_workflow

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

        st.subheader("💼 Live Job Opportunities")

        jobs_text = result.get("jobs_found", "")

        jobs = jobs_text.split("=" * 60)

        displayed = False

        for job in jobs:

            if not job.strip():
                continue

            title = "Job Opportunity"
            company = ""
            location = ""

            for line in job.splitlines():

                if line.startswith("Job Title"):
                    title = line.replace("Job Title:", "").strip()

                elif line.startswith("Company"):
                    company = line.replace("Company:", "").strip()

                elif line.startswith("Location"):
                    location = line.replace("Location:", "").strip()

            with st.expander(f"💼 {title}"):

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown("**🏢 Company**")
                    st.write(company if company else "N/A")

                with col2:
                    st.markdown("**📍 Location**")
                    st.write(location if location else "N/A")

                st.divider()

                st.text(job)

            displayed = True

        if not displayed:
            st.info("No jobs were returned.")

    # -------------------------------------------------
    # ANALYSIS
    # -------------------------------------------------

    with analysis_tab:

        st.subheader("📊 Skill Gap Analysis")

        st.info(result.get("skill_gap_analysis", ""))

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