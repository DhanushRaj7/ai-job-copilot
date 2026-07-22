import streamlit as st


def render_header():

    st.title("🤖 AI Job Copilot")

    st.markdown(
        """
AI-powered career planning using **LangGraph**, **Groq LLM**, and **live job market data**.
"""
    )

    left, right = st.columns([3, 1])

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

        st.info(
            """
### What this AI does

✅ Finds Live Jobs

✅ Analyzes Skill Gaps

✅ Creates Learning Roadmap

✅ Generates Interview Questions
"""
        )

    return goal, run