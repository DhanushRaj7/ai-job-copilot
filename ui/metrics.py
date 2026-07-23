import streamlit as st


def render_metrics(result):
    """
    Render GitHub-style dashboard cards.
    """

    workflow = result.get("tasks", [])

    jobs_text = result.get("jobs_found", "")
    job_count = jobs_text.count("Job Title")

    roadmap = result.get("learning_plan", "")
    roadmap_weeks = max(roadmap.lower().count("week"), 4)

    interview = result.get("interview_questions", "")
    interview_questions = interview.count("?")

    st.markdown("## 📊 Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    cards = [
        ("💼", "Jobs Found", job_count),
        ("⚙️", "Workflow Steps", len(workflow)),
        ("🗺️", "Roadmap Weeks", roadmap_weeks),
        ("🎤", "Interview Qs", interview_questions),
    ]

    for column, (icon, title, value) in zip([c1, c2, c3, c4], cards):

        with column:

            st.markdown(
                f"""
<div style="
background:#F6F8FA;
border:1px solid #D0D7DE;
border-radius:12px;
padding:22px;
text-align:center;
height:150px;
display:flex;
flex-direction:column;
justify-content:center;
">

<div style="font-size:32px;">
{icon}
</div>

<div style="
font-size:15px;
color:#57606A;
margin-top:10px;
">
{title}
</div>

<div style="
font-size:36px;
font-weight:bold;
color:#24292F;
margin-top:10px;
">
{value}
</div>

</div>
""",
                unsafe_allow_html=True,
            )