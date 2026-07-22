import streamlit as st


def render_metrics(result):

    workflow = result.get("tasks", [])

    jobs_text = result.get("jobs_found", "")
    job_count = jobs_text.count("Job Title")

    roadmap = result.get("learning_plan", "")
    roadmap_weeks = max(roadmap.lower().count("week"), 4)

    interview = result.get("interview_questions", "")
    interview_questions = interview.count("?")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Workflow Steps", len(workflow))
    c2.metric("Jobs Found", job_count)
    c3.metric("Roadmap Weeks", roadmap_weeks)
    c4.metric("Interview Questions", interview_questions)