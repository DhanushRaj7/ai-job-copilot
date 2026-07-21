import streamlit as st
from graph import app

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
with st.sidebar:

    st.title("🤖 AI Job Copilot")

    st.markdown("---")

    st.subheader("🛠 Tech Stack")

    st.success("LangGraph")
    st.success("Groq LLM")
    st.success("Adzuna API")
    st.success("Streamlit")

    st.markdown("---")

    st.subheader("⚙️ Agent Workflow")

    st.markdown("""
1️⃣ Planner

⬇️

2️⃣ Dependency Resolver

⬇️

3️⃣ Task Router

⬇️

4️⃣ Search Node

⬇️

5️⃣ Analysis Node

⬇️

6️⃣ Roadmap Node

⬇️

7️⃣ Interview Node
""")

    st.markdown("---")

    st.caption("Built with ❤️ by Dhanush Raj")


# -----------------------------------------------------
# Header
# -----------------------------------------------------
st.title("🤖 AI Job Copilot")

st.markdown(
"""
AI-powered career planning using **LangGraph**, **Groq LLM**, and **live job market data**.
"""
)

# -----------------------------------------------------
# Hero Section
# -----------------------------------------------------
left, right = st.columns([3, 1])

with left:

    goal = st.text_input(
        "🎯 Career Goal",
        placeholder="Example: Become a Machine Learning Engineer"
    )

    run = st.button(
        "🚀 Run AI Agent",
        use_container_width=True
    )

with right:

    st.info(
"""
### What this AI does

✅ Finds Live Jobs

✅ Analyzes Skill Gaps

✅ Creates Learning Roadmap

✅ Generates Interview Questions
"""
    )

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

    workflow = result.get("tasks", [])

    jobs_text = result.get("jobs_found", "")

    job_count = jobs_text.count("Job Title")

    roadmap_text = result.get("learning_plan", "")

    week_count = roadmap_text.lower().count("week")

    interview_text = result.get("interview_questions", "")

    question_count = interview_text.count("?")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Workflow Steps", len(workflow))
    c2.metric("Jobs Found", job_count)
    c3.metric("Roadmap Weeks", max(week_count, 4))
    c4.metric("Interview Questions", question_count)

    st.divider()

    # -------------------------------------------------
    # Workflow
    # -------------------------------------------------

    st.subheader("🧠 Execution Workflow")

    st.info(" ➜ ".join(workflow))

    st.divider()

    # -------------------------------------------------
    # Tabs
    # -------------------------------------------------

    jobs_tab, analysis_tab, roadmap_tab, interview_tab = st.tabs(
        [
            "💼 Jobs",
            "📊 Skill Analysis",
            "🗺️ Roadmap",
            "🎤 Interview Prep"
        ]
    )

    # -------------------------------------------------
    # JOBS
    # -------------------------------------------------

    with jobs_tab:

        st.subheader("💼 Live Job Opportunities")

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

            with st.expander(f"💼 {title}", expanded=False):

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown(f"**🏢 Company**")
                    st.write(company if company else "N/A")

                with col2:
                    st.markdown(f"**📍 Location**")
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

            sections = re.split(r'(?=Week\s+\d+)', roadmap)

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