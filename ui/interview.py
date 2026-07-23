import streamlit as st


def render_interview(result):
    """
    Render the Interview Preparation tab.
    """

    st.subheader("🎤 Interview Preparation")

    interview = result.get("interview_questions", "")

    if not interview.strip():
        st.info("No interview questions available.")
        return

    st.markdown(interview)