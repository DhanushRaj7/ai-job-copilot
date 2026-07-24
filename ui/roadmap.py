import re
import streamlit as st


def render_roadmap(result):
    st.subheader("🗺️ Learning Roadmap")

    roadmap = result.get("learning_plan", "")

    if not roadmap.strip():
        st.info("No roadmap generated.")
        return

    weeks = re.split(r"(?=Week\s+\d+)", roadmap)

    for week in weeks:

        week = week.strip()

        if not week:
            continue

        st.markdown(
            f"""
<div style="
background:#F6F8FA;
border-left:6px solid #0969DA;
padding:18px;
border-radius:10px;
margin-bottom:15px;
">
{week}
</div>
""",
            unsafe_allow_html=True,
        )