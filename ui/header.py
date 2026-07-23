import streamlit as st


def render_header():
    st.markdown(
        """
        <div style="padding:20px 0 10px 0;">
            <h1 style="margin-bottom:0;">🤖 AI Job Copilot</h1>
            <p style="color:#57606A;font-size:18px;margin-top:8px;">
                Discover live jobs, identify skill gaps, build personalized learning roadmaps,
                and prepare for interviews — all powered by AI.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left, right = st.columns([3, 1], gap="large")

    with left:
        goal = st.text_input(
            "🎯 Career Goal",
            placeholder="Example: Become a Machine Learning Engineer",
        )

        run = st.button(
            "🚀 Run AI Agent",
            use_container_width=True,
        )

    with right:
        st.markdown("### 🚀 Features")

        st.success("Live Job Search")
        st.success("Skill Gap Analysis")
        st.success("Learning Roadmap")
        st.success("Interview Preparation")

    return goal, run